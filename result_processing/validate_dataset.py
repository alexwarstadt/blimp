import pandas as pd
import os
import numpy as np

blimp = []
for x in os.listdir("../data"):
    df = pd.read_json("../data/" + x, orient="records", lines=True)
    blimp.append(df)

blimp = pd.concat(blimp)
blimp = blimp.set_index(["UID", "pairID"])
blimp = blimp.rename({"sentence_good": "sentence_good_blimp", "sentence_bad": "sentence_bad_blimp"}, axis=1)

for model in ["ngram", "lstm", "txl", "gpt2"]:
    df = pd.read_json(f"../raw_results/all_outputs/{model}_outputs.jsonl", lines=True, orient="records")
    df = df.set_index(["UID", "pairID"])
    df = pd.concat([df, blimp], axis=1)
    match = df.apply(lambda x: "".join(x["sentence_good"].split()).lower() == "".join(x["sentence_good_blimp"].split()).lower()
                               and "".join(x["sentence_bad"].split()).lower() == "".join(x["sentence_bad_blimp"].split()).lower(),
                     axis=1)
    print(df[~match].to_string())
    # print(np.mean(match))

