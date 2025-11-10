## STEP 6 APPROACH: IDENTIFY VERIFIED KNOWLEDGE FROM THIS SESSION

**Context**: Project memory is incomplete, built incrementally through six-step sessions.

**Your approach for THIS Step 6**:
1. Read Steps 1-5 guide files completely
2. Identify NEW verified knowledge from THIS session that future sessions will need
3. Determine which project memory layers to update with THIS session's knowledge

**What to look for in Steps 1-5:**
- **Architecture additions**: Component relationships, hardware variants, system connections discovered during THIS session's investigation
- **Skills to capture**: Analysis/debugging techniques used during THIS session that are reusable across problems
- **Solution pattern**: Always created for THIS session's problem (main deliverable)
- **Features**: Only if THIS session created new capability or documented existing capability mechanics

**Incremental growth mindset**: Each session contributes verified knowledge → project memory grows richer → future sessions start with more context.

---

## PRIMARY CONTEXT SOURCES: Steps 1-5 (Guide + User-Review)

Read guide files from ALL previous steps for complete context:

**Step 1 - Problem Understanding:**
- **Guide**: `active/{problem_id}/guide/step1_questions.md`
  - What: Complete problem context with reasoning, Category 2/3 questions, architectural diagrams
  - Why: Original problem requirements inform what knowledge should be documented
- **User-review**: `active/{problem_id}/user-review/step1_questions.md`
  - What: Problem summary with key questions
  - Why: Quick reference for problem statement

**Step 2 - Current State Assessment:**
- **Guide**: `active/{problem_id}/guide/step2_assessment.md`
  - What: Complete factual research with evidence, sources, all answered questions
  - Why: Research findings reveal what was learned about the system
- **User-review**: `active/{problem_id}/user-review/step2_assessment.md`
  - What: Assessment summary with answer status
  - Why: Quick reference for factual findings

**Step 3 - Solution Design:**
- **Guide**: `active/{problem_id}/guide/step3_brainstorm.md`
  - What: Investigation findings, solution design with full rationale, task breakdown
  - Why: Solution approach and design decisions form core of solution pattern
- **User-review**: `active/{problem_id}/user-review/step3_brainstorm.md`
  - What: Solution summary with key design decisions
  - Why: Quick reference for solution approach

**Step 4 - Implementation:**
- **Guide**: `active/{problem_id}/guide/step4_implement.md`
  - What: Complete implementation log with architectural decisions, challenges, resolutions, build results
  - Why: Implementation details and code rationale feed into solution pattern
- **User-review**: `active/{problem_id}/user-review/step4_implement.md`
  - What: Implementation summary with task completion and files modified
  - Why: Quick reference for what changed

**Step 5 - Testing & Validation:**
- **Guide**: `active/{problem_id}/guide/step5_testing.md`
  - What: Complete test documentation with methodology, results, issues found and resolved
  - Why: Validation results and lessons learned inform solution pattern and skills
- **User-review**: `active/{problem_id}/user-review/step5_testing.md`
  - What: Test status summary with pass/fail overview
  - Why: Quick reference for validation outcome

**Why guide vs user-review:**
- Guide files: Complete reasoning, evidence, full context needed for accurate curation
- User-review files: Glanceable summaries for quick reference during curation
- Both needed: Guide for depth, user-review for rapid lookup

---

## GIT CONTEXT SOURCES

Use git commands to extract implementation commits and diffs:

**Find relevant commits:**
```bash
# Commits from timeframe (adjust based on step4/step5 duration)
git log --oneline --since="3 days ago"

# Commits by current author
git log --oneline --author="$(git config user.name)" -n 10

# Commits with specific file changes
git log --oneline -- path/to/modified/file.cpp
```

**Get commit details:**
```bash
# Full diff for a specific commit
git show <commit_id>

# Short stat for commit (files changed summary)
git show --stat <commit_id>

# Diff between two commits (before and after implementation)
git diff <before_commit>..<after_commit>
```

**Identify implementation commits:**
- Review `active/{problem_id}/guide/step4_implement.md` for timeframe when code was written
- Match commit messages to tasks from `active/{problem_id}/guide/step3_brainstorm.md`
- Include all commits that are part of the solution

**Why git context:**
- Solutions must include exact code changes for future reference
- Git commits/diffs provide verifiable implementation details
- Future sessions can see actual code patterns used

---

## PROJECT MEMORY SOURCES

Analyze existing project memory to understand current state:

**Architecture Layer:**
- `project_memory/architecture/system_overview.md` - Current system understanding
- `project_memory/architecture/*/README.md` - Component-specific knowledge

**Features Layer:**
- `project_memory/features/*/README.md` - Feature overviews
- `project_memory/features/*/how_it_works.md` - Technical deep-dives

**Solutions Layer:**
- `project_memory/solutions/*.md` - Existing solution patterns
- Identify if current problem extends or relates to existing patterns

**Skills Layer:**
- `project_memory/skills/*.md` - Existing techniques and methodologies
- Identify if current session learned techniques similar to existing skills

**Why analyze existing project memory:**
- Avoid duplicating knowledge that already exists
- Link to related existing knowledge (cross-references)
- Build on previous patterns rather than starting fresh
- Identify gaps that this session fills

---

## CURATION FOCUS

**Primary Deliverable**: Solution pattern with git context (ALWAYS create)

**Conditional Updates**:
- **Architecture**: Update if new component relationships discovered or system structure expanded
- **Features**: Update if new feature created or existing feature mechanics need documentation
- **Skills**: Create if reusable technique/methodology learned during this session
