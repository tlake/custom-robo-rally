import sys


class RR_Alias():
    def __init__(self, raw):
        self.argstrings = raw.split(", ")

        self.substitutions = {
            "ha": ":roborally_hammer:",
            "hu": ":roborally_hulk:",
            "sp": ":roborally_spin:",
            "sq": ":roborally_squash:",
            "tr": ":roborally_trundle:",
            "twi": ":roborally_twitch:",
            "two": ":roborally_twonky:",
            "z": ":roborally_zoom:",
            "bt": ":blue_tower:",
            "rt": ":red_tower:",
            "bb": ":blue_base:",
            "rb": ":red_base:",
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

        self.operations = {
            "#": self.eval_literal,
            "s": self.eval_shots,
            "ex": self.eval_exchange,
            "p": self.eval_phase,
            "0": self.eval_peaceful,
            "d": self.eval_death,
            "gvp": self.eval_victory_points,
        }

    def make_substitutions(self, items):
        result = []
        for item in items:
            try:
                result.append(self.substitutions[item])
            except KeyError:
                result.append(item)

        return result

    def face_left(self, emoji_string):
        return emoji_string.rstrip(":") + "_left:"

    def eval_death(self, contents):
        result = ":rip: {}".format(" ".join(contents))
        return result

    def eval_exchange(self, contents):
        result = "{} :hadouken_left: :hadouken_right: {}".format(
            contents[0],
            self.face_left(contents[1]),
        )

        return result

    def eval_literal(self, contents):
        return " ".join(contents)

    def eval_peaceful(self, contents):
        return ":peace_symbol:ful"

    def eval_phase(self, contents):
        bold = "*"
        result = "{b}Phase {}:{b}".format(
            contents[0],
            b=bold,
        )

        return result

    def eval_shots(self, contents):
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

    def eval_victory_points(self, contents):
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

    def process_argstring(self, argstring):
        result = ""
        args = argstring.split()
        flag, contents = args[0], args[1:]
        try:
            result = self.operations[flag](self.make_substitutions(contents))
        except KeyError:
            result = self.operations["s"](self.make_substitutions(args))

        return result

    def main(self):
        message = ""
        for argstring in self.argstrings:
            if len(message) > 0:
                message += "\n"

            message += self.process_argstring(argstring)

        print(message)


rr = RR_Alias(" ".join(sys.argv[1:]))
rr.main()
