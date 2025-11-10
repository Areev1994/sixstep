## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Generate TWO versions of step5_testing.md:

**USER-REVIEW VERSION**: user-review/step5_testing.md
- Testing summary and status (Passed/Failed/In Progress)
- Test results overview (pass/fail counts, key findings)
- Issues found with severity (Critical/Major/Minor)
- Issues resolved (brief resolution)
- Optimization results (brief impact)
- Next actions needed
- Glanceable format for quick test status review

**GUIDE VERSION**: guide/step5_testing.md
- Comprehensive test documentation
- Complete test methodology
- All test cases with detailed results
- Issues found with:
  - Complete reproduction steps
  - Root cause analysis
  - Resolution details with code references
- Optimization analysis:
  - Performance measurements
  - Optimization techniques applied
  - Impact assessment with data
- Full context for Claude to understand complete testing state

⚠️ **CRITICAL**: You MUST create these two files using Write tool before doing anything else.

## 💬 CONSISTENT CLOSING MESSAGE

**When to show**: Only after completing test execution or presenting test results (not after every question/clarification)

After presenting test results or completing a testing milestone, end with this message format:

```
Please review the test results in active/{problem_id}/user-review/step5_testing.md.

Let me know if you want to add or change anything. When testing is complete and ready to proceed, run `/step-done` to advance to Step 6.
```

**Note**: During iterative testing discussions or debugging, DO NOT show this message after every response. Only show it when you've completed testing activities and are presenting results for user review.

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** meta/{problem_id}/step5.md
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
