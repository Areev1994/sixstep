# Sixstep Overview

## What is sixstep trying to do

- Product I am developing is **sixstep** that improves user experience of sessions with code assistant tools like claude from start to end of solving a problem specifically working on existing codebase

- **Start**: Always a problem statement

- **End**: Mostly of two types
    - One if code change for a feature or fixing bugs
    - Second is increased understanding of a feature or system behavior

- How I think about problem solving is a **journey with four stages**. Journey here is from problem statement to implemented code or increased understanding.

### The Four Stages

- **Stage-1**: Bringing all relevant information of problem statement to forefront
- **Stage-2**: Increasing understanding to a level where user can design a solution. Followed by actually designing the solution
- **Stage-3**: Translating solution design into actual implementation in the form of code
- **Stage-4**: This is a helper stage. This stage document learning and changes made in codebase in a way that would help future problem solving journey

### Stages and Steps

- Each stage is accomplished through one or more concrete **steps**
- In total, there are **6 steps** across the 4 stages (this is why it's called "sixstep"):
  - Stage-1 is done through two steps: step-1 and step-2
  - Stage-2 is done through one step: step-3
  - Stage-3 is done through two steps: step-4 and step-5
  - Stage-4 is done through one step: step-6

---

## How sixstep will help problem solving journey

- sixstep knows what stage user in problem solving journey and behave accordingly

### Stage-1

This stage is done through two steps: **step-1** and **step-2**

**Purpose**: Align user and sixstep about problem and approach strategy

#### Step-1: Three Parts

**Part 1: Architectural Diagram**
- Building block view to indicate what all are components involved for the problem statement and how they fit into overall system
- This is a means to bring the relevant information context to forefront
- This diagram is built from architecture diagram in [project memory](#project-memory) (a knowledge base built over time - more details in Stage-4)

**Part 2: Questions in Two Categories**
- These questions are formed by looking project memory and doing light code search

- **Category 1 - Clarification Questions**
    - sixstep will present questions in this category if problem statement is incomplete or need any clarification like user preference
    - These questions are answered by user directly

- **Category 2 - Context Questions**
    - These questions are to bring factual information (not analytical information) about problem statement to forefront

**Part 3: Approach Strategy for Stage-2**
- This represents strategy that is going to be used in stage-2 to increase understanding of problem to a level where solution can be designed

**Output and Benefits**
- All of these things will be presented to user in markdown file format in glanceable way (easy to scan and review quickly)
- This would give opportunity for user to see how sixstep thinking about the problem and approach strategy that it is going to use to learn about problem statement
- User can correct sixstep in this step in a less expensive way
- This would help to align user and sixstep and also setup a really solid contract for sixstep to proceed further

#### Step-2: Answering Context Questions

- Step-2 would try to figure out answers to context questions of step-1
- If sixstep cannot find answers fully or not confident about answers, it would mark those answers as partially answered or low-confidence
- These answers will be verified again during stage-2
- Step-2 marks end of stage-1 and sets up good context for investigation and brainstorming in stage-2

---

### Stage-2

This stage is done through one step: **step-3**

**Purpose**: Increase understanding of problem statement

**How Investigation Works**
- Stage-2 starts with sixstep doing analysis that was agreed on stage-1 and bring initial analysis to user in a markdown file in glanceable way
- User will look at the file and provide suggestion and input on how to investigate further
- This goes on till understanding of problem reaches to a point where solution can be designed
- This part of the journey would happen like **solution map** (collaborative investigation where user and sixstep work together) to figure out pieces that need to be understood and learning about those pieces

**Solution Design Phase**
- Once good understanding about the problem reached, user and sixstep brainstorm about solution and decide on final solution
- Once final solution is agreed on, solution is broken down into list of tasks
- Each task is added with details on how it is going to be implemented
- Tasklist creation act as preparation for stage-3

---

### Stage-3

This stage is done through two steps: **step-4** and **step-5**

**Purpose**: Translate tasklist into working feature

#### Step-4: Implementation
- Implementation of all tasks in tasklist

#### Step-5: Testing and Bug Fixing
- Testing, debugging and fixing bugs to get fully working feature

---

### Stage-4

This stage is done through one step: **step-6**

**Purpose**: Update project memory with changes made in project and capture any project specific skills learned during current sixstep session

#### Step-6: Project Memory Update

- Project memory is structured in a way that it can effectively updated with changes made and skills captured during current session
- Also it can be really useful for future sixstep sessions
- Project memory is initialized with only first level building block view at first
- Rest of project is incrementally built overtime through step-6 of various sixstep sessions

---

## Project Memory

Project memory is composed of **four directories**:

### 1. Architecture Directory

- Building block view of the project in hierarchical manner
- To be specific, there are levels of block diagram:
    - **First level**: Block diagram of all high level components involved in the project
    - **Next level**: Separate block diagram of each components in the first level
    - **Continues recursively** to create block diagrams in hierarchical manner
- This follows arc42 documentation template specifically building block view (https://docs.arc42.org/section-5/)

### 2. Features Directory

- Features directory holds runtime view of important features
- This would describe concrete behavior and interaction of system's building blocks of important features
- This also follows arc42 documentation specifically runtime view (https://docs.arc42.org/section-6/)

### 3. Solutions Directory

- This directory will hold files summarizing what happened in sixstep session
- Basically, one file is made for a sixstep session
- This file will have complete problem solving journey in a way that becomes useful if any future sixstep session tries to solve a similar problem

### 4. Skills Directory

- This is to capture project specific skills that was used during stage-2 and stage-3
- **Example 1**: How user investigated log files like relating logs from different components using specific marker during stage-2
- **Example 2**: How user tried to test a particular component in the project during stage-3

---

## Implementation Details

### Runtime View of a Step

This shows what happens internally when any single step executes.

```
 ┌─────────────┐
 │ User Input  │
 │ /sixstep    │
 └──────┬──────┘
        │
        ▼
 ┌──────────────────┐
 │ Step Detection   │
 │ (framework_state)│
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────────────────────────────┐
 │ Enhanced Prompt                          │
 │ (compose_input.py)                       │
 │                                          │
 │ Composes:                                │
 │  - Framework Info                        │
 │  - Step Info                             │
 │  - Data Sources                          │
 │  - Output Requirements                   │
 └──────┬───────────────────────────────────┘
        │
        ▼
 ┌──────────────────┐
 │   Claude Code    │
 │   (AI Model)     │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────────────────────────────┐
 │ Response                                 │
 │                                          │
 │ Generates:                               │
 │  - user-review file                      │
 │  - guide file                            │
 │  - project repo updates (Steps 4-5)     │
 │  - project memory updates (Step 6)      │
 └──────┬───────────────────────────────────┘
        │
        ▼
 ┌──────────────────────┐
 │ User reviews files   │
 │                      │
 │ Proceed to next step?│
 └───┬────────────┬─────┘
     │ No         │ Yes
     │            │
     │            ▼
     │     ┌─────────────────┐
     │     │  /step-done     │
     │     │  Advance to     │
     │     │  next step      │
     │     └─────────────────┘
     │
     │ User provides suggestions
     │
     └───────────┐
                 │
                 │ Loop back to same step
                 │
                 ▼
          ┌─────────────┐
          │ User Input  │
          │ /sixstep    │
          └─────────────┘
```

**Key Points:**
- **Step Detection**: Identifies which step/phase we're currently in
- **Enhanced Prompt**: Composes context-aware instructions for Claude
- **Claude Code**: AI model processes the prompt and generates response
- **Response**: Packages outputs into files and updates state
- If user not satisfied, loop back to beginning of same step (step number unchanged)

### Runtime View of a Session

This shows how a complete sixstep session flows from start to finish. Each step box represents the complete pipeline shown in "Runtime View of a Step" above.

```
     ┌─────────────────────────────┐
     │ User runs /start-sixstep    │
     │    Problem Statement        │
     └──────────────┬──────────────┘
                    │
                    ▼
     ┌──────────────────────────────┐
     │         Step-1               │◄──┐
     │  (Pipeline from diagram      │   │
     │   above executes)            │   │ User provides
     │                              │   │ suggestions
     │  Outputs: user-review,       │   │
     │           guide files        │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes (/step-done)
                ▼
     ┌──────────────────────────────┐
     │         Step-2               │◄──┐
     │  (Pipeline executes)         │   │
     │                              │   │
     │  Outputs: user-review,       │   │
     │           guide files        │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes (/step-done)
                ▼
     ┌──────────────────────────────┐
     │         Step-3               │◄──┐
     │  (Pipeline executes)         │   │
     │                              │   │
     │  Outputs: user-review,       │   │
     │           guide files        │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes (/step-done)
                ▼
     ┌──────────────────────────────┐
     │         Step-4               │◄──┐
     │  (Pipeline executes)         │   │
     │                              │   │
     │  Outputs: user-review,       │   │
     │           guide files,       │   │
     │           + project repo     │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes (/step-done)
                ▼
     ┌──────────────────────────────┐
     │         Step-5               │◄──┐
     │  (Pipeline executes)         │   │
     │                              │   │
     │  Outputs: user-review,       │   │
     │           guide files,       │   │
     │           + project repo     │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes (/step-done)
                ▼
     ┌──────────────────────────────┐
     │         Step-6               │◄──┐
     │  (Pipeline executes)         │   │
     │                              │   │
     │  Outputs: user-review,       │   │
     │           guide files,       │   │
     │           + project memory   │   │
     └──────────────┬───────────────┘   │
                    │                   │
                    ▼                   │
            ┌───────────────┐           │
            │ User happy?   │───No──────┘
            └───┬───────────┘
                │ Yes
                ▼
     ┌──────────────────────────────┐
     │     Session Complete         │
     └──────────────────────────────┘
```

**Key Points:**
- Each step box represents the complete step pipeline (detection → enhanced prompt → claude → response → user review)
- User reviews outputs after each step
- If not satisfied, user provides suggestions and step repeats (step number stays same)
- If satisfied, user runs `/step-done` to advance to next step
- Steps 1-3: Understanding and design (read project repo)
- Steps 4-5: Implementation and testing (update project repo)
- Step 6: Knowledge capture (update project memory)

### Building Block View

This shows the main components that make sixstep work and how they interact.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Sixstep System                                 │
│                                                                         │
│  ┌──────────────────┐      ┌──────────────────────────────────┐       │
│  │                  │      │                                  │       │
│  │  Step Detection  │─────▶│      Enhanced Prompt            │       │
│  │                  │      │                                  │       │
│  │  Identifies      │      │  Composes context-aware         │       │
│  │  current step    │      │  instructions from 4            │       │
│  │  and phase       │      │  input components               │       │
│  │                  │      │                                  │       │
│  └──────────────────┘      └────────────┬─────────────────────┘       │
│                                         │                              │
│                                         ▼                              │
│                            ┌──────────────────────────┐               │
│                            │                          │               │
│                            │      Claude Code         │               │
│                            │                          │               │
│                            │  AI model that processes │               │
│                            │  enhanced prompt and     │               │
│                            │  generates response      │               │
│                            │                          │               │
│                            └────────────┬─────────────┘               │
│                                         │                              │
│                                         ▼                              │
│                            ┌──────────────────────────┐               │
│                            │                          │               │
│                            │       Response           │               │
│                            │                          │               │
│                            │  Generates user-review,  │               │
│                            │  guide files, updates    │               │
│                            │  repo and memory         │               │
│                            │                          │               │
│                            └────────────┬─────────────┘               │
│                                         │                              │
│                                         │                              │
│                       ┌─────────────────┴──────────────────┐          │
│                       │                                    │          │
│                       ▼                                    ▼          │
│              User reviews files                  ┌──────────────────┐ │
│              If satisfied ────────────────────────▶│                  │ │
│                                                   │  Step-Done       │ │
│                                                   │  Mechanism       │ │
│                                                   │                  │ │
│                                                   │  Advances        │ │
│                                                   │  framework state │ │
│                                                   │  to next step    │ │
│                                                   │                  │ │
│                                                   └──────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**The 5 main building blocks:**

1. **Step Detection** - Knows which step you're in
2. **Enhanced Prompt** - Creates context-aware instructions for each step
3. **Claude Code** - AI model that does the work
4. **Response** - Packages results into files
5. **Step-Done Mechanism** - Advances to next step when user is satisfied

Each component serves a specific purpose:

#### 1. Step Detection

**Why needed:**
- Sixstep needs to know which step/phase is currently active
- Different steps have different instructions, data sources, and output requirements

**How it works:**
- Uses `framework_state.py` to read current state from `current_state.json`
- Identifies current step number and phase (if applicable)
- This determines which input components to load

#### 2. Enhanced Prompt

**Why needed:**
- Claude needs structured, context-aware instructions for each step
- Generic prompts would not provide step-specific guidance

**How it's composed:**
- Script `compose_input.py` loads 4 input components:
  1. **Framework Info**: Global context about the problem-solving journey
  2. **Step Info**: Current step's role, approach, and constraints
  3. **Data Sources**: Where to find information (project memory, guide files, codebase)
  4. **Output Requirements**: What files to create and in what format

**What it looks like for each step:**
- **Step 1**: Instructions to generate architectural diagram and questions
- **Step 2**: Instructions to answer context questions through research
- **Step 3**: Instructions for investigation and solution design
- **Step 4**: Instructions for implementation of all tasks
- **Step 5**: Instructions for testing and validation
- **Step 6**: Instructions for updating project memory

All step-specific components are stored in `input_components/step{N}/` directories

#### 3. Claude Code

**Why needed:**
- AI model that understands natural language instructions and can work with code
- Processes the enhanced prompt to perform the step's work

**How it works:**
- Receives the composed enhanced prompt
- Has access to project repo, project memory, and previous step outputs
- Generates code, analysis, documentation based on step requirements
- Creates responses following the output format specified in enhanced prompt

#### 4. Response

**Why two files are generated (user-review & guide):**

**User-Review File:**
- **Purpose**: Glanceable format for quick user review
- **Content**: Easy to scan and review quickly (2-3 minutes)
- **Audience**: User who needs to see progress and provide feedback
- **Format**: Concise summaries, key points only

**Guide File:**
- **Purpose**: Complete context for Claude's continuity across steps
- **Content**: Full details, reasoning, evidence, file references
- **Audience**: Claude reading in future steps to understand complete context
- **Format**: Comprehensive documentation with all information

**Other outputs:**
- **Project repo updates**: Code changes made during Steps 4-5
- **Project memory updates**: Knowledge captured during Step 6

#### 5. Step-Done Mechanism

**Why needed:**
- User needs way to signal satisfaction with current step and advance to next
- Framework state must be updated to reflect progression

**How it works:**
- User runs `/step-done` command after reviewing step outputs
- Script `step_done.py` executes:
  1. Extracts user preferences from completed step conversation
  2. Updates step_info files with learned preferences
  3. Advances step number in `current_state.json`
  4. Updates `STATE.md` with progress
  5. Runs `claude compact` to clear context for next step
- Next `/sixstep` command will use updated step number to load appropriate input components

**User interaction flow:**
1. User runs `/sixstep [question]` → Step executes with enhanced prompt
2. Claude generates user-review and guide files
3. User reviews outputs
4. If not satisfied: Provide suggestions → Run `/sixstep` again (same step)
5. If satisfied: Run `/step-done` → Framework advances to next step
