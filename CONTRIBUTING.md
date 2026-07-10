# Contributing Guide

This is the exact step-by-step workflow to make your first (or next) pull request to this repo.

## 1. Fork the repository

Click **Fork** at the top-right of this repo's GitHub page. This creates your own copy under
your account.

## 2. Clone your fork

```
git clone https://github.com/<your-username>/git-practice-hub.git
cd git-practice-hub
```

## 3. Add the original repo as a remote (so you can stay in sync)

```
git remote add upstream https://github.com/<org>/git-practice-hub.git
```

## 4. Claim an issue

Go to the [Issues tab](../../issues), find one in your track that's unclaimed, and comment:

```
I'll take this!
```

## 5. Create a branch

Name your branch with the issue number and a short description:

```
git checkout -b issue-42-fix-readme-typo
```

## 6. Do the work

Make your change. Keep it focused — only touch what the issue asks for.

## 7. Commit and push

```
git add .
git commit -m "Fix typo in SQL README (closes #42)"
git push -u origin issue-42-fix-readme-typo
```

Using `closes #42` (or `fixes #42`) in your commit or PR description automatically closes the
issue when your PR is merged.

## 8. Open a Pull Request

On GitHub, go to your fork and click **Compare & pull request**. Make sure it's comparing your
branch against `<org>/git-practice-hub:main`. Fill in the PR template.

## 9. Respond to review feedback

A reviewer may leave comments. Push more commits to the same branch to address them — they'll
show up automatically on the same PR.

## 10. Get merged, then sync back up

Once merged, clean up locally:

```
git checkout main
git pull upstream main
git branch -d issue-42-fix-readme-typo
```

You're ready for your next issue!

## Branch naming convention

`issue-<number>-<short-description>` e.g. `issue-17-add-name-to-contributors`

## Commit message convention

Short, present-tense, descriptive: `Add validation for null customer_id`, not `update` or `fix stuff`.
