
### Git Testing

This file was created by script 'branch-merge-test.py'
The next few paragraphs are a numbered list (in numerical order).

1b. This is line number 1, edited in repo. master, should not cause conflict.

2c. This is line number 2, edit in multiple branches to test merge conflicts.

3d. This is line number 3, edit in multiple branches to test merge conflicts.

4e. This is line number 4, edit in multiple branches to test merge conflicts.

5f. This is line number 5, edited in repo. master, SHOULD cause conflict.

6g. This is line number 6, edit in multiple branches to test merge conflicts.

7h. This is line number 7, edit in multiple branches to test merge conflicts.

8i. This is line number 8, edit in multiple branches to test merge conflicts.

9j. This is line number 9, edited in repo. master, should not cause conflict.

10k. This is line number 10, edit in multiple branches to test merge conflicts.

Note: having made the file edits above in the repo. master branch, 
about to do a `git merge --no-commit --no-ff` to the just-created branch.&nbsp; 
It should indicate there is a (A as in only one) conflict.