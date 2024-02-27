# Feb 27, 2024
# GitHub Copilot
# with Rich W.

# This is a test file to test the branch merge functionality of git.

import os
import subprocess
import sys
from datetime import datetime


alphabet = "abcdefghijklmnopqrstuvwxyz"
filename = "branch-merge-test.md"
script_filename = os.path.basename(__file__)


def print_test_info():
    print("This script tests the branch merge functionality of git.")
    print("It works in ten steps:")
    print("1. (automatic) Create a new directory if it does not exist.")
    print("2. (automatic) Create a new Markdown file with some text in the directory.")
    print("3. (automatic) Commit the new file to the current branch.")
    print("4. (automatic) Create a new branch with a timestamp name.")
    print("5. (manual) Make some changes to the file in the new branch.")
    print("6. (manual) Commit the changes to the new branch.")
    print("7. (manual) Checkout back to the master branch.")
    print("8. (manual) Make some changes to the file in the master branch.")
    print("9. (manual) Merge the new branch into the main branch.")
    print("10. (manual) Observe that the merge results are correct.")


def create_directory_if_dne(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")


def check_if_file_exists(arg_filename):
    # Check if the file exsts, exiting if it does.
    if os.path.exists(arg_filename):
        print(f"File '{arg_filename}' already exists, exiting.")
        sys.exit()


def create_new_Markdown_file(arg_filename):
    # Proceed with the test and create the file.
    with open(arg_filename, "w") as file:
        file.write("\n### Git Testing\n")
        file.write(f"\nThis file was created by script '{script_filename}'\n")
        file.write("The next few paragraphs are in numerical order.\n")
        for i in range(1, 11):
            file.write(f"\n{i}{alphabet[i]}. This is line number {i}.\n")
    print(f"Markdown file '{arg_filename}' created successfully.")


def commit_file_to_git(arg_filename):
    commit_message = "b.m.t. auto-commit"
    subprocess.run(["git", "add", arg_filename])
    subprocess.run(["git", "commit", "-m", commit_message])
    print("File committed to git successfully.")


def git_status_is_clean() -> bool:
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    output = result.stdout
    if "nothing to commit, working tree clean" in output:
        return True
    else:
        return False


def create_new_git_branch():
    # Create a new branch with a timestamp name.
    branch_name = "branch-" + datetime.now().strftime("%Y%m%d%H%M%S")
    subprocess.run(["git", "checkout", "-b", branch_name])
    print(f"New branch '{branch_name}' created successfully.")


# Main function
if __name__ == "__main__":
    # check if git status is clean, and if not, exit
    if not git_status_is_clean():
        print("git status is not clean. Please commit or stash your changes.")
        print("Exiting script.")
        sys.exit()
    # if directory name is provided proceed with test
    if len(sys.argv) < 2:
        print("Please provide a directory name as a command line argument.")
        print("Or input '--help' for more information.")
    else:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print_test_info()
            sys.exit()
        else:
            input_directory = sys.argv[1]
            new_filename = os.path.join(input_directory, filename)
            create_directory_if_dne(input_directory)
            check_if_file_exists(new_filename)
            create_new_Markdown_file(new_filename)
            commit_file_to_git(new_filename)
            create_new_git_branch()
