## PRIMARY SOURCE: Step 3 Task List

**✅ START HERE**: `active/{problem_id}/guide/step3_brainstorm.md` - Complete task list with implementation context

**What this provides:**
- Complete task breakdown from Step 3 Phase 2 with detailed implementation specifications
- Task order reflecting logical implementation sequence
- Solution design context (Part 2) showing what tasks implement
- Investigation findings (Part 1) showing why solution needed

**Why primary:**
- Tasks define exactly what to implement (concrete deliverables)
- Guide version has full implementation details and rationale from design
- Task order structured for proper dependencies and build-up
- Complete context ensures implementation aligns with validated solution design

## CONTEXT SOURCES: Previous Steps Guide Files

**Read ALL guide files for complete context:**

**`active/{problem_id}/guide/step1_questions.md`** - Problem context and approach pattern
- What it provides: Complete problem understanding, Category 3 approach pattern that guided Step 3 investigation
- Why needed: Understanding original problem and investigation approach informs implementation decisions

**`active/{problem_id}/guide/step2_assessment.md`** - Factual research and current state
- What it provides: Complete factual context about system state, components involved, constraints discovered
- Why needed: Facts about current system inform how to implement changes properly

**Why guide files over user-review:**
- Guide files contain complete reasoning, evidence, and context
- User-review files are glanceable summaries insufficient for implementation decisions
- Full context prevents implementation mistakes from incomplete understanding

## REFERENCE SOURCES: Project Memory

**Architecture Layer** (`project_memory/architecture/`)
- What it provides: Component structure, relationships, where code belongs in codebase
- Why needed: Shows where new code should be placed, existing component interactions, architectural boundaries

**Features Layer** (`project_memory/features/`)
- What it provides: How system features work, usage patterns, implementation conventions
- Why needed: Established patterns for how features are implemented in this project; follow these patterns

**Solutions Layer** (`project_memory/solutions/`)
- What it provides: Past implementation patterns for similar problems with git references
- Why needed: Proven approaches and lessons learned; similar patterns can be adapted

**Why project memory matters:**
- Verified knowledge from previous six-step sessions
- Shows established conventions and patterns specific to this project
- Prevents reinventing solutions that already exist

## PROJECT COMMANDS: Build Validation

**`project_commands/build.md`** - Project-specific build commands (if exists)
- What it provides: Exact build commands for this project (compilation, linking, validation)
- Why needed: Each project has unique build process; these commands ensure correct compilation validation
- Critical: DO NOT guess build commands - use these exact commands or skip build if file doesn't exist

**Why project_commands/ not guessing:**
- Build processes are project-specific and complex
- Wrong commands can break build system or miss validation steps
- Explicit commands guarantee repeatability and correctness

## CODEBASE: Architectural Analysis Sources

**Similar existing implementations**
- What to find: Functions similar to what you're implementing in same module
- Why examine: Pattern matching ensures consistency with established code; reveals module-specific conventions

**API documentation and header files**
- What to find: Function signatures, parameter types, return patterns
- Why examine: Correct interfaces prevent integration issues; following API conventions ensures compatibility

**Error handling patterns in related code**
- What to find: How errors are detected, reported, and propagated in similar functions
- Why examine: Consistent error handling critical for reliability; project-specific conventions must be followed

**Import/include dependencies**
- What to find: What modules/headers are imported in target files
- Why examine: Dependency structure reveals architectural layers; following patterns prevents breaking dependencies

**Resource management patterns**
- What to find: How memory, handles, and resources are allocated and cleaned up
- Why examine: Resource leaks cause instability; proper cleanup patterns are project-critical

**Why codebase analysis matters:**
- Each project has unique conventions and patterns
- Existing code is source of truth for how things should be done
- Pattern matching prevents architectural violations and ensures natural fit
