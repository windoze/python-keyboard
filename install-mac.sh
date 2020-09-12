#!/bin/sh

DIR=$(dirname $0)

cd "$DIR"

cp -a keyboard /Volumes/CIRCUITPY/lib
cp keymaps.py /Volumes/CIRCUITPY/lib
cp code.py /Volumes/CIRCUITPY

