Step 3, Phase 2: Task List Creation

## STAGE 2 CONTEXT

**STAGE 2 (Understanding Expansion) - Step 3 Phase 2 (Final Step)**

You are completing Stage 2 of the four-stage problem-solving model. Phase 1 completed investigation and validated solution design with user. Now in Phase 2, you translate that validated design into a reviewable task list for implementation.

**Why Phase 2 matters:**
- Investigation (Phase 1 Part 1) provided understanding of how system works
- Solution Design (Phase 1 Part 2) defined WHAT to build and WHY
- Task List (Phase 2) defines HOW to build it - concrete implementation tasks
- User reviews tasks to ensure nothing missed before Step 4 implementation

## PHASE 1 → PHASE 2 TRANSITION

**Phase 1 delivered** (already complete):
- Part 1: Investigation Findings (what was learned)
- Part 2: Solution Design (validated approach with user approval)

**Phase 2 job** (your current task):
- Create task list from Phase 1 Part 2 (Solution Design)
- Tasks translate design decisions into concrete implementation steps
- User reviews task list, provides feedback, approves before Step 4

**Why this transition:**
- Design without tasks is abstract; tasks make it concrete and reviewable
- User validates task breakdown before implementation effort begins
- Proper task granularity ensures Step 4 is manageable and trackable

## PURPOSE

**Task List Creation**: Translate validated solution design (Phase 1 Part 2) into concrete, reviewable implementation tasks.

**Why task list:**
- Makes abstract design concrete and actionable
- Enables user to validate nothing is missed before implementation
- Provides clear roadmap for Step 4 implementation
- Allows proper effort estimation and sequencing

## APPROACH

**Task Creation Process:**
- Prescriptive: Read Phase 1 Part 2 (Solution Design) from guide/step3_brainstorm.md as primary source for task derivation
- Descriptive (why): Design has complete rationale, components involved, design decisions - tasks must implement all of this

- Prescriptive: Create reviewable tasks at TOP of step3_brainstorm.md using checkbox format: `- [ ] Task description`
- Descriptive (why): Prepending tasks to existing document keeps Investigation + Design context visible; checkbox format enables tracking in Step 4

- Prescriptive: Tasks should be small enough to be reviewable but not micro-tasks; group related changes into logical pieces
- Descriptive (why): Too large = hard to review and track; too small = overwhelming noise; logical grouping = reviewable units

- Prescriptive: Each task description should be concise, actionable, and include implementation patterns when relevant
- Descriptive (why): Concise = quick to review; actionable = clear what to do; patterns = guides proper implementation approach

- Prescriptive: ULTRATHINK when creating task list - analyze solution design thoroughly to understand proper implementation approach
- Descriptive (why): Hasty task lists miss critical pieces; thorough analysis ensures complete coverage of design decisions

## ARCHITECTURE GUIDANCE

- Prescriptive: Perform architecture pattern recognition for features being implemented - analyze existing code patterns to determine proper placement
- Descriptive (why): New code should follow established conventions, not generic placement; patterns ensure consistency

- Prescriptive: Look for similar existing implementations to understand proper architectural layers and module boundaries
- Descriptive (why): Existing patterns reveal project's architecture philosophy; following them maintains codebase coherence

- Prescriptive: Decide on specific files and functions to change or add based on architectural analysis
- Descriptive (why): Vague tasks ("update API") lead to wrong implementation; specific tasks ("modify parse_request() in api/handlers.cpp") guide correctly

## TASK GRANULARITY

- Prescriptive: Group related changes into logical implementation tasks rather than individual file changes
- Descriptive (why): One task = "Implement command-line flag support" with sub-bullets for specific files; NOT separate tasks per file

- Prescriptive: Use sub-descriptions under main tasks to show specific changes without creating micro-tasks
- Descriptive (why): Main task = reviewable unit; sub-bullets = implementation details; balance between overview and specificity

- Prescriptive: Focus on implementation areas (functionality) rather than file-focused changes (mechanics)
- Descriptive (why): Functionality framing ("Add caching layer") is reviewable; file framing ("Edit cache.cpp") is too granular

- Prescriptive: Each main task should represent one cohesive piece of functionality with bullets showing specific changes needed
- Descriptive (why): Cohesive functionality = logical review unit; specific bullets = implementation guidance without micro-management

## CRITICAL TESTING RULE

**What tasks CAN include:**
- Prescriptive: Tasks CAN include "Write tests for X" (implementing test code)
- Descriptive (why): Writing test code is implementation work that happens in Step 4; test code is deliverable

**What tasks should NOT include:**
- Prescriptive: Tasks should NOT include "Run tests", "Verify results", "Validate performance", "Measure timing"
- Descriptive (why): Running tests, verification, validation are Step 5 activities; Step 4 is implementation only

**Summary**: Writing test code = implementation (Step 4, include in tasks). Running/validating tests = testing (Step 5, exclude from tasks).

## CRITICAL CONSTRAINT

- Prescriptive: Do NOT create task list until Phase 1 solution design is validated with user
- Descriptive (why): Tasks implement design; if design changes after tasks created, rework wasted

- Prescriptive: Tasks should produce concrete code output that can be quickly verified
- Descriptive (why): Vague tasks ("improve performance") hard to verify complete; concrete tasks ("implement batching in protocol handler") clearly done when code exists

- Prescriptive: Simple task descriptions without complex evaluation criteria
- Descriptive (why): Complex criteria ("achieve 50% speedup") belong in Step 5 validation; tasks just describe what to implement

## FORMAT

- Prescriptive: Simple checkbox format at very top of step3_brainstorm.md document: `- [ ] Task description`
- Descriptive (why): Top placement = first thing user sees; checkbox = trackable in Step 4; simple format = quick to scan

## THINGS NOT TO DO

**NEVER DO THESE ACTIONS:**
- ❌ DO NOT execute `framework_state.py advance` - framework advancement is handled automatically by the system
- ❌ DO NOT write or modify code (save for Step 4)
- ❌ DO NOT perform testing or validation (save for Step 5)
- ❌ DO NOT create task list before Phase 1 solution design is validated with user
- ❌ DO NOT create overly granular micro-tasks that focus on individual file changes
- ❌ DO NOT include "Run tests" or "Verify X" tasks (those are Step 5 activities, not Step 4 implementation)

**Why these constraints:**
- Framework state managed by `/step-done` command
- Code changes happen in Step 4 after tasks approved
- Testing/validation happens in Step 5 after implementation complete
- Tasks without validated design = wasted effort if design changes
- Micro-tasks create overwhelming noise; logical units are reviewable
- Implementation tasks describe what to build; validation tasks verify it works (different steps)

## USER PREFERENCES (Auto-Generated)

- When defining test scope in tasks, prefer simple pattern-based implementations over comprehensive coverage unless explicitly requested. Follow existing test patterns rather than creating elaborate test scenarios.
- When tasks involve proposing solutions, structure them to establish background/problem context first before presenting the solution approach.
- When user proactively provides architecture clarifications during task creation (e.g., "there is a ripple2 class"), immediately update tasks to reflect the clarified architecture instead of deferring to implementation discovery.
