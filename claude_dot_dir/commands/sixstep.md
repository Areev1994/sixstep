---
description: Ask question with six-step framework context (pre-process program)
argument-hint: [your question]
---

Please wait - I need to first execute the function call below to enhance your question with six-step framework context, then use the script output as the actual user question to answer.

<function_calls>
<invoke name="Bash">
<parameter name="command">python3 claude_intelligence/solution_map_implementation/compose_input.py "$ARGUMENTS"</parameter>
<parameter name="description">Compose enhanced prompt with six-step framework context</parameter>
</invoke>