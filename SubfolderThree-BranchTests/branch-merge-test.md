
### Git Testing

# Subfolder Three - Branch Tests

This script tests the branch merge functionality of git.&nbsp; It works in ten steps:

1. (automatic) Create a new directory if it does not exist.
2. (automatic) Create a new Markdown file with some text in the directory.
3. (automatic) Commit the new file to the current branch.
4. (automatic) Create a new branch with a timestamp name.
5. (manual) Make some changes to the file in the new branch.
6. (manual) Commit the changes to the new branch.
7. (manual) Checkout back to the master branch.
8. (manual) Make some changes to the file in the master branch.
9. (manual) Merge the new branch into the main branch.
10. (manual) Observe that the merge results are correct.