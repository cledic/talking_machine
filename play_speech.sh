#!/bin/bash

TFILE=$(tempfile)
TFILE2=$TFILE.wav

pico2wave -l=it-IT -w=$TFILE2 "$1"
aplay $TFILE2
rm $TFILE
rm $TFILE2
