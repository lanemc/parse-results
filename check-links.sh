#!/bin/sh

blc https://math.umn.edu -ro > results.txt & sleep 150 ; kill $!

wait $!

python parse_results.py

wait $!

echo "This is the message body" | mutt -a "results.txt" -s "test" -- lanemcunningham@gmail.com
