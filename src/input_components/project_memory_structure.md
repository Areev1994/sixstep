# Project Memory Structure Guide

**Purpose**: Framework-level guidance for understanding and maintaining the four-layer project memory system during Step 6 knowledge curation.

**Audience**: Claude during Step 6, making decisions about what to document and where.

**Scope**: Generic software engineering knowledge structure applicable to any codebase.

---

## Four-Layer Knowledge Architecture

The project memory uses a four-layer model that separates different types of knowledge:

```
Layer 1: ARCHITECTURE (What exists and how it connects)
    ↓ referenced by
Layer 2: FEATURES (How capabilities work)
    ↓ referenced by
Layer 3: SOLUTIONS (How problems were solved)
    ↓ referenced by
Layer 4: SKILLS (How to perform techniques/methodologies)
```

Each layer serves different purposes and is consumed at different stages of the six-step framework.

---

## Layer 1: Architecture

### Purpose
Enable **quick high-level overview** of components in the project to answer: "Which components are involved in this problem?"

**CRITICAL UNDERSTANDING - Incremental Growth**:
- Architecture layer is **incomplete by design**
- Built incrementally through six-step sessions
- Each session adds verified knowledge from THAT session's discoveries
- Gaps are normal: If component not documented, doesn't mean unimportant - just not documented yet
- Your Step 6 job: Add architecture knowledge learned during THIS session
- Over time: More sessions → richer architecture documentation → faster future problem-solving

**CRITICAL UNDERSTANDING**: Architecture files are **SUPPORTING FILES** for source code. They do NOT duplicate source code content. Instead, they explain the **ROLE** of source code within the project's directory structure from a high level.

### Core Principle: Supporting Documentation, Not Duplication

Architecture documentation exists to help Claude:
- **Quickly understand** what role each source directory/component plays
- **Navigate** the project structure efficiently
- **Identify** which components are relevant to a problem

Architecture documentation does NOT:
- ❌ Copy/paste code from source files
- ❌ Duplicate information already in source code
- ❌ Provide detailed implementation explanations (that's for Features layer)
- ❌ Explain how to use APIs in detail (that's for Features layer)

**Example of correct approach**:
- ✅ Source code: `src/api/router.ts` (actual implementation)
- ✅ Architecture doc: `architecture/api/README.md` explains "API layer handles routing and validation, located in `src/api/`, interfaces with Business Logic layer"
- ❌ Wrong: Copying router.ts code into README.md

### Directory Structure: Flexible, Not Rigid

**RULE**: Architecture directory structure loosely follows the project's source directory structure.

**Key principles**:
1. **Skip unnecessary directories** - If a source directory doesn't need explanation, don't create an architecture directory for it
2. **Update existing files instead of creating new directories** - When information can fit into an existing README.md, add it there rather than creating a new subdirectory
3. **Don't force 1:1 mapping** - Architecture structure should mirror project structure only when it helps understanding, not mechanically

**Example**:

Project source structure:
```
src/
├── api/
│   ├── router.ts
│   ├── middleware.ts
│   └── validators/
│       ├── auth.ts
│       └── input.ts
├── business/
│   └── logic.ts
└── data/
    └── repository.ts
```

Architecture structure (GOOD):
```
architecture/
├── system_overview.md
├── api/
│   └── README.md  (mentions validators as part of API, no separate dir)
├── business/
│   └── README.md
└── data/
    └── README.md
```

Architecture structure (BAD - too rigid):
```
architecture/
├── system_overview.md
├── api/
│   ├── README.md
│   └── validators/  ← Unnecessary subdirectory
│       └── README.md
├── business/
│   └── README.md
└── data/
    └── README.md
```

### When to Update
Update architecture layer when:
- ✅ New component relationships are discovered
- ✅ System-level understanding has expanded
- ✅ Component responsibilities/roles are clarified
- ✅ Data flow patterns between components become clear
- ❌ NOT for implementation details (those go in solutions)
- ❌ NOT for how features work (those go in features)
- ❌ NOT to duplicate source code content

### Content Structure

**system_overview.md** - Top-level system diagram
- Component relationship diagram (text/ASCII art)
- Data flow examples between components
- Key interface points
- High-level error handling patterns at system level
- **Purpose**: Enable Claude to quickly see "big picture" of project structure

**Component directories** (flexibly following project structure)
- **REQUIRED**: Every directory inside `architecture/` MUST have a `README.md` file
- **REQUIRED**: Each `README.md` MUST include a diagram showing internal component structure
  - Similar style to `system_overview.md` diagram (text/ASCII art)
  - Shows sub-components and relationships WITHIN this component
  - Provides visual clarity at this architectural level
- `README.md` content for each significant component:
  - **Diagram**: Internal component structure (REQUIRED - similar to system_overview style)
  - **What the component's role is** in the project
  - **Source code locations** in codebase (directory paths)
  - **Key interfaces** (what it exposes to other components)
  - **Relationships** with other components (upstream/downstream)
  - **NOT**: Detailed code, implementation logic, or API tutorials

### Generic Examples

**Component relationships**:
```
Client Application
  → API Layer (handles requests/validation)
    → Business Logic (processes business rules)
      → Data Access Layer (database operations)
        → Database
```

**Interface points**:
- "API Layer communicates with Business Logic via request/response objects"
- "Data Access Layer uses connection pooling to reach Database"

**Example component README.md content**:
```markdown
# API Layer Component

**Role**: Request routing, validation, and response formatting
**Location**: `src/api/`
**Interfaces with**: Business Logic layer (downstream)

## Internal Component Structure

```
API Layer
├── Router
│   ├── Route Registration
│   └── Request Dispatcher
├── Middleware Chain
│   ├── Authentication Middleware
│   ├── Validation Middleware
│   └── Logging Middleware
└── Response Formatter
    ├── JSON Serializer
    └── Error Handler

Data Flow:
Request → Router → Middleware Chain → Business Logic
                                    ↓
Response ← Response Formatter ← Business Logic
```

## What This Component Does
Handles incoming HTTP requests, validates input, routes to business logic, formats responses.

## Source Organization
- `src/api/router.ts` - Main routing logic
- `src/api/middleware.ts` - Request/response middleware
- `src/api/validators/` - Input validation (auth, input sanitization)

## Relationships
**Upstream**: Client applications send HTTP requests
**Downstream**: Calls Business Logic layer for processing

## Key Patterns
- Middleware chain for request processing
- Validator composition for input checking
```

**Notice**:
- README includes internal component diagram (REQUIRED)
- Diagram shows sub-components within API Layer
- Similar visual style to system_overview.md
- Does NOT duplicate router.ts code, explains the ROLE

### Quality Criteria
- ✅ Provides **quick overview** of component roles and relationships
- ✅ **REQUIRED**: Includes internal component diagram (similar to system_overview.md style)
- ✅ Points to **source code locations** (doesn't copy source code)
- ✅ Explains **what role** each component plays in the project
- ✅ Shows **data flow** and **dependencies** between components
- ✅ Enables Claude to **quickly identify** relevant components for a problem
- ✅ **Flexible directory structure** - skips unnecessary subdirectories
- ❌ Does NOT duplicate source code content
- ❌ Does NOT include detailed implementation (that's for Features)
- ❌ Does NOT include problem-solving patterns (that's for Solutions)
- ❌ Does NOT rigidly mirror every source directory (only significant ones)

### When to Update

Update architecture layer when THIS session discovered:
- ✅ Component relationships (e.g., external tool integration path)
- ✅ Hardware architecture details (component variants, capabilities, operational modes)
- ✅ System connections (communication paths between layers/components)
- ✅ Component responsibilities (what role component plays in system)
- ✅ Subsystem structure (internal organization of component with subcomponents)
- ❌ NOT implementation details (Features layer)
- ❌ NOT problem solutions (Solutions layer)

**Incremental growth example**:
- Before session: system_overview.md shows internal architecture only
- THIS session: Discovered external debugger connects via protocol handler
- After session: system_overview.md now shows external debugger → protocol handler → internal architecture
- Result: Future sessions immediately see external tool integration without re-discovering

### Example: Hardware Component Architecture Documentation

**Scenario**: Six-step session analyzes performance and discovers hardware component has multiple generations with different capabilities.

**Before session**: `architecture/core_component/README.md` describes basic component role, no variant details

**THIS session discovered**:
- Component comes in Generation 1 and Generation 2
- Generation 2 has enhanced mode reducing operations from N to M
- Variant detected by reading VERSION register

**After session - what to add** (making architecture richer):

1. **Update `architecture/core_component/README.md`**:
   ```markdown
   **Hardware Variants**: This component has multiple generations. See hardware/ subdirectory for variant details and capabilities.
   ```

2. **Create `architecture/core_component/hardware/README.md`**:
   ```markdown
   # Hardware Component Generations

   ## Overview

   ```
   Hardware Component Family
   ├── Generation 1 (Basic capabilities)
   │   └── Standard mode: N operations per transaction
   └── Generation 2 (Enhanced capabilities)
       ├── Standard mode: N operations per transaction
       └── Enhanced mode: M operations per transaction
   ```

   ## Variant Detection
   System reads VERSION.MAJOR register:
   - Generation 1: VERSION.MAJOR = 1
   - Generation 2: VERSION.MAJOR = 2

   ## Capability Differences
   **Generation 1**: Only standard mode available
   **Generation 2**: Adds enhanced mode with automatic features
   ```

**Result**: Future sessions analyzing Generation 1 vs Generation 2 immediately see capability differences without re-analyzing logs.

**What NOT to document**:
- ❌ Optimization implementation (Solutions layer)
- ❌ Register bit positions (source code)
- ❌ API usage (Features layer)

---

## Layer 2: Features

### Purpose
Document **how system capabilities work** to answer: "How does this feature/mechanism operate?"

### When to Update
Update features layer when:
- ✅ New feature or capability was created
- ✅ Existing feature mechanics need better documentation
- ✅ Feature usage patterns should be captured for reuse
- ✅ Complex mechanisms need technical deep-dive
- ❌ NOT for simple helper functions
- ❌ NOT for problem-specific solutions (those go in solutions)

### Content Structure

Each feature gets a directory: `features/feature_name/`

**Required files**:

1. **README.md** - Feature overview
   - What the feature is
   - Why it exists (problem it solves)
   - When to use it (optimal use cases)
   - When NOT to use it
   - Basic usage example

2. **how_it_works.md** - Technical deep-dive
   - Architecture blocks and components
   - Execution flow and state machines
   - Advanced patterns and mechanisms
   - Error handling and edge cases

**Optional files** (create when valuable):

3. **usage_patterns.md** - Common patterns
   - Pattern catalog with examples
   - Best practices
   - Anti-patterns to avoid

4. **api_reference.md** - API documentation
   - Functions, classes, interfaces
   - Configuration options
   - Return values and error codes

### Generic Examples

**Feature types**:
- Caching system
- Authentication flow
- Batch processing mechanism
- Build/test infrastructure
- Logging framework
- State management system

**Feature documentation structure**:
```
features/caching_system/
├── README.md           # What, why, when to use caching
├── how_it_works.md     # Cache architecture, invalidation, storage
├── usage_patterns.md   # Read-through, write-through, cache-aside patterns
└── api_reference.md    # Cache API: get(), set(), invalidate(), etc.
```

### Quality Criteria
- ✅ Explains **how** a capability works technically
- ✅ Provides both overview (README) and deep-dive (how_it_works)
- ✅ Includes when to use AND when NOT to use
- ✅ Reusable across different problem contexts
- ❌ Does NOT focus on specific problems (those are in solutions)
- ❌ Does NOT duplicate architecture diagrams (links to them instead)

---

## Layer 3: Solutions

### Purpose
Document **past problem implementations** to answer: "How was this type of problem solved before?"

### When to Update
**ALWAYS** create a solution pattern document in Step 6 for every completed problem.

Solutions are the primary deliverable of Step 6.

### Content Structure

Each solution is a single markdown file: `solutions/problem_pattern_name.md`

**Required sections**:

1. **Problem Summary**
   - Problem type and domain
   - Original issue description
   - Why it needed solving

2. **Components Involved**
   - List all components affected (link to `architecture/`)
   - Component relationships relevant to this problem
   - Interface points and data flow

3. **Solution Approach**
   - High-level strategy taken
   - Key design decisions and rationale
   - Patterns and techniques applied

4. **Implementation Details** (CRITICAL)
   - **Git Context** (choose one):
     * Git commit ID(s) with descriptions
     * OR Full git diff for complex changes
   - Key files modified with line number references
   - Function signatures and API changes
   - Code patterns used (with examples)

5. **Lessons Learned**
   - What worked well
   - Challenges and how resolved
   - Architectural insights discovered

6. **Applicability**
   - When to apply this solution pattern
   - Similar problems this approach would solve
   - Preconditions and requirements

### Generic Examples

**Solution pattern types**:
- Performance optimization through caching
- Authentication timing fix in multi-service system
- Batch processing adoption for API calls
- Error recovery mechanism for network operations
- State management refactoring for consistency

**Naming convention**:
- `cache_invalidation_strategy.md`
- `batch_api_call_optimization.md`
- `authentication_timing_fix.md`
- `error_recovery_implementation.md`

### Quality Criteria
- ✅ Includes **git commit ID or full diff** (essential for replication)
- ✅ Links to architecture components involved
- ✅ Links to features used in the solution
- ✅ Explains **why** design decisions were made, not just **what**
- ✅ Captures lessons learned for future similar problems
- ✅ Defines clear applicability criteria
- ❌ Does NOT become overly generic (should reference specific implementation)
- ❌ Does NOT skip git context (critical for seeing exact code changes)

---

## Cross-Layer References

Solutions should reference architecture and features to create a knowledge graph:

### Solution → Architecture
```markdown
## Components Involved

**Primary Component**: Core API Layer (see architecture/core_api/README.md)
- Handles request routing and validation
- Modified request processing pipeline

**Related Component**: Data Access Layer (see architecture/data_layer/README.md)
- Connection pooling configuration
- Query batching implementation
```

### Solution → Features
```markdown
## Solution Approach

This solution uses the **Batch Processing** feature (see features/batch_processing/)
to optimize multiple sequential API calls into a single batched request.

Key patterns from batch_processing/usage_patterns.md:
- Collect phase: Queue operations without execution
- Execute phase: Batch send and distribute responses
```

### Features → Architecture
```markdown
## Architecture Components

### Client Side (Core API)
- Request Router (see architecture/core_api/README.md)
- Batch Controller manages queuing

### Server Side (Data Access Layer)
- Batch Processor (see architecture/data_layer/README.md)
- Handles batched request execution
```

---

## Decision Trees

### Should I Update Architecture Layer?

```
Did you discover NEW component relationships?
├─ YES → Update system_overview.md with new relationships
└─ NO → Continue

Did component responsibilities/interfaces become clearer?
├─ YES → Update component README.md
└─ NO → Skip architecture updates
```

### Should I Update Features Layer?

```
Did you CREATE a new feature/capability?
├─ YES → Create new feature directory with README + how_it_works
└─ NO → Continue

Did you significantly IMPROVE understanding of existing feature?
├─ YES → Update feature documentation
└─ NO → Skip feature updates

Is this just a helper function or utility?
├─ YES → Document in solution only, not as separate feature
└─ NO → Continue evaluation
```

### What Goes in Solution Pattern?

```
ALWAYS include in solutions:
✅ Problem summary and context
✅ Components involved (with architecture links)
✅ Solution approach and design decisions
✅ Git commit ID or full diff (CRITICAL)
✅ Key files modified with line references
✅ Lessons learned
✅ Applicability criteria

CONDITIONALLY include:
⚠️ Features used (if applicable - link to features/)
⚠️ Code examples (when pattern is not obvious from git diff)
⚠️ Performance measurements (when relevant)
⚠️ Test strategy (when novel or important)
```

---

## Content Templates

### Architecture Component Template

```markdown
# Component Name

**Type**: [API Layer | Service | Data Access | Infrastructure | etc.]
**Location**: `path/to/component/`
**Purpose**: [One-sentence component purpose]

---

## What [Component] Does

[Description of component responsibilities]

---

## Internal Component Structure (REQUIRED)

**⚠️ CRITICAL**: Every architecture README.md MUST include this diagram

```
[Component Name]
├── [Sub-component 1]
│   ├── [Part A]
│   └── [Part B]
├── [Sub-component 2]
│   └── [Part C]
└── [Sub-component 3]

Data Flow:
[Input] → [Sub-component 1] → [Sub-component 2] → [Output]
```

Use text/ASCII art similar to system_overview.md style.
Show internal structure and data flow within this component.

---

## Source Code Organization

### Main Files
- `path/to/main.ext` - [Purpose]
- `path/to/secondary.ext` - [Purpose]

### Key Directories
- `path/to/subdir/` - [Purpose]

---

## Key Interfaces

### Interface 1: [Name]
- Purpose: [What it does]
- Used by: [Which components]
- Example: [Code or pseudocode]

---

## Relationships with Other Components

**Upstream** (uses this component):
- [Component A] - [How it uses this]

**Downstream** (this component uses):
- [Component B] - [How this uses it]

---

## Common Patterns

[Patterns commonly used in this component]

---

## Related Documentation

- See features/[feature]/ for [capability] details
- See solutions/[solution].md for [problem type] examples
```

### Feature README Template

```markdown
# Feature Name

**Type**: [Performance | Security | Infrastructure | etc.]
**Status**: [Production | Experimental | Deprecated]
**Primary Components**: [List components - link to architecture/]

---

## What is [Feature]?

[Clear description of the feature]

**Core Idea**: [One-paragraph essence]

---

## Why It Exists

### Problem It Solves
- [Problem 1]
- [Problem 2]

### Impact
- Before: [State before feature]
- After: [State after feature]
- Benefit: [Measurable improvement]

---

## When to Use

### ✅ Optimal Use Cases
- [Use case 1]
- [Use case 2]

### ❌ When NOT to Use
- [Anti-pattern 1]
- [Anti-pattern 2]

---

## Basic Usage Example

[Simple code example showing feature usage]

---

## Files and Documentation

### Feature Documentation (this directory)
- `README.md` (this file) - Overview
- `how_it_works.md` - Technical details
- `usage_patterns.md` - Pattern catalog
- `api_reference.md` - Complete API

### Implementation Files
- [List key source files]

### Related Documentation
- See architecture/[component]/ for component details
- See solutions/[solution].md for usage examples
```

### Solution Pattern Template

```markdown
# Solution Pattern: [Descriptive Name]

**Pattern ID**: [lowercase_with_underscores]
**Date Created**: [YYYY-MM-DD]
**Problem Domain**: [Domain/category]
**Complexity**: [Low | Medium | High]
**Reusability**: [Low | Medium | High]

---

## Problem Summary

### Problem Type
[Category of problem]

### Original Issue
[Description of the problem that needed solving]

### Why It Needed Solving
[Business/technical justification]

---

## Components Involved

### Primary Component
**[Component Name]** (see architecture/[component]/)
- [Role in this solution]
- [What was modified]

### Related Components
- **[Component B]**: [Relationship]
- **[Component C]**: [Relationship]

### Component Relationships
[Diagram or description of how components interact in this solution]

---

## Solution Approach

### High-Level Strategy
[Overall approach taken]

### Key Design Decisions
**Decision 1**: [What was decided]
- Rationale: [Why this choice]
- Alternative rejected: [What was not chosen and why]

**Decision 2**: [What was decided]
- Rationale: [Why this choice]

### Patterns and Techniques Applied
[Design patterns, algorithms, techniques used]

---

## Implementation Details

### Git Context

**OPTION A: Commit IDs** (for simple changes)
```bash
# Relevant commits
git show abc1234  # [Brief description]
git show def5678  # [Brief description]
```

**OPTION B: Full Diff** (for complex changes or multiple related commits)
```bash
# Complete implementation diff
git diff before_commit..after_commit

# Or include full diff inline if critical for understanding
```

### Key Files Modified

**path/to/file1.ext**: [What changed and why]
- Lines [X-Y]: [Specific change]
- Function `functionName()`: [What was modified]

**path/to/file2.ext**: [What changed and why]
- Lines [A-B]: [Specific change]

### Function Signatures and API Changes

[Document any API changes, new functions, signature modifications]

### Code Patterns Used

**Pattern 1**: [Name]
```
[Code example showing pattern]
```

---

## Lessons Learned

### What Worked Well
- [Success 1]
- [Success 2]

### Challenges and How Resolved
**Challenge 1**: [What was difficult]
- Resolution: [How it was solved]
- Lesson: [What to remember for next time]

### Architectural Insights Discovered
- [Insight 1]
- [Insight 2]

---

## Applicability

### When to Apply This Solution Pattern
**Primary use cases**:
- [Use case 1]
- [Use case 2]

**Specific scenarios**:
- [Scenario 1]
- [Scenario 2]

### Similar Problems This Approach Would Solve
- [Problem type 1]
- [Problem type 2]

### Preconditions and Requirements
**Technical preconditions**:
- [Requirement 1]
- [Requirement 2]

**Knowledge requirements**:
- [Knowledge 1]
- [Knowledge 2]

---

## Related Patterns and Solutions

**Related solutions**:
- `solution_name.md` - [How it relates]

**Related features**:
- features/[feature]/ - [How it was used]

**Architecture components**:
- architecture/[component]/ - [Which components involved]

---

## References

**Implementation guide files**:
- [Link to step guide files if relevant]

**Documentation**:
- [Links to related documentation]
```

---

## Layer 4: Skills

### Purpose
Document **reusable techniques and methodologies** to answer: "How do I perform this type of analysis/debugging/testing?"

### Core Concept
Skills capture **procedural knowledge** - the "how to" techniques learned during problem-solving that are reusable across different problems.

**Skills are NOT**:
- ❌ NOT component relationships (that's Architecture)
- ❌ NOT how a feature works (that's Features)
- ❌ NOT how a problem was solved (that's Solutions)

**Skills ARE**:
- ✅ Techniques for working with the codebase
- ✅ Methodologies for analysis/debugging/testing
- ✅ Procedures that apply across multiple problems
- ✅ "How-to" knowledge that isn't feature-specific

### When to Update
Update skills layer when you learn a reusable technique during the session:
- ✅ Log correlation techniques (matching operations across log sources)
- ✅ Debugging workflows (systematic approaches to isolate issues)
- ✅ Testing methodologies (validation procedures)
- ✅ Analysis techniques (breaking down complex operations)
- ✅ Measurement procedures (extracting metrics from logs/traces)
- ❌ NOT for one-time procedures specific to a single problem
- ❌ NOT for feature usage (that goes in Features layer)

### Skills vs. Features Distinction

**Feature** (Layer 2):
- Documents a **system capability**
- Answers: "How does [this capability] work?"
- Example: "How does the caching system work?" → features/caching/

**Skill** (Layer 4):
- Documents a **technique/methodology**
- Answers: "How do I perform [this task]?"
- Example: "How to correlate logs across system layers for timing analysis?" → skills/log_correlation_timing.md

**Rule of thumb**: If it's about understanding a system component, it's a Feature. If it's about a procedure you perform, it's a Skill.

### Content Structure

Each skill is a single markdown file: `skills/descriptive_skill_name.md`

**Target length**: 50-150 lines (200 lines maximum)

**Required sections** (concise format):

1. **What** - 1-2 sentence description
2. **When to Use** - 2-4 bullet points of applicable scenarios
3. **Key Markers/Identifiers** - REQUIRED if technique uses markers/patterns for correlation or identification
4. **Breakdown Structure** - REQUIRED if technique involves hierarchical decomposition (show as ASCII tree)
5. **Procedure** - Concise actionable steps (verb + object + brief context)
6. **Example from Session** - 2-4 lines showing actual usage in THIS session
7. **Common Pitfalls** - 2-4 bullets of things to avoid
8. **Related** - Links to solutions/architecture/features

### Skills Template (Generic Placeholders)

**Note**: Template uses generic placeholders `[like_this]`. When creating actual skill in `project_memory/skills/`, replace with project-specific content from THIS session (actual markers, tool names, component names).

```markdown
# Skill: [Technique Name]

## What
[1-2 sentence description of technique]

## When to Use
- [Applicable scenario 1]
- [Applicable scenario 2]
- [Applicable scenario 3]

## Key Markers/Identifiers
**[Log/Data Source 1 Name]:**
- [Marker A name]: `[actual_pattern]` - [what it indicates]
- [Marker B name]: `[actual_pattern]` - [what it indicates]

**[Log/Data Source 2 Name]:**
- [Marker C name]: `[actual_pattern]` - [what it indicates]

## Breakdown Structure
[If technique involves hierarchical decomposition, show ASCII tree with actual operation names]

```
[High-Level Operation]
├── [Mid-Level Operation 1]
│   ├── [Low-Level Action 1]
│   └── [Low-Level Action 2]
└── [Mid-Level Operation 2]
```

Timing aggregation: [if applicable, show how times aggregate across levels]

## Procedure
1. [Concise actionable step 1: verb + object + context]
2. [Concise actionable step 2]
3. [Concise actionable step 3]
4. [Concise actionable step 4]

## Example from Session
[2-4 lines showing actual usage: "Used in Step N to [accomplish]. Found [numbers/results]. [Key insight]."]

## Common Pitfalls
- [Pitfall 1 with brief solution]
- [Pitfall 2 with brief solution]
- [Pitfall 3 with brief solution]

## Related
- Solutions: [solution pattern that used this technique]
- Architecture: [relevant component(s)]
```

### Example: Template vs Actual Skill

**Purpose**: Show how to transform generic template into concise, marker-focused skill using actual project content.

**Template uses generic placeholders** → **Actual skill uses project-specific content from THIS session**

#### Key Markers Section:

**Template (generic placeholders):**
```markdown
## Key Markers/Identifiers
**[Log Source 1]:**
- [Marker A]: `[pattern]` - [what it indicates]
**[Log Source 2]:**
- [Marker B]: `[pattern]` - [what it indicates]
```

**Actual Skill (project-specific content):**
```markdown
## Key Markers/Identifiers
**LLDB Logs:**
- Step command: User types 'n' in LLDB console
- Packet sent: `vCont;s:1` packet identifier

**Project Logs:**
- Packet receive: `recv:` marker (format: `HH:MM:SS:microseconds|...|recv: [packet_content]`)
- Packet send: `send:` marker
- Read transaction: `## memapr` marker
- Write transaction: `## memapw` marker
```

**Why project-specific**: Future sessions know exact markers to search for. No interpretation needed.

#### Breakdown Structure Section:

**Template (generic placeholders):**
```markdown
## Breakdown Structure
```
[High-Level Operation]
├── [Mid-Level Operation]
│   └── [Low-Level Action]
```
```

**Actual Skill (project-specific content):**
```markdown
## Breakdown Structure
```
LLDB Step Command 'n'
├── Packet 1 (GDB Remote Protocol vCont;s:1)
│   ├── memap write (set address register)
│   ├── memap write (set command register)
│   └── memap read (get result register)
├── Packet 2 (read general registers)
│   └── [memap transactions...]
└── Packet 17
```

Timing aggregation:
- Total command time = sum of all packet times
- Packet time = sum of all memap transaction times
```

**Why specific**: Shows actual hierarchy learned in THIS session, not abstract concept.

#### Length Comparison:

**Template**: ~50 lines (concise guide)
**Actual skill**: 80-120 lines (concise with actual content, NO tutorial fluff)
**Bad example**: 400+ lines (verbose tutorial-style - what to avoid)

### Generic Skill Categories (Examples)

**Analysis & Investigation**:
- Log correlation techniques
- Performance profiling procedures
- Resource usage analysis methods
- Data flow tracing techniques

**Debugging**:
- Systematic bug isolation workflows
- Reproduction step reduction methods
- Root cause analysis procedures
- Error pattern recognition techniques

**Testing & Validation**:
- Test case design methodologies
- Regression test creation procedures
- Performance benchmarking techniques
- Validation automation workflows

**Measurement & Metrics**:
- Timing measurement procedures
- Metric extraction from various sources
- Statistical analysis techniques
- Baseline establishment methods

### Quality Criteria

**Conciseness (CRITICAL)**:
- ✅ Target: 50-150 lines total
- ✅ Maximum: 200 lines (absolute limit)
- ❌ NO tutorial content: exercises, practice sections, success criteria, difficulty ratings, "time to learn", "mastery" sections
- ❌ NO verbose explanations - concise actionable content only
- ❌ NO conceptual sections like "Understanding X", "Core Concepts", "Advanced Techniques" beyond what's needed for procedure

**Marker/Pattern Documentation (CRITICAL for correlation/identification techniques)**:
- ✅ "Key Markers/Identifiers" section REQUIRED if technique uses markers/patterns
- ✅ Use ACTUAL markers from THIS session in project_memory skills (not generic placeholders)
  - Example: `recv:`, `send:`, `## memapr`, `## memapw` - actual project-specific patterns
- ✅ Show marker format/context: `timestamp|component|recv: [packet]`
- ✅ Group markers by log/data source
- ✅ One line per marker: what it indicates
- ❌ NO generic "look for patterns" without specifying actual patterns

**Breakdown Structure (for hierarchical decomposition techniques)**:
- ✅ Show hierarchical decomposition as ASCII tree if technique involves breaking down operations
- ✅ Use actual operation names from THIS session (not placeholders)
  - Example: `LLDB Step Command 'n'` → `GDB Packet` → `memap transaction` (actual names)
- ✅ Show 2-3 levels of hierarchy (not just 1 level)
- ✅ Include timing aggregation if applicable: "Total = sum of packet times, packet time = sum of transaction times"
- ❌ NO vague "operations contain sub-operations" - show actual structure learned in THIS session

**Actionable Steps**:
- ✅ Action verbs: "Search for", "Extract", "Calculate", "Count", "Correlate", "Identify"
- ✅ Concrete objects: "`recv:` markers", "packet timestamps", "transaction count"
- ❌ NO concept verbs: "Understand", "Learn", "Appreciate", "Consider", "Realize"
- ✅ Steps are immediately executable: reader knows exactly what to do

**Session Context**:
- ✅ "Example from Session" uses actual data from THIS session
  - Example: "Found 17 packets, first packet: 320ms (913 transactions)"
- ✅ Cite which step technique was used: "Used in Step 2", "Applied in Step 3 Phase 1"
- ✅ 2-4 lines maximum
- ❌ NO hypothetical examples ("you could use this for...")

**Project-Specific Content (for project_memory)**:
- ✅ Skills in `project_memory/skills/` SHOULD use actual project-specific content
  - Actual markers: `recv:`, `## memapr` (not `[marker]` placeholders)
  - Actual tool names: LLDB, tools, GDB Remote Protocol (not `[external_tool]`)
  - Actual component names: debug module, packet handler (not `[component]`)
- ✅ This makes skills directly actionable with no ambiguity
- ✅ Future sessions know exact patterns to search for
- ❌ NOT generic placeholders in actual skills (placeholders only in template)

**Reusability Test**:
- ✅ Technique applies to multiple similar problems (not just THIS specific problem)
- ✅ Procedure is general enough to work in different contexts
- ❌ NOT one-time procedures specific only to THIS problem (those go in solution pattern)

---

## Framework Integration

### Step 1: Architecture + Features (Overview)
- Shows `system_overview.md` for component context
- Shows feature READMEs for capability awareness
- Purpose: "What components exist and what can the system do?"

### Step 2: Architecture + Features + Solutions + Skills (Deep-Dive)
- Deep-dives into specific features via `how_it_works.md`
- Searches solutions for similar patterns **with git diffs**
- **Uses skills for analysis/research techniques**
- Purpose: "How does this work, how have similar problems been solved, and what techniques help investigation?"

### Step 3 Phase 1: All Layers (Investigation + Design)
- References patterns from all layers
- Architecture for component relationships
- Features for capability mechanics
- Solutions for proven approaches
- **Skills for debugging workflows and investigation techniques**

### Step 4: Features (Build Validation)
- Uses `features/build_system/` for compilation verification
- References other features for implementation guidance

### Step 5: Features + Skills (Testing & Validation)
- Uses features for understanding what was implemented
- **Uses skills for testing methodologies and validation procedures**

### Step 6: Update All Layers (Curation)
- **Always** creates solution pattern
- **Conditionally** updates architecture (if new relationships discovered)
- **Conditionally** updates features (if new capability created/documented)
- **Conditionally** creates skills (if reusable technique learned)

---

## Quality Guidelines

### Generic vs. Project-Specific Balance

**Architecture**: Project-specific structure, generic principles
- ✅ Specific: "Component X talks to Component Y via REST API"
- ✅ Generic: Architecture patterns (layered, event-driven, etc.)

**Features**: Project-specific implementation, generic patterns
- ✅ Specific: How *your* caching system works
- ✅ Generic: Caching patterns (read-through, write-behind, etc.)

**Solutions**: Project-specific problem, generic applicability
- ✅ Specific: Exact git commits and files changed in *your* codebase
- ✅ Generic: When this pattern applies to similar problems

### Avoid These Anti-Patterns

❌ **Architecture becoming implementation dump**
- Don't copy/paste large code blocks
- Focus on structure and relationships
- Link to source files instead

❌ **Features becoming tutorials**
- Document what exists, not how to build from scratch
- Assume reader has codebase access
- Link to actual code examples

❌ **Solutions without git context**
- ALWAYS include commit IDs or diffs
- Without git context, solutions are much less valuable
- Future sessions need to see exact changes

❌ **Over-generic documentation**
- "This component handles requests" (too vague)
- "Request router validates auth tokens via middleware" (better)

❌ **Over-specific documentation**
- Don't hardcode IDs, timestamps, server names in examples
- Use placeholders: "[component_name]", "[feature_id]", etc.

---

## Summary Decision Matrix

| Question | Architecture | Features | Solutions | Skills |
|----------|-------------|----------|-----------|--------|
| **What does it capture?** | Component structure + internal diagrams | How capabilities work | How problems were solved | How to perform techniques |
| **When to update?** | New relationships discovered | New feature created/documented | Always (every Step 6) | Reusable technique learned |
| **Primary content?** | Component diagrams (REQUIRED), interfaces | Technical deep-dives, patterns | Git commits, design decisions | Step-by-step procedures |
| **Links from?** | system_overview | Architecture components | Architecture + Features | All layers |
| **Links to?** | — | Architecture | Architecture + Features | Architecture + Features + Solutions |
| **Used in step?** | Step 1, 2 | Step 1, 2, 4 | Step 2, 3 | Step 2, 3 Phase 1, 5 |
| **Reusability?** | Project-specific structure | Project-specific + reusable patterns | Problem-specific + pattern applicability | Technique reusable across problems |

---

## Final Checklist

Before completing Step 6, verify:

- ✅ **Solution pattern created** with git context (commit IDs or diff)
- ✅ **Architecture updated** if new component relationships discovered
  - ✅ **REQUIRED**: Every architecture directory has README.md with internal component diagram
- ✅ **Features updated** if new capability created or documented
- ✅ **Skills created** if reusable technique/methodology learned
- ✅ **Cross-references correct** (solutions link to architecture/features, skills link to all layers)
- ✅ **Generic applicability defined** (when to reuse patterns/skills)
- ✅ **Quality criteria met** (not too generic, not too specific)
- ✅ **File locations correct** (architecture/, features/, solutions/, skills/)
- ✅ **Templates followed** (all required sections present, including diagrams in architecture READMEs)

The project memory should enable future framework sessions to:
1. Quickly understand system structure (architecture)
2. Deeply understand how features work (features)
3. See how similar problems were solved before (solutions)
4. Apply proven techniques for analysis/debugging/testing (skills)
