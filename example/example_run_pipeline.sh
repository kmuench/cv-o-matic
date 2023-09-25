#!/bin/bash
# Example of command line run of script.
# Reminder to activate conda env: conda activate python_to_latex

OUTPUT_DIR="/my/test/dir"
CONTENT_FOLDER="data"

../python_to_latex.py -o $OUTPUT_DIR -c $CONTENT_FOLDER