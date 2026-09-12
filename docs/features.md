# Initial Feature Set

This document defines the first implementation scope for the AI Agent Harness project.

## Agent Runtime
- Implement the core model -> tool -> model execution loop.
- Continue execution until the model returns a final response.
- Enforce a maximum step count to prevent infinite loops.
- Track the current run state and execution status.

## Tool and Function Calling
- Register tools with a name, description, input schema, and Python handler.
- Allow the model to select which registered tool to call.
- Validate tool arguments before execution.
- Execute the requested tool and return its result to the model.

## Tool Registry
- Maintain a central registry of available tools.
- Store tool metadata and validation schemas.
- Support tools that require user approval before execution.

## Structured Outputs
- Use Pydantic and JSON Schema for predictable model and tool data.
- Validate structured outputs before they are used by the runtime.
- Handle invalid model output cleanly.

## Conversation Persistence
- Store user and assistant messages in PostgreSQL.
- Support multiple conversations.
- Reload conversation history when a conversation is resumed.

## Agent Run Persistence and Tracing
- Store each agent run separately from the visible chat conversation.
- Record model calls, tool calls, tool results, errors, and retries.
- Preserve the sequence of steps so runs can be inspected later.

## Context Management
- Include recent conversation history in model context.
- Include raw tool calls and tool results from the active run.
- Summarize older run information instead of replaying all raw logs.
- Keep runtime traces stored even when they are not included in model context.

## Human-in-the-Loop Approval
- Allow selected tools to pause before execution.
- Surface pending actions to the frontend.
- Allow the user to approve or reject the proposed action.
- Resume or terminate the run based on the user's decision.

## Guardrails and Permissions
- Only allow registered tools to execute.
- Validate arguments against the tool schema.
- Enforce maximum run steps.
- Reject invalid or unauthorized tool calls.

## Error Handling and Retries
- Handle model request failures.
- Handle tool execution failures and timeouts.
- Handle invalid structured output.
- Support limited retries for transient failures.

## Streaming
- Use Server-Sent Events (SSE) to send live run updates to the frontend.
- Stream events for model progress, tool calls, tool results, approvals, errors, and completion.

## Frontend
- Build with Vite, React, and TypeScript.
- Provide a minimal chat interface.
- Display conversation history.
- Display an agent run timeline and tool activity.
- Show approval prompts for approval-gated tools.

## Backend
- Build with Python and FastAPI.
- Use Pydantic for request, response, and runtime schemas.
- Use SQLAlchemy for persistence.
- Use Alembic for database migrations.
- Expose endpoints for conversations, runs, approvals, and SSE streaming.

## Database
- Use PostgreSQL.
- Persist conversations, messages, agent runs, run steps, tool calls, tool results, and approvals.

## Testing
- Use pytest for backend tests.
- Test the agent loop, tool registry, validation, approval logic, and API endpoints.
- Add basic frontend tests where they provide meaningful coverage.

## Docker
- Use Docker for reproducible local development and deployment.
- Run PostgreSQL in a container during development.
- Containerize the backend and frontend for deployment.

## CI/CD
- Use GitHub Actions.
- Run automated tests, linting, and type checks on pushes and pull requests.
- Build deployment artifacts only after checks pass.

## Cloud Deployment
- Deploy the production version on AWS.
- Use container-based deployment for the FastAPI backend.
- Use managed PostgreSQL for production data.
- Add production logging and monitoring as part of deployment.
