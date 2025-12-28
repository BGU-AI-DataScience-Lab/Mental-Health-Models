## Training Process
The process included:
1. pre-training AraBERTv0.2 large with two tasks: MLM and regression (details below)
2. Fine-tuning our pre-trained model  to predict the **suicidality score (GSR)** of a help-seeker based on their chat messages.  

# How to use
First you need to run the split_data.py file to create splits for train, test, unlabeled, as pickle files. Then you can run any of the finetuning scripts. Note that if you already have the pickle data files then no need to run the split_data.py script.


## Pre-Training
We continued the pre-training of AraBERTv0.2 large with two tasks:
### 1. MLM - to adapt to the Sahar conversations style domain
Here we implemented regular BERT style MLM task, which improved the fine-tuning results.
### 2. Regression - to inject domain knowledge
Here is the process of the regression task
   1. Given unlabeled conversations and domain-expert lexicon that contains phrases that indicates to A GSR. The lexicon also contains phrase category
   2. We selected 6 categories "Past suicidal history", "Family suicide history", "Suicidal ideation", "Hopelessness", "Deliberate self harm", and "Perceived burdensomeness". Then calculated each categories' total phrases frequency in the given conversation, and saved it as a vector of size 6.
   3. Add a regression head to the AraBERTv0.2 and train it to produce the calculated frequency vector, optimize it on MSE loss.

## Fine-Tuning
The Fine-Tuning pipeline follows a structured sequence:

1. **Data Loading & Merging**
   - Two datasets were used:
     - **messages**: contains the anonymized text messages from the help-seekers.
     - **conversation info**: contains the corresponding **GSR (suicide risk score)**.
   - Both were merged using `engagement_id`, ensuring that each conversation is aligned with its label.

2. **Preprocessing**
   - Only messages from the **help-seeker** were included (counselor messages were excluded).
   - All messages within a conversation were concatenated using a `[SEP]` token.
   - The dataset was then split into **train (70%)** and **test (30%)**, stratified by label.

3. **Tokenization**
   - The text was tokenized using **AraBERTv0.2 large’s tokenizer**, with `max_length=512` and padding.
   - The tokenized data was converted into **PyTorch tensors** for model input.

4. **Model Training**
   - The base model used was the pre-trained model mentioned above.
   - Optimizer: **AdamW** with linear scheduler with num_warmup_steps=0.
   - Batch size: **8**, Epochs: **30**, Learning rate: **2e-5**
   - Training was performed on GPU when available.
   - Apply gradient clipping

## Evaluation Metrics

After training, the model was evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **F2 Score** (to emphasize recall)
  

### Summary
This approach demonstrates that adapting the model into our specific domain, Sahar conversations in this case and applying domain-exper knowledge mechanism will boost performance.

