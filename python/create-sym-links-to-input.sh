#!/usr/bin/env bash

BASE=$PWD
INPUT_BASE_PATH='../../../../adventofcode-input/'

for P in */*; do
  if [ -d "$BASE/$P" ]; then
    cd "$BASE/$P"
    INPUT_PATH="$INPUT_BASE_PATH$P"
    if [ -d $INPUT_PATH ]; then
      for F in "$INPUT_PATH"/*; do
        ln -s $F .
      done
    fi
  fi
done
