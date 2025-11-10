#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
    """
    Start-sixstep command - Initialize six-step framework for a problem

    Replicates functionality from .claude/commands/start-sixstep.md
    """

    # Get arguments passed to the script
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    # Join arguments as the problem description
    arguments = " ".join(args) if args else ""

    try:
        # Execute the framework_state.py script with "start" and the arguments
        result = subprocess.run(
            [sys.executable, "claude_intelligence/solution_map_implementation/framework_state.py", "start", arguments],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"Error executing framework_state.py: {result.stderr.strip()}")
            return

        # Output the result from the script
        output = result.stdout.strip()
        if output:
            print(output)
        else:
            print("framework_state.py completed but produced no output")

    except subprocess.TimeoutExpired:
        print("framework_state.py execution timed out")
    except FileNotFoundError:
        print("framework_state.py script not found at claude_intelligence/solution_map_implementation/framework_state.py")
    except Exception as e:
        print(f"Error running framework_state.py: {str(e)}")

if __name__ == "__main__":
    main()