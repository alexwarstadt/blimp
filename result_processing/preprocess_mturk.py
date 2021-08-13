# Author: Alex Warstadt
# This script is used to put in a usable format results mturk downloaded from the BLiMP project google drive (not public)

import pandas as pd
import numpy as np

df = pd.read_csv("../raw_results/all_outputs_google_drive/blimp_human_validation_rawMTurk.csv", header=0)
df = df.drop(["HITTypeId", "Title", "Description", "Keywords", "Reward", "CreationTime", "MaxAssignments",
              "RequesterAnnotation", "AssignmentDurationInSeconds", "AutoApprovalDelayInSeconds", "Expiration",
              "NumberOfSimilarHITs", "LifetimeInSeconds", "AssignmentId", "AssignmentStatus", "AcceptTime",
              "SubmitTime", "AutoApprovalTime", "ApprovalTime", "RejectionTime", "RequesterFeedback",
              "WorkTimeInSeconds", "LifetimeApprovalRate", "Last30DaysApprovalRate", "Last7DaysApprovalRate",
              "Input.answer_order", "Answer.ChoiceSample1", "Answer.english", "Answer.humans", "Answer.native",
              "Answer.navtive", "Answer.numanswered", "Answer.useragent", "Approve", "Reject", "Answer.humans_math",
              "Answer.humans_text", "anonCode"], axis=1)
df = df.set_index(["HITId", "Input.list"])

df_items = []
for i in range(1, 6):
    df_i = df[[f"Input.item_{i}_condition", f"Input.field_{i}_1", f"Input.field_{i}_2", f"Answer.Choice{i}"]]
    df_i = df_i.rename({f"Input.item_{i}_condition": "condition", f"Input.field_{i}_1": "sentence1", f"Input.field_{i}_2": "sentence2", f"Answer.Choice{i}": "response"}, axis=1)
    df_items.append(df_i)

df = pd.concat(df_items)
df["UID"] = df["condition"].apply(lambda x: x[:-4])
df["right_answer"] = df["condition"].apply(lambda x: x[-1])
for x in df:
    if np.isnan(x["response"]):
        print(x)
df["response"] = df["response"].apply(lambda x: x[0])

print(df.head(1000).to_string())