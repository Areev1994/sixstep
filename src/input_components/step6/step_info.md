Step 6: Project Memory Curation & Knowledge Documentation

## STAGE 4 CONTEXT

**STAGE 4 (Knowledge Documentation) - Step 6**

You are in Stage 4 of the four-stage problem-solving model. Stages 1-3 completed the problem-solving journey. Now in Stage 4, you document verified knowledge for future sessions.

**Why Stage 4 matters:**
- Stage 1-2 aligned context and expanded understanding
- Stage 3 implemented and validated the solution
- Stage 4 captures verified knowledge so future sessions benefit from this work
- Project memory enables future problem-solving to start with proven knowledge

## ROLE

Step 6 Project Memory Curator - Build and maintain the framework's project memory with verified knowledge across four layers.

**Why this role:**
- Future sessions need structured knowledge to avoid re-discovering same information
- Systematic curation ensures knowledge is findable and reusable
- Four-layer structure organizes different types of knowledge appropriately

## PURPOSE

Create self-contained project memory that captures verified knowledge from this six-step session across four knowledge layers.

**Why self-contained project memory:**
- Primary knowledge base for future framework sessions
- Eliminates dependency on external documentation
- Built incrementally through verified problem-solving sessions

## TARGET AUDIENCE

Future six-step framework sessions that will use project memory for:
- **Step 1**: System architecture diagrams and component context
- **Step 2**: Solution patterns with git diffs, analysis techniques (skills)
- **Step 3 Phase 1**: Debugging workflows (skills), architectural patterns
- **Step 5**: Testing methodologies (skills), validation procedures

**Why specific step targeting:**
- Each step has different knowledge needs during problem-solving
- Architecture helps Step 1 understand "what components exist"
- Features help Steps 1-2-4 understand "how capabilities work"
- Solutions help Steps 2-3 see "how similar problems were solved"
- Skills help Steps 2-3-5 apply "techniques for analysis/debugging/testing"

---

## UNDERSTANDING PROJECT MEMORY: INCREMENTAL VERIFIED KNOWLEDGE

**CRITICAL MINDSET**: Project memory is NOT a comprehensive artifact created once. It is built incrementally from scratch through six-step sessions.

**What project memory IS**:
- ✅ **Verified information** - Each piece created through systematic six-step process
- ✅ **Incomplete by design** - Built piece-by-piece as problems are solved
- ✅ **Evolving knowledge base** - Gets better and more complete with each session
- ✅ **Picture made of pieces** - Many pieces are expected to be missing

**What project memory is NOT**:
- ❌ NOT comprehensive or complete
- ❌ NOT covering all aspects of the project
- ❌ NOT exhaustive documentation

**Your role in Step 6**:
- Prescriptive: Add verified knowledge from THIS session to project memory
- Descriptive (why): Each six-step session contributes verified knowledge; project memory grows richer over time

- Prescriptive: Do NOT assume existing project_memory coverage is comprehensive
- Descriptive (why): Many components/features/patterns likely undocumented; gaps are normal and expected

- Prescriptive: Do NOT hesitate to add verified knowledge (components, features, patterns, skills) discovered during THIS session
- Descriptive (why): Your session may be first to document this knowledge; that's valuable contribution

**Expected state of project_memory**:
- **Architecture layer**: May only have a few components documented, many components likely undocumented
- **Features layer**: May only have features that previous sessions created/documented
- **Solutions layer**: Only contains patterns from completed six-step sessions
- **Skills layer**: Only contains techniques learned and documented in past sessions

**Implications for your work**:
- If a component is not in architecture/, that doesn't mean it's unimportant - it just hasn't been documented yet
- If a feature is not in features/, you may be the first to document it
- If a skill is not in skills/, you're capturing a reusable technique for the first time
- Your solution pattern will likely reference components/features not yet in project_memory - that's normal
- Focus on adding THIS session's verified knowledge, even if surrounding context is missing

**Making Project Memory Richer After This Session:**
- Prescriptive: Identify NEW knowledge from Steps 1-5 that future sessions will need
- Descriptive (why): Project memory grows incrementally; each session contributes verified knowledge

- Prescriptive: Architecture - add component relationships, hardware variants, system connections learned in THIS session
- Descriptive (why): Future Step 1/2 benefit from richer architecture context when scoping problems

- Prescriptive: Skills - capture analysis/debugging techniques from THIS session that are reusable
- Descriptive (why): Future sessions apply these proven techniques to similar problems

**Concrete examples of what to add:**
- System overview missing external tool integration? Add it if THIS session discovered how tool connects
- Component README missing hardware variant details? Add hardware/ subdirectory if THIS session learned about variants
- Skills directory missing analysis technique? Add it if THIS session used reusable procedure
- Solution pattern always created for THIS session's problem

**What happens over time:**
- Session 1 adds knowledge it discovered → incomplete but useful
- Session 2 adds more knowledge it discovered → getting richer
- Session N adds more knowledge it discovered → increasingly complete picture
- Each session makes project memory more valuable for future sessions

---

## PROJECT MEMORY STRUCTURE

📖 **For detailed structure guidance, decision criteria, content templates, and quality criteria**, see:
   `input_components/project_memory_structure.md`

**Four-layer knowledge system** in `project_memory/`:
- **Layer 1: Architecture** - Component relationships and system structure
- **Layer 2: Features** - How system capabilities/features work
- **Layer 3: Solutions** - Problem solutions with git context (ALWAYS create)
- **Layer 4: Skills** - Reusable techniques and methodologies

**Why four layers:**
- Different types of knowledge serve different purposes
- Architecture answers "what exists and how connected"
- Features answer "how does this capability work"
- Solutions answer "how was this problem solved"
- Skills answer "how do I perform this technique"

## CURATION WORKFLOW

**Overview**: Step 6 uses phased review workflow to prevent cognitive overload and ensure complete, accurate knowledge capture.

**Why phased approach:**
- Reading all guide files at once creates information overload
- Sequential step-by-step review ensures no discoveries are missed
- Holistic review catches relationships across steps
- Verification phase maintains high-quality verified knowledge

---

### PHASE 1: SEQUENTIAL STEP REVIEW

**Purpose**: Review each step individually to identify discoveries without cognitive overload.

**Process**: For EACH step (1 through 5), do complete review cycle:

**Step 1 Review:**
- Prescriptive: Read ONLY `active/{problem_id}/guide/step1_questions.md`
- Prescriptive: Apply SESSION DISCOVERY REVIEW questions Q1-Q3 (external tool, component relationships, system boundaries)
- Prescriptive: Document findings: "Step 1 - Q[N] YES: [discovery]" or "Step 1 - No architecture discoveries"
- Descriptive (why): Focused review of single step prevents missing discoveries in information overload

**Step 2 Review:**
- Prescriptive: Read ONLY `active/{problem_id}/guide/step2_assessment.md`
- Prescriptive: Apply SESSION DISCOVERY REVIEW questions Q4-Q6 (hardware variants, log correlation, timing/measurement)
- Prescriptive: Document findings: "Step 2 - Q[N] YES: [discovery]" or "Step 2 - No architecture/skills discoveries"
- Descriptive (why): Step 2 research often reveals hardware details and analysis techniques

**Step 3 Review:**
- Prescriptive: Read ONLY `active/{problem_id}/guide/step3_brainstorm.md`
- Prescriptive: Apply SESSION DISCOVERY REVIEW questions Q7-Q8 (investigation workflow, analysis technique)
- Prescriptive: Document findings: "Step 3 - Q[N] YES: [discovery]" or "Step 3 - No skills discoveries"
- Descriptive (why): Step 3 investigation findings often contain reusable debugging workflows

**Step 4 Review:**
- Prescriptive: Read ONLY `active/{problem_id}/guide/step4_implement.md`
- Prescriptive: Check for architectural decisions or component relationships discovered during implementation
- Prescriptive: Document findings: "Step 4 - Architecture: [discovery]" or "Step 4 - No new discoveries"
- Descriptive (why): Implementation sometimes reveals unexpected architectural details

**Step 5 Review:**
- Prescriptive: Read ONLY `active/{problem_id}/guide/step5_testing.md`
- Prescriptive: Apply SESSION DISCOVERY REVIEW question Q9 (testing methodology)
- Prescriptive: Document findings: "Step 5 - Q9 YES: [discovery]" or "Step 5 - No testing methodology to capture"
- Descriptive (why): Testing validation may use reusable testing procedures

**Phase 1 Output:**
- List of discoveries per step with SESSION DISCOVERY REVIEW question references
- Clear identification of which architecture updates and skills to create

---

### PHASE 2: HOLISTIC CONTEXT REVIEW

**Purpose**: After individual step reviews, read all guide files together to catch cross-step patterns and ensure nothing was missed.

**Process:**

**1. Read all guide files together:**
- Prescriptive: Read Steps 1-5 guide files in sequence
- Descriptive (why): Holistic view reveals patterns across steps that individual reviews might miss

**2. Check for cross-step patterns:**
- Prescriptive: Look for discoveries that span multiple steps (e.g., external tool mentioned in Step 1, used in Step 3)
- Prescriptive: Verify that Phase 1 findings are complete
- Prescriptive: Identify any additional discoveries missed in Phase 1
- Descriptive (why): Some patterns only emerge when viewing complete session flow

**3. Finalize discovery list:**
- Prescriptive: Combine Phase 1 findings with Phase 2 additional discoveries
- Prescriptive: Create final list of architecture updates and skills to create
- Descriptive (why): Complete discovery list ensures all verified knowledge is captured

---

### PHASE 3: CREATE OUTPUTS

**Purpose**: Generate all Step 6 deliverables based on finalized discovery list.

**Process:**

**1. Generate dual insights files:**
- Prescriptive: Create `active/{problem_id}/user-review/step6_insights.md` (glanceable version)
- Prescriptive: Create `active/{problem_id}/guide/step6_insights.md` (complete version)
- Descriptive (why): User-review for quick insights; guide for complete documentation and reasoning

**2. Extract git context:**
- Prescriptive: Use git commands to extract commit IDs or diffs
- Descriptive (why): Solutions must include implementation details; git context provides exact code changes for future reference

**3. Create solution pattern (ALWAYS):**
- Prescriptive: Create `project_memory/solutions/[pattern_name].md` using template from project_memory_structure.md
- Prescriptive: Include git commit ID or full diff in Implementation Details section
- Descriptive (why): Every six-step session solves a problem; solution pattern is required deliverable

**4. Create architecture updates (if Phase 1/2 identified discoveries):**
- Prescriptive: Update `project_memory/architecture/**/*.md` files based on finalized discovery list
- Prescriptive: Use templates from project_memory_structure.md Layer 1
- Descriptive (why): Architecture updates make system structure clearer for future sessions

**5. Create skills (if Phase 1/2 identified reusable techniques):**
- Prescriptive: Create `project_memory/skills/[skill_name].md` using template from project_memory_structure.md Layer 4
- Prescriptive: Follow quality criteria: 50-150 lines max, NO tutorial fluff (exercises, practice sections, verbose explanations)
- Prescriptive: Use ACTUAL project-specific content: real markers (`log_marker:`, `## process_name`), real tool names, real component names
- Prescriptive: If technique uses markers for correlation/identification, "Key Markers/Identifiers" section is REQUIRED with actual marker patterns from THIS session
- Prescriptive: If technique involves hierarchical breakdown, "Breakdown Structure" section is REQUIRED showing ASCII tree with actual operation names
- Prescriptive: Ensure reusability test passed (technique applies to multiple problems)
- Descriptive (why): Skills with actual markers are directly actionable; future sessions know exact patterns to search for, no interpretation needed

**6. Update meta file:**
- Prescriptive: Replace placeholder with response summary in meta/{problem_id}/step6.md
- Descriptive (why): Framework tracking; maintains conversation log

---

### PHASE 4: VERIFICATION

**Purpose**: Double-check all project_memory changes to ensure accuracy before finalizing.

**Why verification critical:**
- Project memory is verified knowledge used by future six-step sessions
- Inaccurate information in project_memory causes confusion and errors in future work
- Verification maintains high-quality knowledge base

**Process:**

**1. Verify solution pattern:**
- Prescriptive: Re-read `project_memory/solutions/[pattern_name].md`
- Prescriptive: Confirm all information comes from THIS session's Steps 1-5
- Prescriptive: Check git commit ID/diff is included and correct
- Prescriptive: Verify no speculation or assumptions added
- Descriptive (why): Solution pattern is primary reference for similar future problems

**2. Verify architecture updates:**
- Prescriptive: Re-read ALL modified `project_memory/architecture/**/*.md` files
- Prescriptive: Confirm component relationships/hardware variants are from THIS session's discoveries
- Prescriptive: Check cross-references to other architecture files are correct
- Prescriptive: Verify no project_memory-breaking changes (e.g., contradicting existing verified knowledge)
- Descriptive (why): Architecture forms foundation for future sessions' system understanding

**3. Verify skills:**
- Prescriptive: Re-read ALL created `project_memory/skills/[skill_name].md` files
- Prescriptive: Confirm technique was actually used in THIS session (reference specific step)
- Prescriptive: Verify reusability (technique applies beyond this specific problem)
- Prescriptive: Check procedure steps are accurate and complete
- Descriptive (why): Skills are reusable techniques; inaccurate procedures mislead future sessions

**4. Document verification:**
- Prescriptive: In meta file, add "Verification: Re-read and confirmed accuracy of [list files]"
- Descriptive (why): Verification documentation shows Step 6 quality assurance was performed

**Phase 4 Output:**
- Verified project_memory changes ready for future sessions
- Documentation of verification in meta file

---

## SESSION DISCOVERY REVIEW

**Purpose**: Systematically review Steps 1-5 to identify verified knowledge that warrants architecture or skills updates.

**When to use**: Before deciding "NOT NEEDED" for architecture/skills updates, complete this review.

**Why this matters**: Generic criteria ("if THIS session discovered...") require structured review of actual discoveries. This section provides specific review questions to guide decision-making.

---

### Step 1 Discovery Review

Read `active/{problem_id}/guide/step1_questions.md` and answer:

**Q1: External Tool Integration Discovered?**
- Did THIS session identify how external tool/system connects to the project?
- Examples: debugger connection path, test framework integration, monitoring tool interface
- **YES** → Update `architecture/system_overview.md` to show external tool connection

**Q2: Component Relationships Identified?**
- Did THIS session reveal how components communicate or depend on each other?
- Examples: protocol handler → internal module, layer-to-layer communication, data flow paths
- **YES** → Update relevant `architecture/[component]/README.md` or system_overview.md

**Q3: System Boundaries Clarified?**
- Did THIS session distinguish between layers/subsystems (e.g., UI layer vs API layer vs hardware layer)?
- Examples: user interface → server → API → hardware, internal vs external boundaries
- **YES** → Update `architecture/system_overview.md` to show layer boundaries

---

### Step 2 Discovery Review

Read `active/{problem_id}/guide/step2_assessment.md` and answer:

**Q4: Hardware Component Variants Discovered?**
- Did THIS session learn that hardware component comes in multiple versions/generations/variants?
- Examples: Component Gen1 vs Gen2, different capability modes, version-dependent features
- **YES** → Create/update `architecture/[component]/hardware/README.md` documenting variants

**Q5: Log Correlation Technique Used?**
- Did THIS session correlate information across multiple log sources to understand behavior?
- Examples: matching operations using markers, transaction identifiers, timestamps
- **Critical**: Document ACTUAL markers used for correlation (not generic "markers exist")
  - What exact patterns did you search for? (`recv:`, `send:`, transaction IDs, log prefixes?)
  - What format/structure? (`timestamp|component|marker: data`?)
  - Were there hierarchical breakdowns? (command → packets → transactions?)
- Reusability test: Could this technique apply to other multi-source log analysis problems?
- **YES to both** → Create `skills/log_correlation_[descriptive_name].md`
  - MUST include "Key Markers/Identifiers" section with ACTUAL markers from THIS session
  - MUST include "Breakdown Structure" section if hierarchical decomposition used

**Q6: Timing/Measurement Technique Applied?**
- Did THIS session extract timing, performance, or operational metrics from logs/traces?
- Examples: timestamp analysis, operation counting, transaction measurement
- Reusability test: Could this technique apply to other performance analysis problems?
- **YES to both** → Create `skills/measurement_[descriptive_name].md`

---

### Step 3 Discovery Review

Read `active/{problem_id}/guide/step3_brainstorm.md` (especially investigation findings) and answer:

**Q7: Investigation Workflow Used?**
- Did THIS session use systematic debugging/investigation approach to isolate root cause?
- Examples: binary search isolation, phase-by-phase breakdown, layer-by-layer analysis
- Reusability test: Could this workflow apply to other debugging problems?
- **YES to both** → Create `skills/debugging_workflow_[descriptive_name].md`

**Q8: Analysis Technique Applied?**
- Did THIS session decompose complex operation into measurable components?
- Examples: breaking down end-to-end operation into phases, analyzing operation patterns
- Reusability test: Could this technique apply to other analysis problems?
- **YES to both** → Create `skills/analysis_technique_[descriptive_name].md`

---

### Step 5 Discovery Review

Read `active/{problem_id}/guide/step5_testing.md` and answer:

**Q9: Testing Methodology Documented?**
- Did THIS session use validation procedure that is reusable across problems?
- Examples: regression test design, performance benchmarking approach, validation checklist
- Reusability test: Could this methodology apply to other testing scenarios?
- **YES to both** → Create `skills/testing_methodology_[descriptive_name].md`

---

### Applying Discovery Review to Update Decisions

**Architecture Layer Decision:**
- If ANY of Q1-Q4 answered YES → Architecture update NEEDED
- Specific updates:
  - Q1 YES → Update system_overview.md with external tool integration
  - Q2 YES → Update component README or system_overview with relationships
  - Q3 YES → Update system_overview.md with layer boundaries
  - Q4 YES → Create/update hardware/ subdirectory with variant documentation

**Skills Layer Decision:**
- If ANY of Q5-Q9 answered YES (and reusability test passed) → Skills creation NEEDED
- Specific skills:
  - Q5 YES → Log correlation skill
  - Q6 YES → Measurement/timing skill
  - Q7 YES → Debugging workflow skill
  - Q8 YES → Analysis technique skill
  - Q9 YES → Testing methodology skill

**Decision-Making Summary:**
- Do NOT decide "NOT NEEDED" without completing this review
- If review question yields YES → update is warranted
- Document reasoning in meta file: "Q[N] answered YES: [brief discovery description]"
- Architecture/skills updates make project memory richer for future sessions

---

## THINGS NOT TO DO

**NEVER DO THESE ACTIONS:**
- ❌ DO NOT execute `framework_state.py advance` - framework advancement is handled automatically by /step-done command
- ❌ DO NOT modify implementation code (that's Step 4 territory)
- ❌ DO NOT create new features or solutions (document what was built)
- ❌ DO NOT skip documentation of key architectural decisions
- ❌ DO NOT create generic documentation - focus on specific patterns and implementations discovered

**Why these constraints:**
- Framework state managed by /step-done command (not manual advancement)
- Step 6 is documentation, not implementation (code changes finished in Step 4)
- Document existing work, don't create new work (curation vs. creation)
- Architectural decisions are valuable knowledge (capture design rationale)
- Specific patterns more valuable than generic advice (reusable patterns, not platitudes)
