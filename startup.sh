#!/usr/bin/env bash
Xvfb :10 -ac &
export DISPLAY=:10
python3 ./src/eshinbun.py
