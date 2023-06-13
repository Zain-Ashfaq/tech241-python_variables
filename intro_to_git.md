# Intro to Git

## What is version control?
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

## Local Version Control
Many people’s version-control method of choice is to copy files into another directory. This approach is very error prone as is easy to forget which directory you’re in and accidentally write to the wrong file or copy over files you don’t mean to.

![Local version control diagram](https://git-scm.com/book/en/v2/images/local.png)

## Git Commands
```
git init
```

The git init command is used to initialize a new Git repository in the current directory. It creates a new hidden folder called ".git" that contains all the necessary files and folders to manage version control for your project.
```
git status
```
The git status command shows the current status of your Git repository. It provides information about which files have been modified, which files are staged for commit, and which files are untracked. This command is useful to get an overview of the changes made to your project.
```
git add .
```
The git add . command is used to add all modified and untracked files in the current directory and its subdirectories to the staging area. The staging area is where you prepare your changes before committing them. After running this command, the specified files are ready to be committed.
```
git commit -m "message"
```
The git commit command records the changes made to the files in the staging area as a new commit in the Git repository. The -m flag is used to specify a commit message, which should briefly describe the changes being committed.
