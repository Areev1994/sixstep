USER-PROVIDED INPUTS (Check FIRST):
- active/{problem_id}/input_dump/ - User-provided materials (logs, specs, screenshots, config files, etc.)
- Check this directory FIRST for problem-specific evidence before searching project memory or codebase
- If empty, proceed to context sources below

---

PRIMARY CONTEXT SOURCES:
Read guide files from previous steps for complete context:
- active/{problem_id}/guide/step1_questions.md - Contains Category 1 answers (use for context), Category 2 questions (answer these), Category 3 approach (for Step 3, not Step 2)

---

PROJECT MEMORY SOURCES:

**Project Memory Structure**:
- Built incrementally through six-step sessions (may be incomplete)
- Four layers: Architecture → Features → Solutions → Skills
- Start with project memory before searching codebase
- Solutions layer contains git diffs from past implementations
- Skills layer contains reusable techniques for analysis/research

---

**1. Architecture Layer**:
- `project_memory/architecture/system_overview.md` - System-wide component relationships diagram
- `project_memory/architecture/[component]/README.md` - Component roles, internal diagrams, source locations, key interfaces

**2. Features Layer**:
- `project_memory/features/[feature]/README.md` - What feature is, why it exists, when to use
- `project_memory/features/[feature]/how_it_works.md` - Technical architecture, execution flow, mechanisms
- `project_memory/features/[feature]/usage_patterns.md` - Pattern catalog with examples
- `project_memory/features/[feature]/api_reference.md` - Complete API documentation

**3. Solutions Layer**:
- `project_memory/solutions/*.md` - Past problem patterns with git commit IDs or full diffs
- Each solution includes: problem summary, components involved, approach, git diffs, key files modified, lessons learned

**4. Skills Layer**:
- `project_memory/skills/*.md` - Reusable techniques and methodologies
- Analysis techniques (log correlation, performance profiling, data flow tracing)
- Research methodologies (systematic investigation approaches, metric extraction)
- Each skill includes: what it is, when to use, step-by-step procedure, examples, common pitfalls

---

CODEBASE SEARCH SOURCES (Secondary - after project memory):
- Source code and headers
- Documentation and README files
- Configuration and build files
- Logs and test data

**SEARCH SEQUENCE**: Project memory (Architecture → Features → Solutions → Skills) → Codebase (code → docs → configs → logs)

---

**EXAMPLE**:

Problem: "Optimize database query performance"

**Step 1 Category 2 question:** "What is current query execution time?"

1. **User-provided inputs**: Check input_dump/ for performance logs
2. **Architecture Layer**: Read `architecture/system_overview.md` and `architecture/database/README.md` for database structure
3. **Features Layer**: Read `features/query_optimization/README.md` for optimization capabilities
4. **Solutions Layer**: Check `solutions/database_performance_*.md` for past optimizations with git diffs
5. **Codebase**: Search database configuration, query implementations
6. **Result**: Answer "Current execution time is 3-5 seconds based on logs in input_dump/"

Reference Step 1 Category 1 (clarification) answers for context. Answer Category 2 questions with factual evidence. Use Grep/Glob tools with question-specific terms.