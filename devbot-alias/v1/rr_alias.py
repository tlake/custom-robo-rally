import sys


robots = {
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
try:
    line = " ".join(sys.argv[1:])
    sections = line.split(", ")
    for section in sections:
        if section[0] == "#":
            if section[1] == " ":
                section = section[0] + section[2:]
            section = section + " "
            for i, j in robots.iteritems():
                section = section.replace(" " + i + " ", " " + j + " ")
                section = section.replace("#" + i + " ", "#" + j + " ")
                section = section.replace("#" + i + ",", "#" + j + ",")
                section = section.replace(" " + i + ",", " " + j + ",")
                section = section.replace(" " + i + ".", " " + j + ".")
            print(section[1:])
        elif section[0] == "p":
            bold = "*"
            if int(section[1]) < 1:
                phase = "Start of Round"
            elif int(section[1]) > 5:
                phase = "End of Round"
            else:
                phase = "Phase " + section[1]
            print("{}{}:{}".format(bold, phase, bold))
        elif section[0] == "0":
            print(":peace_symbol:ful")
        elif section[0] == "d":
            items = section.split(" ")
            print(":rip: {}".format(robots[items[1]]))
        elif section[0] == "x":
            items = section.split(" ")
            print("{} :hadouken_left: :hadouken_right: {}".format(
                robots[items[1]],
                robots[items[2]].rstrip(":") + "_left:",
            ))
        else:
            items = section.split(" ")
            if items[1] == "gvp" and items[2].isdigit():
                print("{} gains {} victory point{}.".format(
                    robots[items[0]],
                    items[2],
                    "" if int(items[2]) == 1 else "s"
                ))
            elif items[1].isdigit():
                booms = ":boom:" * int(items[1])
                print("{} {} {}".format(robots[items[0]], booms, robots[items[2]]))
            else:
                print("{} :boom: {}".format(robots[items[0]], robots[items[1]]))
except:
    pass
