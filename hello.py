print("Hello Mr Rakesh yadav , welcome to python world")
import os
import sys

def main():
    print("Hello from Jenkins Python script!")
    print(f"Python version: {sys.version}")
    print("Current working directory contents:")
    # List files in the current directory (which is the Jenkins workspace)
    for item in os.listdir('.'):
        print(f"- {item}")
    print("Script finished successfully.")

if __name__ == "__main__":
    main()

