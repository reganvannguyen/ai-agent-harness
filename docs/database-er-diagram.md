# Database ER Diagram

This document describes the initial database structure for conversations, user-visible messages, agent runs, internal run traces, and compact run summaries used for future context.

```mermaid
erDiagram
    CONVERSATION ||--o{ MESSAGE : contains
    CONVERSATION ||--o{ AGENT_RUN : has
    MESSAGE ||--o| AGENT_RUN : triggers
    AGENT_RUN ||--o{ RUN_STEP : contains
    AGENT_RUN ||--o| RUN_SUMMARY : produces

    CONVERSATION {
        int id PK
        string name
        datetime created_at
    }

    MESSAGE {
        int id PK
        int conversation_id FK
        string role
        text content
        datetime created_at
    }

    AGENT_RUN {
        int id PK
        int conversation_id FK
        int trigger_message_id FK
        string status
        datetime started_at
        datetime completed_at
    }

    RUN_STEP {
        int id PK
        int agent_run_id FK
        int step_order
        string step_type
        jsonb payload
        datetime created_at
    }

    RUN_SUMMARY {
        int id PK
        int agent_run_id FK
        text summary
        datetime created_at
    }
```

## Table Responsibilities

### Conversation
Represents one chat thread. It groups together the user-visible messages and all agent runs that happen within that conversation.

### Message
Stores only the clean conversation shown to the user. This includes user prompts and final assistant responses, but not internal tool calls or raw execution logs.

`role` is expected to contain values such as `user` and `assistant`.

### AgentRun
Represents one execution of the agent runtime. A run is normally triggered by a user message and may contain multiple model calls, tool calls, approvals, retries, and other internal steps before producing the final assistant response.

### RunStep
Stores the internal trace for an agent run. Each row represents one ordered step in the execution.

Possible `step_type` values include:

- `model_call`
- `tool_call`
- `tool_result`
- `approval_request`
- `approval_result`
- `retry`
- `error`
- `final_response`

The `payload` column uses PostgreSQL `JSONB` so each step type can store the data appropriate to that step without requiring separate tables initially.

`step_order` provides deterministic ordering within a run instead of relying only on timestamps.

### RunSummary
Stores a compact summary of what happened during an agent run. The context manager can use these summaries in later prompts instead of replaying every raw `RunStep` from previous runs.

The raw run trace remains stored for debugging, evaluation, and observability, while the summary is intended for efficient conversational context.

## Context Flow

A future model request can be constructed from:

1. Recent user-visible `Message` records.
2. Raw `RunStep` results from the currently active run.
3. Relevant `RunSummary` records from previous runs.
4. The newest user message.

This keeps the full execution history available in the database without unnecessarily filling the model's context window with old raw logs.
