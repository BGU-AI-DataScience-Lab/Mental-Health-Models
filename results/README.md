# 📊 Model Performance Comparison

This report summarizes the evaluation results of multiple Hebrew-language models: **AlephBERT**, **Gemma-2-2B**, and **Gemma-2-9B** - across three setups:  
**Binary**, **Multiclass**, and **Multilabel** classification.  
Metrics include **Accuracy**, **Precision**, **Recall**, **F1**, **ROC-AUC**, and **F2** scores.

---

## GSR Results Summary

| Model          | Dataset      | Accuracy | Precision | Recall | F1  | ROC_AUC | F2  |
|----------------|--------------|-----------|------------|--------|-----|----------|-----|
| **AlephBERT**  | Original     | 0.90 | 0.74 | 0.68 | 0.71 | 0.92 | 0.69 |
|                | Anonymized   | 0.89 | 0.71 | 0.72 | 0.71 | 0.92 | 0.71 |
| **Gemma-2-2B** | Original     | 0.89 | 0.70 | 0.71 | 0.70 | 0.91 | 0.71 |
|                | Anonymized   | 0.89 | 0.82 | 0.56 | 0.67 | 0.91 | 0.60 |
| **Gemma-2-9B** | Original     | 0.90 | 0.72 | 0.78 | 0.75 | 0.93 | 0.77 |
|                | Anonymized   | 0.90 | 0.74 | 0.75 | 0.75 | 0.92 | 0.75 |

---

## Observations

- **AlephBERT** maintains consistent performance between Original and Anonymized data.  
- **Gemma-2-2B** shows a notable **drop in Recall** under anonymization.  
- **Gemma-2-9B** demonstrates **robust generalization**, with minimal degradation.  
- The **highest overall F1 and F2** are achieved by **Gemma-2-9B (Original)**.

---

## Binary Classification Results

| Category (Hebrew) | Model | Accuracy | Precision | Recall | F1  | ROC-AUC | F2  |
|--------------------|--------|-----------|------------|--------|-----|----------|-----|
| Depression         | AlephBERT | 0.78 | 0.65 | 0.53 | 0.59 | 0.81 | 0.55 |
|                    | Gemma-2-9B     | 0.79 | 0.65 | 0.60 | 0.62 | 0.83 | 0.61 |
| Self Hurt          | AlephBERT | 0.96 | 0.63 | 0.55 | 0.59 | 0.93 | 0.57 |
|                    | Gemma-2-9B     | 0.96 | 0.66 | 0.71 | 0.68 | 0.96 | 0.70 |
| Sexual Hurt        | AlephBERT | 0.95 | 0.59 | 0.73 | 0.65 | 0.94 | 0.70 |
|                    | Gemma-2-9B     | 0.96 | 0.82 | 0.66 | 0.73 | 0.94 | 0.69 |

### Insights
- **Gemma** consistently surpasses **AlephBERT** in both Recall and F1 across all binary tasks.

---

## Multiclass Classification Results

| Category (Hebrew) | Model | Precision | Recall | F1 |
|--------------------|--------|------------|--------|----|
| Depression         | AlephBERT | 0.65 | 0.53 | 0.58 |
|                    | Gemma-2-9B     | 0.58 | 0.75 | 0.65 |
| Self Hurt          | AlephBERT | 0.52 | 0.60 | 0.55 |
|                    | Gemma-2-9B     | 0.59 | 0.54 | 0.56 |
| Sexual Hurt        | AlephBERT | 0.64 | 0.65 | 0.65 |
|                    | Gemma-2-9B     | 0.67 | 0.80 | 0.73 |
| Other              | AlephBERT | 0.80 | 0.85 | 0.83 |
|                    | Gemma-2-9B     | 0.88 | 0.76 | 0.81 |

### Observations
- **Gemma** outperforms **AlephBERT** on emotional and trauma-related categories (higher recall & F1).  
- **AlephBERT** maintains strong performance in the “Other” category.

---

## Multilabel Classification Results

| Category (Hebrew) | Model | Precision | Recall | F1 |
|--------------------|--------|------------|--------|----|
| Depression         | AlephBERT | 0.63 | 0.61 | 0.62 |
|                    | Gemma-2-9B     | 0.62 | 0.69 | 0.65 |
| Self Hurt          | AlephBERT | 0.62 | 0.67 | 0.64 |
|                    | Gemma-2-9B     | 0.64 | 0.68 | 0.66 |
| Sexual Hurt        | AlephBERT | 0.84 | 0.54 | 0.66 |
|                    | Gemma-2-9B     | 0.84 | 0.63 | 0.72 |
| Other              | AlephBERT | 0.82 | 0.82 | 0.82 |
|                    | Gemma-2-9B     | 0.84 | 0.83 | 0.84 |

### Insights
- **Multilabel setup** improves balance between Recall and F1 across all classes.  
- **Gemma** shows better recall, especially in overlapping emotional categories.  
- **AlephBERT** performs well on distinct classes like “Other” and “Trauma”.

---

*All results were computed using identical dataset splits and preprocessing pipelines.  
Metrics represent macro-averaged values unless otherwise stated.*

