#!/bin/bash

# Get original python program
content=$( cat rr_alias.py )

# Remove first three lines
content=$( echo "$content" | tail -n+4 )

# Add Slack alias replacement to top of glob
content=$( echo "$content" | sed 's/class RR_Alias():/!alias replace rr !pyevalformatted class RR_Alias():/' )

# Convert sys.argv argument to Slack alias input
content=$( echo "$content" | sed 's/" ".join(sys.argv\[1:\])/"""$?"""/' )

# Shorten words and remove blank lines because Slack has a 4000 character limit in its messages
content=$( echo "$content" \
    | sed 's/operation/op/g' \
    | sed 's/substitution/sub/g' \
    | sed 's/message/msg/g' \
    | sed 's/result/r/g' \
    | sed 's/contents/c/g' \
    | sed 's/digit_index/i/g' \
    | sed 's/process_argstring/proc/g' \
    | sed 's/argstring/argstr/g' \
    | sed 's/face_left/fl/g' \
    | sed 's/eval_//g' \
    | sed 's/emoji_string/emoji/g' \
    | sed 's/points/pts/g' \
    | awk 'NF' \
)

echo "$content" 
echo
echo ${#content}

