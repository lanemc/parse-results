#!/bin/sh

blc https://math.umn.edu -ro > results.txt & sleep 150 ; kill $!

wait $!

python parse_results.py
