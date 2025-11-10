#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
    """
    Sixstep command - Ask question with six-step framework context (pre-process program)

    Replicates functionality from .claude/commands/sixstep.md
    """

    # Get arguments passed to the script
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    # Join arguments as the user's question
    arguments = " ".join(args) if args else ""

    try:
        # Execute the compose_input.py script with the arguments
        result = subprocess.run(
            [sys.executable, "claude_intelligence/solution_map_implementation/compose_input.py", arguments],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.getcwd()
        )

        if result.returncode != 0:
            print(f"Error executing compose_input.py: {result.stderr.strip()}")
            return

        # Output the result from the script
        output = result.stdout.strip()
        if output:
            print(output)
        else:
            print("compose_input.py completed but produced no output")

    except subprocess.TimeoutExpired:
        print("compose_input.py execution timed out")
    except FileNotFoundError:
        print("compose_input.py script not found at claude_intelligence/solution_map_implementation/compose_input.py")
    except Exception as e:
        print(f"Error running compose_input.py: {str(e)}")

if __name__ == "__main__":
    main()