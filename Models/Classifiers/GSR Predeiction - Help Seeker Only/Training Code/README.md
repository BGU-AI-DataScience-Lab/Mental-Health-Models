## Training Process

The model was trained to predict the **suicidality score (GSR)** of a help-seeker based on their chat messages.  
The pipeline follows a structured sequence:

1. **Data Loading & Merging**
   - Two datasets were used:
     - **messages**: contains the anonymized text messages from the help-seekers.
     - **conversation info**: contains the corresponding **GSR (suicide risk score)**.
   - Both were merged using `engagement_id`, ensuring that each conversation is aligned with its label.

2. **Preprocessing**
   - Only messages from the **help-seeker** were included (counselor messages were excluded).
   - All messages within a conversation were concatenated using a `[SEP]` token.
   - The dataset was then split into **train (80%)** and **test (20%)**, stratified by label.

3. **Tokenization**
   - The text was tokenized using **AlephBERT’s tokenizer**, with `max_length=512` and padding.
   - The tokenized data was converted into **PyTorch tensors** for model input.

4. **Model Training**
   - The base model used was [`onlplab/alephbert-base`](https://huggingface.co/onlplab/alephbert-base).
   - Optimizer: **AdamW**
   - Batch size: **16**, Epochs: **3**, Learning rate: **2e-5**
   - Training was performed on GPU when available.
   - For each batch:
     - Compute loss.
     - Backpropagate gradients.
     - Apply gradient clipping and optional differential privacy noise (see below).


## Differential Privacy (DP) Mechanism

To protect sensitive information contained in the text (even during training), we experimented with adding **Differential Privacy (DP)** noise to the model gradients.

### How It Works
Differential Privacy ensures that the inclusion or exclusion of any individual conversation does **not significantly affect the model’s parameters** or predictions.

After each gradient update step:
1. **Gradient Clipping**  
   All gradients are clipped to a fixed L2 norm (e.g., `clip_norm = 1.0`) to limit their sensitivity.
2. **Noise Addition**  
   Gaussian noise is added to the gradients:

   `g' = g + N(0, σ²)`

   where:  
   - `g` = original gradient  
   - `ε` (epsilon): privacy budget — smaller values = stronger privacy, more noise  
   - `δ`: small probability of privacy failure
   - `σ`: 
    $$
     \sigma = \sqrt{2 \log\left(\frac{1.25}{\delta}\right)} \cdot \frac{\text{sensitivity}}{\epsilon}
    $$  



### Our Configuration
| Parameter | Description | Value |
|------------|--------------|-------|
| `epsilon` | Privacy budget | 10 |
| `delta` | Probability of failure | 1e-5 |
| `clip_norm` | Gradient clipping norm | 1.0 |
| `sensitivity` | Max gradient influence | 1.0 |
| `σ (sigma)` | Calculated noise std | ≈ 0.018 |

The threshold **σ ≈ 0.018** was empirically found to be optimal - adding enough noise to preserve privacy while maintaining model performance.

## Evaluation Metrics

After training, the model was evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **F2 Score** (to emphasize recall)
- **ROC-AUC**

All metrics were computed on the **test set**, with probabilistic outputs used for AUC calculations.

---

### Summary
This approach demonstrates that integrating **privacy-preserving techniques** such as Differential Privacy into **language models** is feasible without significantly degrading classification accuracy — a promising step toward **ethical AI in mental health** applications.
