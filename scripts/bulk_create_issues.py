#!/usr/bin/env python3
"""
Bulk-creates all issues from issues.csv into a GitHub repo using the GitHub CLI (`gh`).

Prerequisites:
  1. Install the GitHub CLI: https://cli.github.com/
  2. Authenticate:            gh auth login
  3. Create labels first (recommended, see labels.sh in this folder) so the
     track:/tier: labels exist before issues reference them.

Usage:
  python3 scripts/bulk_create_issues.py <owner>/<repo> [--start N] [--dry-run]

Examples:
  python3 scripts/bulk_create_issues.py your-org/cohort-practice-hub
  python3 scripts/bulk_create_issues.py your-org/cohort-practice-hub --dry-run
  python3 scripts/bulk_create_issues.py your-org/cohort-practice-hub --start 45
"""
import csv
import subprocess
import sys
import time
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="owner/repo, e.g. your-org/cohort-practice-hub")
    parser.add_argument("--csv", default=os.path.join(os.path.dirname(__file__), "..", "issues.csv"))
    parser.add_argument("--start", type=int, default=1, help="Resume from this issue 'number' column")
    parser.add_argument("--dry-run", action="store_true", help="Print commands instead of running them")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds to wait between issue creations (avoid rate limits)")
    args = parser.parse_args()

    with open(args.csv, newline="") as f:
        rows = list(csv.DictReader(f))

    print(f"Loaded {len(rows)} issues from {args.csv}")
    created = 0

    for row in rows:
        num = int(row["number"])
        if num < args.start:
            continue

        title = row["title"]
        body = row["body"]
        labels = row["labels"]

        cmd = [
            "gh", "issue", "create",
            "--repo", args.repo,
            "--title", title,
            "--body", body,
            "--label", labels,
        ]

        if args.dry_run:
            print("DRY RUN:", " ".join(f'"{c}"' if " " in c else c for c in cmd))
            continue

        print(f"[{num}/{len(rows)}] Creating: {title}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ERROR creating issue {num}: {result.stderr.strip()}")
            print(f"  Re-run with --start {num} to resume from here.")
            sys.exit(1)
        else:
            created += 1
            print(f"  -> {result.stdout.strip()}")

        time.sleep(args.delay)

    print(f"\nDone. Created {created} issues.")

if __name__ == "__main__":
    main()
