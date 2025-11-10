## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Update step3_brainstorm.md with task list PREPENDED to existing Phase 1 content:

**CRITICAL - Task List Placement:**
- Prescriptive: Task list goes AT TOP of existing step3_brainstorm.md (which already has Investigation & Design from Phase 1)
- Descriptive (why): PREPEND task list, don't replace Phase 1 content; keeps Investigation + Design context visible below tasks

**Document structure after Phase 2:**
```markdown
# Investigation & Design v1
*Timestamp*

## TASK LIST

- [ ] Task 1: Description
- [ ] Task 2: Description
- [ ] Task 3: Description

---

## PART 1: Investigation Findings
[Phase 1 content - keep as-is]

## PART 2: Solution Design
[Phase 1 content - keep as-is]
```

**Why prepend, not replace:**
- Investigation findings provide context for why tasks exist
- Solution design shows what tasks implement
- Complete document = context + plan + tasks (all visible together)

---

**USER-REVIEW VERSION**: `active/{problem_id}/user-review/step3_brainstorm.md`
- Task list at top using checkbox format: `- [ ] Task description`
- Clean, reviewable tasks (quick to evaluate, not taking much time)
- Simple descriptions with implementation patterns when relevant
- Glanceable format for quick user review of what needs to be done
- Phase 1 content (Investigation + Design) preserved below task list

**GUIDE VERSION**: `active/{problem_id}/guide/step3_brainstorm.md`
- Complete task list at top with full context
- Tasks with detailed derivation from solution design
- Implementation patterns and architectural context
- Concrete code output expectations
- Full reasoning for task breakdown and sequencing
- Context for how tasks relate to agreed solution
- Phase 1 content (Investigation + Design) preserved below task list

**Task requirements:**
- Derived from the agreed solution design (Phase 1 Part 2)
- Small and reviewable (quick to evaluate, not taking much time)
- Concrete code output that can be quickly verified
- Simple descriptions without complex evaluation criteria
- Include implementation pattern when relevant (e.g., "should follow funcA→funcB→funcC pattern")
- Can include "Write tests for X" (implementation); should NOT include "Run tests" or "Verify X" (validation belongs in Step 5)

⚠️ **CRITICAL**: You MUST update both files using Edit tool (prepending task list) before doing anything else.

CRITICAL: Keep task list synchronized with Step 4 progress. Update status (- [ ] → - [x]) ONLY after user approves each completed task.

## 💬 CONSISTENT CLOSING MESSAGE

**When to show**: Only after creating or updating the task list (not after every question/response during task refinement)

After creating or updating the task list, end with this message format:

```
Please review the task list in active/{problem_id}/user-review/step3_brainstorm.md.

Let me know if you want to add or change anything. When the task list is approved and ready for implementation, run `/step-done` to advance to Step 4.
```

**Note**: During iterative task refinement conversations, DO NOT show this message after every response. Only show it when you've created or significantly updated the task list and are ready for user review.

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** meta/{problem_id}/step3_phase2.md
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
