
### Git Testing

# Subfolder **Four** - Pull Requests

## Pull request from upstream fork on GitHub.md

This .md document is about the process of merging the changes 
from an upstream repository to a fork of that repository.

Before writing this manual experiment/test report 
I thought to find some sort of version number for the GitHub website 
so as to have something to reference if the described features change.&nbsp; 
The closest I found to that was the GitHub
[public roadmap project tracker](https://github.com/orgs/github/projects/4247) 
which allows searching for keywords.&nbsp; 
From that, this linked 
[search for "pull"](https://github.com/orgs/github/projects/4247/views/1?filterQuery=pull) 
shows that occasionally some changes are made to the GitHub website app's 
pull request workflow.&nbsp; 
When this was initially written in March 2024, there were no project issues matching the 
word "pull" scheduled for all of 2024.&nbsp; There were five matching project issues, the 
earliest one 
[#347 commenting anywhere in a changed file in a pull request](https://github.com/github/roadmap/issues/347)
was created in Dec. 15, 2021.

That being the as-of-this-writing situation, here are my observations of handling a pull 
request created from an upstream repository to a fork of that repository.

0) I had forked the [expressjs](https://github.com/expressjs/express) repository 
about two weeks earlier
1) On the GitHub front page for my downstream repository a 'branch info bar' box appeared
above the list of files in the project's rootmost directory with a 
[link](https://github.com/WriteRead024/express/compare/master...expressjs%3Aexpress%3Amaster)
to compare the changes.
2) Clicking the link loaded a page saying, among other things, 
that the branches could be automatically merged.
3) Reviewing the changes in the seven commits found nothing unusual.&nbsp; Here is a summary:
    * Project Technical Committee information and volunteers/maintainers list updates
    * history.md notes about dependencies, and Release-Process.md updates
    * a bit of added extra logic to 'response.js' file
    * incrementing the version in the 'package.json' file
    * a test that the 'cookie-parser' (presently only a devDependency, perhaps as an in-evaluation stage trial) correctly transmits a "Partitioned" value in the 'Set-Cookie' header.
    * two new tests for the 'res.location' function
4) Entered the title "7 commits from upstream repo." and a description comment for the pull request then clicked the button to create the pull request.
5) Clicked the 'Merge pull request' button.
6) Used the title from the pull request for the merge commit.
7) Pulled the repo changes to a local copy.
8) Observed the new commit from the website in the local copy.

Here is a link to the commit:
[WR-express/commit/4aced72b07](https://github.com/WriteRead024/express/commit/4aced72b078f821dfc41d9ce08f2f74d8a09338a)