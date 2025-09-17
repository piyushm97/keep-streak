# keep-streak

[![Keep GitHub Streak](https://github.com/piyushm97/keep-streak/actions/workflows/keep-streak.yml/badge.svg)](https://github.com/piyushm97/keep-streak/actions/workflows/keep-streak.yml)

name: Keep GitHub Streak

on:
  schedule:
    - cron: "0 5 * * *" # 12:00 AM CDT (UTC-5)
    - cron: "0 6 * * *" # 12:00 AM CST (UTC-6)
  workflow_dispatch:

permissions:
  contents: write

jobs:
  commit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup Git
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"

      - name: Make empty commit
        run: |
          git commit --allow-empty -m "chore: keep streak alive"
          git push
