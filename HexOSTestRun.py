text = open("./HexOSFiles/OSVer", "r").read()
text = text.split(".")

text[2] = str(int(text[2]) + 1)

open("./HexOSFiles/OSVer", "w").write(text[0] + "." + text[1] + "." + text[2])
