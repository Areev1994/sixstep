---
description: Initialize six-step framework for a problem
argument-hint: [problem description]
---

Please wait - I need to first execute the function call below to enhance your question with six-step framework context, then use the script output as the actual user question to answer.

<function_calls>
<invoke name="Bash">
<parameter name="command">python3 claude_intelligence/solution_map_implementation/framework_state.py start "$ARGUMENTS"</parameter>
<parameter name="description">Initialize six-step framework with the provided problem statement</parameter>
</invoke>

IMPORTANT: This command ONLY initializes the framework structure. Do NOT:
- Analyze the problem
- Create todo lists
- Research the codebase
- Start implementation work
- Use any other tools

Simply run the command and stop. The framework will guide the user to use `/sixstep` when ready to begin.