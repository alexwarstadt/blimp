# Author: Alex Warstadt
# This script is used to put in a uniform format results downloaded from the BLiMP project google drive (not public)

import pandas as pd
import re

# Get linguistics term
lstm = pd.read_json("../raw_results/all_outputs_google_drive/blimp-lstm_simplelm_peephole.jsonl", orient="records", lines=True)
linguistics_terms = {x["UID"]: x["linguistics_term"] for _, x in lstm.iterrows()}
linguistics_terms = {x: "argument_structure" if linguistics_terms[x]=="s-selection" else linguistics_terms[x]
                     for x in linguistics_terms}

# GPT2
gpt2 = pd.read_json("../raw_results/all_outputs_google_drive/blimp-gpt2_simplelm.jsonl", orient="records", lines=True)
gpt2["sent1_str"] = gpt2["sent1_str"].apply(lambda x: re.sub(r"Ġ", "", x))
gpt2["sent2_str"] = gpt2["sent2_str"].apply(lambda x: re.sub(r"Ġ", "", x))
gpt2 = gpt2.drop(["sent_mask1", "sent_mask2"], axis=1)
gpt2 = gpt2.rename({"sent1_str": "sentence_good", "sent2_str": "sentence_bad", "lm_prob1": "prob_good", "lm_prob2": "prob_bad"}, axis=1)
gpt2["linguistics_term"] = gpt2.apply(lambda x: linguistics_terms[x["UID"]], axis=1)
gpt2 = gpt2[gpt2["UID"].apply(lambda x: x not in ["coordinate_structure_constraint_subject_extraction", "wh_questions_object_gap_long_distance"])]
gpt2.to_json("../raw_results/all_outputs/gpt2_outputs.jsonl", orient="records", lines=True)

# LSTM
lstm = pd.read_json("../raw_results/all_outputs_google_drive/blimp-lstm_simplelm_peephole.jsonl", orient="records", lines=True)
lstm = lstm[["sentence_good", "sentence_bad", "UID", "lm_prob1", "lm_prob2", "pairID"]]
lstm = lstm.rename({"lm_prob1": "prob_good", "lm_prob2": "prob_bad"}, axis=1)
lstm["linguistics_term"] = lstm.apply(lambda x: linguistics_terms[x["UID"]], axis=1)
lstm = lstm[lstm["UID"].apply(lambda x: x not in ["coordinate_structure_constraint_subject_extraction", "wh_questions_object_gap_long_distance"])]
lstm.to_json("../raw_results/all_outputs/lstm_outputs.jsonl", orient="records", lines=True)

# TXL
txl = pd.read_json("../raw_results/all_outputs_google_drive/blimp-txl_simplelm.jsonl", orient="records", lines=True)
txl = txl.drop(["sent_mask1", "sent_mask2"], axis=1)
txl = txl.rename({"sent1_str": "sentence_good", "sent2_str": "sentence_bad", "lm_prob1": "prob_good", "lm_prob2": "prob_bad"}, axis=1)
txl["linguistics_term"] = txl.apply(lambda x: linguistics_terms[x["UID"]], axis=1)
txl = txl[txl["UID"].apply(lambda x: x not in ["coordinate_structure_constraint_subject_extraction", "wh_questions_object_gap_long_distance"])]
txl.to_json("../raw_results/all_outputs/txl_outputs.jsonl", orient="records", lines=True)

# ngram
ngram = pd.read_json("../raw_results/all_outputs_google_drive/ngram_outputsimpLM.jsonl", orient="records")
ngram = ngram.rename({"p_good": "prob_good", "p_bad": "prob_bad"}, axis=1)
ngram["linguistics_term"] = ngram.apply(lambda x: linguistics_terms[x["UID"]], axis=1)
ngram = ngram[ngram["UID"].apply(lambda x: x not in ["coordinate_structure_constraint_subject_extraction", "wh_questions_object_gap_long_distance"])]
ngram.to_json("../raw_results/all_outputs/ngram_outputs.jsonl", orient="records", lines=True)

