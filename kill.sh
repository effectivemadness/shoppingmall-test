#!/bin/sh
kill $(ps -aux | grep -E "python.*py" | awk 'BEGIN {ORS=" "}; {print $2}')
