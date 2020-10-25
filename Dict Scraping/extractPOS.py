import json

dct = {}

with open("./Combined/vdict VI-EN.json", "r") as infile:
    data = json.load(infile)

for (word, translations) in data.items():
    if translations != "N/A":
        numTrans = translations["nums"]
        for i in range(1, numTrans+1):
            translation = translations[str(i)]
            pos = translation["POS"]
            if pos != "":
                if word not in dct:
                    dct[word] = [pos]
                elif pos not in dct[word]:
                    dct[word] += [pos]

with open("./pos.json", "w") as outfile:
    json.dump(dct, outfile)
