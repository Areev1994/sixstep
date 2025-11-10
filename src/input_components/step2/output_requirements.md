## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Generate TWO versions of step2_assessment.md:

**USER-REVIEW VERSION**: user-review/step2_assessment.md

**PURPOSE**: Glanceable status overview - user can quickly see answers without reading details.

**FORMAT RULES**:
- Keep each question answer to 5-10 lines maximum
- Answer summary: 1-2 sentences stating the factual answer (not detailed breakdown)
- Evidence: High-level only (e.g., "Found in user logs and codebase", not specific line numbers)
- NO detailed breakdowns, sequences, or explanations (save for guide version)

**STRUCTURE**:
- Start with "Step 1 Category 1 (Clarification) Questions and Answers" section (if any)
- For each Step 1 Category 2 question:
  - Question text
  - **Status**: Fully Answered / Partially Answered / Unanswered
  - **Confidence**: High / Medium / Low
  - **Answer**: 1-2 sentence factual answer (what is it, what's the measurement, etc.)
  - **Evidence**: High-level source mention (e.g., "User logs, system configuration files")
- Note: Category 3 (Approach Pattern) guides Step 3 - not answered in Step 2
- Total document should be scannable in under 1 minute

**EXAMPLE - Glanceable Question Entry:**
```
### Question: What is current query execution time?

**Status**: Fully Answered
**Confidence**: High
**Answer**: Current execution time is 3-5 seconds based on performance logs.
**Evidence**: User-provided logs, database configuration files
```

**NOT THIS (too detailed for user-review):**
```
### Question: What is current query execution time?

**Status**: Fully Answered
**Confidence**: High

**Answer Summary**:
- Detailed breakdown of timing
- Multiple measurements with timestamps
- Step-by-step sequence
- Technical analysis...
[50+ lines of detail]
```

**Remember**: User-review is for STATUS checking, not detailed research reading. Details go in guide version.

---

**GUIDE VERSION**: guide/step2_assessment.md
- Complete "Step 1 Category 1 (Clarification) Questions and Answers" section
- For each Step 1 Category 2 question:
  - Question text
  - Status with detailed reasoning
  - Confidence level with full justification
  - Complete factual answer with all context
  - **Detailed source documentation**:
    - Project memory files read (architecture/features/solutions)
    - Codebase files examined with specific file:line references
    - Git commits/diffs referenced from solutions layer
    - What was searched in project memory but not found
    - What was searched in codebase but yielded no results
  - Search strategy employed (three-layer approach)
  - Evidence quality assessment
  - Knowledge gaps identified
- Full reasoning for Claude to understand complete research state

⚠️ **CRITICAL**: You MUST create these two files using Write tool before doing anything else.

## 💬 CONSISTENT CLOSING MESSAGE

After completing your response, ALWAYS end with this message format:

```
Please review the research findings in active/{problem_id}/user-review/step2_assessment.md.

Let me know if you want to add or change anything. When ready to proceed, run `/step-done` to advance to Step 3.
```

**Note**: This closing message should appear after EVERY response in Step 2, ensuring user knows where to review and how to proceed.

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** meta/{problem_id}/step2.md
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
