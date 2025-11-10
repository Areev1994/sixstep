## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Generate TWO versions of step1_questions.md with THREE-CATEGORY structure:

---

### USER-REVIEW VERSION: user-review/step1_questions.md

**Glanceable format for quick user review.**

**REQUIRED STRUCTURE:**

**1. CLARIFICATION QUESTIONS** (if problem statement incomplete)
- 0-2 questions only
- Collect answers immediately in Step 1 before proceeding
- If problem is complete, state "Problem statement is complete - no clarification needed"
- **User answers these in Step 1**

**2. BRINGING RELEVANT INFORMATION TO FOREFRONT**
- **Architectural diagram** (REQUIRED) showing anticipated components involved
  - Text/ASCII art format
  - Formatted to make sense for problem (data flow, relationships, etc.)
  - Based on current understanding (may be refined in Step 2)
- Context questions (2-4 questions):
  - "What is X?"
  - "What is current state of Y?"
  - "Which components interact for this operation?"
  - **NO answers provided - these will be answered in Step 2**
- **User can modify/add/remove questions**

**3. APPROACH PATTERN FOR STAGE 2**
- Single statement (1-2 sentences)
- Explains investigation strategy for Stage 2 (understanding expansion in Step 3)
- Example: "Break down operation into steps and measure timing at each step"
- **Note:** This is for Stage 2 (Step 3), not for Step 2 which just answers Category 2 questions
- **User can modify this approach**

**FORMAT:** Clean, glanceable. User can quickly review questions and approach, make modifications before Step 2.

---

### GUIDE VERSION: guide/step1_questions.md

**Complete context for Claude to understand full reasoning.**

**REQUIRED STRUCTURE:** Same 3 categories as user-review, PLUS detailed reasoning:

**1. CLARIFICATION QUESTIONS**
- Questions (if any)
- For each question: Why it qualifies as CLARIFICATION (what gap in problem statement?)
- User answers (collected in Step 1)
- If empty: Explain why problem statement is complete

**2. BRINGING RELEVANT INFORMATION TO FOREFRONT**
- Architectural diagram (same as user-review)
- **Diagram explanation:**
  - Which project_memory sources were used
  - What codebase searches were performed (if any)
  - Why diagram is formatted this way for this problem
  - What was found vs. what's missing
  - Note: This is anticipated architecture based on current understanding, may be refined in Step 2
- Context questions (WITHOUT answers)
- For each question:
  - Why this context is relevant
  - Why this reflects user's natural thought progression
  - How this will be answered in Step 2
  - User can modify these questions

**Handling Uncertainty in Diagrams:**

When components or relationships are based on unverified information (light codebase search), mark them as uncertain rather than stating as facts.

❌ **BAD (states unverified as facts):**
```
┌─────────────────────┐
│  auth_handler.py    │  ← found via light search, stated as fact
│  (Authenticator)    │  ← claimed role without verification
└─────────────────────┘
```

❌ **ALSO BAD (adds speculative details):**
```
┌────────────────────────────────────┐
│  DebugTool Integration             │
│  (PythonBindings/Core bindings)    │  ← speculative details added
└────────────────────────────────────┘
```

❌ **ALSO BAD (shows unverified internals):**
```
┌────────────────────────────┐
│  API Core                  │
│  1. Disable watchpoints    │  ← internal sequence
│  2. Single step            │  ← not verified yet
│  3. Re-enable watchpoints  │  ← don't show in Step 1
└────────────────────────────┘
```

✅ **GOOD (shows complete uncertainty):**
```
┌───────────────────────────┐
│  DebugTool Integration?   │  ← question mark shows uncertainty
└───────────────────────────┘
```

✅ **ALSO GOOD (minimal generic label):**
```
┌─────────────────────┐
│  Integration Layer  │
│  (TBD in Step 2)    │  ← no specifics, just marks as TBD
└─────────────────────┘
```

**Key principle:** If uncertain, prefer showing "Component?" over "Component (with speculative details)".

Use "?", "TBD", or generic placeholders when uncertain. DO NOT add:
- Specific file/module names found via light search (e.g., "PythonBindings", "CoreFramework")
- Protocol/technology options in lists (e.g., "ProtocolA/ProtocolB", "USB/Network/Serial")
- Internal sequences or steps (save for Step 2 analysis)
- Parenthetical details that are speculative (e.g., "(API bindings)", "(handles auth)")

**When uncertain about component:**
- ✅ Show: "Component?" or "Integration Layer (TBD)"
- ❌ Don't show: "Component (SpecificTech/SpecificModule)" or "Component: Protocol1/Protocol2"

**Exception - Verified Examples with "like" Notation:**

When examples are from VERIFIED sources (project_memory or user input), you can use "like X, Y":

✅ **GOOD (verified examples):**
```
┌────────────────────────────────┐
│  Database Layer                │
│  (like SQL, NoSQL)             │  ← project_memory confirms these types exist
└────────────────────────────────┘
```

✅ **ALSO GOOD (verified examples):**
```
┌────────────────────────────────┐
│  Protocol                      │
│  (like HTTP, WebSocket)        │  ← user mentioned these protocols
└────────────────────────────────┘
```

❌ **BAD (slash notation - implies exhaustive):**
```
┌────────────────────────────────┐
│  Database (SQL/NoSQL)          │  ← slash suggests ONLY these two
└────────────────────────────────┘
```

❌ **BAD (unverified examples):**
```
┌────────────────────────────────┐
│  Protocol                      │
│  (like HTTP, gRPC)             │  ← found via light search, not verified
└────────────────────────────────┘
```

**Rule:** "like X, Y" signals:
1. X and Y are verified examples from project_memory or user input
2. There might be other options (non-exhaustive)

**Only use "like" notation with verified examples. If unverified, use "?" or "TBD" instead.**

**3. APPROACH PATTERN FOR STAGE 2**
- Approach statement (same as user-review)
- **Reasoning:**
  - Why this approach fits the problem
  - How it builds on questions from Category 2
  - What user should expect in Stage 2 (Step 3 Phase 1-2)
  - Clarify: This is for Stage 2 (understanding expansion in Step 3), not for Step 2 (which answers Category 2 questions)
  - User can modify this approach

**ADDITIONAL CONTEXT IN GUIDE:**
- Why each category has the content it does
- What technical analysis was deliberately avoided (saved for Step 2)
- How Categories 2-3 might change if Category 1 reveals new information
- How collaboration/alignment was emphasized
- How questions build on each other in natural learning progression

---

⚠️ **CRITICAL:** Create these two files using Write tool BEFORE anything else.

**CRITICAL:**
- Category 1 questions: Collect user answers immediately in Step 1, update Categories 2-3 if needed
- Category 2 questions: NO answers in Step 1 - will be answered in Step 2
- Category 3 approach: For Stage 2 (Step 3), user can modify before Step 2 begins
- Document all Category 1 answers in BOTH versions

## 💬 CONSISTENT CLOSING MESSAGE

After completing your response, ALWAYS end with this message format:

```
Please review the questions in active/{problem_id}/user-review/step1_questions.md.

The output has three categories:
1. CLARIFICATION - factual gaps in problem statement (please answer if present)
2. BRINGING INFO TO FOREFRONT - questions to research in Step 2 (you can modify/add/remove)
3. APPROACH PATTERN - how I'll expand understanding in Stage 2/Step 3 (you can change this approach)

Let me know if you want to modify questions or approach. When ready to proceed, run `/step-done` to advance to Step 2.
```

**Note:** This closing message should appear after EVERY response in Step 1.

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** meta/{problem_id}/step1.md
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
