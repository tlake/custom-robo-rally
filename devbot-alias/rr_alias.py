import sys


def get_argstrings():
    raw = " ".join(sys.argv[1:])
    return raw.split(", ")


def get_substitutions():
    substitutions = {
        "ha": ":roborally_hammer:",
        "hu": ":roborally_hulk:",
        "sp": ":roborally_spin:",
        "sq": ":roborally_squash:",
        "tr": ":roborally_trundle:",
        "twi": ":roborally_twitch:",
        "two": ":roborally_twonky:",
        "z": ":roborally_zoom:",
        "ra": "is randomized",
        "ara": "are randomized",
        "rip": ":rip:",
        "pu": "powers up",
        "pd": "powers down",
        "apu": "power up",
        "apd": "power down",
        "fc": "fire-controls",
        "reg": "register",
        "regs": "registers",
        "b": "Board",
        "iotf": "is on the flag",
        "np": "is the new President",
        "nvp": "is the new Vice President",
        "na": "is the new asshole",
        "gavp": "gets a victory point",
        "agavp": "all get victory points",
        "gw": "get health, money and an option",
        "agw": "all get health, money and options",
    }

    return substitutions


def get_operations():
    operations = {
        "#": eval_literal,
        "s": eval_shots,
        "ex": eval_exchange,
        "p": eval_phase,
        "0": eval_peaceful,
        "d": eval_death,
        "gvp": eval_victory_points,
    }

    return operations


def make_substitutions(items):
    result = []
    substitutions = get_substitutions()
    for item in items:
        try:
            result.append(substitutions[item])
        except KeyError:
            result.append(item)

    return result


def face_left(emoji_string):
    return emoji_string.rstrip(":") + "_left:"


def eval_death(contents):
    contents = make_substitutions(contents)
    result = ":rip: {}".format(" ".join(contents))
    return result


def eval_exchange(contents):
    contents = make_substitutions(contents)
    result = "{} :hadouken_left: :hadouken_right: {}".format(
        contents[0],
        face_left(contents[1]),
    )

    return result


def eval_literal(contents):
    contents = make_substitutions(contents)
    return " ".join(contents)


def eval_peaceful(contents):
    return ":peace_symbol:ful"


def eval_phase(contents):
    bold = "*"
    result = "{b}Phase {}:{b}".format(
        contents[0],
        b=bold,
    )

    return result


def eval_shots(contents):
    contents = make_substitutions(contents)
    result = ""
    digit_index = None
    for item in contents:
        if item.isdigit():
            digit_index = contents.index(item)
            break

    if digit_index:
        booms = ":boom:" * int(contents[digit_index])
        result = "{} {} {}".format(
            " ".join(contents[0:digit_index]),
            booms,
            " ".join(contents[digit_index + 1:]),
        )

    else:
        result = "{} :boom: {}".format(
            contents[0],
            " " .join(contents[1:]),
        )

    return result


def eval_victory_points(contents):
    contents = make_substitutions(contents)
    result = ""
    points = 1
    digit_index = None
    for item in contents:
        if item.isdigit():
            digit_index = contents.index[item]
            break

    if digit_index:
        points = int(contents[digit_index])

    result = "{} {} {} victory point{}".format(
        " ".join(contents[0:digit_index]),
        "each gain" if digit_index and digit_index > 1 else "gains",
        points,
        "" if points == 1 else "s",
    )

    return result


def process_argstring(argstring):
    result = ""
    args = argstring.split()
    flag, contents = args[0], args[1:]
    operations = get_operations()
    try:
        result = operations[flag](contents)
    except KeyError:
        result = operations["#"](args)

    return result


def main():
    message = ""
    argstrings = get_argstrings()
    for argstring in argstrings:
        if len(message) > 0:
            message += "\n"

        message += process_argstring(argstring)

    print(message)


main()
