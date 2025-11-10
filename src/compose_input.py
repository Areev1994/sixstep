#!/usr/bin/env python3
"""
Input Composition Engine - The "pre-process program" from solution map
Composes different input components based on current step detection
"""

import sys
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime
from framework_state import FrameworkState

def compose_enhanced_prompt(user_question):
    """
    Pre-process program: Compose input components based on detection-logic
    This is the core of the solution map implementation
    """
    
    state_manager = FrameworkState()
    
    # Detection-logic: Get current step and phase
    components = state_manager.get_input_components()
    current_state = state_manager.load_current_state()
    
    if not components or not current_state:
        return f"❌ No active six-step session. Use /start-sixstep first.\n\nUser question: {user_question}"
    
    # Compose input components as per solution map
    enhanced_prompt = f"""[SIX-STEP FRAMEWORK ACTIVE]

🏗️  FRAMEWORK INFO: {components['framework_info']}

📍 CURRENT STEP/PHASE: {components['step_info']}

📚 DATA SOURCES: {components['data_sources']}

📋 OUTPUT REQUIREMENTS: {components['output_requirements']}

🔍 PROBLEM CONTEXT:
- Problem: {components['problem_description']}
- Problem ID: {components['problem_id']}
- Active Directory: ../active/{components['problem_id']}/

[USER QUESTION]
{user_question}

[FRAMEWORK INSTRUCTION]
Before answering, read the current STATE.md and relevant step files from the active directory above. Follow the step/phase instructions exactly."""
    
    return enhanced_prompt

def get_real_context_usage():
    """Get real Claude session context usage via /context command"""
    try:
        # Run /context command to get current session context
        result = subprocess.run(['claude', 'context'], 
                               capture_output=True, text=True, timeout=10)
        
        if result.returncode != 0:
            return None, "Failed to get context info"
        
        # Parse the context output to extract usage percentage
        output = result.stdout
        
        # Check if this is actually context output or a normal Claude response
        if "Context Usage" not in output and "tokens" not in output:
            return None, "Command returned normal Claude response, not context info"
        
        # Look for patterns like "126k/200k tokens (63%)" or similar
        token_match = re.search(r'(\d+\.?\d*)k?/(\d+)k?\s+tokens\s*\((\d+\.?\d*)%\)', output)
        if token_match:
            used_tokens = float(token_match.group(1)) * (1000 if 'k' in token_match.group(1) else 1)
            total_tokens = float(token_match.group(2)) * 1000  # Always in k
            percentage = float(token_match.group(3))
            
            return {
                'percentage': percentage,
                'used_tokens': int(used_tokens),
                'total_tokens': int(total_tokens),
                'raw_output': output.strip()
            }, None
        
        # Alternative pattern matching for different formats
        percent_match = re.search(r'(\d+\.?\d*)%', output)
        if percent_match:
            percentage = float(percent_match.group(1))
            return {
                'percentage': percentage,
                'used_tokens': None,
                'total_tokens': None,
                'raw_output': output.strip()
            }, None
            
        return None, f"Could not parse context output: {output[:100]}"
        
    except subprocess.TimeoutExpired:
        return None, "Context command timed out"
    except FileNotFoundError:
        return None, "Claude CLI not found - using fallback estimation"
    except Exception as e:
        return None, f"Error getting context: {e}"

def estimate_context_usage_fallback(text):
    """Fallback estimation when /context command fails"""
    # Rough estimate: 1 token ≈ 4 characters, 200k context window
    chars = len(text)
    estimated_tokens = chars / 4
    context_percentage = (estimated_tokens / 200000) * 100
    return min(context_percentage, 100)  # Cap at 100%

def log_enhanced_prompt(enhanced_prompt, user_question, current_state, components):
    """Log enhanced prompt to meta directory with strict format contract"""
    try:
        meta_dir = Path(__file__).parent / "meta"
        step = current_state["current_step"]
        phase = current_state.get("current_phase", 1)
        problem_id = current_state["problem_id"]
        
        # Create problem directory
        problem_dir = meta_dir / problem_id
        problem_dir.mkdir(exist_ok=True, parents=True)
        
        # Generate log filename - one file per step (or phase for step 3)
        if step == "3" and phase == 2:
            log_file = problem_dir / f"step{step}_phase{phase}.md"
        else:
            log_file = problem_dir / f"step{step}.md"
        
        # Get real Claude session context usage
        context_info, error = get_real_context_usage()
        
        if context_info:
            context_percent = context_info['percentage']
            context_display = f"{context_percent:.1f}%"
            if context_info['used_tokens'] and context_info['total_tokens']:
                context_display += f" ({context_info['used_tokens']:,}/{context_info['total_tokens']:,} tokens)"
            context_status = "⚠️  HIGH" if context_percent > 60 else "✅ OK"
            context_source = "Real Session Context"
        else:
            # Fallback to estimation
            context_percent = estimate_context_usage_fallback(enhanced_prompt)
            context_display = f"~{context_percent:.1f}% (estimated from prompt)"
            context_status = "⚠️  HIGH" if context_percent > 60 else "✅ OK"
            context_source = f"Fallback Estimation ({error})"
        
        # Check if file exists for appending vs creating
        is_new_file = not log_file.exists()
        
        # Create appropriate log entry using new format contract
        if is_new_file:
            # First entry - create header and entry
            log_entry = f"""# Enhanced Prompt Log - Step {step}{"" if step != "3" else " (Phase " + str(phase) + ")"}
**Problem ID**: {problem_id}
**Started**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## Interaction 1
**Timestamp:** {datetime.now().isoformat()}
**Enhanced Prompt:**
```
{enhanced_prompt}
```

**Claude Response Summary:**
[CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

---

"""
        else:
            # Subsequent entry - count existing interactions and append
            with open(log_file, 'r') as f:
                content = f.read()
            interaction_count = content.count('## Interaction ') + 1
            
            log_entry = f"""
## Interaction {interaction_count}
**Timestamp:** {datetime.now().isoformat()}
**Enhanced Prompt:**
```
{enhanced_prompt}
```

**Claude Response Summary:**
[CLAUDE_RESPONSE_HERE - Replace with response summary using format from response_summary_format.md]

---

"""
        
        # Write or append the entry
        mode = 'w' if is_new_file else 'a'
        with open(log_file, mode) as f:
            f.write(log_entry)
            
        return context_percent
        
    except Exception as e:
        print(f"Warning: Failed to log enhanced prompt: {e}", file=sys.stderr)
        return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python compose_input.py 'user question'")
        return
    
    user_question = " ".join(sys.argv[1:])
    
    # Get state and components for logging
    state_manager = FrameworkState()
    components = state_manager.get_input_components()
    current_state = state_manager.load_current_state()
    
    # Generate enhanced prompt
    enhanced_prompt = compose_enhanced_prompt(user_question)
    
    # Get real session context and log the prompt  
    if components and current_state:
        # Get real context usage for display
        context_info, error = get_real_context_usage()
        
        if context_info:
            context_percent = context_info['percentage']
            status_emoji = "⚠️" if context_percent > 60 else "✅"
            if context_info['used_tokens'] and context_info['total_tokens']:
                context_display = f"[SESSION CONTEXT: {context_percent:.1f}% ({context_info['used_tokens']:,}/{context_info['total_tokens']:,} tokens) {status_emoji}]"
            else:
                context_display = f"[SESSION CONTEXT: {context_percent:.1f}% {status_emoji}]"
        else:
            # Fallback display
            context_percent = estimate_context_usage_fallback(enhanced_prompt)
            status_emoji = "⚠️" if context_percent > 60 else "✅"
            context_display = f"[CONTEXT: ~{context_percent:.1f}% (estimated) {status_emoji}]"
        
        # Log with full context info
        log_enhanced_prompt(enhanced_prompt, user_question, current_state, components)
        
        print(enhanced_prompt + "\n" + context_display)
    else:
        print(enhanced_prompt)

if __name__ == "__main__":
    main()