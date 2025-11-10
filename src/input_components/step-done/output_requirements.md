**AUTOMATIC PREFERENCE ADDITION**: When new preferences are found, automatically update step_info files and report changes.

**PROCESS**:
1. Analyze conversation logs and identify new user preferences (max 3)
2. Automatically add preferences to USER PREFERENCES section of the **COMPLETED step's** step_info.md (the file path is provided in CONTEXT section)
3. Report what was added to the user

**REQUIRED OUTPUT FORMAT**: If new preferences were found and added:
```
✅ Found and added the following user preferences to step_info:

- <preference1>
- <preference2>
- <preference3>

These preferences are now active for future framework sessions.
```

**IF NO NEW PREFERENCES**: Output exactly:
```
No new user preferences detected that aren't already captured in input components.
```

**SYSTEM PROMPT FORMAT**: Each preference should be:
- 1-2 sentences maximum
- Actionable instruction for Claude's behavior
- Generic (no project-specific terms)
- Captures user working style preference

**EXAMPLES OF GOOD SYSTEM PROMPTS**:

*Step 1 examples:*
- "When generating questions, include architectural diagrams to visualize component relationships."
- "Prioritize project_memory search over codebase exploration when understanding components."

*Step 2 examples:*
- "Present research findings with evidence-first structure, followed by analysis summary."
- "Use table format for comparing multiple implementation approaches."

*Step 3 examples:*
- "Begin design discussions by identifying risks and constraints before exploring solutions."
- "Include trade-off analysis when presenting multiple design options."

*Step 4 examples:*
- "Build after each substantial implementation chunk (multiple files) rather than after single file changes."
- "Group test writing tasks together for batch approval, but seek approval for each core implementation task individually."

*Step 5 examples:*
- "Require unit tests for all new API functions, integration tests only for multi-component features."
- "Document test setup steps in guide files for future reference."

**CRITICAL**:
- Update the COMPLETED step's input components file (not the next step)
- Do not add prompts for preferences already present in completed step's input components
- Maximum 3 new preferences per step completion
- Must be generic working style patterns, not project-specific details

## CRITICAL - DO NOT AUTO-ADVANCE TO NEXT STEP

After outputting your preference addition results:
- Inform user that the completed step is done and state has been advanced to the next step
- **SPECIAL CASE - Step 5 → Step 6 transition**: Inform user that `/compact` will be run to clear context before Step 6
- Tell user to run `/sixstep` when ready to begin the next step
- **DO NOT automatically begin next step work**
- **DO NOT read next step files or start next step tasks**
- **STOP after preference addition output**

The framework state has been advanced by the system, but the user must explicitly start the next step using `/sixstep`.

## CONTEXT MANAGEMENT

**When transitioning from Step 5 to Step 6**:
- Run `/compact` command to clear the context window before Step 6
- This ensures a clean context for knowledge curation work in Step 6
- Inform the user that context has been cleared