#!/usr/bin/env python3
"""
Update input components with intelligent constraint handling
Actually modifies input component files with new USER PREFERENCES
"""

import sys
import re
import argparse
from pathlib import Path
from framework_state import FrameworkState


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Update input components with new user preferences')
    parser.add_argument('prompts', help='New prompts separated by | (e.g., "prompt1 | prompt2 | prompt3")')
    parser.add_argument('--step', type=str, help='Target step number (e.g., "4"). If not provided, uses current step')
    return parser.parse_args()


def split_prompts(prompts_string):
    """Split prompts string by | delimiter and clean up"""
    prompts = [prompt.strip() for prompt in prompts_string.split('|')]
    return [p for p in prompts if p]  # Remove empty prompts


def calculate_section_size(preferences_list):
    """Calculate total character count of USER PREFERENCES section"""
    if not preferences_list:
        return len("## USER PREFERENCES (Auto-Generated)\n\n")

    header = "## USER PREFERENCES (Auto-Generated)\n\n"
    bullets = "\n".join(f"- {pref}" for pref in preferences_list)
    return len(header + bullets)


def check_duplication(new_prompt, existing_prompts, threshold=0.7):
    """Check if new prompt is too similar to existing ones"""
    new_words = set(new_prompt.lower().split())

    for existing in existing_prompts:
        existing_words = set(existing.lower().split())
        if not new_words or not existing_words:
            continue

        # Calculate Jaccard similarity
        intersection = len(new_words.intersection(existing_words))
        union = len(new_words.union(existing_words))
        similarity = intersection / union if union > 0 else 0

        if similarity >= threshold:
            return True, existing

    return False, None


def consolidate_preferences(existing_prefs, new_prefs, max_size=2000):
    """Intelligently consolidate preferences to fit size constraints"""
    all_prefs = existing_prefs.copy()

    # Add new preferences that aren't duplicates
    for new_pref in new_prefs:
        is_duplicate, similar_existing = check_duplication(new_pref, all_prefs)
        if not is_duplicate:
            all_prefs.append(new_pref)
        else:
            print(f"⚠️  DUPLICATE DETECTED: Skipping '{new_pref}' (similar to '{similar_existing}')")

    # Check size constraints
    current_size = calculate_section_size(all_prefs)
    if current_size <= max_size:
        return all_prefs

    print(f"⚠️  Size constraint exceeded ({current_size} > {max_size}). Consolidating...")

    # Strategy: Prioritize new prompts, then consolidate existing ones
    # Keep new prompts (they're most important)
    consolidated = []

    # Add non-duplicate new prompts first
    for new_pref in new_prefs:
        is_duplicate, _ = check_duplication(new_pref, existing_prefs)
        if not is_duplicate:
            consolidated.append(new_pref)

    # Add existing prompts until we hit size limit, prioritizing shorter ones
    existing_sorted = sorted(existing_prefs, key=len)
    for existing_pref in existing_sorted:
        test_prefs = consolidated + [existing_pref]
        if calculate_section_size(test_prefs) <= max_size:
            consolidated.append(existing_pref)

    return consolidated


def update_step_info_file(target_file, new_preferences):
    """Update step_info.md file with new USER PREFERENCES section"""
    if not target_file.exists():
        print(f"❌ Target file not found: {target_file}")
        return False

    content = target_file.read_text()

    # Generate new USER PREFERENCES section
    if new_preferences:
        new_section = "## USER PREFERENCES (Auto-Generated)\n\n"
        new_section += "\n".join(f"- {pref}" for pref in new_preferences)
    else:
        new_section = "## USER PREFERENCES (Auto-Generated)\n\n- No preferences configured"

    # Check if USER PREFERENCES section already exists
    preferences_pattern = r'## USER PREFERENCES \(Auto-Generated\)\n\n.*?(?=\n\n##|\n\n[A-Z]|\Z)'

    if re.search(preferences_pattern, content, re.DOTALL):
        # Replace existing section
        updated_content = re.sub(preferences_pattern, new_section, content, flags=re.DOTALL)
    else:
        # Add new section at the end
        updated_content = content.rstrip() + "\n\n" + new_section + "\n"

    # Write back to file
    target_file.write_text(updated_content)
    return True


def main():
    """Main entry point - actually update input component files"""
    try:
        args = parse_arguments()
    except SystemExit:
        print("Usage: python update_input_components.py 'prompt1 | prompt2 | prompt3' [--step N]")
        print("Example: python update_input_components.py 'Ask clarifying questions first | Present work in phases' --step 4")
        return

    try:
        # Initialize framework state
        state_manager = FrameworkState()
        current_state = state_manager.load_current_state()

        if not current_state:
            print("❌ No active six-step session found. Please start a session with /start-sixstep first.")
            return

        # Determine target step
        if args.step:
            target_step = args.step
            print(f"🎯 Targeting step {target_step} (specified via --step)")
        else:
            # When no --step provided, target the COMPLETED step (previous step)
            # This is because step-done.py advances the state before calling update-input-components
            current_step_num = int(current_state["current_step"])
            if current_step_num > 1:
                target_step = str(current_step_num - 1)
                print(f"🎯 Targeting completed step {target_step} (current state shows step {current_step_num})")
            else:
                # Edge case: if somehow we're at step 1, stay at step 1
                target_step = "1"
                print(f"🎯 Targeting step 1 (cannot go below step 1)")

        # Determine target file path
        if target_step == "3":
            # For step 3, we need to determine which phase was completed
            # If current step is 4, then step 3 phase 2 was completed
            # If current step is still 3, then step 3 phase 1 was completed
            current_step_num = int(current_state["current_step"])
            if current_step_num == 4:
                # Step 3 phase 2 was completed (both phases done)
                target_file_path = f"step3/phase2_step_info.md"
                print(f"📋 Step 3 completed (both phases), targeting phase 2 input components")
            else:
                # Step 3 phase 1 was completed, still in step 3
                target_file_path = f"step3/phase1_step_info.md"
                print(f"📋 Step 3 phase 1 completed, targeting phase 1 input components")
        else:
            target_file_path = f"step{target_step}/step_info.md"

        target_file = state_manager.components_dir / target_file_path

        print(f"📁 Target file: {target_file}")

        # Parse new prompts
        new_prompts = split_prompts(args.prompts)
        print(f"📝 New prompts ({len(new_prompts)}): {new_prompts}")

        if not new_prompts:
            print("❌ No valid prompts provided")
            return

        # Validate prompt lengths
        for prompt in new_prompts:
            if len(prompt) > 200:
                print(f"⚠️  Warning: Prompt exceeds 200 characters: '{prompt[:50]}...'")

        # Read existing USER PREFERENCES if they exist
        existing_preferences = []
        if target_file.exists():
            content = target_file.read_text()
            preferences_match = re.search(r'## USER PREFERENCES \(Auto-Generated\)\n\n(.*?)(?=\n\n##|\n\n[A-Z]|\Z)', content, re.DOTALL)
            if preferences_match:
                existing_text = preferences_match.group(1).strip()
                # Extract bullet points
                for line in existing_text.split('\n'):
                    line = line.strip()
                    if line.startswith('- '):
                        existing_preferences.append(line[2:])  # Remove "- " prefix

        print(f"📋 Existing preferences ({len(existing_preferences)}): {existing_preferences}")

        # Consolidate preferences with size constraints
        final_preferences = consolidate_preferences(existing_preferences, new_prompts)

        final_size = calculate_section_size(final_preferences)
        print(f"📏 Final section size: {final_size} characters (limit: 2000)")
        print(f"✅ Final preferences ({len(final_preferences)}): {final_preferences}")

        # Update the file
        if update_step_info_file(target_file, final_preferences):
            print(f"✅ Successfully updated {target_file}")
            print(f"   Added {len(new_prompts)} new prompts")
            print(f"   Total preferences: {len(final_preferences)}")
        else:
            print("❌ Failed to update file")

    except Exception as e:
        print(f"❌ Error updating input components: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()