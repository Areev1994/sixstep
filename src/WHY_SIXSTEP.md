# Why Sixstep?

## The Problem with Current Approach

- When I used Claude Code, I had a few expectations but it failed to meet those. **Sixstep is an attempt to either meet those expectations or work around them**

- My experience with Claude Code was mixed:
  - **Positive**: I could eventually go from problem statement to implemented code
  - **Negative**: Required a lot of back and forth, frequent rework, and made the journey frustrating

- **Sixstep is an attempt to keep the positive outcomes while making the journey smoother**

---

## The Root Cause: Six Implicit Assumptions

When I thought about reasons why the journey was not great, it comes down to a bunch of **assumptions that are implicit** and causing mismatch in expectation and making the journey not good.

**Why implicit assumptions are problematic:**
- They're never stated explicitly, so you don't realize they exist
- When assumptions are violated, the interaction breaks down
- You waste time in back-and-forth fixing misunderstandings
- Both user and Claude operate with different mental models

Here are the 6 key assumptions I identified:

### Assumption 1: Clear Codebase

- Assumption is that codebase has clear information meaning there is no ambiguity and misleading information
- And also codebase is enough to understand how the system works and its place in ecosystem

**Example scenario:**
- Claude suggests using a deprecated function because it found it in the codebase, but there's no documentation explaining it's deprecated
- This leads to wasted time implementing wrong solution

### Assumption 2: No Understanding Gap

- Assumption is that once user provided problem statement, there is no gap in understanding between user and Claude since there is codebase for reference

**Example scenario:**
- User asks to "fix the authentication bug" but Claude doesn't know if you mean OAuth, session management, or password validation
- Claude makes assumption about which one and implements wrong fix

### Assumption 3: Claude Remembers Everything

- Assumption is Claude remembers instructions provided by user in the session
- But there is limited context window and during context compaction, some of these context will be lost

**Example scenario:**
- You tell Claude "use the pattern from earlier conversation" but that context was lost during compaction
- Claude doesn't know what pattern you're referring to and has to ask again or guesses wrong

### Assumption 4: User Has Complete Understanding

- Assumption is that either user knows the solution from beginning, or Claude knows how to solve the problem and user agreed with that solution

**Example scenario:**
- User asks to "optimize the query" but doesn't actually know why it's slow
- Without investigation, both user and Claude work on wrong optimization approach

### Assumption 5: Single Prompt Solution Design

- Assumption is user can clearly provide solution in single prompt and Claude would get it

**Example scenario:**
- User says "implement caching" but Claude interprets it differently than user intended (in-memory vs Redis vs file-based)
- Results in implementation that doesn't match user's mental model

### Assumption 6: Claude Remembers Corrections

- Assumption is once I have provided some correction, it remembers and understands the reasoning behind it
- This is not true because Claude doesn't know which context is important and which is not
- And because of that, it can overload context window and lose some contexts during compaction

**Example scenario:**
- You correct Claude saying "don't use approach X because it breaks feature Y" but later it uses X again because the correction was lost
- You have to repeat the same correction multiple times

---

## How Sixstep Addresses Each Assumption

### For Assumption 1 (Clear Codebase)

- **Problem**: Codebase alone has ambiguity and missing context about how system works
- **Sixstep solution**: Project memory acts as supporting documentation to make codebase clearer and less scope for misinterpretation
- **How it helps**: You build up verified knowledge over time in project memory. When Claude reads project memory + codebase, it gets both code AND context about how things work
- **Result**: Less misinterpretation, fewer wrong suggestions based on incomplete understanding

### For Assumption 2 (No Understanding Gap)

- **Problem**: User's problem statement may not be fully understood by Claude even with codebase available
- **Sixstep solution**: Step-1 tries to align user and sixstep about the problem
- **How it helps**: Step-1 allows user to correct how sixstep should think and approach problem before any implementation work starts. It helps to achieve alignment between user and sixstep in low-cost way
- **Result**: Both user and sixstep have shared understanding before investing effort in wrong direction

### For Assumption 3 (Claude Remembers Everything)

- **Problem**: Limited context window means some instructions and context will be lost during compaction
- **Sixstep solution**: Sixstep creates guide file at each step. This allows sixstep to remember context that is needed
- **How it helps**: This also allows to set in sixstep levels of priority in context. Meaning guide file is high priority context and whereas conversation history is not high priority context. Guide files are always available and never lost
- **Result**: Important context persists across steps and conversation compactions

### For Assumption 4 (User Has Complete Understanding)

- **Problem**: User may not have complete understanding of problem to solve it from beginning
- **Sixstep solution**: Step-3 makes explicit that there is gap in understanding
- **How it helps**: It brings both user and sixstep in same page through collaborative investigation. Step-3 focuses on increasing understanding before jumping to solution
- **Result**: Both user and sixstep improve understanding of problem statement together before designing solution

### For Assumption 5 (Single Prompt Solution Design)

- **Problem**: User may not be able to clearly provide complete solution design in single prompt
- **Sixstep solution**: Step-3 also explicit about designing solution and then making tasklist
- **How it helps**: It helps user to provide solution in more detailed and structured way to sixstep through iterative design process, then breaks it down into concrete tasks
- **Result**: Solution design is validated and clear before implementation begins, reducing mismatches

### For Assumption 6 (Claude Remembers Corrections)

- **Problem**: Corrections provided during session may be lost or forgotten due to context limitations
- **Sixstep solution**: Having user-review and guide helps to make sixstep to remember corrections in problem solving journey in more effective way
- **How it helps**: Corrections and important decisions are captured in guide files with reasoning. These files are read at each subsequent step
- **Result**: Corrections persist and don't need to be repeated. Claude understands not just what to do, but why

---

## Key Concepts Referenced

Understanding these key concepts will help clarify how sixstep works:

- **Project Memory**: Verified knowledge base built over time through sixstep sessions. Contains 4 directories: architecture, features, solutions, and skills. Acts as supporting documentation for the codebase.

- **Guide File**: Complete context file created at each step for Claude to read in future steps. Contains full details, reasoning, evidence, and file references. High priority context that persists.

- **User-Review File**: Glanceable summary file created at each step for quick user review. Concise format (2-3 minutes to scan). Helps user track progress.

- **Step-1**: First step in sixstep journey where user and sixstep align on problem understanding. Includes architectural diagram, questions, and approach strategy.

- **Step-3**: Investigation and solution design step. Makes explicit the gap in understanding. Collaborative investigation followed by solution design and task breakdown.

---

## What This Means

By making these implicit assumptions **explicit** and building structure around them:

- **Less wasted work**: Align before implementing (Step-1). Validate understanding before designing (Step-3)

- **Better context management**: Guide files + project memory preserve important information across steps and sessions

- **Collaborative problem-solving**: Step-3 brings user and sixstep to same understanding through investigation before solution design

- **Structured progress**: Each step builds on verified knowledge from previous steps. Context persists through guide files

- **Corrections that stick**: User-review and guide files capture corrections with reasoning so they don't get lost

**The result**: Smoother journey from problem statement to working solution, with less frustration and rework.
