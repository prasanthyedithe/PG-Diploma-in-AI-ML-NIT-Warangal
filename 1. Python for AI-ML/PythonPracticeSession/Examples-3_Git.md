# Example: Session 3, Git 

## Initialization
### Initialize repo

    git init git_example
    cd git_example


### Show '.git' folder

    ls -a

## Commit
### Create a file

    touch small_initial_file.txt
    nano small_initial_file.txt

And add some text

### Index changes

    git status
    git add .
    git status

### Create a new file

    touch anothe_initial_file.txt
    git status

### Commit indexed changes and show log and status
    git commit -m "Initial commit"
    git log
    git status

### Add "untracked" file into the previous commit
    git add anothe_initial_file.txt
    git commit --amend --no-edit
    git log
    git status



##Branches
### Show branches
    git branch	
### Checkout to a new branch
    git checkout -b feature
    git branch
### Create a new commit
    touch file_for_feature_branch.txt
    git add *.txt
    git commit  -m "commit for our important feature"
    git log
    ls
### Switch to the master branch and back
    git checkout master
    ls
    git log
    git checkout feature
    ls


##Merge
### Create conflict file
    echo "file for feature branch">>conflict_file.txt
    git add .
    git commit -m "file with conflict for feature"
    git checkout master 
    echo "file for master branch">>conflict_file.txt
    git add .
    git commit -m "file conflict for master"

### Merge feature and solve conflict
    git merge feature
    git status

    git add conflict_file.txt
    git commit