# BLiMP: The Benchmark of Linguistic Minimal Pairs

BLiMP is a challenge set for evaluating what language models (LMs) know about major grammatical phenomena in English. BLiMP consists of 67 sub-datasets, each containing 1000 minimal pairs isolating specific contrasts in syntax, morphology, or semantics. The data is automatically generated according to expert-crafted grammars. Aggregate human agreement with the labels is 96.4%. We use BLiMP to evaluate an _n_-gram LM, LSTM LM, GPT-2, and Transformer-XL.

## Repository Contents
- The BLiMP paper: ```blimp/BLiMP.pdf```
- The BLiMP icon: ```blimp/blimp_icon.jpg```
- BLiMP data: ```blimp/data/```
- Summary of model results for all paradigms: ```blimp/raw_results/blimp_full_results_summary.csv```
- Summary of human validation results: ```blimp/raw_results/blimp_human_validation_summary.csv```
- Full human validation judgments: ```blimp/raw_results/blimp_human_validation_rawMTurk.csv```
- Description of all paradigms: ```blimp/supplemental_materials/BLiMP_Paradigms.pdf```
- Results plots for all paradigms: ```blimp/supplemental_materials/figures/*```

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

## The BLiMP Icon
The icon used to refer to BLiMP in the paper is included in this repository as ```blimp/blimp\_icon.jpg```. To include this icon in your paper, you can use the following macro in LaTex (make sure you include packages ```graphicx``` and ```scalerel``` and add the ```blimp_icon.jpg``` to your project):

```\def\BLiMP{\scalerel*{\includegraphics{blimp_icon.jpg}}{X}\,}```
