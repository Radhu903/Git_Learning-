# Git_Learning-
This repository is mainly set up to learn the workings of github
The commands that I usually used, the best practice I had so far:

I usually first create new repository on github or bitbucket first, then
`git clone`
After I made changes to my local repository master branch, and want to push it to remote master branch
```
git status
git add .
git commit -m 'whatever'
git push origin main
```
what if in remote repository, we want multiple branches? I will first create branch through web portal in github or bitbucket. Then,

`git clone`

probabaly `git pull` or `git fetch` would work as well, but hasn't tested yet.

Then, after making changes in my local master branch,
```
git status
git add .
git commit -m 'your message'
git show-ref
git push origin HEAD:branch_name

```
what if you accidentally push to remote master?

Go to remote, find the commit ID you want to restore
```
git reset --hard commitID
git push origin master
```
But by doing that, your updates in local master branch will be removed. So more smart way is to first create new branch to save the current updates.
```
git branch backup
git checkout backup
git checkout master
git reset --hard commitID
git push origin master
```
