## PRIMARY SOURCE: Category 3 Approach Pattern

**✅ START HERE**: `active/{problem_id}/guide/step1_questions.md` - **Category 3: Approach Pattern for Stage 2**

**What this provides:**
- The specific investigation strategy to follow in Step 3 Phase 1
- Tells you HOW to increase understanding (break down operations, trace execution, measure timing, compare implementations, etc.)
- This is your investigation roadmap decided in Step 1

**Why Category 3 is primary:**
- Investigation without strategy leads to unfocused exploration
- Step 1 analyzed the problem and decided the best investigation approach
- Following this pattern ensures systematic understanding expansion
- Your job in Stage 2 is to execute this investigation strategy

## CONTEXT SOURCES: Guide Files for Complete Understanding

**✅ READ GUIDE FILES** (complete context with full reasoning, evidence, all iterations):

1. **`active/{problem_id}/guide/step1_questions.md`**
   - **What this provides**: Complete Step 1 context including:
     - Category 1: Clarification question answers (factual gaps filled)
     - Category 2: Context questions (what you'll investigate based on)
     - Category 3: Investigation approach pattern (your strategy)
     - Full reasoning, architectural diagrams with all details
   - **Why you need this**: Understand problem context, see complete architectural understanding, get investigation strategy

2. **`active/{problem_id}/guide/step2_assessment.md`**
   - **What this provides**: Complete Step 2 research findings including:
     - Full answers to Category 2 questions with detailed evidence
     - All source documentation (project memory files read, codebase files examined with file:line references)
     - Search strategy employed, evidence quality assessment, knowledge gaps
   - **Why you need this**: Understand what's already known (factual context), identify what still needs investigation (analytical depth), see evidence quality to assess confidence

**Why guide files over user-review:**
- Guide files contain ALL details Claude needs for informed investigation
- Full reasoning, complete evidence, all file references, all iterations documented
- User-review is concise summary for user glancing - not sufficient for Claude's analysis
- You need complete context to conduct effective investigation

**📋 User-review files** (`active/{problem_id}/user-review/`) **are for user glancing only:**
- Quick status overview without details
- Not sufficient for Claude's investigation work
- Read these for overview, but rely on guide files for complete understanding

## REFERENCE SOURCES

**User-Provided Materials:**
- `active/{problem_id}/input_dump/` - User-provided materials (logs, specs, screenshots, config files, etc.)
- **Why check this**: See Step 1/2 guide files for assessment of relevance to current investigation
- **When to use**: When investigation needs specific measurements, error traces, or configuration details

**Project Memory:**
- `project_memory/architecture/` - Component structure and relationships
  - **Why use**: Understand system architecture when investigating component interactions
- `project_memory/features/` - Feature mechanics and patterns
  - **Why use**: Deep-dive into specific features relevant to your investigation
- `project_memory/solutions/` - Past problem solutions with git diffs
  - **Why use**: Find similar past patterns for investigation inspiration and solution reference
- `project_memory/skills/` - Reusable debugging and investigation techniques
  - **Why use**: Apply proven methodologies for systematic investigation, debugging workflows, analysis techniques

**Why project memory matters:**
- Architecture layer shows verified component relationships (not assumptions)
- Features layer explains how capabilities work (saves re-investigation time)
- Solutions layer provides past patterns with exact git changes (implementation reference)
- Skills layer provides proven techniques for investigation and debugging (systematic approaches)

## DATA SOURCE WORKFLOW

**Step-by-step investigation source usage:**

1. **Read Category 3 approach** from Step 1 guide → Understand investigation strategy
2. **Read Step 1 guide completely** → Get full problem context and architectural understanding
3. **Read Step 2 guide completely** → Get complete factual research and evidence
4. **Glance at user-review files** → Quick overview only (5 min)
5. **Execute Category 3 investigation** → Follow the approach pattern using codebase, measurements, tracing
6. **Reference input_dump as needed** → Get specific measurements or error details
7. **Reference project memory** → Use verified knowledge for architecture/features/past solutions

**Why this sequence:**
- Category 3 gives you direction before diving into details
- Guide files provide complete foundation (context + research + reasoning)
- User-review gives quick orientation but not investigation depth
- Investigation follows systematic strategy, not ad-hoc exploration
- References support investigation but guide files are your foundation