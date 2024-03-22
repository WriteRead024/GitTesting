
### GitTesting

# Subfolder **Three** - Branch Tests

## Useful Git Branch Concepts

To see a diff-list of files comparing two branches: 'git diff --name-only branchname master' (https://stackoverflow.com/a/9332648/23476205).

To preserve a branch but delete it from the normal working list of branches: 
'git tag archive/<branchname> <branchname>' then 'git branch -d <branchname>'.&nbsp; 
A 'git tag' shows a list of tagged branches.&nbsp; 
Later the deleted branch can be restored as the working copy with 'git checkout -b <branchname> archive/<branchname>'.&nbsp; 