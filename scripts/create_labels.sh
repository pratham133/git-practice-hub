#!/usr/bin/env bash
# Creates all labels used by issues.csv before you bulk-create issues.
# Usage: ./scripts/create_labels.sh <owner>/<repo>

set -e
REPO="$1"

if [ -z "$REPO" ]; then
  echo "Usage: ./scripts/create_labels.sh <owner>/<repo>"
  exit 1
fi

create_label () {
  gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force
}

create_label "track:sql"              "1F77B4" "SQL track issue"
create_label "track:python"           "2CA02C" "Python track issue"
create_label "track:data-engineering" "9467BD" "Data Engineering track issue"
create_label "track:data-science"     "D62728" "Data Science track issue"
create_label "tier:1"                 "0E8A16" "Git mechanics practice issue"
create_label "tier:2"                 "1D76DB" "Track challenge issue"
create_label "challenge"              "FBCA04" "Real technical challenge"

echo "Labels created for $REPO"
