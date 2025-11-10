Claude works in six-step framework. Read claude_intelligence/solution_map_implementation/README.md and claude_intelligence/solution_map_implementation/config.yaml for complete framework details and constraints.

Current session state in claude_intelligence/solution_map_implementation/active/{problem_id}/

## Path Resolution

All paths are relative to `claude_intelligence/solution_map_implementation/`. Prepend working directory + `claude_intelligence/solution_map_implementation/` when reading/writing files.

Example: `active/{problem_id}/guide/step1_questions.md` → `~/solution_map_implementation/active/{problem_id}/guide/step1_questions.md`

## FOUR-STAGE PROBLEM-SOLVING MODEL

The six-step framework maps to four natural stages in problem-solving. Understanding these stages provides context for why each step asks for specific outputs.

**Stage 1: Context Alignment (Steps 1-2)**
This stage brings all relevant context to the forefront. Both user and Claude need to be looking at the same picture - what components are involved, what's the current state, what's known vs unknown. Most importantly, this stage ends with deciding the approach pattern: HOW will understanding be increased in Stage 2? Step 1 identifies what questions need answers and decides the approach pattern for Stage 2. Step 2 answers those questions through research.

**Stage 2: Understanding Expansion (Step 3 Phase 1-2)**
Using the approach pattern decided in Stage 1, this stage increases understanding of the problem until reaching a level where solution can be designed. Phase 1 explores different solution approaches. Phase 2 translates the chosen approach into a concrete task list.

**Stage 3: Solution Translation (Steps 4-5)**
This stage translates the task list into actual implementation. Step 4 implements the tasks. Step 5 validates the implementation through testing.

**Stage 4: Knowledge Documentation (Step 6)**
This stage documents everything learned during the session, updating project memory with verified knowledge for future problems.

Understanding these stages helps frame what each step naturally produces. Step 1 isn't just "ask questions" - it's "identify what questions need answers AND decide approach pattern for Stage 2 (understanding expansion in Step 3)."