# How Sixstep Differs from Other Tools

## Sixstep vs Claude Code, OpenAI Codex, Cursor

### Core Difference: Problem Solving as a Journey

- **Sixstep** sees problem solving as journey with multiple stages
- **Other tools** (Claude Code, OpenAI Codex, Cursor) don't see it that way

**Why this matters:**
- Different stages need different kinds of help
- What you need at beginning (alignment) is different from what you need at end (knowledge capture)
- Without journey view, tools give same generic help throughout
- With journey view, sixstep can provide stage-appropriate support

- Since sixstep sees problem solving as journey, it can integrate well with that journey and behave accordingly at every stage

---

## Organic vs Manual: The Key Difference

### Other Tools: Manual Effort Model

To get good experience, you must invest effort outside problem solving:
- Build custom slash commands for common patterns
- Write skills to capture project-specific knowledge
- Manually document solutions for future reference
- Constantly manage context to avoid losing important information

### Sixstep: Organic Growth Model

Experience improves automatically through normal use:
- Sixstep guides you naturally through stages
- Each session leaves knowledge in project memory
- No extra configuration or meta-work required
- Focus stays on solving the problem, not managing the tool

---

## Three Levels of Help

Sixstep helps at three levels. Each level addresses what's missing in other tools.

### Level 1: Current Session Support

**Without sixstep:**
- Jump straight to implementation without alignment
- No journey-specific memory - context window fills and important decisions get lost
- No visibility into what stage you're at

**With sixstep:**
- **Alignment (Step-1)**: Problem understanding aligned before work starts
- **Session Memory (Guide files)**: Context preserved with priority levels - guide files never lost
- **Progress Tracking (User-review files)**: Clear snapshot of current stage

### Level 2: Future Session Benefit

**Without sixstep:**
- Knowledge from completed sessions stays in chat history
- Next similar problem starts from scratch
- Manual documentation rarely happens

**With sixstep:**
- **Automatic Capture (Step-6)**: Project memory updated with verified knowledge
- **Organic Improvement**: Future sessions benefit from past learnings
- **Complete Loop**: Using sixstep makes sixstep better for next time

### Level 3: Team Knowledge Sharing

**Without sixstep:**
- Individual knowledge stays isolated
- New team members start with zero context
- Knowledge transfer requires manual effort

**With sixstep:**
- **Shareable Memory**: Project memory works for entire team
- **Easier Adoption**: New users start with accumulated knowledge
- **Collective Improvement**: Team benefits from everyone's sessions

---

## Concrete Examples: How It Actually Works

### Example 1: Starting New Feature Implementation

**Other tools:**
```
User: "Add rate limiting to the API"
→ Claude: Suggests Redis-based implementation
→ User: "Wait, we don't have Redis infrastructure"
→ Claude: "Oh, then use in-memory rate limiting"
→ User: "That won't work across multiple instances"
→ Back-and-forth to understand constraints
→ Finally implement with existing middleware
```

**Sixstep:**
```
User: /start-sixstep Add rate limiting to API
→ Step-1: Shows API architecture diagram
→ Step-1: Asks "What infrastructure available? Multiple instances?"
→ User clarifies in low-cost way
→ Aligned approach: Use existing middleware
→ Implementation starts with correct approach
```

**Key difference**: Misunderstanding caught in Step-1 (cheap) vs during implementation (expensive)

### Example 2: Long Investigation Session

**Other tools:**
```
Hour 1: Decide to investigate timing at each pipeline stage
Hour 2: Find bottleneck in serialization layer
Hour 3: Context compaction happens
Hour 4: Claude suggests investigating timing - already did this!
→ User must re-explain what was already investigated
```

**Sixstep:**
```
Step-3: Investigation findings captured in guide file
- Timing measured at each stage
- Bottleneck identified: serialization
Step-4: Guide file clearly shows investigation results
→ No repeated investigation
→ Implementation uses verified findings
```

**Key difference**: Investigation preserved in guide vs lost to context compaction

### Example 3: Solving Similar Problem Later

**Other tools:**
```
Week 1: Solve authentication caching problem (2 hours)
Week 4: Similar session caching problem comes up
→ No memory of Week 1 solution
→ Start from scratch again (2 hours)
```

**Sixstep:**
```
Week 1: Solve auth caching through sixstep
→ Step-6: Captures pattern in project memory
Week 4: Start session caching problem
→ Step-1: Sees related solution in project memory
→ Suggests proven approach from Week 1
→ Solve in 30 minutes using established pattern
```

**Key difference**: Learning from past vs starting fresh every time

---

## What Journey View Enables

Understanding problem-solving as stages unlocks capabilities other tools can't provide:

### Enable 1: Stage-Appropriate Guidance

Because sixstep knows which stage you're in:
- **Step-1**: Focuses on alignment and questions (not premature solutions)
- **Step-2**: Gathers facts (not opinions or analysis yet)
- **Step-3**: Investigates collaboratively (not jumping to implementation)
- **Step-4**: Implements systematically (not guessing requirements)
- **Step-6**: Captures knowledge (not losing learnings)

Other tools: Same behavior regardless of stage (usually "suggest implementation immediately")

### Enable 2: Intelligent Memory Management

Because sixstep understands journey context:
- Guide files = high priority (decisions, reasoning, findings)
- Chat history = low priority (can be compacted)
- Project memory = permanent (verified knowledge)

Other tools: Everything equally weighted in context window

### Enable 3: Automatic Workflow

Because framework knows the stages:
- Knows when alignment needed → Step-1
- Knows when investigation needed → Step-3
- Knows when knowledge capture needed → Step-6

Other tools: User decides workflow, often skip important stages

---

## Summary

| Aspect | Other Tools (Claude Code, Codex, Cursor) | Sixstep |
|--------|------------------------------------------|---------|
| **Problem solving view** | No journey stages concept | Journey with multiple stages |
| **Behavior adaptation** | Same behavior throughout | Behaves differently at each stage |
| **Customization** | Requires manual slash commands/skills | Organic help at 3 levels |
| **Current session memory** | Limited context window + basic memory | Guide files specific to journey |
| **Future session benefit** | Manual setup needed | Project memory updates automatically |
| **Knowledge sharing** | Not designed for it | Project memory shareable across team |
| **Getting better over time** | User effort required | Organic improvement through use |
