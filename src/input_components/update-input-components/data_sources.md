**PRIMARY SOURCES**:
- Guide files if context needed: `active/{problem_id}/guide/step{current_step}_*.md` (optional, for understanding step context)
- Current step's step_info.md file: Read existing USER PREFERENCES section
- New system prompts: The prompts provided via command arguments
- Framework constraints: Size and duplication rules

**ANALYSIS TARGETS**:
1. **Current USER PREFERENCES section** from current step's input_components
2. **Character count** of existing USER PREFERENCES section
3. **Semantic overlap** between new and existing prompts
4. **Priority assessment** of existing vs new prompts

**FILE PATHS TO CHECK**:
- **Step 3 Phase 1**: `input_components/step3/phase1_step_info.md`
- **Step 3 Phase 2**: `input_components/step3/phase2_step_info.md`
- **All other steps**: `input_components/step{N}/step_info.md`

**CONSTRAINT VALIDATION**:
- Count characters in existing USER PREFERENCES section
- Calculate total with new prompts added
- Identify semantic duplicates or near-duplicates
- Assess which prompts provide most value