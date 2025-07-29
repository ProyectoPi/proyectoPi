# Gemini CLI Instructions

This document outlines the rules and guidelines for the Gemini CLI agent working on this project.

## Core Mandates

- **Adherence to Conventions:** Rigorously adhere to existing project conventions when reading or modifying code. Analyze surrounding code, tests, and configuration first.
- **Library/Framework Verification:** NEVER assume a library/framework is available. Verify its established usage within the project before employing it.
- **Style & Structure Mimicry:** Mimic the style (formatting, naming), structure, framework choices, and architectural patterns of existing code.
- **Idiomatic Changes:** Ensure changes integrate naturally and idiomatically with the local context.
- **Minimalist Commenting:** Add comments sparingly. Focus on *why* something is done, not *what* is done. Add high-value comments only if necessary for clarity.
- **Proactiveness:** Fulfill the user's request thoroughly, including reasonable, directly implied follow-up actions.
- **Confirm Ambiguity:** Do not take significant actions beyond the clear scope of the request without user confirmation.

## Operational Guidelines

- **Concise & Direct Tone:** Adopt a professional, direct, and concise tone suitable for a CLI environment.
- **Path Construction:** Always use absolute paths for file operations.
- **Explain Critical Commands:** Before executing commands that modify the file system or system state, provide a brief explanation of the command's purpose and potential impact.
- **Security First:** Always apply security best practices. Never introduce code that exposes, logs, or commits secrets or sensitive information.
- **Git Repository Workflow:**
    1. Use `git status`, `git diff HEAD`, and `git log -n 3` to gather context before committing.
    2. Propose a clear and concise commit message, focusing on the "why".
    3. Confirm commit success with `git status`.
    4. Never push changes to a remote repository unless explicitly asked.
