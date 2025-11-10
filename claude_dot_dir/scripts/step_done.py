#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
    """
    Step-done command - Advance to next step or phase in six-step framework and extract user preferences

    Replicates functionality from .claude/commands/step-done.md
    """

    try:
        # Execute the step_done.py script (no arguments needed according to the original command)
        result = subprocess.run(
            [sys.executable, "claude_intelligence/solution_map_implementation/step_done.py"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"Error executing step_done.py: {result.stderr.strip()}")
            return

        # Output the result from the script
        output = result.stdout.strip()
        if output:
            print(output)
        else:
            print("step_done.py completed but produced no output")

    except subprocess.TimeoutExpired:
        print("step_done.py execution timed out")
    except FileNotFoundError:
        print("step_done.py script not found at claude_intelligence/solution_map_implementation/step_done.py")
    except Exception as e:
        print(f"Error running step_done.py: {str(e)}")

if __name__ == "__main__":
    main()