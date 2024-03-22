
### GitTesting

# Subfolder **Three** - Branch Tests

## Useful Git Branch Concepts

To see a diff-list of files comparing two branches: 'git diff --name-only branchname master' (https://stackoverflow.com/a/9332648/23476205).

'git switch' is like 'git checkout' but is newer and has more safety checks.

#### archiving branches with 'git tag'

To preserve a branch but delete it from the normal working list of branches: 
'git tag archive/<branchname> <branchname>' then 'git branch -d <branchname>'.&nbsp; 
A 'git tag' shows a list of tagged branches.&nbsp; The 'archive' could be anything but is very logical.&nbsp; 
(https://stackoverflow.com/a/1309934/23476205)

Later the deleted branch can be restored as the working copy with 'git checkout archive/<branchname>'.&nbsp; 
That will leave the working copy as a detached head branch, 'git checkout -b <branchname> archive/<branchname>' 
will create an attached new branch for the detached tagged branch.&nbsp; 



