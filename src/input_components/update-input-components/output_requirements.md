**REQUIRED OUTPUT**: Updated USER PREFERENCES section in exact markdown format:

```markdown
## USER PREFERENCES (Auto-Generated)

- [Consolidated and optimized list of prompts]
- [Including both existing and new prompts]
- [Respecting size and duplication constraints]
```

**INTEGRATION SCENARIOS**:

**Scenario 1 - Simple Addition** (if no size/duplication issues):
```markdown
## USER PREFERENCES (Auto-Generated)

- [existing prompt 1]
- [existing prompt 2]  
- [new prompt 1]
- [new prompt 2]
```

**Scenario 2 - Consolidation Required** (if size constraint exceeded):
```markdown
## USER PREFERENCES (Auto-Generated)

- [consolidated prompt combining similar existing ones]
- [rewritten existing prompt for brevity]
- [new prompt 1]
- [new prompt 2]
```

**Scenario 3 - Duplication Detected**:
```
DUPLICATE DETECTED: New prompt "[prompt text]" is similar to existing "[existing prompt]". 
Not adding duplicate prompt.

## USER PREFERENCES (Auto-Generated)
[unchanged section]
```

**CRITICAL**:
- Output ONLY the updated USER PREFERENCES section markdown
- Do not modify any other parts of the step_info.md file
- Ensure total section stays under 2000 characters
- Each prompt should be clear, actionable, and generic

## CRITICAL - STOP AFTER OUTPUT

After outputting the updated USER PREFERENCES section:
- **STOP immediately**
- **DO NOT continue with any step work**
- **DO NOT start researching or implementing**
- The user will continue with their current step work using `/sixstep`

This command only updates preferences - it does not advance the framework or trigger new work.