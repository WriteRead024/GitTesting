
### Git Testing

This file was created by script 'branch-merge-test.py'
The next few paragraphs are a numbered list (in numerical order).

1b. This is line number 1, edit in multiple branches to test merge conflicts.

2c. This is line number 2, edit in multiple branches to test merge conflicts.

3d. This is line number 3, edit in multiple branches to test merge conflicts.

4e. This is line number 4, edit in multiple branches to test merge conflicts.

5f. This is line number 5, edit in multiple branches to test merge conflicts.

6gg. This is line number 6, edited in multiple branches (first branch-20240228110422 then now in the merged master branch as per test procedure) to test merge conflicts.&nbsp; The merge conflict text was committed the commit before this one.

7h. This is line number 7, edit in multiple branches to test merge conflicts.

8i. This is line number 8, edit in multiple branches to test merge conflicts.

9j. This is line number 9, edit in multiple branches to test merge conflicts.

10k. This is line number 10, edit in multiple branches to test merge conflicts.

Notes: vscode displayed a warning prompt when the commit with the merge conflict text was attempted, but clicking 'Yes' committed the commit without further problem.&nbsp; vscode also has syntax highlighting for the merge conflict text (in the Markdown syntax highlighting/git diff tool).

A `git reset --keep commithash` with commithash for the commit with the commit 
messages then viewed in vscode did display those commit message syntax 
highlights.&nbsp; git resetting to the commit with the actually resolved 
conflicts required discarding the commit messages then detected as changes 
in comparison to the resolved-conflict changes, at which point the working 
directory was detected as clean, this paragraph was typed and the commit labled 'conflict message test complete' was committed.&nbsp; 