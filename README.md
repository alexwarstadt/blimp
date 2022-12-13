# BLiMP: The Benchmark of Linguistic Minimal Pairs

BLiMP is a challenge set for evaluating what language models (LMs) know about major grammatical phenomena in English. BLiMP consists of 67 sub-datasets, each containing 1000 minimal pairs isolating specific contrasts in syntax, morphology, or semantics. The data is automatically generated according to expert-crafted grammars. Aggregate human agreement with the labels is 96.4%. We use BLiMP to evaluate an _n_-gram LM, LSTM LM, GPT-2, and Transformer-XL.

## Repository Contents
- BLiMP data: ```blimp/data/``` and ```blimp/BLiMP.zip``` (same contents)
- The BLiMP paper: ```blimp/BLiMP.pdf```
- The BLiMP icon: ```blimp/blimp_icon.jpg```
- Summary of model results for all paradigms: ```blimp/raw_results/summary/models_summary.jsonl```
- Summary of human validation results: ```blimp/raw_results/summary/human_validation_summary.csv```
- Full model outputs for full sentence method: ```blimp/raw_results/all_outputs/*_outputs.jsonl```
- Full model outputs for prefix methods: ```blimp/raw_results/all_outputs_prefix_methods```
- Full human validation judgments: ```blimp/raw_results/all_outputs/human_responses.csv```
- Description of all paradigms: ```blimp/supplemental_materials/BLiMP_Paradigms.pdf```
- Results plots for all paradigms: ```blimp/supplemental_materials/figures```

## External Links
- Data generation code: https://github.com/alexwarstadt/data_generation
- _n_-gram implementation: https://github.com/anhad13/blimp_ngram
- LSTM LM implementation: https://github.com/sheng-fu/colorlessgreenRNNs
- GPT-2 and Transformer-XL implementations (jiant): https://github.com/nyu-mll/jiant/tree/blimp-and-npi/scripts/blimp 

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

## Recommended Citation
If you use BLiMP in your work, please cite it as follows:
```
@article{warstadt2020blimp,
    author = {Warstadt, Alex and Parrish, Alicia and Liu, Haokun and Mohananey, Anhad and Peng, Wei and Wang, Sheng-Fu and Bowman, Samuel R.},
    title = {BLiMP: The Benchmark of Linguistic Minimal Pairs for English},
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {8},
    number = {},
    pages = {377-392},
    year = {2020},
    doi = {10.1162/tacl\_a\_00321},
    URL = {https://doi.org/10.1162/tacl_a_00321},
    eprint = {https://doi.org/10.1162/tacl_a_00321},
    abstract = { We introduce The Benchmark of Linguistic Minimal Pairs (BLiMP),1 a challenge set for evaluating the linguistic knowledge of language models (LMs) on major grammatical phenomena in English. BLiMP consists of 67 individual datasets, each containing 1,000 minimal pairs—that is, pairs of minimally different sentences that contrast in grammatical acceptability and isolate specific phenomenon in syntax, morphology, or semantics. We generate the data according to linguist-crafted grammar templates, and human aggregate agreement with the labels is 96.4\%. We evaluate n-gram, LSTM, and Transformer (GPT-2 and Transformer-XL) LMs by observing whether they assign a higher probability to the acceptable sentence in each minimal pair. We find that state-of-the-art models identify morphological contrasts related to agreement reliably, but they struggle with some subtle semantic and syntactic phenomena, such as negative polarity items and extraction islands. }
}
```

## License
BLiMP is distributed under a [CC-BY](https://creativecommons.org/licenses/by/4.0/) license.

## Updates & Errata
**16 August 2021** Some results in Tables 3 and 4 were mis-reported in the published TACL version. If you wish to cite specific numbers from the results, please consult the results files in this repo, or the corrected .pdf in this repo and on [arxiv](https://arxiv.org/pdf/1912.00582.pdf).
