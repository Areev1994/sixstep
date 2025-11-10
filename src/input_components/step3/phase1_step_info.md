Step 3, Phase 1: Investigation → Solution Design

## STAGE 2 CONTEXT

**STAGE 2 (Understanding Expansion) - Step 3 Phase 1**

You are in Stage 2 of the four-stage problem-solving model. Stage 1 (Steps 1-2) identified what factual questions need answers and decided an approach pattern for investigation. Now in Stage 2, you follow that approach pattern to increase understanding through systematic investigation, then design a solution when understanding is sufficient.

**Why Stage 2 matters:**
- Stage 1 completed factual context alignment ("what is the current situation")
- Stage 2 investigates deeper ("how does it work internally", "why does X happen")
- Step 1 Category 3 provided the investigation approach pattern to follow
- Your job: Follow that pattern, gain understanding, then design solution

## PURPOSE

**Investigation → Solution Design**: Increase understanding of the problem through systematic investigation (following Step 1 Category 3 approach pattern), then design a clear solution when understanding is sufficient.

**Why this two-part flow:**
- Can't design effective solution without understanding how things work
- Investigation follows the specific approach pattern decided in Step 1 Category 3
- Understanding grows iteratively through analysis, tracing, measuring, comparison
- Solution design emerges naturally when understanding threshold is reached
- User and Claude build shared understanding through collaborative investigation

## TWO-PART WORKFLOW

### **PART 1: INVESTIGATION PHASE**

**Approach:** Follow Step 1 Category 3 approach pattern to systematically increase understanding.

**CRITICAL - Investigation First:**
- Prescriptive: Start with investigation ONLY - do NOT jump to design in first response
- Descriptive (why): Investigation requires user collaboration and validation before design; premature design wastes effort if investigation direction is wrong; user may have insights that change approach

**Iterative Investigation:**
- Prescriptive: Present investigation findings incrementally - add findings, get user feedback, refine understanding, repeat
- Descriptive (why): Collaboration during investigation keeps Claude aligned with user's needs; prevents wasted investigation effort; user may redirect or provide domain insights

**Activities:**
- Execute the investigation strategy from Step 1 Category 3 (break down operations, trace execution, measure timing, compare implementations, etc.)
- Conduct deep code analysis, execution tracing, performance measurement
- Document findings as investigation progresses
- Collaborate with user to validate findings and gather domain insights
- Update investigation findings iteratively as understanding grows
- **DO NOT move to design without user feedback on investigation**

**Why investigation first:**
- Analytical investigation (Stage 2) builds on factual context (Stage 1)
- Systematic approach prevents solution design based on assumptions
- Investigation findings inform solution constraints and opportunities
- User collaboration ensures investigation focuses on relevant aspects
- User may identify issues with findings before design effort wasted

### **TRANSITION CHECKPOINT: Investigation → Design**

**Before moving from Part 1 to Part 2:**

- Prescriptive: Explicitly ask user for approval to move to design
- Descriptive (why): User may want more investigation, question findings, have insights that change design direction, or identify gaps in understanding

**Required Question to User:**
```
Based on these investigation findings, should I:
1. Investigate further (what aspects?)
2. Proceed with solution design
```

**Why this checkpoint is critical:**
- User decides when understanding is sufficient (not Claude alone)
- Prevents premature design based on incomplete investigation
- Allows user to redirect investigation before design commitment
- Ensures collaborative decision-making, not autonomous progression

### **PART 2: DESIGN PHASE**

**Approach:** Design solution when understanding from investigation is sufficient AND user approves.

**Criteria for "sufficient understanding" (Guide for Claude):**
- ✅ Know HOW the current system works internally (traced and understood)
- ✅ Know WHY the problem occurs (root cause identified)
- ✅ Know WHERE changes need to happen (components/functions identified)
- ✅ Know WHAT constraints exist (performance, compatibility, architecture)
- ❌ Don't over-investigate - move to design when above criteria met

**BUT - User Approval Required:**
- Prescriptive: These criteria guide YOU, but USER decides when to move to design
- Descriptive (why): User has domain knowledge and project constraints Claude doesn't know; user may see gaps in understanding Claude missed; collaborative decision prevents wrong design direction

**Activities:**
- Create clear solution design (approach, components involved, key changes)
- Design should be detailed enough to avoid misunderstanding
- Maintain glanceable format (user-review as shared document)
- Document trade-offs, design decisions, and rationale
- Validate design with user before moving to Phase 2 (task creation)

**Why design criteria matter:**
- Premature design (without understanding) leads to wrong solutions
- Over-investigation delays progress without adding value
- Clear design prevents misunderstanding in implementation phase
- Shared document keeps user and Claude aligned on approach

## USER-REVIEW AS SHARED DOCUMENT

**User-review is the shared document** showing current state of investigation + general plan.

**What "shared document" means:**
- Both user and Claude see same understanding (investigation findings)
- Both know what's been discovered and what plan is (or investigation status if design not ready)
- Document updates dynamically as investigation progresses
- Glanceable format allows quick user review without reading details
- User provides feedback/ideas, Claude incorporates and updates document

**Why this matters:**
- Ensures alignment between user domain knowledge and Claude's analysis
- Prevents Claude from pursuing irrelevant investigation paths
- Allows user to guide investigation with insights and constraints
- Creates collaborative problem-solving environment

## COLLABORATION RULES

**During Investigation:**
- When encountering knowledge gaps → ASK USER for domain insights
- When multiple investigation paths exist → Present options and get user preference
- When findings seem contradictory → Discuss with user to resolve
- Build on user ideas and combine with systematic analysis

**During Design:**
- Present multiple solution options with trade-offs
- Get user preference on design approach
- Incorporate user constraints and requirements
- Validate design understanding before finalizing

**Why collaboration matters:**
- User has domain knowledge Claude can't infer from code
- User knows project constraints, conventions, future plans
- User feedback keeps investigation focused and relevant
- Collaborative design ensures practical, implementable solutions

## DOCUMENT STRUCTURE REQUIREMENTS

**Replace, don't append:**
- When creating new versions, replace old content completely
- Use version headers: "# Investigation & Design v2"
- Each version should be standalone and immediately understandable

**Why replacement over appending:**
- User reads user-review for quick understanding, not history
- Appending creates long documents that aren't glanceable
- Previous versions exist in guide file and meta logs
- Clean current state more important than showing iterations

**Reference, don't embed:**
- Reference code files and functions instead of including code snippets
- Example: "See `parse_request()` in api/handlers.cpp:145" not code blocks

**Why reference over embedding:**
- Code snippets make document long and not glanceable
- References keep focus on approach and understanding, not implementation
- Actual implementation happens in Step 4, not Step 3

**Standalone clarity:**
- Each version readable without reading prior versions
- Include context needed to understand current state
- User should understand investigation status and design by reading once

**Why standalone versions matter:**
- User may not remember previous iterations
- New collaborators can understand current state quickly
- Glanceable document loses value if it requires reading history

## THINGS NOT TO DO

**NEVER DO THESE ACTIONS:**
- ❌ DO NOT execute `framework_state.py advance` - framework advancement is handled automatically by the system
- ❌ DO NOT create task lists or implementation plans (save for Phase 2 only)
- ❌ DO NOT write or modify code (save for Step 4)
- ❌ DO NOT perform testing or validation (save for Step 5)
- ❌ DO NOT jump directly to design without investigation
- ❌ DO NOT create both Part 1 AND Part 2 in single response without user feedback between them
- ❌ DO NOT move to design without explicitly asking user for approval
- ❌ DO NOT include code snippets or debugging details in investigation findings
- ❌ DO NOT create "CORRECTED" sections - replace content instead

**Why these constraints exist:**
- Framework state changes must go through proper `/step-done` flow
- Task lists in Phase 1 create premature commitment before understanding is complete
- Code changes happen in Step 4 after design is validated
- Testing happens in Step 5 after implementation
- Investigation must establish understanding before design
- **Part 1→Part 2 transition requires user collaboration (not autonomous decision)**
- **Doing investigation+design in one shot violates collaborative workflow**
- Code snippets and debugging details make documents not glanceable
- Corrections via replacement maintains clean, standalone versions

## PHASE COMPLETION GUIDANCE

When Phase 1 investigation and design are complete and user is ready to proceed:

**Correct instruction:**
- Tell user to run `/step-done` to advance to Phase 2 (task list creation)

**NEVER say:**
- "Run /sixstep to proceed to Phase 2" - this is INCORRECT

**Command usage clarification:**
- `/sixstep` = Continue working within current phase (iterate investigation, ask questions, refine design)
- `/step-done` = Advance to next phase or step (triggers framework state change)

**Why this distinction matters:**
- `/sixstep` keeps Claude in investigation/design mode with proper context
- `/step-done` advances framework state and shifts to task creation mode
- Using wrong command breaks framework flow and context management

## USER PREFERENCES (Auto-Generated)

- When user specifies implementation strategy (e.g., "modify called functions instead of callers"), incorporate strategy into solution map and explain benefits (future-proofing, maintainability).
- When user requests test additions referencing existing patterns, locate and analyze reference tests to ensure new tests follow exact same structure and conventions.
- When presenting analysis findings, always update the user-review step document to reflect completed work with concrete results, not just methodology plans.
- When user questions estimates or derived data, immediately verify against ground truth log markers and extract exact counts rather than relying on calculations.
- When designing solutions, support user's phased approach that validates simpler optimizations before adding complexity (incremental risk management).
- When user requests solution format changes (e.g., "I want to format it well like question and answer pattern"), immediately restructure the solution map to match requested format, replacing entire document content rather than appending to it.
- When user eliminates options they don't like from brainstormed solutions (e.g., "I don't like rest of brainstormed solution. Just keep X"), remove those alternatives completely from solution map rather than keeping them as "not chosen" options.
- When user acknowledges uncertainty about part of solution (e.g., "I haven't thought about it much yet but might have infrastructure"), preserve that uncertainty in solution map and frame as open question requiring collaboration, rather than forcing premature solution specification.
- When user requests table format for analysis findings, reorganize data into comprehensive tables showing packet-by-packet or operation-by-operation breakdown with timing and transaction counts.
- When user provides exact implementation algorithms with step-by-step examples, incorporate them verbatim into the solution design rather than creating your own interpretation.
- When user specifies they will handle testing manually, acknowledge this explicitly in solution design and omit test design sections.
