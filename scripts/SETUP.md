# One-time setup (for the instructor)

1. Create the repo on GitHub (e.g. `your-org/cohort-practice-hub`) and push this scaffold to it:
   ```
   cd cohort-practice-hub
   git init
   git add .
   git commit -m "Initial scaffold"
   git branch -M main
   git remote add origin https://github.com/<org>/cohort-practice-hub.git
   git push -u origin main
   ```

2. Install the GitHub CLI and log in: https://cli.github.com/ then `gh auth login`

3. Create the labels used by every issue:
   ```
   ./scripts/create_labels.sh <org>/cohort-practice-hub
   ```

4. Bulk-create all 150 issues:
   ```
   python3 scripts/bulk_create_issues.py <org>/cohort-practice-hub
   ```
   Tip: run with `--dry-run` first to preview without creating anything.
   If it stops partway (rate limit, network), re-run with `--start N` using the
   next issue number shown in the error.

5. (Optional but recommended) Create a Project board:
   - Go to the repo's **Projects** tab -> **New project** -> **Board** template.
   - Add columns: `Available`, `Claimed`, `In Review`, `Merged`.
   - Use the built-in **workflow automation** (Project settings -> Workflows) to
     auto-move an issue to "In Review" when a linked PR opens, and to "Merged"
     when it's merged.
   - Filter/group by the `track:*` label to get a per-cohort view without a
     separate board per cohort.

6. Turn on branch protection on `main` (Settings -> Branches) requiring a PR
   before merging, so nobody can push directly and every contribution goes
   through review.

7. Share the repo link with all three cohorts. Point each cohort to its track
   folder and its `track:<name>` label filter in Issues.
