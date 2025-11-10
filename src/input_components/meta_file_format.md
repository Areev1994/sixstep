# Meta File Writing Standards

## File Structure
**Location:** `meta/{problem_id}/step{N}.md` (or `step{N}_phase{P}.md` for multi-phase steps)

## Interaction Format Template

Each interaction in a meta file MUST follow this exact structure:

```markdown
## Interaction {N}
**Timestamp:** {ISO_timestamp}
**Enhanced Prompt:**
```
{complete_enhanced_prompt}
```

**Claude Response Summary:**
{response_summary_in_specified_format}

---
```

## Claude Writing Rules

When Claude writes to meta files, it MUST follow these strict rules:

### ✅ ALLOWED ACTIONS:
- **Replace placeholders only**: Find `[CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]` and replace with response summary
- **Use exact format**: Follow the response summary format from `response_summary_format.md`
- **Preserve formatting**: Maintain all existing markdown structure

### ❌ FORBIDDEN ACTIONS:
- **NEVER modify existing content** above your response section
- **NEVER change timestamps** or metadata written by compose_input.py
- **NEVER alter the Enhanced Prompt section**
- **NEVER modify interaction numbering**
- **NEVER change the separator lines (---)**
- **NEVER add or remove sections** not designated for Claude responses

## File Structure Example

```markdown
# Enhanced Prompt Log - Step 1
**Problem ID**: example_problem
**Started**: 2025-09-15 10:30:00

---

## Interaction 1
**Timestamp:** 2025-09-15T10:30:00
**Enhanced Prompt:**
```
[SIX-STEP FRAMEWORK ACTIVE]
🏗️ FRAMEWORK INFO: Claude works in six-step framework...
📍 CURRENT STEP/PHASE: Step 1: Understanding Problem Statement
...complete enhanced prompt...
```

**Claude Response Summary:**
**Tools Used:** Grep (2x), Read (1x)
**Files Modified:** active/problem_id/step1_questions.md
**Key Actions:** Generated 5 clarification questions about runtime control
**Next Steps:** User should review and refine questions before Step 2

---

## Interaction 2
**Timestamp:** 2025-09-15T10:45:00
**Enhanced Prompt:**
```
[Enhanced prompt for interaction 2...]
```

**Claude Response Summary:**
[CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

---
```

## Placeholder System

**compose_input.py creates:** Enhanced Prompt sections with placeholders
**Claude replaces:** Only the designated placeholder text
**Result:** Complete conversation log with consistent formatting

## Error Prevention

- **Read before writing**: Claude should verify the correct interaction section exists
- **Exact replacement**: Replace only `[CLAUDE_RESPONSE_HERE...]` text
- **Format validation**: Follow response_summary_format.md exactly
- **Boundary respect**: Never modify content outside designated Claude sections