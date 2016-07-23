#!/bin/bash

ROOT_DIR="$PWD"
CURRENT_DIR="${BASH_SOURCE%/*}"
DONE="Finished"

for f in `find $ROOT_DIR/$CURRENT_DIR -name '*.py'`; do python "$f"; done; echo $DONE

