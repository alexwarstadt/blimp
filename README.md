# BLiMP: The Benchmark of Linguistic Minimal Pairs

Downloadable BLiMP data and supplementary materials.

## Data

All 67 sub-datasets of BLiMP are available in .jsonl format.

Each contains 1000 lines in json format, with the following fields:
- "sentence_good": The acceptable sentence 
- "sentence_bad": The unacceptable sentence 
- "field": Subfield of linguistics associated with the paradigm (there are 4 possible values: morphology, syntax, syntax-semantics, and semantics)
- "linguistics_term": The category of phenomenon illustrated by the paradigm (there are 12 possible values, discussed in the paper)
- "UID": The unique identifier for the paradigm 
- "simple_LM_method": Boolean, identifies whether the paradigm is consistent with the "simple LM method" 
- "one_prefix_method": Boolean, identifies whether the paradigm is consistent with the "one prefix method" 
- "two_prefix_method": Boolean, identifies whether the paradigm is consistent with the "two prefix method"
- "lexically_identical": Boolean, identifies whether the sentences in the paradigm are lexically identical
- "pairID": A number from 0-999 identifying the index of the pair in the paradigm.
