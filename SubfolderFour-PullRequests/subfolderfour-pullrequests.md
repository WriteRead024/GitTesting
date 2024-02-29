
### Git Testing

# Subfolder **Four** - Pull Requests

This subfolder is a demo/test sandbox for pull requests on GitHub.

The [GitHub documentation on Pull Requests](https://docs.github.com/en/pull-requests) 
is surprisingly extensive.&nbsp; 
The sections on [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) 
and specifically [creating pull requests from repository forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) 
are perhaps excessive for the information needed in this testing work, but were useful in finding out information on things like
how to reject pull requests (the term is 'Close' pull requests).

This repository subfolder only deals with in-repository pull requests, not inter-(forked-)repositories' pull requests.

The process is:
1) Get a repository local copy on a development machine.
2) Create a branch with `git checkout newbranchname`.
3) Make some edits, additions, changes in the new branch.
4) Push the branch and changes to GitHub.
5) Create the pull request on GitHub from the new branch.

    The last commit message might be auto-populated in the new pull request process on GitHub, 
    if there is more than one commit, it might use the branch name for the pull request commit message.

6) Manage any conflicts, test failures, or other problems.
7) Approve or Close the pull request.

Also interesting to note is that pull requests can be used to 
[automatically close issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).&nbsp; 
That might be an interesting thing to test further.

After the pull request was merged on GitHub, GitHub created a commit for the result of the merge 
and the pull-req-test branch was left active on the repository.&nbsp; 
It is probably normal to then delete the branch if it is not going to be worked on further, 
but I left the pull-req-test branch specificially as part of the exercise.