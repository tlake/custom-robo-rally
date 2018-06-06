#!/bin/bash

content=$( \
    cat rr_alias.py \
    | tail -n+4 \
    | sed 's/def get_argstrings():/!alias replace rr !pyevalformatted def get_argstrings():/' \
    | sed 's/raw = " ".join(sys.argv\[1:\])/raw = """$?"""/' \
    | sed 's/operation/op/' \
    | sed 's/substitution/sub/' \
    | sed 's/message/msg/' \
    | sed 's/result/r/' \
    | awk 'NF' \
)

echo "$content" 

