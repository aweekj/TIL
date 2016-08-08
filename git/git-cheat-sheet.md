# Git Cheet Sheet

## Install Git

[Github Desktop](https://desktop.github.com)

## Configure User

```bash
$ git config [--global] user.name ["YOUR_NAME"]
$ git config [--global] user.email ["YOUR_EMAIL"]
```

## Create Repositories

```bash
$ git init
$ git clone URL [LOCAL_REPO_NAME]
```

## Make Changes

```bash
$ git status
$ git diff
$ git add [FILE_NAME]
$ git commit -m "COMMIT MESSAGE"
```

## Group Changes

```bash
$ git branch
$ git branch [BRANCH_NAME]
$ git checkout [-b] [BRANCH_NAME]
$ git merge [BRANCH_NAME]
$ git branch -d [BRANCH_NAME]
```

## Undoing things

#### Commit again

```bash
$ git commit -m 'initial commit'
$ git add <forgotten-file>
$ git commit --amend
```

#### Unstage a staged file

```bash
$ git reset HEAD <file>
```

#### Unmodify a modified file

_NOTE_ - This command could be dangerous.

```bash
$ git checkout -- <file>
```

## Synchronize Changes

```bash
$ git fetch [BOOKMARK]
$ git merge [BOOKMARK]/[BRANCH]
$ git push [ALIAS] [BRANCH]
$ git pull
```


---
## Refer to
[Git Cheat Sheet - Official](https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf)
[Git-scm Book](https://git-scm.com/book/en/v2)
