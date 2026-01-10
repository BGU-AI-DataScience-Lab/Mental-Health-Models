# 📊 Model Performance Comparison

This report summarizes the evaluation results of **Gemma-3-12B** LLM for the generation task, each experiement involved different approach of teaching the model to talk more the "Sahar" style. 

Metrics include **BERTScore**, **Perplexity**.

## Experiements

|#| Model                    | Description |
|-|--------------------------|-------|
|1|**Gemma-3-12B basic model**    |standard [Gemma-3-12B](https://huggingface.co/google/gemma-3-12b-it) without finetuning|
|2|**Gemma-3-12B 2000 steps**        | [Gemma-3-12B](https://huggingface.co/google/gemma-3-12b-it) finetuned (causal LM) on the Sahar data for 2000 steps|
|3|**Gemma-3-12B lexiocon as text**          | same as **Gemma-3-12B 2000 steps** but added 5 most relevant categories of the last user message (categories from lexicon) as a text in the prompt during training time|

---

## Results Summary


| Model | BERTScore | Perplexity |
| :--- | :--- | :--- |
| **Gemma-3-12B basic model** | 0.6356 | 15571294.791 |
| **Finetuned Gemma3 (2000 steps)** | 0.7534 | 1254.392 |
| **Gemma-3-12B lexiocon as text**  | 0.7523 | 1822.310 |
---

## Insights

Fine-tuning Gemma-3-12B for 2,000 steps significantly improved the BERTScore and dramatically reduced perplexity, indicating a model that effectively adopted the "Sahar" counselors' Dialectal Arabic (DA) expression. Conversely, finetuning with the lexicon as domain knowledge did not improve the BERTScore and actually degraded perplexity. Furthermore, despite having a comparable BERTScore to the base fine-tuned model, the lexicon-integrated version frequently generated sentences without meaning, making it less reliable for coherent text generation.
