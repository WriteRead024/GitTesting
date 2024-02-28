
### Git Testing

# Subfolder Three - Branch Tests

This script tests the branch merge functionality of git.&nbsp; It works in ten steps, 
listed below.&nbsp; The automatic steps can be performed by the 'branch-merge-test.py' script.

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

The first iteration of this test on Feb. 27, 2024 found that the F39 Linux managed RPM installed 
system local implementation of Git 2.43.2 automatically deleted the branch during the 
`git merge` merge conflict resolution.

Four additional iterations were performed on Feb. 28, 2024.&nbsp; 

The first is in a subfolder "unconflicted-merge" and is an example of a merge that did not have conflicts.&nbsp; 

The second is an example of very unorthodox git usage where the merge conflict text is committed 
to the local branch repository, then resolved and committed again.&nbsp; That test is in the 
"committed-merge-text" subfolder.&nbsp; The merge text had to be edited so that the git program recognized the 
merge conflict as resolved.

The third test is in the "partial-merge-conflict" subfolder, it has both unconflicting edits and merge conflict edits.

The fourth test is in the branch-20240228 subfolder and is left as an unmerged branch for future testing ease.
