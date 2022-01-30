# HuzunluArtemis - 2021 (Licensed under GPL-v3)

def getListAsString(liste, splitter = ","):
    toret = ""
    for i, item in enumerate(liste):
        toret += f"<code>{item}</code>"
        if i != len(liste)-1: toret += f"{splitter} "
    return toret

