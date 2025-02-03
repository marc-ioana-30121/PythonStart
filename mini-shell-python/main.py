import sys
import os
import subprocess  # Importing subprocess to execute external commands

def find_in_path(param):
    path = os.environ['PATH']
    for directory in path.split(":"):
        filepath = os.path.join(directory, param)
        if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
            return filepath
    return None

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input().strip()
        if not command:
            continue

        parts = command.split()

        match parts:
            case ["exit", "0"]:
                exit(0)

            case ["echo", *cmd]:
                print(" ".join(cmd))

            case ["type", *cmd]:
                if cmd[0] in ["echo", "exit", "type"]:
                    print(f"{cmd[0]} is a shell builtin")
                else:
                    location = find_in_path(cmd[0])
                    if location:
                        print(f"{cmd[0]} is {location}")
                    else:
                        print(f"{cmd[0]}: not found")

            case _:
                executable = find_in_path(parts[0])
                if executable:
                    try:
                        # Execute the external program with its arguments
                        result = subprocess.run(parts, capture_output=True, text=True)
                        print(result.stdout, end="")  # Print the output from the external program
                    except Exception as e:
                        print(f"Error executing command: {e}")
                else:
                    print(f"{command}: command not found")

if __name__ == "__main__":
    main()
