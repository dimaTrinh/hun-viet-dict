#!/usr/bin/env python
# coding: utf-8


import json
import glob

files = glob.glob("../../mnt/permanent/Language/French/Dic/Fr-Hu/**/*")

def findTranslations(container):
    if "content" in container:
        return [container["content"]]
    elif "connected" in container:
        return findTranslations(container["connected"])
    elif "connections" in container:
        temp = []
        for connection in container["connections"]:
            temp.extend(findTranslations(connection))
        return temp         

d = {}
for file in files:
    try:
        with open(file, "r") as infile:
            data = json.load(infile)
        print("Found json file: {}".format(file.split("/")[-1]))
        word = data["content"]
        translations = []
        for container in data["connections"]:
            translations.extend(findTranslations(container))
        for translation in translations:
            if translation not in d:
                d[translation] = [word]
            elif (word not in d[translation]):
                d[translation].append(word)
    except:
        print("Not json file: {}".format(file.split("/")[-1]))

with open("./hu-fr.json", "w") as outfile:
    json.dump(d, outfile)