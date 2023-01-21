import os
import re
import json

path = "transcripts/transcripts_full"
output_path = "transcripts/lines_raw.json"

fpaths = [file for file in os.listdir(path)]
files = []

for fpath in fpaths:
    if ".txt" in fpath:
        files.append(open(path + "/" + fpath, "r").read())

text = ""
in_name = False

name = ""
line = ""

dialogue = {}

for file in files:
    for c in file:
        text += c
        if "'''" in text:
            if in_name:
                name = text[0:-3]
                name = name.replace("\"", "").strip()
            else:
                line = text[0:-3]
                line = line.replace(":", "").strip()
                line = line.replace("\n", "")

                if name not in dialogue:
                    dialogue[name] = []

                dialogue[name].append(line)

            in_name = not in_name
            text = ""

obj = json.dumps(dialogue, indent=2)

file = open(output_path, "w")
file.write(obj)
file.close()
