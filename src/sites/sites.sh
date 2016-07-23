#!/bin/bash

ROOT_DIR="$PWD"
CURRENT_DIR="${BASH_SOURCE%/*}"

for f in `find $ROOT_DIR/$CURRENT_DIR -name '*.py'`; do python "$f"; done

