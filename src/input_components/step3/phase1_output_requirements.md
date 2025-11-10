## 🎯 PRIMARY OUTPUT REQUIREMENTS (CRITICAL - MUST DO FIRST)

Generate TWO versions of step3_brainstorm.md with TWO-PART structure (Investigation Findings + Solution Design):

**Why two versions:**
- **user-review**: Glanceable shared document for user to see current understanding + plan
- **guide**: Complete context for Claude to maintain full investigation and design state across iterations

**Why two-part structure:**
- **Part 1 (Investigation Findings)**: Shows what was learned following Category 3 approach, updates dynamically as understanding grows
- **Part 2 (Solution Design)**: Appears when understanding is sufficient AND user approves, shows clear solution map for implementation

---

## DOCUMENT STRUCTURE

```markdown
# Investigation & Design v1
*Timestamp*

## PART 1: Investigation Findings
**Following Category 3 Approach:** [One-line summary]

### Finding 1: [Title]
- **What we learned**: [1-2 sentences]
- **Evidence**: [High-level source]

## PART 2: Solution Design
[Appears when investigation sufficient AND user approves]
[Or: "Investigation in progress - design pending"]

**Core Approach:** [2-3 sentence summary]
### Key Design Decisions
### Components Involved
### Trade-offs Considered
```

---

## FORMAT SPECIFICATIONS: User-Review vs Guide

### Part 1: Investigation Findings

| Aspect | User-Review (Glanceable) | Guide (Complete) |
|--------|--------------------------|------------------|
| **Purpose** | Quick scan (2-3 min) | Full context for Claude |
| **Length per finding** | 5-10 lines | Complete details with reasoning |
| **What we learned** | 1-2 sentence finding | Complete finding with all context |
| **Evidence** | High-level mention ("Log analysis") | Specific file:line references, actual measurements |
| **Additional content** | None | **Reasoning**: Why finding matters, how connects to problem, confidence level |
| **Updates** | Add findings as investigation progresses | Document investigation progression, show iterations if relevant |

**Why glanceable user-review**: User sees "what was learned" quickly for rapid feedback; details exist in guide for Claude's use.

### Part 2: Solution Design

| Aspect | User-Review (Glanceable) | Guide (Complete) |
|--------|--------------------------|------------------|
| **When to include** | When criteria met AND user approves | Same - user approval required |
| **Length** | Scan in 2-3 minutes | Complete design rationale |
| **Core Approach** | 2-3 sentence summary | Complete strategy with full rationale + connection to findings |
| **Design Decisions** | What + brief why | What + Why + Implementation considerations + Risks/mitigations |
| **Components** | Component + Role | Current role + New role + Changes required + Dependencies |
| **Trade-offs** | Chosen (benefit + cost), Alternative (why not) | Complete pros/cons analysis, all alternatives with full reasoning |
| **Additional content** | None | **Design Evolution**: If design changed through iterations, **Open Questions**: Future considerations |

**Why glanceable design**: User validates approach without implementation details; design conveys reasoning, not code.

**⚠️ CRITICAL Transition Rule**:
- ❌ DO NOT create Part 2 in same response as first Part 1 - investigation must come first with user feedback
- Ask user: "Should I proceed with solution design?" before adding Part 2
- Why: User may want more investigation, question findings, or change direction

---

## EXAMPLES: Good vs Too Detailed

### Investigation Finding Example

| ✅ User-Review (Good) | ❌ Too Detailed |
|----------------------|-----------------|
| **Finding 1: Operation Breakdown Identified**<br>- What: DebugTool step triggers 10+ DebugProtocol operations, not just single step<br>- Evidence: Log analysis and protocol tracing | **Finding 1: Operation Breakdown**<br>- Detailed packet-by-packet analysis with timestamps<br>- Complete register read sequence<br>- Memory access patterns with addresses<br>- [30+ lines of technical detail] |

### Solution Design Example

| ✅ User-Review (Good) | ❌ Too Detailed |
|----------------------|-----------------|
| **Core Approach:** Optimize register reads by batching requests and using autoexec feature<br><br>**Key Decisions:**<br>- Batch reads: Group multiple ops (reduces round-trips)<br>- Use autoexec: Hardware feature for automatic access<br><br>**Trade-offs:**<br>- Chosen: 80% reduction, requires protocol changes<br>- Alternative (caching): Simpler, only 30% reduction | [Implementation steps with code snippets]<br>[Detailed protocol specifications]<br>[Line-by-line execution plans]<br>[Task breakdown (belongs in Phase 2)]<br>[50+ lines mixing design with implementation] |

---

## CONTENT RULES (Both Versions)

- **Replace, don't append**: Create new versions by replacing old content completely (why: user reads current state, not history; appending creates long non-glanceable documents)
- **Reference, don't embed**: Use file:line references, not code snippets (why: keeps focus on approach; actual code in Step 4)
- **Standalone clarity**: Each version readable without prior versions (why: user may not remember iterations; new collaborators understand quickly)
- **Version control**: Use "# Investigation & Design v2" headers with timestamp (why: clear progression tracking; user knows which version)

---

## BANNED CONTENT (Both Versions)

**Why bans exist**: Maintain glanceable format, separate concerns across framework phases, prevent premature commitment, ensure collaborative workflow

- ❌ **Task lists** (Phase 2), **Code snippets** (Step 4), **"CORRECTED" sections** (replace instead)
- ❌ **Debugging details** (keep at finding level), **Implementation steps** (design approach, not execution)
- ❌ **Investigation + Design in single response** - MUST have user feedback between Part 1 and Part 2 (why: user may question findings or redirect before design effort wasted; violates collaborative workflow)

---

## DYNAMIC DOCUMENT UPDATES

- **Investigation findings**: Add new findings as investigation progresses, update existing if understanding changes (why: document evolves with understanding; investigation is iterative)
- **Solution design**: Add Part 2 when sufficient understanding criteria met AND user approves; show "investigation in progress" until then (why: design requires understanding foundation; premature design leads to wrong solutions)
- **Version updates**: Increment version number, update timestamp, replace content don't append (why: clear progression; old versions in meta logs)

---

⚠️ **CRITICAL**: You MUST create these two files (user-review + guide) using Write tool before doing anything else.

## 💬 CONSISTENT CLOSING MESSAGE

**When to show**: Only after presenting/updating the investigation & design document (not after every question/response in collaborative investigation)

After presenting or updating the document, end with this message format:

```
Please review the investigation findings and design in active/{problem_id}/user-review/step3_brainstorm.md.

Let me know if you want to add or change anything. When investigation is complete and design is approved, run `/step-done` to advance to Phase 2 (task creation).
```

**Why only after document updates**: During iterative investigation, many responses are analyses, questions, discussions; showing closing message after every response is repetitive and adds noise.

---

## 📝 SECONDARY OUTPUT (Meta Logging - Do After Primary Files)

**Target File:** `meta/{problem_id}/step3.md`
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging is for framework tracking only. It is SECONDARY to creating user-facing files above.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
