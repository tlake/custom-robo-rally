#!/bin/bash

# Get the contents of the original python program.
content=$( cat rr_alias.py )

# Remove first three lines.
content=$( echo "$content" | tail -n+4 )

# Add Slack alias replacement to top of glob.
content=$( echo "$content" | sed 's/class RR_Alias():/!alias replace rr2 !pyevalformatted class RR_Alias():/' )

# Convert sys.argv input to Slack alias input.
content=$( echo "$content" | sed 's/" ".join(sys.argv\[1:\])/"$?"/' )

# Compress because Slack has a 4000-character message limit.
## Shorten function names.
## The leading _ exists because Slack will add link formatting to something like 'self.lt',
## which will cause a syntax error.
content=$( echo "$content" \
    | sed 's/self\./self\._/g' \
    | sed '/    def _/! s/def /def _/g' \
    | sed 's/rr\./rr\._/g' \
    | sed 's/eval_literal/lt/g' \
    | sed 's/eval_shots/sh/g' \
    | sed 's/eval_exchange/ex/g' \
    | sed 's/eval_phase/ph/g' \
    | sed 's/eval_peaceful/pf/g' \
    | sed 's/eval_death/de/g' \
    | sed 's/eval_victory_points/vp/g' \
    | sed 's/process_argstring/pa/g' \
    | sed 's/main/m/g' \
    | sed 's/make_substitutions/ms/g' \
    | sed 's/face_left/fl/g' \
)

## Shorten frequently-used variables.
content=$( echo "$content" \
    | sed 's/operation/op/g' \
    | sed 's/substitution/sub/g' \
    | sed 's/message/msg/g' \
    | sed 's/result/r/g' \
    | sed 's/contents/c/g' \
    | sed 's/digit_index/i/g' \
    | sed 's/argstring/a/g' \
    | sed 's/emoji_string/es/g' \
    | sed 's/which_phase/wp/g' \
    | sed 's/point/pt/g' \
    | sed 's/item/x/g' \
)

## Shorten formatting.
content=$( echo "$content" \
    | sed 's/": /":/g' \
    | sed 's/ = /=/g' \
    | sed 's/ > />/g' \
    | sed 's/ < /</g' \
    | sed 's/ += /+=/g' \
    | sed 's/ -= /-=/g' \
    | sed 's/, /,/g' \
)

## Remove blank lines
content=$( echo "$content" \
    | awk 'NF' \
)

# Print out the formatted and mildly-compressed program.
echo "$content" 

# Also print out how many characters the shortened version contains.
echo
echo ${#content}
