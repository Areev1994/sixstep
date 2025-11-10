## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Generate TWO versions of step4_implement.md:

**USER-REVIEW VERSION**: `active/{problem_id}/user-review/step4_implement.md`
- Prescriptive: Implementation summary and current status in glanceable format
- Descriptive (why): User can quickly see progress without reading detailed implementation notes

**Content requirements:**
- Task list with checkboxes showing completion status
- Files modified (list with brief changes)
- Key implementation decisions (concise)
- Build validation status (if performed)
- What it provides: Quick progress overview scannable in 2-3 minutes

**GUIDE VERSION**: `active/{problem_id}/guide/step4_implement.md`
- Prescriptive: Comprehensive implementation tracking with complete context
- Descriptive (why): Claude can understand full implementation state across sessions; maintains complete record

**Content requirements:**
- Each task with complete implementation details
- All examined files with what patterns were found
- Architectural analysis and pattern matching decisions
- Implementation challenges and resolution approaches
- Code rationale and design decisions
- Build validation output (if performed)
- What it provides: Full context for Claude to maintain implementation continuity

⚠️ **CRITICAL**: You MUST create these two files using Write tool before doing anything else.

---

## TASK TRACKING AND COMPLETION

**Task Completion Workflow:**

- Prescriptive: Mark tasks complete immediately after implementing them in BOTH user-review and guide versions
- Descriptive (why): Real-time tracking keeps state current; user can see progress at any point; no waiting for approval delays

- Prescriptive: Update checkboxes in both `user-review/step4_implement.md` AND `guide/step4_implement.md` when task done
- Descriptive (why): Both versions must stay synchronized; user-review for user glancing, guide for Claude's context

- Prescriptive: `step3_brainstorm.md` remains unchanged during Step 4
- Descriptive (why): Step 3 output is reference document; Step 4 tracks progress in step4_implement.md; don't modify reference

**Why immediate marking matters:**
- Shows real progress state without artificial delays
- User can check status anytime during implementation
- No context loss from waiting for approvals between tasks
- Continuous flow maintains implementation coherence

---

## BUILD VALIDATION REQUIREMENTS

**When to build:**
- Prescriptive: Build ONLY after ALL tasks are implemented (not incrementally)
- Descriptive (why): Final build validates complete integration; incremental builds interrupt flow without adding value

**How to build:**
- Prescriptive: Use commands ONLY from `project_commands/build.md` - do NOT guess or improvise
- Descriptive (why): Project-specific commands ensure correct process; guessing can break build or miss validation steps

- Prescriptive: If `project_commands/build.md` doesn't exist, skip build validation entirely
- Descriptive (why): Not all projects have standardized build; framework adapts to project structure

**What build validates:**
- Prescriptive: Build validates compilation success (syntax, integration), NOT functional correctness
- Descriptive (why): Step 4 goal is compilable code; functional testing happens in Step 5

**Document build results:**
- Include build output in both user-review (summary: success/failure) and guide (complete output)
- If build fails, document errors and resolution approach
- Build success confirms Step 4 complete; ready for Step 5 validation

---

## IMPLEMENTATION STANDARDS

**Code Quality:**
- Prescriptive: Follow established codebase patterns rigorously
- Descriptive (why): Consistency more valuable than personal preference; uniform code easier to maintain

- Prescriptive: Validate all function signatures and API calls against existing conventions
- Descriptive (why): API mismatches cause integration failures; following patterns ensures compatibility

- Prescriptive: Ensure proper error handling and resource management matching project patterns
- Descriptive (why): Consistent error handling enables debugging; proper resource cleanup prevents leaks

- Prescriptive: Maintain architectural consistency and module boundaries
- Descriptive (why): Proper boundaries maintain clean architecture; violations create technical debt

**Architectural Analysis:**
- Prescriptive: Examine similar existing implementations before creating new code
- Descriptive (why): Pattern matching ensures consistency; avoids reinventing solutions

- Prescriptive: Document architectural decisions in guide version
- Descriptive (why): Future sessions need context for why code structured certain way

**Testing Code:**
- Prescriptive: Can write test code as implementation task
- Descriptive (why): Test code is deliverable like any other implementation

- Prescriptive: Must NOT run tests or execute validation
- Descriptive (why): Test execution is Step 5; Step 4 focuses on implementation only

---

## 💬 CONSISTENT CLOSING MESSAGE

**When to show**: Only after ALL tasks are implemented and build validation completed (not during implementation)

After completing all tasks and build validation, end with this message format:

```
Please review the complete implementation in active/{problem_id}/user-review/step4_implement.md.

All tasks have been implemented and build validation completed [successfully/with errors noted]. Let me know if you want to add or change anything. When ready, run `/step-done` to advance to Step 5 (Testing & Validation).
```

**Note**: During implementation, DO NOT show closing message after each task. Only show it when ALL work is complete and ready for user review.

**Why end-of-implementation message:**
- User reviews cohesive completed work, not incremental progress
- Single review point more efficient than multiple interruptions
- Implementation flow maintained without context-switching

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** `meta/{problem_id}/step4.md`
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from `input_components/response_summary_format.md`
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from `input_components/meta_file_format.md` exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
