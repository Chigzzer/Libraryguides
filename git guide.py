git init  # creates a git in the folder where you entered bash

git touch xxxx.zz  # Creates a file in the folder with xxxx.zz being the file name and extension

git add filename  # adds the file to be committed

git add *.extension  # addds all filenames to be committed

git add .  # adds all files in folder to be committed.

git commit -m 'Commit Message'  # commits the files to the branch with the message in between ""

git push  # pushes the commited branch to github online

git status  # List the files you've changed and those you still need to add or commit:

git remote add origin <server>  # If you haven't connected your local repository to a remote server, add the server to be able to push to it

git branch  # list all the branches

git checkout -b <branchname>  # create a new branch and change to it

git checkout <branchname>  # changes to new branch

git branch -d <branchname>  # delete featured branch

git pull  # Fetch and merge changes on the remote server to your working directory:

git merge <branchname>  # To merge a different branch into your active branch:

git touch .gitignore  # creates an file, which you edit and add names to it for git to ignore when adding/committing

git remote add origin xxxx  # creates origin as the online depositary

git push origin branch name  # pushes branch onto origin location