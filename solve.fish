#!/usr/bin/env fish

if ! set -q aoc_session_cookie
	echo "Add your advent of code session cookie as aoc_session_cookie env variable"
	exit 1
end

set current_day (string split -f 5-6 / $PWD)
set current_day[2] (string trim -l -c 0 $current_day[2])

set answer (python solution.py)

set aoc_answer_url https://adventofcode.com/$current_day[1]/day/$current_day[2]/answer
curl -X POST $aoc_answer_url --cookie session=$aoc_session_cookie -d "level=1&answer=$answer"

