# Response Summary Format

## Standard Format Template

Claude MUST use this exact format when writing response summaries to meta files:

```markdown
**Tools Used:** [List of tools: Grep, Edit, Read, Write, Bash, etc.]
**Files Modified:** [Full paths of files changed/created, or "None"]
**Key Actions:** [1-2 sentence summary of main accomplishment]
**Next Steps:** [What user should do next, if any, or "Continue to next interaction"]
```

## Field Specifications

### **Tools Used:**
- List all tools invoked during the response
- Use tool names: Grep, Edit, Read, Write, Bash, MultiEdit, etc.
- Include count if tool used multiple times: "Grep (3x), Edit (2x)"
- If no tools used: "None - provided analysis only"

### **Files Modified:**
- Full absolute paths of files that were created or changed
- Use format: `path/to/file.ext (created)` or `path/to/file.ext (modified)`
- If no files modified: "None"
- Include active directory files: `active/{problem_id}/step1_questions.md`

### **Key Actions:**
- One to two sentences maximum
- Focus on the main accomplishment or decision made
- Use active voice and be specific
- Examples:
  - "Generated 5 clarification questions about async runtime control implementation"
  - "Identified existing macro structure and proposed runtime toggle approach"
  - "Created implementation plan with 3 phases for Platform X Feature integration"

### **Next Steps:**
- What the user should do immediately next
- Can be procedural ("Review questions and proceed to Step 2") or interactive ("Provide feedback on approach")
- If response completes the step: "Run /step-done to advance to Step 2"
- If continuing current step: "Continue current step with additional questions"

## Examples

### Example 1: Analysis Response
```markdown
**Tools Used:** Grep (2x), Read (1x)
**Files Modified:** None
**Key Actions:** Analyzed existing async macro usage and identified 3 key integration points for runtime control
**Next Steps:** User should clarify preferred approach before implementation planning
```

### Example 2: Implementation Response  
```markdown
**Tools Used:** Edit (1x), Write (1x)
**Files Modified:** active/async_runtime_control/step4_implementation.md (created)
**Key Actions:** Created detailed implementation plan with code examples for Platform X Feature async integration
**Next Steps:** Run /step-done to advance to Step 5 for testing phase
```

### Example 3: Question Generation Response
```markdown
**Tools Used:** Write (1x)
**Files Modified:** active/problem_example/step1_questions.md (created)
**Key Actions:** Generated 5 targeted questions to align understanding of runtime control requirements
**Next Steps:** Review and refine questions, then run /step-done to proceed to assessment
```

## Quality Guidelines

- **Be specific**: "Modified 3 files" vs "Modified files"
- **Be concise**: Focus on primary accomplishment, not every detail
- **Be actionable**: Next steps should give clear user guidance
- **Be consistent**: Use the same format every time
- **Be accurate**: Only list tools/files actually used/modified