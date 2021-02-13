#!/usr/bin/env bash

BASE=$PWD
INPUT_BASE_PATH='../../../references/'

for P in */*; do
  if [ -d "$BASE/$P" ]; then
    cd "$BASE/$P"
    INPUT_PATH="$INPUT_BASE_PATH$P"
    if [ -d $INPUT_PATH ]; then
      for F in "$INPUT_PATH"/*; do
        [ -e $F ] || continue
        ln -s $F .
      done
    fi
  fi
done
