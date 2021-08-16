import pandas as pd
import numpy as np

results = []
for model in ["ngram", "lstm", "txl", "gpt2"]:
    df = pd.read_json(f"../raw_results/all_outputs/{model}_outputs.jsonl", lines=True, orient="records")
    df["correct"] = df.apply(lambda x: x["prob_good"] > x["prob_bad"], axis=1)
    df["model"] = model
    correct = df[["correct", "UID", "linguistics_term", "model"]]
    correct = pd.pivot_table(correct, values="correct", index=["UID", "linguistics_term"], aggfunc=np.mean)
    correct = correct.rename({"correct": model}, axis=1)
    results.append(correct)

results = pd.concat(results, axis=1).reset_index()
results = results.sort_values(by=["linguistics_term", "UID"])

term_overall = results.set_index(["UID", "linguistics_term"]).stack().reset_index()
term_overall = pd.pivot_table(term_overall, index="linguistics_term", columns="level_2", values=0, aggfunc=np.mean)
term_overall = term_overall.reset_index()
term_overall["UID"] = "overall"

total_overall = results.set_index(["UID", "linguistics_term"]).stack().reset_index()
total_overall = pd.pivot_table(total_overall, columns="level_2", values=0, aggfunc=np.mean)
total_overall = total_overall.reset_index()
total_overall["UID"] = "overall"
total_overall["linguistics_term"] = "overall"

results = pd.concat([results, term_overall, total_overall])
results = results.drop(["index"], axis=1)


results.to_json("../raw_results/summary/models_summary.jsonl", lines=True, orient="records")

