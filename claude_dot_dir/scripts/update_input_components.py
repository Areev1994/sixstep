#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
    """
    Update-input-components command - Intelligently update input components with constraint handling and duplication checking

    Replicates functionality from .claude/commands/update-input-components.md
    """

    # Get arguments passed to the script (should be pipe-separated prompts)
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    try:
        # Execute the update_input_components.py script with all arguments
        cmd = [sys.executable, "claude_intelligence/solution_map_implementation/update_input_components.py"] + args

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"Error executing update_input_components.py: {result.stderr.strip()}")
            return

        # Output the result from the script
        output = result.stdout.strip()
        if output:
            print(output)
        else:
            print("update_input_components.py completed but produced no output")

    except subprocess.TimeoutExpired:
        print("update_input_components.py execution timed out")
    except FileNotFoundError:
        print("update_input_components.py script not found at claude_intelligence/solution_map_implementation/update_input_components.py")
    except Exception as e:
        print(f"Error running update_input_components.py: {str(e)}")

if __name__ == "__main__":
    main()