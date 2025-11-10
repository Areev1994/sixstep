#!/usr/bin/env python3
"""
Enhanced step-done: Advance framework + Extract user preferences
Works like compose_input.py - composes input components and outputs enhanced prompt
"""

import sys
from pathlib import Path
from framework_state import FrameworkState


def main():
    """Main entry point - advance state then compose preference extraction prompt"""
    try:
        state_manager = FrameworkState()

        # IMPORTANT: Save current step/phase info BEFORE advancing
        # This ensures we extract preferences from the correct (completed) step
        pre_advance_state = state_manager.load_current_state()
        if not pre_advance_state:
            print("❌ No active six-step session found")
            return

        completed_step = pre_advance_state["current_step"]
        completed_phase = pre_advance_state.get("current_phase", 1)
        problem_id = pre_advance_state["problem_id"]

        # Now advance the framework state (original step-done behavior)
        print("🚀 Advancing framework step/phase...")
        result = state_manager.advance_step_phase()
        print(result)

        # Check if advancement was successful
        if "❌" in result or "No active" in result or "Framework complete" in result:
            return

        print("\n🔍 Extracting user preferences from completed step...")
        print("=" * 60)

        # Load current state for framework info (after advancement)
        current_state = state_manager.load_current_state()
        if not current_state:
            print("❌ Could not load current state for preference extraction")
            return
        
        # Get step-done input components
        step_done_components = state_manager.input_component_files.get(("step-done", 1), {})
        
        if not step_done_components:
            print("❌ Step-done input components not found")
            return
        
        # Load each component
        components = {}
        for component_type, filename in step_done_components.items():
            file_path = state_manager.components_dir / filename
            if file_path.exists():
                with open(file_path, 'r') as f:
                    components[component_type] = f.read().strip()
            else:
                components[component_type] = f"❌ Missing file: {filename}"
        
        # Use COMPLETED step info for preference extraction (pre-advancement values)
        # This ensures we compare meta files from completed step with input components from same step

        # Determine step-specific paths using COMPLETED step info
        if completed_step == "3":
            if completed_phase == 1:
                current_step_info_path = f"input_components/step3/phase1_step_info.md"
                meta_file_path = f"meta/{problem_id}/step3.md"
            else:  # phase 2
                current_step_info_path = f"input_components/step3/phase2_step_info.md"
                meta_file_path = f"meta/{problem_id}/step3_phase2.md"
        else:
            current_step_info_path = f"input_components/step{completed_step}/step_info.md"
            meta_file_path = f"meta/{problem_id}/step{completed_step}.md"
        
        # Compose and output the enhanced prompt (like compose_input.py)
        enhanced_prompt = f"""[SIX-STEP FRAMEWORK ACTIVE]

🏗️  FRAMEWORK INFO: {components.get('framework_info', 'Missing framework info')}

📍 CURRENT TASK: Extract user preferences from completed step and add them to step_info file

🎯 STEP INFO: {components.get('step_info', 'Missing step info')}

📚 DATA SOURCES: {components.get('data_sources', 'Missing data sources')}

📋 OUTPUT REQUIREMENTS: {components.get('output_requirements', 'Missing output requirements')}

🔍 CONTEXT:
- Problem ID: {problem_id}
- Completed Step: {completed_step} (Phase {completed_phase})
- **FILE TO UPDATE**: {current_step_info_path}
- Meta File to Analyze: {meta_file_path}
- Active Directory: active/{problem_id}/

IMPORTANT: Update preferences in the COMPLETED step's file: {current_step_info_path}

Analyze the conversation from the completed step to extract NEW user working preferences not already captured in the completed step's input components, then automatically add them to the step_info file."""
        
        print(enhanced_prompt)
        
    except Exception as e:
        print(f"❌ Error in enhanced step-done: {e}")


if __name__ == "__main__":
    main()