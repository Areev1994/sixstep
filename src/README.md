# Solution Map Implementation

This directory contains the implementation of the six-step framework solution map as described in `claude_intelligence/six_step_framework_thoughts.md`.

## Overview

This implementation follows the exact solution map design with enhanced user preference learning and self-contained project memory:
- **Pre-process program**: Composes input components based on detection-logic
- **Detection-logic**: Identifies current step/phase from structured state
- **Input components**: Framework info, step info, data sources, output requirements
- **Consistent state management**: Problem ID-based tracking (not timestamp-based)
- **🆕 Dual output structure**: user-review (glanceable) + guide (complete context) directories
- **🆕 Automatic preference learning**: step-done auto-extracts and adds preferences to step_info
- **🆕 Context continuity**: Claude reads ALL guide files from previous steps for informed decisions
- **🆕 Manual preference override**: update-input-components available for custom additions
- **✨ Three-layer project memory**: Architecture + Features + Solutions (replaces external claude_docs)
- **🎯 Step 6 enhancements**: Incremental knowledge mindset + four-layer project memory (Skills layer) + 4-phase workflow (Sequential Review → Holistic Context → Create Outputs → Verification) + SESSION DISCOVERY REVIEW (Q1-Q9) for systematic decision-making + comprehensive structure guide (`project_memory_structure.md`) with decision trees and templates

## Enhanced Architecture

### Core Files

1. **`framework_state.py`** - State Management Engine
   - Handles problem initialization and step/phase transitions
   - Maintains consistent state in `current_state.json` and `STATE.md`
   - Implements detection-logic to identify current step/phase
   - Contains input component definitions for all steps/phases + special commands
   - 🆕 Creates user-review/ and guide/ subdirectories for dual output structure

2. **`compose_input.py`** - Pre-process Program (Sixstep)
   - The core "pre-process program" from solution map
   - Composes all 4 input components based on current step detection
   - Generates enhanced prompts with proper framework context
   - Called by `/sixstep` slash command
   - 🆕 Logs conversations with strict format contract

3. **🆕 `step_done.py`** - Enhanced Step Transitions with Automatic Preference Addition
   - Advances framework state (original functionality)
   - Composes preference extraction prompt using input components
   - 🆕 Automatically extracts user preferences from completed step conversation
   - 🆕 Directly updates step_info.md files with discovered preferences (max 3 per step)
   - 🆕 Reports added preferences to user
   - Single script following same pattern as `compose_input.py`

4. **🆕 `update_input_components.py`** - Intelligent Integration
   - Composes constraint-aware integration prompt using input components
   - Handles size management, duplication detection, consolidation logic
   - Single script following same pattern as `compose_input.py`

### Enhanced Hook Commands

**🔧 Migration from Slash Commands to Hooks**

The framework now uses Claude Code hooks instead of slash commands to ensure reliable execution and native prompt delivery. Hooks guarantee the Python scripts are executed and send enhanced prompts directly to Claude without tool use overhead.

1. **`/start-sixstep`** - Framework Initialization
   - Usage: `/start-sixstep [problem description]`
   - **Hook**: Executes `framework_state.py start "$ARGUMENTS"`
   - Creates consistent problem ID and directory structure
   - Initializes state files and framework session
   - Sends native initialization confirmation to Claude

2. **🆕 `/step-done`** - Enhanced Step/Phase Transitions with Automatic Preference Addition
   - Usage: `/step-done`
   - **Hook**: Executes `step_done.py`
   - Advances to next step or phase
   - **Automatically extracts and adds user preferences** to step_info files (max 3 per step)
   - Analyzes completed step conversation for working style patterns
   - Reports what preferences were added to the user
   - **Automatically runs `claude compact`** to clear context for next step
   - No manual `/update-input-components` command needed (but still available for manual additions)

3. **`/sixstep`** - Enhanced Question Processing
   - Usage: `/sixstep [your question]`
   - **Hook**: Executes `compose_input.py "$ARGUMENTS"`
   - Runs pre-process program to compose input components
   - Provides framework-aware context for every question
   - 🆕 Includes accumulated user preferences automatically
   - 🆕 Logs complete conversations to meta files with response summaries
   - **Enhanced prompts sent natively to Claude** (not via tool output)

4. **🆕 `/update-input-components`** - Manual Preference Integration
   - Usage: `/update-input-components [prompt1] | [prompt2] | [prompt3]`
   - **Hook**: Executes `update_input_components.py "$ARGUMENTS"`
   - Composes constraint-aware integration prompt for Claude
   - Claude handles size constraints, duplication detection, consolidation
   - Updates current step's input components with intelligent management
   - **Use this for manual preference additions** (automatic additions happen via `/step-done`)

## Enhanced Input Components Structure

### 🆕 Dual Output Directory Structure

Each step generates TWO versions of output files for different audiences:

**📋 user-review/** - Glanceable deliverables for quick user review
- Clean, concise format
- Actual deliverable content (not summaries)
- Quick status overview
- Key decisions and findings only

**📚 guide/** - Complete context for Claude's continuity
- Comprehensive details with full reasoning
- All evidence, file references, and analysis
- Complete working notes and thought process
- Enables Claude to understand full state across steps

**Why Two Versions?**
- **user-review**: User can quickly see progress and deliverables without reading lengthy details
- **guide**: Claude reads ALL guide files from previous steps to maintain full context and make informed decisions

**Examples by Step:**
- **Step 1**: user-review = questions list | guide = questions + reasoning + alignment analysis
- **Step 2**: user-review = answers with status/confidence | guide = complete research with all sources
- **Step 3**: user-review = solution map (glanceable) | guide = solution map + all iterations + trade-offs
- **Step 4**: user-review = implementation summary | guide = complete implementation log with architecture
- **Step 5**: user-review = test status overview | guide = comprehensive test documentation
- **Step 6**: user-review = key insights | guide = complete analysis with full context

### Framework Step Components
Each step/phase has four input components stored as individual files in `input_components/`:

- **Framework Info**: Global framework context
- **Step Info**: `step{N}/step_info.md` or `step3/phase{P}_step_info.md`
- **Data Sources**: Analysis targets and search strategies  
- **Output Requirements**: Expected outputs and formats

### 🆕 Special Command Components

#### **`input_components/step-done/`** - Automatic User Preference Extraction and Addition
- **Framework Info**: Extraction goals and automatic update process
- **Step Info**: Role as preference extraction and integration specialist
- **Data Sources**: Meta files, guide files, input components, active directory
- **Output Requirements**: Automatic file update process and success reporting format
- **Behavior**: Analyzes conversations, extracts max 3 generic preferences, automatically adds to step_info files

#### **`input_components/update-input-components/`** - Intelligent Integration
- **Framework Info**: Size constraints and integration strategy (≤2000 chars total)
- **Step Info**: Role as integration specialist with constraint handling
- **Data Sources**: Current step files and existing preferences
- **Output Requirements**: Updated USER PREFERENCES section with smart consolidation

### 🆕 Enhanced Component Features
- **USER PREFERENCES sections**: Auto-generated system prompts in step_info.md files
- **Size management**: Intelligent consolidation when limits exceeded
- **Duplication detection**: Prevents redundant prompts
- **Phase-aware**: Correctly handles Step 3 Phase 1 and Phase 2

### File-Based Components
- **Framework Info**: `step{N}_phase{P}_framework_info.md`
- **Step Info**: `step{N}_phase{P}_step_info.md` 
- **Data Sources**: `step{N}_phase{P}_data_sources.md`
- **Output Requirements**: `step{N}_phase{P}_output_requirements.md`

### Benefits of File-Based Approach
- **Editable**: Modify component content without touching code
- **Maintainable**: Each component is a separate, focused file
- **Versionable**: Track changes to instructions over time
- **Reusable**: Copy/modify components for different projects

### Component Types

1. **Framework Info** - Basic framework awareness and session context
2. **Step Info** - Current step name, phase, and specific instructions  
3. **Data Sources** - Files/directories to reference and search strategies
4. **Output Requirements** - Files to generate/update and format requirements

## Step/Phase Definitions

| Step | Phases | Purpose |
|------|---------|---------|
| 1 | 1 | Understanding Problem Statement - Generate 3-category output (clarification, context, approach) |
| 2 | 1 | Current Situation Assessment - Answer questions with evidence |
| 3 | 1,2 | Brainstorming (Phase 1) + Task List Creation (Phase 2) |
| 4 | 1 | Implementation - Execute tasks with user approval + 🆕 Project-specific build/test validation |
| 5 | 1 | Testing & Optimization - Validate solution |
| 6 | 1 | Insights Extraction - Update knowledge base (incremental verified knowledge, guided by project_memory_structure.md) |

## Enhanced Usage Workflow

### Basic Framework Usage (Original)
```bash
# 1. Start new problem
/start-sixstep Build automated API testing framework

# 2. Ask questions with framework context  
/sixstep What are the key questions I should ask?

# 3. Advance when step complete
/step-done

# 4. Continue with next step
/sixstep How do I assess current testing tools?
```

### 🆕 Enhanced Workflow with Hook-Based Commands

**Benefits of Hook-Based Architecture:**
- ✅ **Guaranteed Execution**: Hooks ensure Python scripts always run
- ✅ **Native Prompt Delivery**: Enhanced prompts sent directly to Claude, not via tool output
- ✅ **Seamless User Experience**: No visible tool execution overhead
- ✅ **Reliable State Management**: Framework state changes happen automatically
- ✅ **Context Management**: Automatic `claude compact` after step transitions

```bash
# 1. Start new problem
/start-sixstep Build automated API testing framework
# Hook executes framework_state.py → sends native confirmation to Claude

# 2. Have conversations in framework steps
/sixstep What are the key questions I should ask?
# Hook executes compose_input.py → sends enhanced prompt natively to Claude
# Claude responds with step_info.md guidance + logs to meta/problem_id/step1.md
# User fills response summary as instructed

# 3. Enhanced step completion with automatic preference learning
/step-done
# Hook executes step_done.py which:
# ✅ Advances to Step 2
# 🔍 Analyzes completed step conversation for user working preferences
# ✅ Automatically adds discovered preferences to step_info files
# 📝 Reports: "✅ Found and added the following user preferences to step_info: ..."
# 🧹 Automatically runs `claude compact` to clear context window

# 4. Optional: Manually add custom preferences anytime
/update-input-components "Custom preference 1 | Custom preference 2"
# Hook executes update_input_components.py which:
# ✅ Composes integration prompt for Claude (sent natively)
# 🔧 Claude handles size constraints and duplication detection
# ✅ Outputs updated USER PREFERENCES section for current step

# 5. Continue with accumulated preferences (auto + manual)
/sixstep How should I assess current testing tools?
# Hook executes compose_input.py → enhanced prompt includes user preferences automatically
```

## 🆕 Conversation Logging & Meta Files

### Strict Format Contract
Every `/sixstep` interaction creates structured logs:

```markdown
meta/{problem_id}/step{N}.md:

## Interaction 1
**Timestamp:** 2025-09-15T10:30:00
**Enhanced Prompt:**
```
[Complete enhanced prompt with input components]
```

**Claude Response Summary:**
**Tools Used:** Grep (2x), Edit (1x)
**Files Modified:** active/problem_id/step1_questions.md
**Key Actions:** Generated 5 clarification questions
**Next Steps:** User should review questions before Step 2
```

### Response Summary Requirements
Claude must fill response summaries using format from `response_summary_format.md`:
- **Tools Used**: All tools invoked during response
- **Files Modified**: Full paths of files changed/created
- **Key Actions**: 1-2 sentence summary of main accomplishment
- **Next Steps**: What user should do next

## 🆕 Input Dump Directory

### Purpose
The `input_dump/` directory is created in each problem's active directory to store user-provided supporting materials that help Claude understand and solve the problem.

### Usage
**When to populate:**
- Before starting Step 1 - if you already have relevant materials
- During Step 1 or Step 2 - when you find materials that would help Claude's research
- Anytime during the framework - though most useful in early steps

**What to include:**
- **Log files**: Error logs, debug output, system logs
- **Specification documents**: API specs, requirements docs, design documents
- **Screenshots**: UI mockups, error messages, system states
- **Configuration files**: Settings files, build configs
- **Data dumps**: Database exports, JSON/XML data, test data
- **Error messages**: Stack traces, compiler errors
- **Reference materials**: Existing documentation, related code snippets

### How Claude Uses It
- **Step 1**: Checks input_dump/ FIRST before searching project memory or codebase
  - Extracts problem-specific context from user materials
  - Uses materials to inform question generation
  - References materials in architectural diagrams

- **Step 2**: Uses input_dump/ as primary evidence source
  - Searches user-provided materials before project memory
  - Documents which input materials were analyzed
  - Correlates user materials with codebase findings

- **Step 3+**: Available as reference material
  - Decision about primary vs. reference use comes from Step 1/2 guide files
  - Materials remain accessible throughout the framework

### Directory Location
```
active/{problem_id}/input_dump/
```

**Note**: The directory is created empty by `/start-sixstep`. You populate it manually by copying/moving files into it as needed.

## 🆕 Preference Learning System

### How It Works
1. **Conversation Analysis**: `/step-done` analyzes complete interaction logs
2. **Pattern Detection**: Extracts user workflow, communication, and quality preferences  
3. **Genericity Filter**: Removes project-specific details, keeps working style patterns
4. **Smart Suggestions**: Outputs max 3 short system prompts (1-2 sentences)

### Example Preference Evolution
```bash
# After Step 1 completion
/step-done
# Suggests: run /update-input-components "Ask clarifying questions before implementation"

# After Step 4 completion  
/step-done
# Suggests: run /update-input-components "Present work in reviewable phases | Include validation steps"

# Result: Step 5+ automatically includes these preferences
/sixstep How should I test this solution?
# Enhanced prompt now includes:
# - Ask clarifying questions before implementation  
# - Present work in reviewable phases
# - Include validation steps
```

## State Management

### Persistent State (`claude_intelligence/current_state.json`)
- Problem ID and description
- Current step and phase numbers
- Timestamps and status
- Active directory paths

### Human-Readable State (`active/{problem_id}/STATE.md`)
- Progress overview with checkboxes
- Session log with timeline
- Step progression tracking

## Enhanced Key Advantages

### Original Framework Benefits
1. **Consistent Problem Tracking** - Uses descriptive problem IDs, not timestamps
2. **Structured Input Composition** - All 4 components composed automatically
3. **Step-Aware Context** - Different instructions/sources per step
4. **State Synchronization** - JSON and Markdown states stay in sync
5. **Detection-Logic** - Automatic step/phase identification
6. **Framework Compliance** - Forces proper six-step methodology
7. **🆕 Context Management** - Automatic `claude compact` after step completion ensures clean context for next step

### 🆕 Enhanced Learning Capabilities
8. **Personalized Framework** - Learns and adapts to individual working styles
9. **Preference Accumulation** - Builds user preference knowledge over time
10. **Intelligent Integration** - Smart constraint handling prevents prompt bloat
11. **Conversation-Driven Learning** - Extracts patterns from actual usage, not manual configuration
12. **Generic Pattern Focus** - Maintains reusability across different problem domains
13. **Automatic Quality Management** - Size limits, duplication prevention, consolidation

### 🆕 Enhanced Implementation Features
14. **Project Commands Integration** - Separates project-specific build/test commands from generic framework
15. **Build Validation** - Step 4 automatically references project commands for compilation verification
16. **Framework Portability** - Project commands directory enables reuse across different codebases

### ✨ Three-Layer Project Memory (New!)
17. **Self-Contained Knowledge Base** - Replaces external claude_docs with integrated project memory
18. **Incremental Verified Knowledge** - Built piece-by-piece through six-step sessions, incomplete by design
19. **Architecture Layer** - Supporting docs explaining component roles and relationships (not code copies)
20. **Features Layer** - How system features/capabilities work (async/replay, authentication, etc.)
21. **Solutions Layer** - Problem-specific patterns with git commit/diff references (grows with each session)
22. **Progressive Context** - Step 1 shows architecture/features, Step 2 deep-dives with past solutions
23. **Knowledge Curation** - Step 6 updates all three layers based on completed work
24. **Structure Guidance** - Comprehensive framework-level guide in `input_components/project_memory_structure.md`

### 🎯 Step 1 & Step 2 Project Memory Integration (Enhanced!)
25. **Step 1 Architectural Diagrams** - Required output includes problem-relevant component diagrams in both user-review and guide versions
26. **Step 1 Light Search Policy** - Project memory as primary source, minimal codebase search only when gaps exist
27. **Step 1 User Interaction Minimization** - Only ask user when problem statement incomplete, find technical details autonomously
28. **Step 2 Layered Search Strategy** - Architecture → Features → Solutions → Codebase with full workflow in step_info
29. **Step 2 Source Documentation** - Output requirements mandate documenting which project memory layers and codebase areas were searched
30. **Clean Component Separation** - step_info (role/approach/workflow), data_sources (what/where sources exist), output_requirements (what to create)

## Enhanced Comparison

| Aspect | Original Implementation | Enhanced Implementation |
|--------|------------------------|-------------------------|
| State tracking | Problem ID-based | Problem ID-based + conversation logs |
| Context injection | Structured input components | Input components + learned preferences |
| Step awareness | Detailed step/phase instructions | Instructions + accumulated user patterns |
| Learning | None | Conversation analysis → system prompts |
| Adaptation | Static behavior | Dynamic preference incorporation |
| Constraint management | Manual | Intelligent size/duplication handling |
| Workflow | Framework-enforced | Framework-enforced + personalized |
| Scalability | Fixed component size | Smart consolidation when needed |
| **Knowledge base** | **External claude_docs** | **✨ Integrated project_memory (3 layers)** |
| **Step 1/2 context** | **Basic claude_docs search** | **✨ Architecture + Features + Solutions with git diffs** |

## Enhanced Files Created During Session

Each problem creates structured directory with dual output format and enhanced logging:
```
claude_intelligence/active/{problem_id}/
├── STATE.md                      # Human-readable progress (root level)
├── input_dump/                   # 🆕 User-provided materials (logs, specs, screenshots, etc.)
├── user-review/                  # 🆕 Glanceable deliverables for user
│   ├── step1_questions.md        # Questions list (clean format)
│   ├── step2_assessment.md       # Answers with status/confidence
│   ├── step3_brainstorm.md       # Solution map (glanceable)
│   ├── step4_implement.md        # Implementation summary
│   ├── step5_testing.md          # Test status overview
│   └── step6_insights.md         # Key insights
└── guide/                        # 🆕 Complete context for Claude
    ├── step1_questions.md        # Questions + full reasoning
    ├── step2_assessment.md       # Complete research with all sources
    ├── step3_brainstorm.md       # Solution map + iterations + trade-offs
    ├── step4_implement.md        # Complete implementation log
    ├── step5_testing.md          # Comprehensive test documentation
    └── step6_insights.md         # Complete analysis with full context

claude_intelligence/meta/{problem_id}/     # 🆕 Conversation logs
├── step1.md                      # Step 1 interaction logs
├── step2.md                      # Step 2 interaction logs
├── step3.md                      # Step 3 Phase 1 logs
├── step3_phase2.md               # Step 3 Phase 2 logs
├── step4.md                      # Step 4 interaction logs
├── step5.md                      # Step 5 interaction logs
└── step6.md                      # Step 6 interaction logs
```

## Enhanced Directory Structure

### Input Components Directory

```
input_components/
├── framework_info.md                    # Global framework context
├── response_summary_format.md           # 🆕 Response logging format
├── meta_file_format.md                  # 🆕 Conversation logging rules
├── project_memory_structure.md          # 🆕 Step 6 structure guide (generic, framework-level)
├── step1/
│   ├── step_info.md                     # + 🆕 USER PREFERENCES sections
│   ├── data_sources.md
│   └── output_requirements.md           # + 🆕 Meta logging requirements
├── step2/ ... step6/                    # Similar structure for all steps
├── step3/
│   ├── phase1_step_info.md              # Phase-specific files
│   ├── phase1_data_sources.md
│   ├── phase1_output_requirements.md
│   ├── phase2_step_info.md
│   ├── phase2_data_sources.md
│   └── phase2_output_requirements.md
├── step-done/                           # 🆕 Preference extraction components
│   ├── framework_info.md                # Extraction constraints & goals
│   ├── step_info.md                     # Role as preference specialist
│   ├── data_sources.md                  # Analysis sources
│   └── output_requirements.md           # Command output format
└── update-input-components/             # 🆕 Integration components
    ├── framework_info.md                # Size constraints & integration
    ├── step_info.md                     # Role as integration specialist
    ├── data_sources.md                  # Existing preferences context
    └── output_requirements.md           # Smart consolidation scenarios
```

**🆕 Project Memory Structure Guide** (`project_memory_structure.md`):
- **Purpose**: Comprehensive framework-level guidance for Step 6 project memory curation
- **Content**: Three-layer architecture explanation, decision trees, content templates, quality criteria
- **Generic Design**: Uses abstract examples applicable to any software project (not project-specific)
- **Key Sections**:
  - Layer 1: Architecture (supporting docs for source code, flexible directory structure)
  - Layer 2: Features (how capabilities work)
  - Layer 3: Solutions (problem patterns with git context)
  - Cross-layer references and decision matrices
- **Referenced by**: `step6/step_info.md` and `step6/output_requirements.md` for detailed guidance

### 🆕 Project Commands Directory

```
project_commands/
├── README.md                            # Directory purpose and usage
├── build.md                             # Project-specific build commands
├── test.md                              # Testing procedures (future)
├── lint.md                              # Code quality tools (future)
└── debug.md                             # Debugging commands (future)
```

**Purpose**: Contains project-specific commands that are too specific to include in generic input components but essential for Step 4 implementation validation.

**Benefits**:
- **Separation of Concerns**: Keeps project commands separate from generic framework
- **Easy Maintenance**: Can modify build/test commands without touching input components  
- **Framework Portability**: Other projects can create their own project_commands directory
- **Step 4 Integration**: Claude automatically references these for build/test validation

**Current Commands**:
- **build.md**: Contains Xcode build command for compilation after code changes

### ✨ Project Memory Directory (New!)

**🔑 Key Concept: Incremental Verified Knowledge**
- **Built incrementally** through six-step sessions, not created once
- **Verified information** from systematic problem-solving process
- **Incomplete by design** - picture made of pieces, many pieces expected to be missing
- **Evolving over time** - gets better with each completed session
- Architecture layer may only document a few components; Features layer only captures documented features; Solutions layer grows with each session

**📖 Structure Guidance**: For detailed templates, decision trees, and quality criteria, see `input_components/project_memory_structure.md`

```
project_memory/
├── architecture/                    # Layer 1: Component structure (supporting docs, not code copies)
│   ├── system_overview.md          # Top-level component relationships diagram
│   ├── api_service/
│   │   └── README.md               # API Service details, source locations, interfaces
│   ├── daemon_service/
│   │   └── README.md               # Daemon service details (future)
│   ├── console/
│   │   └── README.md               # Console & bindings (future)
│   └── core_framework/
│       └── README.md               # Framework details (future)
├── features/                        # Layer 2: Feature mechanics
│   ├── async_replay/
│   │   ├── README.md               # What async/replay is, when to use
│   │   ├── how_it_works.md         # Technical architecture & execution flow
│   │   ├── usage_patterns.md       # Pattern catalog with examples
│   │   └── api_reference.md        # Complete API documentation
│   └── build_system/
│       └── README.md               # Build commands, Xcode configuration
└── solutions/                       # Layer 3: Problem solutions (grows with each session)
    └── async_cpu_register_adoption.md  # Past solution with git context
```

**Purpose**: Self-contained knowledge base that replaces external claude_docs. Provides three types of knowledge:

**Layer 1 - Architecture** (supporting docs for source code):
- **Role explanation**: What role each component plays in the project structure
- **Source locations**: Where components live in codebase (NOT code copies)
- **Component relationships**: Data flow and interface points between components
- **Flexible structure**: Loosely follows project directory structure, skips unnecessary subdirs
- Used in Step 1 for quick component overview and problem scoping

**Layer 2 - Features**:
- How system features work (async operations, authentication, hardware protocol, build system, etc.)
- Technical deep-dives with execution flow
- Usage patterns and best practices
- Build commands and validation procedures
- Used in Step 1 (overview) and Step 2 (deep-dive), Step 4 (build validation)

**Layer 3 - Solutions** (main Step 6 deliverable):
- Past problem implementations with git commit IDs or full diffs
- Components involved, approach taken, lessons learned
- Applicability guide for similar problems
- Used in Step 2 for pattern reference and Step 3 for design inspiration

**Step Integration**:
- **Step 1**: Shows architecture diagrams + feature overviews for problem context
- **Step 2**: Deep-dives features + searches solutions for similar patterns (with git diffs!)
- **Step 3**: References patterns from all three layers for brainstorming
- **Step 4**: Uses build_system feature for compilation validation
- **Step 6**: Updates all three layers - always creates solution, conditionally updates architecture/features

## 🆕 Step 1 Enhancements: Four-Stage Model & Three-Category Output

**Session Updates (Latest)**: Major Step 1 improvements for better context alignment and uncertainty handling.

### Four-Stage Problem-Solving Model

Added to `framework_info.md` - explains how 6 framework steps map to 4 natural problem-solving stages:

- **Stage 1: Context Alignment (Steps 1-2)** - Bring context forward, decide approach pattern for Stage 2
- **Stage 2: Understanding Expansion (Step 3 Phase 1-2)** - Increase understanding using approach from Stage 1
- **Stage 3: Solution Translation (Steps 4-5)** - Implement and test the solution
- **Stage 4: Knowledge Documentation (Step 6)** - Update project memory with verified knowledge

**Why this matters:** Helps Claude understand that Step 1 isn't just "ask questions" - it's "identify what questions need answers AND decide approach pattern for understanding expansion in Step 3."

### Three-Category Step 1 Output Structure

Changed from 2 categories (CLARIFICATION/RESEARCH) to 3 categories:

**Category 1: CLARIFICATION QUESTIONS**
- **Purpose:** Fill factual gaps in problem statement itself
- **When:** ONLY when problem statement is incomplete (0-2 questions max)
- **Answered:** Immediately in Step 1
- **Examples:** "Do you have error logs?", "Which component is affected?"

**Category 2: BRINGING RELEVANT INFORMATION TO FOREFRONT**
- **Purpose:** Identify factual context questions to establish problem environment
- **When:** Always - includes required architecture diagram + 2-4 factual questions
- **Answered:** In Step 2 through light research
- **Examples:** "What is current measured timing?", "Which subsystems are involved?"
- **Critical Distinction:** FACTUAL questions only ("What is X?"), NOT analytical ("How does X work internally?")

**Category 3: APPROACH PATTERN FOR STAGE 2**
- **Purpose:** Decide investigation strategy for Stage 2 (understanding expansion in Step 3)
- **Format:** Single statement (1-2 sentences), not questions
- **Examples:** "Break down operation into phases and measure timing at each phase"
- **Note:** This guides Step 3, NOT Step 2 (which just answers Category 2 questions)

### Factual vs Analytical Distinction

Added explicit guidance to prevent analytical questions in Category 2:

**✅ FACTUAL CONTEXT (Category 2 - Stage 1):**
- "What platform/component/version is this?"
- "What is current measured performance?"
- "Which components are involved?" (from architecture docs, high-level)
- Answerable through light research: docs, logs, configs

**❌ ANALYTICAL INVESTIGATION (Save for Stage 2 - Step 3):**
- "What is internal breakdown of operation phases?"
- "How does component X translate request Y to Z?"
- "Why is X slow?"
- Requires deep code analysis, tracing, comparison studies

**Rule:** Category 2 establishes WHAT the situation is. Stage 2 (Step 3) investigates HOW it works internally.

### Information Reliability: Verified vs Unverified

Added strict guidance about handling uncertainty to prevent speculative details:

**✅ VERIFIED INFORMATION (can state as facts):**
- Project memory content (verified through six-step sessions)
- User-provided information (problem statement, answers, logs)
- Direct observations from user materials

**❌ UNVERIFIED INFORMATION (treat as hypotheses):**
- Light codebase search findings (file names, directory structure)
- Inferences from naming conventions
- Assumptions from partial code reading

**How to handle uncertainty in Step 1:**

1. **In diagrams:** Show ONLY generic placeholders - NO speculative details
   - ❌ BAD: "DebugTool Integration (CoreFramework/PythonBindings API)"
   - ✅ GOOD: "DebugTool Integration?"
   - ❌ BAD: Showing step sequences inside blocks (unverified)
   - ✅ GOOD: Single box with "?" - save internals for Step 2

2. **In questions:** Don't embed ANY speculative details
   - ❌ BAD: "What is connection type (USB/Network/Serial)?"
   - ✅ GOOD: "What probe type is used?"
   - **Rule:** Open-ended questions. Don't list options in parentheses.

3. **Exception - "like X, Y" for verified examples:**
   - ✅ "Communication Protocol (like HTTP, WebSocket)" - if project_memory confirms
   - ❌ "Protocol (HTTP/WebSocket)" - slash implies exhaustive
   - ❌ "Protocol (like HTTP, gRPC)" - if only from light search (unverified)
   - **Rule:** "like" signals verified examples, non-exhaustive list

4. **Avoid irrelevant questions:**
   - ❌ BAD: "What is CPU purpose?" when problem is about timing (purpose not needed)
   - ✅ GOOD: Only ask what's directly relevant to problem

**Principle:** In Step 1, prefer showing "I don't know yet" over stating unverified information as facts.

### Updated Component Organization

**Each input component file has clear purpose:**

| File | Contains | Does NOT Contain |
|------|----------|------------------|
| **framework_info.md** | Four-stage model, path resolution, global context | Step-specific instructions |
| **step_info.md** | Role, PURPOSE, mindset, APPROACH, strategy, workflow, constraints, information reliability rules | Data source locations, output format details |
| **data_sources.md** | Structure, file paths, WHAT exists, WHERE to find, simple example | Usage strategy, output requirements, detailed workflows |
| **output_requirements.md** | What to CREATE, format specs, content requirements, uncertainty handling examples | Search strategies, data source descriptions |

### Updated Step 1 Flow

1. **framework_info.md** tells Claude:
   - Four-stage problem-solving model
   - Stage 1 = Steps 1-2 (context alignment)
   - Step 1 identifies questions AND decides approach for Stage 2

2. **step_info.md** tells Claude:
   - Three-category output structure
   - Factual vs analytical distinction
   - Verified vs unverified information handling
   - Information reliability rules (show uncertainty, no speculation)

3. **data_sources.md** tells Claude WHERE data is:
   - input_dump/ (check FIRST for user materials)
   - project_memory/ (verified information)
   - Codebase (secondary, unverified from light search)

4. **output_requirements.md** tells Claude WHAT to create:
   - user-review/step1_questions.md with 3 categories
   - guide/step1_questions.md with reasoning
   - Diagram uncertainty handling examples

### Example Output Structure

**Step 1 now produces:**

```markdown
## CATEGORY 1: CLARIFICATION QUESTIONS
(if problem incomplete - otherwise empty)

## CATEGORY 2: BRINGING RELEVANT INFO TO FOREFRONT
- Architectural diagram (with "?" for uncertain components)
- Factual context questions (no embedded assumptions)

## CATEGORY 3: APPROACH PATTERN FOR STAGE 2
- Investigation strategy for Step 3 (understanding expansion)
```

## 🆕 Step 2 Enhancements: Completing Stage 1 (Context Alignment)

**Session Updates (Latest)**: Major Step 2 improvements aligned with new Step 1 three-category structure.

### Stage 1 Completion Context

Step 2's role has been clarified as the second half of Stage 1 (Context Alignment):
- **Step 1**: Identifies what factual questions need answers (Category 2) and decides approach pattern for Stage 2 (Category 3)
- **Step 2**: Answers the Category 2 factual questions through systematic research, completing Stage 1
- **Note**: Category 3 (Approach Pattern) is NOT answered in Step 2 - it guides Stage 2 (Step 3) investigation

### Terminology Updates

Changed throughout Step 2 input components:
- **Old**: "RESEARCH questions" from Step 1
- **New**: "Category 2 questions" from Step 1
- **Reason**: Aligns with new Step 1 three-category structure (Clarification, Bringing Info to Forefront, Approach Pattern)

### Factual vs Analytical Distinction

Step 2 now emphasizes answering FACTUAL questions only:
- **✅ Factual Context (Step 2 - Stage 1)**: "What is X?", "What is current state?", "Which components are involved?"
- **❌ Analytical Investigation (Step 3 - Stage 2)**: "How does X work internally?", "Why is X slow?", "What is internal breakdown?"
- **Rule**: Step 2 establishes WHAT the situation is. Step 3 investigates HOW it works internally.

### Glanceable User-Review Format

Added explicit format requirements to make user-review truly glanceable:

**user-review/step2_assessment.md requirements:**
- **Purpose**: Quick status overview - user can see answers without reading details
- **Format Rules**:
  - Keep each question answer to 5-10 lines maximum
  - Answer summary: 1-2 sentences stating factual answer (not detailed breakdown)
  - Evidence: High-level only (e.g., "Found in user logs and codebase", not specific line numbers)
  - NO detailed breakdowns, sequences, or explanations (save for guide version)
  - Total document should be scannable in under 1 minute

**Example - Glanceable Question Entry:**
```markdown
### Question: What is current query execution time?

**Status**: Fully Answered
**Confidence**: High
**Answer**: Current execution time is 3-5 seconds based on performance logs.
**Evidence**: User-provided logs, database configuration files
```

**guide/step2_assessment.md requirements:**
- Complete factual answers with all context
- Detailed source documentation (project memory files, codebase files with file:line references)
- Search strategy employed (three-layer approach)
- Evidence quality assessment
- Knowledge gaps identified

### Three-Layer Search Strategy

**Step 2 Enhancements:**
- **Three-Layer Search Understanding**: Architecture → Features → Solutions → Codebase
- **Layered Search Workflow**: Added two-phase approach (Project Memory Deep-Dive → Codebase Search) in step_info
- **Source Documentation Required**: Output must document which project memory files read and codebase areas searched
- **Git Diffs Emphasized**: Solutions layer contains past implementations with exact changes
- **Clean Component Separation**: Same principle as Step 1

### Updated Step 2 Flow

1. **step_info.md** tells Claude:
   - Role as Context Research Specialist completing Stage 1
   - Answer Step 1 Category 2 questions (factual, not analytical)
   - Two-phase approach: Project Memory Deep-Dive → Codebase Search
   - Phase 1: Architecture (components) → Features (mechanics) → Solutions (git diffs)
   - Phase 2: Search codebase with context from project memory
   - Note: Category 3 (Approach Pattern) guides Step 3, not answered in Step 2

2. **data_sources.md** tells Claude WHERE data is:
   - User-provided inputs in input_dump/ (check FIRST)
   - Step 1 guide files for complete context (Category 1 answers, Category 2 questions, Category 3 approach)
   - Project memory structure (three layers with file paths)
   - Codebase categories (code, docs, configs, logs)

3. **output_requirements.md** tells Claude WHAT to create:
   - **user-review/step2_assessment.md**: Glanceable status (5-10 lines per question)
   - **guide/step2_assessment.md**: Complete research with detailed source documentation
   - Must document: project memory files read, codebase files examined, what was searched but not found
   - Assessment categories: Fully Answered / Partially Answered / Unanswered

### Assessment Categories

For each Category 2 question:
- **Fully Answered**: Complete factual information found with strong evidence
- **Partially Answered**: Some factual information found, but gaps remain
- **Unanswered**: No relevant information found despite thorough search

**Step Integration**:
- **Step 1**: Identifies Category 2 questions (factual context) and Category 3 approach (for Step 3)
- **Step 2**: Answers Category 2 questions through systematic research, completing Stage 1
- **Step 3**: Uses Category 3 approach pattern for analytical investigation (Stage 2)
- **Step 4**: Uses build_system feature for compilation validation
- **Step 6**: Updates all three layers - always creates solution, conditionally updates architecture/features

## 🆕 Step 3 Phase 1 Enhancements: Investigation → Solution Design (Stage 2)

**Session Updates**: Major Step 3 Phase 1 improvements implementing two-part Investigation→Design flow with prescriptive+descriptive pattern.

### Stage 2 (Understanding Expansion) Context

Step 3 Phase 1 is the core of Stage 2 in the four-stage problem-solving model:
- **Stage 1 (Steps 1-2)**: Completed factual context alignment - established "what the situation is"
- **Stage 2 (Step 3)**: Now investigate deeper - understand "how it works internally" and "why problems occur"
- **Step 1 Category 3**: Provided the investigation approach pattern to follow
- **Step 3 Phase 1 Job**: Execute that pattern to gain understanding, then design solution

**Why Stage 2 matters:**
- Can't design effective solutions without understanding how system works
- Investigation follows specific approach pattern decided in Step 1
- Understanding grows iteratively through analysis, tracing, measuring
- Solution design emerges naturally when understanding threshold reached

### Two-Part Workflow: Investigation → Design

Changed from single "brainstorming/solution mapping" to explicit two-part flow:

#### **Part 1: Investigation Phase**

**Purpose:** Follow Step 1 Category 3 approach pattern to systematically increase understanding

**Activities:**
- Execute investigation strategy from Category 3 (break down operations, trace execution, measure timing, compare implementations)
- Conduct deep code analysis, execution tracing, performance measurement
- Document findings as investigation progresses
- Collaborate with user to validate findings and gather domain insights
- Update investigation findings iteratively
- **Start with investigation ONLY - do NOT jump to design in first response**

**Why investigation first:**
- Analytical investigation (Stage 2) builds on factual context (Stage 1)
- Systematic approach prevents solution design based on assumptions
- Investigation findings inform solution constraints and opportunities
- Premature design wastes effort if investigation direction is wrong
- User may have insights that change approach

#### **Transition Checkpoint: Investigation → Design**

**Critical collaborative step before moving to design:**

Added explicit checkpoint requiring user approval before transitioning from investigation to design:

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
- User may question findings or have insights that change design direction

**What Claude must NOT do:**
- ❌ Create both Part 1 AND Part 2 in single response without user feedback
- ❌ Move to design without explicitly asking user for approval
- ❌ Autonomously decide investigation is "sufficient" without user input

**Why this prevents the "do everything in one shot" problem:**
- Forces Claude to STOP after investigation and ASK user
- User feedback loop ensures investigation validated before design
- Prevents wasted design effort if investigation needs correction

#### **Part 2: Design Phase**

**Purpose:** Design solution when understanding from investigation is sufficient AND user approves

**Sufficient Understanding Criteria (Guide for Claude):**
- ✅ Know HOW current system works internally (traced and understood)
- ✅ Know WHY the problem occurs (root cause identified)
- ✅ Know WHERE changes need to happen (components/functions identified)
- ✅ Know WHAT constraints exist (performance, compatibility, architecture)
- ❌ Don't over-investigate - move to design when criteria met

**BUT - User Approval Required:**
- These criteria guide Claude, but USER decides when to move to design
- User has domain knowledge and project constraints Claude doesn't know
- User may see gaps in understanding Claude missed
- Collaborative decision prevents wrong design direction

**Activities:**
- Create clear solution design (approach, components involved, key changes)
- Design detailed enough to avoid misunderstanding but maintain glanceable format
- Document trade-offs, design decisions, and rationale
- Validate design with user before Phase 2 (task creation)

**Why design criteria matter:**
- Premature design without understanding leads to wrong solutions
- Over-investigation delays progress without adding value
- Clear design prevents misunderstanding in implementation phase

### User-Review as Shared Document

Emphasized user-review as "shared document" showing current state:

**What "shared document" means:**
- Both user and Claude see same understanding (investigation findings)
- Both know what's been discovered and what plan is
- Document updates dynamically as investigation progresses
- Glanceable format allows quick user review
- User provides feedback/ideas, Claude incorporates and updates

**Why this matters:**
- Ensures alignment between user domain knowledge and Claude's analysis
- Prevents pursuing irrelevant investigation paths
- Allows user to guide investigation with insights and constraints
- Creates collaborative problem-solving environment

### Two-Part Output Structure

Restructured output documents to match Investigation→Design flow:

#### **user-review/step3_brainstorm.md (Glanceable)**

**Part 1: Investigation Findings**
- 5-10 lines per finding, scannable in 2-3 minutes
- Format: What was discovered + brief evidence reference
- No detailed analysis (save for guide)
- Updates dynamically as investigation progresses

**Part 2: Solution Design** (appears when understanding sufficient)
- Clear and glanceable: Detailed enough to avoid misunderstanding, concise enough to scan in 2-3 minutes
- Approach-focused: What will be done and why, not implementation steps
- No code snippets, no task lists (Phase 2)

**Example - Glanceable Investigation Finding:**
```markdown
### Finding 1: Operation Breakdown Identified
- **What we learned**: DebugTool step command triggers 10+ DebugProtocol operations, not just single step
- **Evidence**: Log analysis and protocol tracing
```

**Example - Glanceable Solution Design:**
```markdown
## PART 2: Solution Design

**Core Approach:** Optimize register reads by batching requests and using autoexec feature.

### Key Design Decisions
- **Batch register reads**: Group multiple reads into single operation (reduces round-trips)
- **Use autoexec**: Leverage hardware feature for automatic register access after step

### Trade-offs Considered
- **Chosen (batching + autoexec)**: 80% reduction in operations, requires protocol changes
- **Alternative (caching)**: Simpler but less effective, ~30% reduction only
```

#### **guide/step3_brainstorm.md (Complete Context)**

**Part 1: Investigation Findings**
- Complete details with full reasoning and evidence
- Specific file:line references for all code examined
- Actual measurements, not summaries
- Complete methodology and confidence assessment

**Part 2: Solution Design**
- Complete design rationale with all trade-offs analyzed
- All alternatives considered with full reasoning
- Every component's role with implementation considerations
- Design iterations if applicable

### Category 3 Approach as Primary Guide

Updated data_sources to emphasize Category 3 approach pattern from Step 1:

**Primary Source:**
- `active/{problem_id}/guide/step1_questions.md` - Category 3: Approach Pattern for Stage 2
- This defines the specific investigation strategy to follow
- Tells HOW to increase understanding (investigation roadmap)

**Why Category 3 is primary:**
- Investigation without strategy leads to unfocused exploration
- Step 1 analyzed problem and decided best investigation approach
- Following this pattern ensures systematic understanding expansion

### Guide Files Emphasized Over User-Review

Strengthened guidance on reading guide files for complete context:

**✅ Read GUIDE files (complete context):**
- Full reasoning, complete evidence, all file references, all iterations
- Guide files contain ALL details Claude needs for informed investigation
- User-review is concise summary for user glancing - not sufficient for Claude

**📋 User-review files are for user glancing only:**
- Quick status overview without details
- Not sufficient for Claude's investigation work
- Read for overview, rely on guide for complete understanding

**Data Source Workflow:**
1. Read Category 3 approach from Step 1 guide → Understand investigation strategy
2. Read Step 1 guide completely → Get full problem context
3. Read Step 2 guide completely → Get complete factual research
4. Glance at user-review files → Quick overview only (5 min)
5. Execute Category 3 investigation → Follow approach pattern
6. Reference input_dump as needed → Specific measurements/errors
7. Reference project memory → Verified architecture/features/past solutions

### Prescriptive + Descriptive Pattern

Applied consistent prescriptive+descriptive pattern throughout all input components:

**Pattern Structure:**
- **Prescriptive**: Clear "WHAT to do" rules (✅/❌, requirements, format)
- **Descriptive**: Explain "WHY" for each rule (purpose, reasoning, context)

**Example from step_info:**
- Prescriptive: "✅ Know HOW current system works internally (traced and understood)"
- Descriptive (why): "Premature design without understanding leads to wrong solutions"

**Example from data_sources:**
- Prescriptive: "✅ READ GUIDE FILES (complete context with full reasoning)"
- Descriptive (why): "Guide files contain ALL details Claude needs for informed investigation"

**Example from output_requirements:**
- Prescriptive: "5-10 lines per finding, scannable in 2-3 minutes"
- Descriptive (why): "User needs to see 'what was learned' quickly, not read research paper"

### Updated Step 3 Phase 1 Flow

1. **phase1_step_info.md** tells Claude:
   - Stage 2 (Understanding Expansion) context and purpose
   - Two-part workflow: Investigation → Design with criteria for transition
   - User-review as shared document concept
   - Collaboration rules for investigation and design phases
   - Document structure requirements with rationale

2. **phase1_data_sources.md** tells Claude WHERE data is:
   - Category 3 approach pattern as PRIMARY guide (investigation strategy)
   - Guide files for complete context (read these, not user-review)
   - Step 1/2 guides with full reasoning and evidence
   - Reference sources (input_dump, project memory)
   - Data source workflow (sequential steps)

3. **phase1_output_requirements.md** tells Claude WHAT to create:
   - **user-review**: Two-part glanceable document (investigation findings + solution design)
   - **guide**: Two-part complete context (full details for both parts)
   - Format requirements with examples (good vs bad)
   - Content rules (replace/reference/standalone) with rationale
   - Banned content with reasons
   - Dynamic update guidance

**Step Integration:**
- **Step 1**: Identified Category 2 questions (factual) and Category 3 approach (investigation strategy)
- **Step 2**: Answered Category 2 questions through research, completed Stage 1
- **Step 3 Phase 1**: Follows Category 3 approach to investigate and design solution (Stage 2)
- **Step 3 Phase 2**: Creates task list based on validated design
- **Step 4**: Implements tasks with design as reference

## 🆕 Step 3 Phase 2 Enhancements: Task List Creation (Completing Stage 2)

**Session Updates**: Major Step 3 Phase 2 improvements emphasizing continuation from Phase 1 and clear task list creation focus.

### Stage 2 Completion Context

Step 3 Phase 2 completes Stage 2 (Understanding Expansion) by translating the validated solution design into concrete implementation tasks:
- **Phase 1 (Investigation → Design)**: Investigated how system works and designed solution (two-part output)
- **Phase 2 (Task List Creation)**: Translates Phase 1 Part 2 (Solution Design) into reviewable task list
- **Purpose**: Make abstract design concrete and actionable before implementation begins

**Why Phase 2 matters:**
- Phase 1 provided understanding and solution approach
- Phase 2 breaks down that approach into specific implementation tasks
- User validates task breakdown before Step 4 implementation effort
- Proper task granularity ensures Step 4 is manageable and trackable

### Phase 1 → Phase 2 Transition

Added clear transition explanation showing Phase 2's relationship to Phase 1:

**Phase 1 delivered** (already complete):
- Part 1: Investigation Findings (what was learned)
- Part 2: Solution Design (validated approach with user approval)

**Phase 2 job** (current task):
- Create task list from Phase 1 Part 2 (Solution Design)
- Tasks translate design decisions into concrete implementation steps
- User reviews task list, provides feedback, approves before Step 4

**Why this transition:**
- Design without tasks is abstract; tasks make it concrete and reviewable
- User validates task breakdown before implementation effort begins
- Proper task granularity ensures Step 4 is manageable and trackable

### Primary Data Source: Phase 1 Part 2 (Solution Design)

Restructured data_sources.md to emphasize Phase 1 Part 2 as PRIMARY source:

**✅ START HERE**: `active/{problem_id}/guide/step3_brainstorm.md` - **Part 2: Solution Design**

**What this provides:**
- Complete solution strategy with full rationale
- Key design decisions with implementation considerations
- Components involved with their roles and required changes
- Complete trade-off analysis showing why approach was chosen
- This is your PRIMARY source - tasks implement this design

**Why Part 2 is primary:**
- Phase 1 Part 2 contains validated solution design approved by user
- Design decisions map directly to implementation tasks
- Components, decisions, and trade-offs define WHAT to build
- Tasks translate design into HOW to build it

**Guide vs User-Review for Task Creation:**
- **Guide files** (`guide/step3_brainstorm.md`): Complete implementation details, full rationale, specific component changes - use this for task creation
- **User-review files** (`user-review/step3_brainstorm.md`): Glanceable summaries, good for reference but insufficient for complete task derivation

### Task List Placement: Prepend to Phase 1 Content

Added critical guidance on task list placement in output_requirements.md:

**CRITICAL - Task List Placement:**
- Prescriptive: Task list goes AT TOP of existing step3_brainstorm.md (which already has Investigation & Design from Phase 1)
- Descriptive (why): PREPEND task list, don't replace Phase 1 content; keeps Investigation + Design context visible below tasks

**Document structure after Phase 2:**
```markdown
# Investigation & Design v1
*Timestamp*

## TASK LIST

- [ ] Task 1: Description
- [ ] Task 2: Description
- [ ] Task 3: Description

---

## PART 1: Investigation Findings
[Phase 1 content - keep as-is]

## PART 2: Solution Design
[Phase 1 content - keep as-is]
```

**Why prepend, not replace:**
- Investigation findings provide context for why tasks exist
- Solution design shows what tasks implement
- Complete document = context + plan + tasks (all visible together)

### Testing Rule Clarification

Fixed testing rule contradiction and clarified implementation vs validation:

**What tasks CAN include:**
- Prescriptive: Tasks CAN include "Write tests for X" (implementing test code)
- Descriptive (why): Writing test code is implementation work that happens in Step 4; test code is deliverable

**What tasks should NOT include:**
- Prescriptive: Tasks should NOT include "Run tests", "Verify results", "Validate performance", "Measure timing"
- Descriptive (why): Running tests, verification, validation are Step 5 activities; Step 4 is implementation only

**Summary**: Writing test code = implementation (Step 4, include in tasks). Running/validating tests = testing (Step 5, exclude from tasks).

### Prescriptive + Descriptive Pattern

Applied consistent prescriptive+descriptive pattern throughout all Phase 2 input components:

**Example from step_info:**
- Prescriptive: "Tasks should produce concrete code output that can be quickly verified"
- Descriptive (why): "Vague tasks ('improve performance') hard to verify complete; concrete tasks ('implement batching in protocol handler') clearly done when code exists"

**Example from data_sources:**
- Prescriptive: "Read Phase 1 Part 2 (Solution Design) from guide/step3_brainstorm.md as primary source"
- Descriptive (why): "Design has complete rationale, components involved, design decisions - tasks must implement all of this"

**Example from output_requirements:**
- Prescriptive: "Task list at top using checkbox format: `- [ ] Task description`"
- Descriptive (why): "Top placement = first thing user sees; checkbox = trackable in Step 4; simple format = quick to scan"

### Updated Step 3 Phase 2 Flow

1. **phase2_step_info.md** tells Claude:
   - Stage 2 completion context (Phase 2 as final step of Understanding Expansion)
   - Phase 1→Phase 2 transition (design → tasks)
   - Task creation approach (derive from design, reviewable granularity)
   - Architecture guidance (pattern recognition, proper placement)
   - Task granularity (logical units, not micro-tasks or file-focused)
   - Testing rule (write tests OK, run tests NOT OK)

2. **phase2_data_sources.md** tells Claude WHERE data is:
   - Phase 1 Part 2 (Solution Design) as PRIMARY source
   - Phase 1 Part 1 (Investigation Findings) for context
   - Guide files emphasized over user-review for complete details
   - Previous steps for additional context

3. **phase2_output_requirements.md** tells Claude WHAT to create:
   - Task list PREPENDED to existing step3_brainstorm.md
   - Both user-review and guide versions updated with task list at top
   - Task requirements (derived from design, reviewable, concrete output)
   - Checkbox format for Step 4 tracking
   - Keep task list synchronized with Step 4 progress

**Step Integration:**
- **Step 3 Phase 1**: Created Investigation Findings + Solution Design (two-part output)
- **Step 3 Phase 2**: Prepends task list to Phase 1 output, translating design into concrete tasks
- **Step 4**: Implements all tasks in one stretch, marks complete immediately after implementing

## 🆕 Step 4 Enhancements: Continuous Implementation (Stage 3)

**Session Updates**: Major Step 4 improvements removing task-by-task approval workflow and implementing continuous task execution.

### Stage 3 (Solution Translation) Context

Step 4 is the first half of Stage 3 (Solution Translation):
- **Stage 1-2 completed**: Context aligned, problem investigated, solution designed, tasks created
- **Step 4 (Implementation)**: Translate task list into working code
- **Step 5 (Validation)**: Verify implementation works correctly (comes next)
- **Goal**: Produce compilable code that integrates properly; functional testing in Step 5

**Why Stage 3 matters:**
- Stage 2 produced validated design and concrete task breakdown
- Stage 3 translates that design into reality through implementation and validation
- Step 4 focuses on implementation only (writing code); Step 5 focuses on validation (testing code)

### Continuous Task Execution (No Approval Workflow)

Changed from sequential task-by-task approval to continuous implementation:

**OLD workflow (removed):**
- Work on one task → Present to user → Wait for approval → Mark complete → Next task
- Interruptions after every task broke implementation flow
- Context-switching overhead between tasks

**NEW workflow:**
- Prescriptive: Work through ALL tasks in one stretch (unless user requests otherwise)
- Descriptive (why): Continuous implementation maintains flow and context; related tasks completed together ensure coherent changes

**Task completion:**
- Prescriptive: Mark each task complete immediately after implementing it
- Descriptive (why): Real-time tracking shows progress; user can check status anytime without waiting for artificial approval delays

**User interaction:**
- Prescriptive: Present complete implementation to user at the end (after all tasks done and build validated)
- Descriptive (why): User reviews finished work as cohesive whole; avoids interruptions during implementation

### Build Only After All Tasks

Changed from incremental builds to single final build:

**Build timing:**
- Prescriptive: Build ONLY after ALL tasks are implemented (not incrementally during implementation)
- Descriptive (why): Final build validates complete integration; incremental builds interrupt flow without adding value

**Build commands:**
- Prescriptive: Use commands ONLY from `project_commands/build.md` - do NOT guess or improvise
- Descriptive (why): Project-specific commands ensure correct process; guessing can break build or miss validation steps

- Prescriptive: If `project_commands/build.md` doesn't exist, skip build validation entirely
- Descriptive (why): Not all projects have standardized build; framework adapts to project structure; validation can happen in Step 5 instead

**What build validates:**
- Prescriptive: Build validates compilation success (syntax, integration), NOT functional correctness
- Descriptive (why): Step 4 goal is compilable code; functional testing happens in Step 5

### Removed step4_references.md

Cleaned up data sources by removing references to `step4_references.md`:
- This file is no longer created during Step 4
- Removed entire "TRACKING REQUIREMENTS" section from data_sources.md
- Simplified data source structure

### Restructured Data Sources

Organized data_sources.md into clear sections matching Steps 1-3 pattern:

**PRIMARY SOURCE**: Step 3 task list
- `active/{problem_id}/guide/step3_brainstorm.md` with complete task breakdown and implementation context
- Why primary: Tasks define exactly what to implement; guide version has full specifications

**CONTEXT SOURCES**: Previous steps guide files
- Step 1 guide: Problem context and approach pattern
- Step 2 guide: Factual research and current state
- Why needed: Complete context prevents implementation mistakes

**REFERENCE SOURCES**: Project memory
- Architecture layer: Component structure and placement
- Features layer: Implementation patterns and conventions
- Solutions layer: Past patterns from similar problems
- Why needed: Established project-specific patterns and conventions

**PROJECT COMMANDS**: Build validation
- `project_commands/build.md`: Exact build commands for this project
- Why critical: Each project has unique build process; don't guess commands

**CODEBASE**: Architectural analysis
- Similar implementations, API docs, error handling patterns, dependencies
- Why needed: Pattern matching ensures consistency with established code

### Testing Rule Clarification

Maintained clear distinction between implementation and validation:

**What Step 4 CAN do:**
- Prescriptive: Can write test code as part of implementation tasks
- Descriptive (why): Writing test code is implementation work; test files are deliverables

**What Step 4 should NOT do:**
- Prescriptive: Must NOT run tests, execute validation, verify results, or measure performance
- Descriptive (why): Running tests and validation are Step 5 activities; clear separation between implementation and validation stages

### Prescriptive + Descriptive Pattern

Applied consistent prescriptive+descriptive pattern throughout all Step 4 input components:

**Example from step_info.md:**
- Prescriptive: "Work through ALL tasks in one stretch (unless user requests otherwise)"
- Descriptive (why): "Continuous implementation maintains flow and context; completing related tasks together ensures coherent changes"

**Example from data_sources.md:**
- Prescriptive: "Use build commands ONLY from project_commands/build.md"
- Descriptive (why): "Project-specific commands ensure correct process; guessing can break build system"

**Example from output_requirements.md:**
- Prescriptive: "Mark tasks complete immediately after implementing them in BOTH user-review and guide versions"
- Descriptive (why): "Real-time tracking keeps state current; user can see progress at any point"

### Updated Step 4 Flow

1. **step_info.md** tells Claude:
   - Stage 3 context (Solution Translation, Step 4 implements, Step 5 validates)
   - Task execution workflow (all tasks in one stretch, mark complete immediately, build at end, present at end)
   - Build validation strategy (only at end, use project_commands/, skip if doesn't exist)
   - Testing rule (write tests OK, run tests NOT OK)
   - Architecture guidance and code quality standards with rationale

2. **data_sources.md** tells Claude WHERE data is:
   - Primary source: Step 3 task list from guide
   - Context sources: Steps 1-2 guide files
   - Reference sources: Project memory (architecture, features, solutions)
   - Project commands: Build validation commands
   - Codebase: Pattern matching sources

3. **output_requirements.md** tells Claude WHAT to create:
   - Dual output: user-review (glanceable) + guide (complete context)
   - Task tracking: Mark complete immediately (not waiting for approval)
   - Build validation: Document results after all tasks complete
   - Closing message: Show only at end when all work done

**Step Integration:**
- **Step 3 Phase 2**: Created task list from validated design
- **Step 4**: Implements all tasks continuously, builds at end, presents complete implementation
- **Step 5**: Validates implementation through testing

## 🆕 Step 5 Enhancements: Validation (Completing Stage 3)

**Session Updates**: Step 5 improvements adding Stage 3 context and restructuring data sources with guide + user-review files.

### Stage 3 (Solution Translation) Completion

Step 5 completes Stage 3 (Solution Translation):
- **Stage 1-2 completed**: Context aligned, problem investigated, solution designed, tasks created
- **Step 4 (Implementation)**: Translated task list into working compilable code
- **Step 5 (Validation)**: Verify implementation works correctly and meets original requirements
- **Goal**: Confirm solution solves original problem before documenting knowledge

**Why Stage 3 completion matters:**
- Step 4 produced compilable code; Step 5 confirms it functions correctly
- Testing reveals issues, regressions, or gaps in implementation
- Validation provides confidence before knowledge documentation (Stage 4 - Step 6)
- Solution measured against original problem requirements from Step 1

### Applied Prescriptive+Descriptive Pattern

Converted all Step 5 guidance to consistent prescriptive+descriptive format:

**Example from step_info.md:**
- Prescriptive: "Test both new functionality AND existing functionality to ensure no regressions"
- Descriptive (why): "Changes can break existing behavior; regression testing prevents introducing new problems while fixing old ones"

**Example from step_info.md:**
- Prescriptive: "Focus on ensuring solution meets original problem requirements"
- Descriptive (why): "Implementation success measured against original goals, not arbitrary standards"

### Restructured Data Sources with Guide + User-Review

Major restructure of data_sources.md to include BOTH guide and user-review files for all previous steps:

**PRIMARY SOURCE: Step 4 Implementation**
- Guide: Complete implementation log with architectural decisions, challenges, resolutions
- User-review: Implementation summary with quick reference
- Why primary: Need full context of what was implemented to design proper validation

**CONTEXT SOURCES: Steps 1-3 (Guide + User-Review)**
- **Step 1**: Problem understanding with requirements (validation criteria)
  - Guide: Complete context with reasoning, diagrams, Category 2/3
  - User-review: Problem summary for quick reference

- **Step 2**: Current state assessment before implementation
  - Guide: Complete research with evidence
  - User-review: Assessment summary

- **Step 3**: Solution design and task breakdown
  - Guide: Investigation findings, design rationale, tasks
  - User-review: Solution summary

**CURRENT STEP OUTPUTS:**
- Guide: Complete test documentation (methodology, results, issues, resolutions)
- User-review: Test status summary (pass/fail overview)

**Why guide vs user-review:**
- Guide files: Complete reasoning and context for Claude's comprehensive analysis
- User-review files: Glanceable summaries for quick reference checks
- Both needed: Guide for depth, user-review for rapid lookup

### Removed step4_references.md Reference

Cleaned up outdated reference:
- ❌ Removed mention of "active/{problem_id}/step4_references.md"
- This file is no longer created during Step 4
- Simplified data source structure

### Updated Step 5 Flow

1. **step_info.md** tells Claude:
   - Stage 3 completion context (validation after implementation)
   - Validation purpose (verify solution works and meets requirements)
   - Testing approach (review implementation, run tests, debug issues)
   - Regression constraint (test new AND existing functionality)
   - All with prescriptive+descriptive pattern

2. **data_sources.md** tells Claude WHERE data is:
   - Primary source: Step 4 implementation (guide + user-review)
   - Context sources: Steps 1-3 (guide + user-review for each)
   - Current step outputs: Step 5 guide + user-review
   - Why each source needed for validation

3. **output_requirements.md** tells Claude WHAT to create:
   - Dual output: user-review (test status) + guide (complete test documentation)
   - No changes needed (already structured correctly)

**Step Integration:**
- **Step 4**: Implemented all tasks, produced compilable code
- **Step 5**: Validates implementation works correctly, meets original requirements
- **Step 6**: Documents verified knowledge for future problems

## 🆕 Step 6 Enhancements: Knowledge Documentation + Skills Layer (Stage 4)

**Session Updates**: Step 6 improvements adding Stage 4 context, four-layer project memory system, and new Skills layer for reusable techniques.

### Stage 4 (Knowledge Documentation)

Step 6 is Stage 4 of the four-stage problem-solving model:
- **Stages 1-3 completed**: Problem solved through context alignment, understanding expansion, and solution translation
- **Step 6 (Knowledge Documentation)**: Capture verified knowledge for future sessions
- **Goal**: Build project memory incrementally so future problem-solving starts with proven knowledge

**Why Stage 4 matters:**
- Future sessions benefit from verified knowledge captured in this session
- Project memory eliminates re-discovering same information
- Systematic curation ensures knowledge is findable and reusable

### Four-Layer Project Memory System

Expanded from three-layer to **four-layer system** with new Skills layer:

**Layer 1: Architecture** - Component relationships and system structure
- What exists and how it connects
- Used in Steps 1-2 for understanding system components

**Layer 2: Features** - How system capabilities/features work
- Technical deep-dives into how capabilities operate
- Used in Steps 1-2-4 for understanding feature mechanics

**Layer 3: Solutions** - Problem solutions with git context
- How past problems were solved with exact code changes
- Used in Steps 2-3 for finding similar patterns
- ALWAYS created in every Step 6

**Layer 4: Skills** (NEW) - Reusable techniques and methodologies
- How to perform analysis/debugging/testing techniques
- Procedural knowledge applicable across multiple problems
- Used in Steps 2 (analysis techniques), 3 Phase 1 (debugging workflows), 5 (testing methodologies)

### Skills Layer: Reusable Techniques

**What is a Skill:**
- Reusable technique/methodology learned during problem-solving
- Procedural knowledge: "how to perform this task"
- Applies across multiple problems (not problem-specific)

**Skills vs Other Layers:**
- **NOT Architecture**: Skills are techniques, not component relationships
- **NOT Features**: Skills are procedures, not system capabilities
- **NOT Solutions**: Skills are reusable methods, not specific problem implementations

**Skill Categories** (all generic examples):
- **Analysis & Investigation**: Log correlation techniques, performance profiling, resource analysis
- **Debugging**: Systematic bug isolation, root cause analysis, error pattern recognition
- **Testing & Validation**: Test case design, validation procedures, benchmarking techniques
- **Measurement & Metrics**: Timing measurement, metric extraction, statistical analysis

**Skills Template Structure (Concise - 50-150 lines):**
1. **What** - 1-2 sentence description
2. **When to Use** - 2-4 applicable scenarios
3. **Key Markers/Identifiers** - REQUIRED for marker-based techniques (actual project-specific markers)
4. **Breakdown Structure** - REQUIRED for hierarchical techniques (ASCII tree with actual operation names)
5. **Procedure** - Concise actionable steps
6. **Example from Session** - 2-4 lines with actual data
7. **Common Pitfalls** - 2-4 bullets
8. **Related** - Links to solutions/architecture/features

**Quality Criteria:**
- ✅ 50-150 lines (200 max) - NO tutorial fluff
- ✅ ACTUAL project-specific markers: `recv:`, `## process_name` (not generic placeholders)
- ✅ ACTUAL operation names in breakdown: `DebugTool Step 'n'` → `DebugProtocol Packet` → `hardware transaction`
- ✅ Action verbs only: "Search", "Extract", "Calculate" (NOT "Understand", "Learn")
- ❌ NO exercises, practice sections, difficulty ratings, verbose explanations

**When to Create Skills** (in Step 6):
- Learned reusable technique during this session
- Technique applies across multiple problem types
- Procedural knowledge worth capturing for future use

**Where Skills Are Used:**
- **Step 2**: Analysis and research techniques, measurement procedures
- **Step 3 Phase 1**: Debugging workflows, investigation methodologies
- **Step 5**: Testing methodologies, validation procedures

### Updated Step 6 Workflow

Applied prescriptive+descriptive pattern throughout:

**Example from step_info.md:**
- Prescriptive: "Add the verified piece from THIS session to the incomplete puzzle"
- Descriptive (why): "Each session contributes one verified piece; completeness emerges over time"

**Example from data_sources.md:**
- Prescriptive: "Read guide files from ALL previous steps (Steps 1-5)"
- Descriptive (why): "Complete context ensures accurate knowledge extraction; guide files have full reasoning needed for curation"

**Example from output_requirements.md:**
- Prescriptive: "Create skills if reusable technique/methodology learned"
- Descriptive (why): "Skills capture procedural knowledge applicable to future problems; systematic approaches worth documenting"

### Updated Step 6 Input Components

1. **step_info.md** tells Claude:
   - Stage 4 context (knowledge documentation after solution complete)
   - Four-layer project memory system (architecture, features, solutions, skills)
   - Incremental verified knowledge mindset (project memory incomplete by design)
   - 🆕 **PHASED REVIEW WORKFLOW**: Four-phase approach (Sequential Step Review → Holistic Context → Create Outputs → Verification)
   - 🆕 **SESSION DISCOVERY REVIEW**: Structured review questions (Q1-Q9) to systematically evaluate Steps 1-5 for architecture/skills updates
   - All with prescriptive+descriptive pattern

2. **data_sources.md** tells Claude WHERE data is:
   - Guide + user-review for ALL previous steps (Steps 1-5)
   - Git context extraction commands
   - Existing project memory layers (check before duplicating)
   - No references to step4_references.md (removed)

3. **output_requirements.md** tells Claude WHAT to create:
   - 🆕 **Phased workflow overview**: Explains 4-phase structure and why this order
   - 🆕 **Phase-aligned checklist**: Completion checklist organized by phases
   - Solution pattern (ALWAYS)
   - Architecture updates (if new relationships discovered)
   - Feature documentation (if new capability created)
   - Skills documentation (NEW - if reusable technique learned)
   - 🆕 **Review reminders**: Points to SESSION DISCOVERY REVIEW before deciding "NOT NEEDED"
   - 🆕 **Verification requirements**: Phase 4 checklist for double-checking project_memory accuracy
   - Git context extraction for solutions

4. **project_memory_structure.md** documents:
   - Four-layer architecture with Skills as Layer 4
   - Skills template and examples (generic, no project-specific info)
   - Decision matrix showing when to use each layer
   - Framework integration showing which steps use which layers
   - Quality criteria for all layers

### SESSION DISCOVERY REVIEW: Structured Decision-Making

**Problem**: Generic criteria ("if THIS session discovered...") don't guide Claude through systematic review of actual discoveries from Steps 1-5, leading to conservative "NOT NEEDED" decisions.

**Solution**: Added structured review questions (Q1-Q9) in `step_info.md` that walk Claude through specific discovery areas:

**Architecture Discovery (Q1-Q4):**
- Q1: External tool integration discovered?
- Q2: Component relationships identified?
- Q3: System boundaries clarified?
- Q4: Hardware component variants discovered?

**Skills Discovery (Q5-Q9):**
- Q5: Log correlation technique used?
- Q6: Timing/measurement technique applied?
- Q7: Investigation workflow used?
- Q8: Analysis technique applied?
- Q9: Testing methodology documented?

**Decision Rule**: If ANY review question yields YES → update is warranted.

**Why this works**:
- **Systematic review**: Forces evaluation of specific discovery areas
- **Generic questions**: Uses abstract terms (external tool, hardware variants) applicable to any project
- **Clear YES/NO decisions**: Removes ambiguity in decision-making
- **Reusability test**: Skills questions include "Could this technique apply to other problems?"
- **Documentation requirement**: Claude must document reasoning in meta file

**Benefits**:
- Prevents incorrect "NOT NEEDED" decisions when discoveries exist
- Guides Claude through complete review without project-specific examples
- Makes decision-making transparent and traceable
- Ensures project memory grows richer with each session

### Phased Review Workflow: Preventing Cognitive Overload

**Problem**: Reading all guide files at once creates information overload, making it easy to miss important details in large context.

**Solution**: Four-phase workflow that reviews information sequentially, then holistically, then verifies accuracy:

**Phase 1: Sequential Step Review**
- Review each step (1-5) individually with SESSION DISCOVERY REVIEW questions
- Document findings per step: "Step N - Q[X] YES: [discovery]"
- Create Phase 1 discovery list with question references
- **Why**: Focused review of single step prevents missing discoveries in information overload

**Phase 2: Holistic Context Review**
- Read all Steps 1-5 guide files together
- Check for cross-step patterns missed in Phase 1
- Finalize complete discovery list (Phase 1 + Phase 2 additions)
- **Why**: Some patterns only emerge when viewing complete session flow

**Phase 3: Create Outputs**
- Generate insights files (user-review + guide)
- Extract git context
- Create solution pattern (ALWAYS required)
- Create architecture updates (if Phase 1/2 identified discoveries)
- Create skills (if Phase 1/2 identified reusable techniques)
- Update meta file
- **Why**: Phases 1-2 identify WHAT to document before creating outputs

**Phase 4: Verification**
- Re-read and verify solution pattern accuracy
- Re-read and verify ALL architecture updates (if created)
- Re-read and verify ALL skills (if created)
- Document verification in meta file: "Verification: Re-read and confirmed accuracy of [files]"
- **Why**: Project memory is verified knowledge for future sessions; verification ensures accuracy

**Benefits**:
- **Reduced cognitive load**: One step at a time prevents information overload
- **Complete coverage**: Sequential review ensures no step is skipped
- **Holistic view**: Final complete review catches relationships across steps
- **Quality assurance**: Verification phase ensures project_memory accuracy
- **Verified knowledge**: Double-checking maintains high-quality knowledge base for future sessions

**Step Integration:**
- **Step 5**: Completed validation, verified solution works
- **Step 6**: Documents knowledge (solution + optionally architecture/features/skills)
- **Future sessions**: Use project memory to start with proven knowledge

### Updated Steps That Use Skills

Added skills/ references to steps that use techniques:

**Step 2 data_sources.md:**
- Added Skills layer to project memory sources
- Analysis techniques, research methodologies, metric extraction

**Step 3 Phase 1 data_sources.md:**
- Added Skills layer to project memory sources
- Debugging workflows, investigation techniques, systematic approaches

**Step 5 data_sources.md:**
- Added new "PROJECT MEMORY SOURCES (TESTING SKILLS)" section
- Testing methodologies, validation procedures, benchmarking techniques

**To modify framework behavior:** Simply edit the relevant component files. Changes take effect immediately without code modifications. The framework now also learns from your usage patterns and automatically enhances your input components over time.

## Input Component Design Pattern: Prescriptive + Descriptive

**All input components across ALL steps should follow the prescriptive+descriptive pattern:**

- **Prescriptive**: State clearly WHAT to do (rules, requirements, format specifications)
- **Descriptive**: Explain WHY for each "what to do" (purpose, reasoning, context)

**Why this pattern matters:**
- Prescriptive gives Claude clear instructions on what actions to take
- Descriptive provides deeper understanding of the intent and reasoning
- Combination prevents misunderstandings by explaining rationale behind rules
- Ensures Claude both knows what to do AND understands why it matters
- Creates self-documenting input components that are easier to maintain

**Example of prescriptive+descriptive pattern:**
```markdown
**Prescriptive (WHAT):**
- ✅ Read GUIDE files for complete context (full reasoning, evidence, all iterations)

**Descriptive (WHY):**
- Guide files contain ALL details Claude needs for informed investigation
- User-review is concise summary for user glancing - not sufficient for Claude's analysis
- You need complete context to conduct effective investigation
```

**Where this pattern applies:**
- ✅ **step_info.md files**: Every approach, constraint, and workflow instruction
- ✅ **data_sources.md files**: Every source mentioned with what it provides and why needed
- ✅ **output_requirements.md files**: Every format rule, content requirement, and banned item
- ✅ **All steps (1-6)**: Consistent pattern across entire framework

**Current implementation status:**
- ✅ Step 1: Fully updated with prescriptive+descriptive pattern
- ✅ Step 2: Fully updated with prescriptive+descriptive pattern
- ✅ Step 3 Phase 1: Fully updated with prescriptive+descriptive pattern
- ✅ Step 3 Phase 2: Fully updated with prescriptive+descriptive pattern, continuation from Phase 1, task list creation focus
- ✅ Step 4: Fully updated with prescriptive+descriptive pattern, continuous implementation, build at end
- ✅ Step 5: Fully updated with prescriptive+descriptive pattern, Stage 3 completion, guide + user-review sources
- ✅ Step 6: Fully updated with prescriptive+descriptive pattern, Stage 4 context, four-layer project memory, Skills layer added

**When updating any input component:**
1. Review each instruction/rule/requirement
2. Ensure it states WHAT to do clearly (prescriptive)
3. Add explanation of WHY it matters (descriptive)
4. Test that Claude can understand both the action and the reasoning

## Enhanced System Evolution

This enhanced implementation transforms the original solution map from a static framework into a **learning, adaptive system** that:

### 🧠 **Learns from Usage**
- Analyzes actual conversation patterns, not just stated preferences
- Extracts generic working style preferences automatically
- Builds personalized system prompts through real usage

### 🎯 **Maintains Quality**
- Intelligent size management prevents prompt bloat
- Duplication detection keeps preferences clean and focused
- Smart consolidation preserves meaning while optimizing space

### 🔄 **Scales Intelligently**  
- Handles constraint violations gracefully through consolidation
- Priority-based selection maintains most valuable prompts
- Continuous learning without manual maintenance

### 🏗️ **Preserves Framework Integrity**
- Uses established input component patterns consistently
- Maintains separation between workflow preferences and domain knowledge
- Supports all original framework features while adding learning capabilities

The result is a **self-improving framework** that becomes more personalized and effective with each problem you solve, while maintaining the systematic methodology and friction-reducing experience originally envisioned.

### ✨ **Self-Contained Knowledge System** (New!)
- Three-layer project memory replaces external claude_docs dependency
- **Incremental verified knowledge**: Built piece-by-piece through six-step sessions, incomplete by design
- **Architecture layer**: Supporting docs for source code explaining component roles (flexible structure, not rigid 1:1 mapping)
- **Features layer**: Documents how capabilities work (async operations, auth, hardware protocol, etc.)
- **Solutions layer**: Preserves problem patterns with git commit/diff references
- **Progressive knowledge delivery**: Step 1 (overview) → Step 2 (deep-dive + past solutions)
- **Automatic curation**: Step 6 updates all three layers based on completed work
- **Comprehensive guidance**: `input_components/project_memory_structure.md` provides decision trees, templates, and quality criteria

## ✅ Testing & Verification

### Comprehensive Testing Completed
All enhanced functionality has been thoroughly tested and verified:

**🧪 Framework Initialization**
- ✅ Creates proper problem ID and directory structure
- ✅ Initializes active and meta directories correctly  
- ✅ Sets up current_state.json and STATE.md files

**🧪 Sixstep Command**
- ✅ Loads input components correctly for all steps/phases
- ✅ Composes enhanced prompts with all 4 components
- ✅ Includes meta logging instructions and response summary format
- ✅ Provides step-specific context and constraints

**🧪 Step-Done Command**  
- ✅ Successfully advances framework state (Step 1 → Step 2 verified)
- ✅ Composes preference extraction prompt using step-done input components
- ✅ Provides correct file paths for analysis (meta files, input components)
- ✅ Includes all constraint instructions (max 3 prompts, generic only)

**🧪 Update-Input-Components Command**
- ✅ Loads constraint-handling input components correctly
- ✅ Reads existing USER PREFERENCES sections (or detects when none exist)
- ✅ Provides integration scenarios and smart consolidation instructions
- ✅ Includes size management and duplication detection guidance

**🧪 Meta File Logging**
- ✅ Creates proper interaction format with timestamps
- ✅ Uses strict format contract from meta_file_format.md
- ✅ Includes placeholders for Claude response summaries

**🧪 Architectural Consistency**
- ✅ All commands use single Python script (consistent with `/sixstep`)
- ✅ Each script loads input components and outputs enhanced prompts  
- ✅ No complex orchestration or subprocess calls needed
- ✅ Clean, maintainable code structure

### Command Architecture Summary
```
/start-sixstep    →    Hook executes: framework_state.py start "$ARGUMENTS"
/sixstep          →    Hook executes: compose_input.py "$ARGUMENTS"
/step-done        →    Hook executes: step_done.py
/update-input-components → Hook executes: update_input_components.py "$ARGUMENTS"
```

**Key Architecture Benefits:**
- **Hook-Based Execution**: All commands use Claude Code hooks for guaranteed script execution
- **Native Prompt Delivery**: Enhanced prompts sent directly to Claude without tool use overhead
- **Consistent Pattern**: Load input components → compose enhanced prompt → send natively to Claude