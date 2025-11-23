#!/bin/bash

COLUMN_NAMES=$(head -n 1 <MeritList.csv)
COLUMN_VALUES=$(fzf <MeritList.csv)

paste -d ',' \
  <(echo "$COLUMN_NAMES" | tr ',' '\n') \
  <(echo "$COLUMN_VALUES" | tr ',' '\n') |
  awk -F ',' '{print $1 ": " $2}'
