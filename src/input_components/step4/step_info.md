Step 4: Implementation

## STAGE 3 CONTEXT

**STAGE 3 (Solution Translation) - Step 4 (Implementation)**

You are in Stage 3 of the four-stage problem-solving model. Stages 1-2 completed context alignment and understanding expansion. Now in Stage 3, you translate the task list into working code.

**Why Stage 3 matters:**
- Stage 1 (Steps 1-2) aligned on problem context and decided approach
- Stage 2 (Step 3) investigated how system works and designed solution with task breakdown
- Stage 3 (Steps 4-5) translates design into reality: Step 4 implements, Step 5 validates
- Step 4 produces working code; Step 5 verifies it works correctly

## PURPOSE

**Implementation**: Work through task list from Step 3 Phase 2, implementing all tasks to produce working code.

**Why implementation focus:**
- Task list came from validated solution design (Step 3 Phase 2)
- Each task represents concrete implementation work
- Goal is working code that compiles and integrates properly
- Testing and validation happen in Step 5, not here

## APPROACH

**Task Execution Workflow:**

- Prescriptive: Work through ALL tasks in one stretch (unless user requests otherwise)
- Descriptive (why): Continuous implementation maintains flow and context; completing related tasks together ensures coherent changes

- Prescriptive: Work tasks sequentially in the order listed
- Descriptive (why): Task order from Step 3 reflects logical implementation sequence; dependencies and build-up structured correctly

- Prescriptive: Mark each task complete immediately after implementing it (update checkboxes in both user-review and guide step4_implement.md files)
- Descriptive (why): Real-time tracking shows progress; keeps implementation state current; user can see what's done at any point

- Prescriptive: Build validation ONLY after ALL tasks are implemented, using commands from project_commands/build.md
- Descriptive (why): Final build validates complete integration of all changes together; project_commands/ contains project-specific commands ensuring correct build process

- Prescriptive: Present complete implementation to user at the end (after all tasks done and build validated)
- Descriptive (why): User reviews finished work as cohesive whole; avoids context-switching during implementation flow

## BUILD VALIDATION STRATEGY

- Prescriptive: Build ONLY after ALL tasks are implemented (not incrementally during implementation)
- Descriptive (why): Final build validates complete integration of all changes together; incremental builds interrupt flow without adding value in Step 4

- Prescriptive: Use build commands ONLY from project_commands/build.md - do NOT guess or improvise build commands
- Descriptive (why): Project-specific commands ensure correct build process; guessing can break build system or miss critical validation steps; each project has unique build requirements

- Prescriptive: If project_commands/build.md doesn't exist, skip build validation entirely
- Descriptive (why): Not all projects have standardized build commands; framework adapts to project structure; validation can happen in Step 5 instead

- Prescriptive: Build validates compilation success (syntax, integration), NOT functional correctness
- Descriptive (why): Step 4 goal is code that compiles cleanly; functional testing happens in Step 5

## TESTING RULE

**What Step 4 CAN do:**
- Prescriptive: Can write test code as part of implementation tasks
- Descriptive (why): Writing test code is implementation work; test files are code deliverables like any other implementation

**What Step 4 should NOT do:**
- Prescriptive: Must NOT run tests, execute validation, verify results, or measure performance
- Descriptive (why): Running tests and validation are Step 5 activities; Step 4 focuses on implementation only; clear separation between implementation and validation stages

**Summary**: Writing test code = implementation (Step 4, OK). Running/validating tests = testing (Step 5, NOT OK).

## ARCHITECTURE GUIDANCE

- Prescriptive: ALWAYS examine existing similar implementations before creating new code
- Descriptive (why): Pattern matching ensures consistency with established conventions; avoids reinventing solutions that already exist

- Prescriptive: Look for established patterns in the same module/file for new functions
- Descriptive (why): Local patterns reveal module-specific conventions; following them maintains module coherence

- Prescriptive: Follow API conventions - check function signatures, parameter types, return patterns
- Descriptive (why): API consistency prevents integration issues; callers expect specific interfaces

- Prescriptive: Study related functions to understand proper error handling and resource management
- Descriptive (why): Error handling and resource cleanup patterns are project-critical; inconsistency causes bugs and leaks

- Prescriptive: Match existing code style, variable naming, and structure patterns
- Descriptive (why): Code consistency improves readability and maintainability; reduces cognitive load for future developers

- Prescriptive: Verify architectural placement - ensure functions go in appropriate modules
- Descriptive (why): Proper module boundaries prevent circular dependencies and maintain clean architecture

- Prescriptive: Check for existing utility functions before implementing new ones
- Descriptive (why): Reduces code duplication; leverages tested functionality; maintains single source of truth

- Prescriptive: Analyze import/include patterns to understand module dependencies
- Descriptive (why): Dependency structure reveals architectural layers; following patterns prevents breaking dependencies

## CODE QUALITY

- Prescriptive: Write clean, self-documenting code with NO inline comments
- Descriptive (why): Good code explains itself through structure and naming; comments rot as code changes; self-documenting code stays current

- Prescriptive: Use descriptive variable names and function names to convey intent
- Descriptive (why): Names are documentation that can't get out of sync; clear names eliminate need for comments

- Prescriptive: Structure code clearly so intent is obvious from the code itself
- Descriptive (why): Clear structure reduces cognitive load; obvious intent prevents misunderstandings

- Prescriptive: DO NOT add inline comments - code should be self-explanatory
- Descriptive (why): If code needs comments to explain, restructure code instead; comments are maintenance burden

- Prescriptive: Follow existing codebase patterns and conventions rigorously
- Descriptive (why): Consistency is more valuable than personal preference; uniform code is easier to understand and maintain

- Prescriptive: Maintain consistency with surrounding code style
- Descriptive (why): Style discontinuities are jarring; consistent style improves readability across entire codebase

- Prescriptive: Perform architectural pattern matching before implementation
- Descriptive (why): Understanding existing patterns prevents architectural violations; ensures changes fit naturally into codebase

## VALIDATION APPROACH

- Prescriptive: Verify API compatibility and calling conventions match established patterns
- Descriptive (why): API mismatches cause integration failures; following patterns ensures proper integration

- Prescriptive: Check error handling follows project conventions
- Descriptive (why): Consistent error handling enables proper error propagation and debugging

- Prescriptive: Ensure proper resource management (memory, handles, etc.)
- Descriptive (why): Resource leaks cause system instability; proper cleanup is critical for reliability

- Prescriptive: Validate function placement and module boundaries
- Descriptive (why): Proper boundaries maintain clean architecture; violations create technical debt

- Prescriptive: Build after ALL implementation complete - run build command from project_commands/build.md
- Descriptive (why): Final build verifies code compiles cleanly and integrates properly; project_commands/ ensures correct build process

- Prescriptive: Compilation-focused validation - success means code compiles, not that it works correctly
- Descriptive (why): Step 4 delivers compilable code; functional correctness validated in Step 5

## THINGS NOT TO DO

**NEVER DO THESE ACTIONS:**
- ❌ DO NOT execute `framework_state.py advance` - framework advancement is handled automatically by /step-done command
- ❌ DO NOT work on multiple tasks simultaneously - work sequentially one at a time
- ❌ DO NOT guess build commands - use project_commands/build.md only (or skip if file doesn't exist)
- ❌ DO NOT run tests or validation - write test code only, execution happens in Step 5
- ❌ DO NOT build incrementally during implementation - build once at the end only

**Why these constraints:**
- Framework state managed by /step-done command (not manual advancement)
- Sequential task execution maintains clear progression and context
- Project-specific build commands ensure correct process; guessing breaks builds
- Implementation (Step 4) and validation (Step 5) are separate stages
- Incremental builds interrupt flow without adding value; final build validates complete integration

## USER PREFERENCES (Auto-Generated)

- User actively corrects over-engineering and enforces existing codebase patterns over new abstractions
- User prefers brief, decisive task progression without verbose explanations or confirmations
- When copying task lists from Step 3, include the detailed implementation comments below each task item, as these provide critical implementation specifications that must be followed during Step 4.
- When terminology is too generic, check project_memory documentation for more accurate technical terms before making changes.
- For iterative refinement tasks (like email drafting), expect multiple small adjustment rounds where user provides direct feedback on specific phrases or wordings.
- User values politeness and respectful tone in external communications (e.g., "please let me know what time works best") and expects timezone considerations to be explicitly mentioned.
- When drafting external communications (emails, messages), present context/quotes from the other party before asking clarification questions to maintain conversational flow.
- When user indicates that actual implementation already exists in a specific commit, use git checkout to apply that exact implementation rather than implementing from scratch.
