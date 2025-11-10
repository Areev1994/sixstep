Intelligently integrate new system prompts into current step's input components while respecting size constraints and avoiding duplication.

**TARGET**: Add maximum 3 new system prompts without exceeding size limits
**CONSTRAINTS**: 
- Total USER PREFERENCES section: ≤2000 characters
- Individual prompt: ≤200 characters
- No duplication of existing prompts

**INTEGRATION STRATEGY**:
If size constraints exceeded:
1. **Prioritize new prompts**: Keep the most important new ones
2. **Consolidate existing**: Merge similar existing prompts
3. **Rewrite for brevity**: Shorten prompts while preserving meaning
4. **Remove redundant**: Drop least useful existing prompts if necessary

**FAILURE CONDITIONS**:
- If new prompts duplicate existing ones exactly
- If integration would make section too verbose or unwieldy
- If new prompts contain project-specific details