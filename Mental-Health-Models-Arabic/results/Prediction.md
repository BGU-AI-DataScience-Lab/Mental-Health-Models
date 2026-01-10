# 📊 Model Performance Comparison

This report summarizes the evaluation results of multiple Arabic-language models: **DK (domain knowledge) AraBERTv0.2-large**, **Gemma-3-4B**, and **Famar-9B** - across four  prediction tasks: GSR, depression, self-hurt, sexual-hurt
Metrics include **Accuracy**, **Precision**, **Recall**, **F1**, and **F2** scores.

---
## Models used

|#| Model                    | Description |
|-|--------------------------|-------|
|1|**AraBERTv0.2 large**    |standard AraBERTv0.2 large ([aubmindlab/bert-large-arabertv02](https://huggingface.co/aubmindlab/bert-large-arabertv02))|
|2|**DK AraBERTv0.2 large** | pretrained model #1 on MLM (on the Arabic Sahar dataset) and domain knowledge (more details in [training folder](https://github.com/AyalSwaid/Mental-Health-models-Arabic/tree/main/Models/Classifiers/GSR%20Predeiction%20-%20Help%20Seeker%20Only/Training%20Code))|
|3|**DK Gemma-3-4B**        | [Gemma3-4b-it](https://huggingface.co/google/gemma-3-4b-it) with sequence-length=1200, Domain knowledge is inserted into prompts as GSR phrases examples from the lexicon|
|4|**DK Fanar-9B**          | [Fanar-1-9B-Instruct](QCRI/Fanar-1-9B-Instruct) with sequence-length=700, Domain knowledge is inserted into prompts as GSR phrases examples from the lexicon|
---

## GSR Results Summary

| Model          | Accuracy | Precision | Recall | F1  | F2 | AUC-ROC  |
|----------------|-----------|------------|--------|-----|----------|-----|
| **AraBERTv0.2 large**         | 0.93 | 0.67 | 0.66 | 0.67 | 0.66 | 0.91 |
| **DK AraBERTv0.2 large**      | 0.94 | 0.66 | 0.74 | 0.70 | 0.72 | 0.92 |
| **DK Gemma-3-4B**                | 0.93 | 0.66 | 0.59 | 0.62 | 0.60 | 0.87 |
| **DK Fanar-9B**                  | 0.94 | 0.68 | 0.68 | 0.68 | 0.68 | 0.94 |
---

## Observations

- **DK AraBERT** achives the highest overall performance.  
- Arabic models (**AraBERT** and **DK Fanar-9b**) outperformed multilingual (**DK Gemma-3-4b**).  
- **DK Gemma-3-4B** is the most unstable .

---

## Subject Classification Results
All models struggeled in subject prediction due to lack of positive labels.

| Category | Support | Model | Accuracy | Precision | Recall | F1  | F2  | ROC-AUC |
|----------|---------|--------|-----------|------------|--------|-----|----------|-----|
| Depression  | 102  | AraBERTv0.2 large | 0.83 | 0.41 | 0.30 | 0.35 | 0.2 | 0.79 |
|             |      | DK AraBERTv0.2 large     | 0.85 | 0.50 | 0.44 | 0.46 | 0.45 | 0.82 |
|             |      | DK Fanar-9B     | 0.83 | 0.43 | 0.52 | 0.47 | 0.50 | 0.79 |
|  Self Hurt  |  10  | AraBERTv0.2 large     | 0.98 | 0.2 | 0.1 | 0.13 | 0.11 | 0.87 |
|             |      | DK AraBERTv0.2 | 0.97 | 0.18 | 0.2 | 0.19 | 0.19 | 0.89 |
|             |      | DK Fanar-9B     | 0.98 | 0.50 | 0.2 | 0.28 | 0.22 | 0.87 |
| Sexual Hurt |  15  | AraBERTv0.2 large     | 0.97 | 0.45 | 0.6 | 0.51 | 0.56 | 0.86 |
|             |      | DK AraBERTv0.2 large | 0.97 | 0.47 | 0.66 | 0.55 | 0.61 | 0.9 |
|             |      | DK Fanar-9B     | 0.98 | 0.66 | 0.93 | 0.77 | 0.86 | 0.99 |

### Insights
- **dk Fanar** consistently surpasses **DK AraBERTv0.2** in both Recall and F1 across all subject prediction tasks. Though performance remains low due to lack of positive data. Same for **DK AraBERTv0.2** and **AraBERTv0.2** large respectively
- in sexual-hurt **Fanar** showed great recall score even though it is only 2% of the data. It is still unreliable, Cross-Validation is recommended to ensure the performance isn't due to chance or overfitting on rare cases.
- All models had trouble with depression prediction even though it contains more positive samples.
- The reason for **DK AraBERTv0.2** did not benifit from its domain knowledge is because it trained on suicidal categories only domain knowledge.


---

*All results were computed using identical dataset splits and preprocessing pipelines, **except sexual-hurt** which used different split due to target distribution in train and test sets.
It is important to note that **DK AraBERTv0.2** did not see the prediction test set during its MLM&reg pre-training, **except for the sexual-hurt split**. While this may be considered a form of data leakage, it did not produce any suspicious or anomalous results.
Metrics represent binary-averaged values unless otherwise stated.*














