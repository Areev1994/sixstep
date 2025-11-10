Step 5: Testing & Optimization

## STAGE 3 CONTEXT

**STAGE 3 (Solution Translation) - Step 5 (Validation)**

You are completing Stage 3 of the four-stage problem-solving model. Step 4 implemented the code. Now in Step 5, you validate that implementation works correctly.

**Why Stage 3 completion:**
- Stage 1-2 completed context alignment and understanding expansion
- Stage 3 translates design into reality: Step 4 implemented, Step 5 validates
- Step 5 verifies implementation meets original problem requirements from Step 1
- Validation confirms solution ready for knowledge documentation (Stage 4 - Step 6)

## PURPOSE

**Validation**: Verify solution works correctly and meets original problem requirements.

**Why validation focus:**
- Step 4 produced compilable code; Step 5 confirms it functions correctly
- Testing reveals issues, regressions, or gaps in implementation
- Optimization ensures solution performs adequately
- Validation provides confidence before documenting knowledge in Step 6

## APPROACH

- Prescriptive: Review all implementation in step4_implement.md and actual code changes
- Descriptive (why): Understanding what was implemented guides test design and validation strategy

- Prescriptive: Run tests and verify functionality against original problem requirements from Step 1
- Descriptive (why): Step 1 defined what problem needed solving; validation confirms solution actually solves it

- Prescriptive: Debug any issues found during testing
- Descriptive (why): Issues must be resolved before solution can be considered complete

- Prescriptive: Focus on ensuring solution meets original problem requirements
- Descriptive (why): Implementation success measured against original goals, not arbitrary standards

## CONSTRAINT

- Prescriptive: Test both new functionality AND existing functionality to ensure no regressions
- Descriptive (why): Changes can break existing behavior; regression testing prevents introducing new problems while fixing old ones

## THINGS NOT TO DO

**NEVER DO THESE ACTIONS:**
- ❌ DO NOT execute `framework_state.py advance` - framework advancement is handled automatically by /step-done command
- ❌ DO NOT modify implementation code without first validating current functionality
- ❌ DO NOT skip regression testing of existing functionality
- ❌ DO NOT proceed to Step 6 without thorough validation
- ❌ DO NOT optimize without first establishing that basic functionality works

**Why these constraints:**
- Framework state managed by /step-done command (not manual advancement)
- Understand current behavior before changing code (prevents breaking working parts)
- Regression testing catches unintended side effects (changes can break existing features)
- Thorough validation required before knowledge documentation (Step 6 documents verified solutions)
- Basic functionality first, optimization second (working code more valuable than fast broken code)

## USER PREFERENCES (Auto-Generated)

- User performs manual testing independently and reports results, preferring documentation updates over detailed test execution collaboration
- For non-code deliverables (documentation, communications), skip Step 5 entirely with a brief note explaining no testing is applicable.
