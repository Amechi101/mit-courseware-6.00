#!/bin/bash

ROOT_DIR="$PWD"
CURRENT_DIR="${BASH_SOURCE%/*}"
DONE="Finished"

for f in `find $ROOT_DIR -name 'initialization.py'`; do python "$f"; done; echo $DONE

