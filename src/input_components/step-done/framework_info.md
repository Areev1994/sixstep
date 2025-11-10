Extract new user working preferences from completed step conversation that are NOT already captured in current step's input components, then automatically add them to step_info files.

**TARGET**: Generate maximum 3 short system prompts (1-2 sentences each)
**FOCUS**: Step-specific preferences based on completed step (see step_info.md for guidance), generic workflow patterns, communication style, quality preferences
**AVOID**: Project-specific details, technical implementations, domain knowledge

**ANALYSIS APPROACH:**
1. Compare conversation patterns against existing input_components
2. Identify NEW preference patterns not already captured
3. Extract only generic working style elements
4. Format as concise, actionable system prompts

**AUTOMATIC UPDATE PROCESS:**
1. Analyze conversations and extract preferences
2. Automatically update step_info.md files with new preferences
3. Report what was added to the user