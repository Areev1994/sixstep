## 🎯 STEP 6 GOAL: ADD THIS SESSION'S VERIFIED KNOWLEDGE

**Context**: Project memory is incomplete, built incrementally through six-step sessions.

**Your Step 6 job**:
1. Extract verified knowledge from THIS session (Steps 1-5)
2. Add knowledge to appropriate project memory layers
3. Make project memory richer for future sessions

**What to add from THIS session:**
- Solution pattern (ALWAYS) - documents THIS problem's solution
- Architecture updates (IF component relationships/hardware variants discovered)
- Skills documentation (IF reusable analysis/debugging techniques used)
- Features (IF new capability created or mechanics need documentation)

**Result**: Future sessions start with richer verified knowledge → faster problem-solving.

---

## ✅ STEP 6 COMPLETION CHECKLIST

Complete ALL items below following the FOUR-PHASE workflow from step_info.md. Do NOT skip any phase.

**PHASE 1: SEQUENTIAL STEP REVIEW**
- [ ] Review Step 1 guide file individually (apply Q1-Q3, document findings)
- [ ] Review Step 2 guide file individually (apply Q4-Q6, document findings)
- [ ] Review Step 3 guide file individually (apply Q7-Q8, document findings)
- [ ] Review Step 4 guide file individually (check architecture discoveries, document findings)
- [ ] Review Step 5 guide file individually (apply Q9, document findings)
- [ ] Create Phase 1 discovery list with SESSION DISCOVERY REVIEW question references

**PHASE 2: HOLISTIC CONTEXT REVIEW**
- [ ] Read all Steps 1-5 guide files together
- [ ] Check for cross-step patterns missed in Phase 1
- [ ] Finalize complete discovery list (Phase 1 + Phase 2 additions)

**PHASE 3: CREATE OUTPUTS**
- [ ] Create `active/{problem_id}/user-review/step6_insights.md` (glanceable version)
- [ ] Create `active/{problem_id}/guide/step6_insights.md` (complete version)
- [ ] Extract git context (commit IDs or diffs)
- [ ] Create `project_memory/solutions/[pattern_name].md` (ALWAYS - required)
- [ ] Create architecture updates (if Phase 1/2 identified discoveries)
- [ ] Create skills (if Phase 1/2 identified reusable techniques)
- [ ] Update `meta/{problem_id}/step6.md` with response summary

**PHASE 4: VERIFICATION**
- [ ] Re-read and verify solution pattern accuracy
- [ ] Re-read and verify ALL architecture updates accuracy (if created)
- [ ] Re-read and verify ALL skills accuracy (if created)
- [ ] Document verification in meta file: "Verification: Re-read and confirmed accuracy of [list files]"

**CLOSING MESSAGE**
- [ ] Output closing message referencing user-review file and solution pattern

**Why phased workflow matters**: Sequential review prevents cognitive overload, holistic review catches cross-step patterns, verification ensures project_memory maintains high-quality verified knowledge for future sessions.

---

## 🎯 STEP 6 WORKFLOW OVERVIEW

**Step 6 uses a four-phase workflow** (detailed in step_info.md):

**Phase 1: Sequential Step Review** - Review each step (1-5) individually with SESSION DISCOVERY REVIEW
**Phase 2: Holistic Context Review** - Read all guide files together to catch cross-step patterns
**Phase 3: Create Outputs** - Generate insights, solution pattern, and project_memory updates
**Phase 4: Verification** - Double-check all project_memory changes for accuracy

**Why this order:**
- Phases 1-2 identify WHAT to document before creating outputs
- Phase 3 creates all deliverables based on finalized discovery list
- Phase 4 ensures project_memory accuracy (verified knowledge for future sessions)

---

## 📋 PRIMARY OUTPUT REQUIREMENTS (CREATED IN PHASE 3)

Generate TWO versions of step6_insights.md in Phase 3:

**USER-REVIEW VERSION**: `active/{problem_id}/user-review/step6_insights.md`
- Key accomplishments (3-5 bullets)
- Main lessons learned (3-5 bullets)
- Patterns discovered (brief)
- Recommendations for similar problems (brief)
- Framework effectiveness for this problem type
- Glanceable format for quick insights review

**GUIDE VERSION**: `active/{problem_id}/guide/step6_insights.md`
- Comprehensive insights documentation
- Complete implementation overview with context
- Detailed lessons learned with rationale
- All patterns discovered with examples
- Framework effectiveness analysis
- Complete recommendations with reasoning
- Full context for Claude and future reference

**Both versions required**: Do NOT skip user-review version. Both files must be created in Phase 3.

---

## PROJECT MEMORY DELIVERABLES (CREATED IN PHASE 3)

📖 **For detailed content templates and structure guidance**, see:
   `input_components/project_memory_structure.md`

**Project Memory Paths** (all relative to `claude_intelligence/solution_map_implementation/`):
- Same directory level as `active/`, `meta/`, `input_components/`
- Example structure:
  ```
  claude_intelligence/solution_map_implementation/
  ├── active/{problem_id}/
  ├── meta/{problem_id}/
  ├── input_components/
  └── project_memory/
      ├── architecture/
      ├── features/
      ├── solutions/
      └── skills/
  ```

**1. SOLUTION PATTERN** (⚠️ ALWAYS CREATE - REQUIRED FOR EVERY STEP 6):
- **Location**: `project_memory/solutions/`
- **Naming**: `descriptive_pattern_name.md`
- **Example path**: `project_memory/solutions/memory_optimization_pattern.md`
- **Template**: Use Solution Pattern Template from project_memory_structure.md
- **CRITICAL**: Must include git commit ID(s) or full diff in Implementation Details section
- **Why ALWAYS**: Every six-step session solves a problem; every problem solution belongs in solutions/ for future reference

**2. ARCHITECTURE UPDATES** (ONLY IF NEEDED):
- **When**: THIS session discovered component relationships, hardware architecture details, system-level understanding, or component responsibilities

⚠️ **BEFORE deciding "NOT NEEDED"**: Complete SESSION DISCOVERY REVIEW from step_info.md
- Review Questions Q1-Q4 guide architecture update decision
- If ANY of Q1-Q4 answers YES → Architecture update NEEDED
- Document reasoning in meta file

- **Location**: `project_memory/architecture/`
- **What to update** (adding THIS session's architecture knowledge):
  * `system_overview.md` (if THIS session discovered component relationships or external tool integration)
  * `[component]/README.md` (if THIS session discovered interfaces/capabilities/hardware variants; add pointer to subdirectories)
  * `[component]/hardware/README.md` (if THIS session learned hardware component variants, capabilities, modes, mechanisms)
  * Create new `[component]/hardware/` directory (if hardware variant details from THIS session need documentation)
  * Create new `[component]/` directory (if THIS session involved entirely new component)
- **How**: See Layer 1: Architecture section in project_memory_structure.md for structure guidance
- **Incremental growth examples**:
  * System diagram incomplete? Add external tool integration if THIS session discovered connection path
  * Component README incomplete? Add hardware/ subdirectory if THIS session learned about variants
  * Missing component? Add it if THIS session involved that component

**3. FEATURE DOCUMENTATION** (ONLY IF NEEDED):
- **When**: New feature/capability created, existing feature mechanics need documentation, or usage patterns should be captured
- **Location**: `project_memory/features/[feature_name]/`
- **What to create**: Feature directory with README.md, how_it_works.md, and optional usage_patterns.md/api_reference.md
- **Example path**: `project_memory/features/async_debugging/README.md`
- **How**: See Layer 2: Features section in project_memory_structure.md for structure guidance

**4. SKILLS DOCUMENTATION** (ONLY IF NEEDED):
- **When**: THIS session used reusable technique/methodology applicable across multiple problems

⚠️ **BEFORE deciding "NOT NEEDED"**: Complete SESSION DISCOVERY REVIEW from step_info.md
- Review Questions Q5-Q9 guide skills creation decision
- If ANY of Q5-Q9 answers YES (and reusability test passed) → Skills creation NEEDED
- Document reasoning in meta file

- **Location**: `project_memory/skills/`
- **Naming**: `descriptive_skill_name.md`
- **Example path**: `project_memory/skills/log_correlation_timing_analysis.md`
- **Template**: Use Skills Template from project_memory_structure.md (Layer 4: Skills section)
- **Examples of reusable techniques** (capture if used in THIS session):
  * **Log correlation techniques**: Matching operations across log sources using markers and transaction identifiers
  * **Debugging workflows**: Systematic approaches to isolate issues (binary search, phase-by-phase analysis)
  * **Testing methodologies**: Validation procedures (regression test design, performance benchmarking)
  * **Analysis techniques**: Breaking down complex operations (timing decomposition, operation-level measurement)
  * **Measurement procedures**: Extracting metrics from logs/traces (timestamp analysis, transaction counting)
- **NOT skills** (use other layers):
  * Feature usage documentation → Features layer
  * One-time procedure specific only to THIS problem → Part of solution pattern
  * Component relationships → Architecture layer
- **Incremental growth**: If THIS session used technique not yet in skills/, add it to help future sessions apply same technique

**5. GIT CONTEXT EXTRACTION** (REQUIRED FOR SOLUTIONS):
Use these commands to extract implementation commits:

```bash
# Find commits during implementation
git log --oneline --since="3 days ago" --author="$(git config user.name)"

# Get full diff for specific commit
git show <commit_id>

# Or get diff between two points
git diff <start_commit>..<end_commit>
```

**Choose format**:
- Simple changes: Include commit ID only
- Complex changes: Include full diff in solution pattern
- Multiple commits: List all relevant commit IDs with descriptions

---

## ✅ VERIFICATION REQUIREMENTS (PHASE 4 - CRITICAL)

**Purpose**: Double-check all project_memory changes to ensure accuracy before finalizing.

**Why verification is critical:**
- Project memory is verified knowledge used by future six-step sessions
- Inaccurate information causes confusion and errors in future work
- Verification maintains high-quality knowledge base

**Verification checklist:**

**1. Verify Solution Pattern:**
- [ ] Re-read `project_memory/solutions/[pattern_name].md`
- [ ] Confirm all information from THIS session's Steps 1-5 (not speculation)
- [ ] Check git commit ID/diff included and correct
- [ ] Verify solution approach matches actual implementation

**2. Verify Architecture Updates (if created):**
- [ ] Re-read ALL modified `project_memory/architecture/**/*.md` files
- [ ] Confirm discoveries are from THIS session (cite step: "discovered in Step 2")
- [ ] Check cross-references to other files are correct paths
- [ ] Verify no contradictions with existing architecture knowledge

**3. Verify Skills (if created):**
- [ ] Re-read ALL created `project_memory/skills/[skill_name].md` files
- [ ] Confirm technique was used in THIS session (cite step: "used in Step 3")
- [ ] Verify reusability test (applies beyond this specific problem)
- [ ] Check procedure steps are accurate and complete

**4. Document Verification in Meta File:**
- [ ] Add to meta file: "Verification: Re-read and confirmed accuracy of [list all project_memory files created/modified]"
- [ ] This documents that Phase 4 verification was completed

**What to check during verification:**
- ✅ All information is verified (from actual Steps 1-5, not assumptions)
- ✅ Git references are accurate (correct commit IDs/diffs)
- ✅ Cross-references work (file paths correct)
- ✅ No contradictions with existing project_memory
- ✅ Skills are reusable (not problem-specific procedures)
- ✅ Architecture reflects actual discoveries (cite source step)

**If errors found during verification:**
- Fix immediately before finalizing
- Update meta file to document what was corrected: "Verification: Found and corrected [description]"

---

## 💬 CONSISTENT CLOSING MESSAGE

After completing your response, ALWAYS end with this message format:

```
Please review the insights and project memory updates in `active/{problem_id}/user-review/step6_insights.md`.

Step 6 is complete! You can review the solution pattern in `project_memory/solutions/` to see the documented implementation.

When ready to complete this six-step session, run `/step-done`.
```

**Note**: This closing message should appear after EVERY response in Step 6. Running `/step-done` after Step 6 will mark the session as complete.

---

## 📝 META FILE (Framework Tracking - Required for Completion)

**⚠️ REQUIRED**: Every Step 6 must create/update meta file for framework tracking.

**Target File:** meta/{problem_id}/step6.md
**Action:** Replace placeholder text with response summary
**Format:** Use exact format from input_components/response_summary_format.md
**Placeholder:** [CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

**Note:** Meta file logging tracks framework conversations for analysis and improvement.

**Rules:**
- NEVER modify existing Enhanced Prompt sections
- ONLY replace the placeholder text in your assigned Claude Response Summary section
- Follow format contract from input_components/meta_file_format.md exactly
- Include all required fields: Tools Used, Files Modified, Key Actions, Next Steps
