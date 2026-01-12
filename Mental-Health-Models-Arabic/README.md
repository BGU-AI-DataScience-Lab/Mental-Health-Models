# **Arabic Mental Health Models**

The models in this repository include fine-tuned large language models and classifiers built to provide emotional support and detect mental crisis risk in Arabic conversations. Trained on anonymized chat data from [Sahar](https://sahar.org.il/) oraganization, they can identify indicators of suicidality, depression, self-harm, and sexual harm in real interactions.

A complementary dataset used in this research, the [Help-Seeking-Corpus](https://resources.nnlp-il.mafat.ai/?search=help-seeking-corpus), is released independently and provides anonymized help-seeker/volunteer conversations (available in Hebrew and Arabic).

Together, these models offer a strong foundation for developing safe, empathetic, and culturally informed AI systems for mental health support.

---

##  Models

This repository provides both **classifier models** for risk detection and **generative models** for supportive response generation, all fine-tuned on Arabic data.

### 🔍 Classifiers
- **Fine-tuned Arabic models** to identify **multiple risk levels** in conversations.  
- Tasks include:
  - **GSR Prediction** (binary suicidality detection for General Suicide Risk)  
  - **IMSR Prediction** (binary suicidality detection for Immediate Suicide Risk)  
  - **Subject Prediction** (binary classification for depression, self-harm, sexual harm)  
- Implemented using **AraBERTv0.2 large**, **Gemma-3**, and **Fanar** models.  
- Trained on anonymized **help-seeker messages**

### 🧠 Generative
- Fine-tuned **gemma-3 via Unsloth** model to process and generate a response to an **Arabic conversation** between help-seeker and a counselor. The model is trained to be supportive and empathic mimicing  a real counselor behavior.

Together, these models allow for:
1. **Risk detection** – automatically identifying high-risk conversations.  
2. **Response generation** – producing empathetic counselor-style messages to assist in support settings.  



## Fine-tuning Classifiers

All fine-tune scripts here are based on the Sahar dataset. 
Here is some background:


### Dataset
Both datasets contains more information, but We will describe only what's neccessary.

**Messages** contains 
* engagement_id 
* text (original messages) 

**Conversation info** contains
* engagement_id
* gsr (suicide score assessment - 0 or 1)
* Subject (conversation subject)

### Flow of the model
We try to predict whether a help-seeker is suicidal based on a combination of the chat.

This model takes into account only the messages of the help seeker,

and it does not takes into account the counselor messages.

* We merge both datasets based on engagement_id.
* We tokenize every batch
* We train the model


## Fine-tuning the Generative Model
All generative fine-tuning experiments in this repository are based on the Sahar progressive emotional support dataset.
The goal is to adapt an **LLM** (**Gemma-3-12B**) to produce empathetic, counselor-aligned responses in crisis and support conversations in **Arabic**.

### Dataset
We use an **Arabic** conversation dataset structured as pairs of turns:

Input – the help-seeker’s anonymized message.
Output – the counselor’s supportive response (written by Sahar volunteers).
This ensures that the model learns how to respond to diverse, emotionally intense situations in a safe and non-judgmental way.
The dataset is anonymized, cleaned, and formatted into a chat-template format that follows a user → assistant dialogue structure.

### Flow of the model
The generative fine-tuning follows these steps:

* Load pretrained base model:
Gemma-3-12B in 4-bit precision ([unsloth/gemma-3-12b-it-unsloth-bnb-4bit](https://huggingface.co/unsloth/gemma-3-12b-it-unsloth-bnb-4bit)) is chosen for efficiency and strong Arabic support.

* Parameter-efficient fine-tuning (PEFT):
We apply LoRA adapters with small rank (r=8, lora_alpha=8) to reduce GPU memory usage while keeping performance.

* Chat template formatting:
Each training sample is converted into a structured dialogue:

* User message (help-seeker)
Assistant response (counselor)
This standardization ensures consistent model conditioning.

* System prompt - inserting system prompt helps controlling the style of the model ouput. Used to insert domain knowledge as a part of the prompt too. 
Note that it is included in the code (inference.ipynb and inference_with_lexicon.ipynb).
##  Inference

After fine-tuning, you can run both **classifier** and **generative** models for predictions.

### Classifier (AraBERT)
- Load the tokenizer and model (aubmindlab/bert-large-arabertv02).  
- Load your saved weights (`.pth` file).  
- Tokenize input text and run it through the model.  
- Output is **0 = Not Suicidal** or **1 = Suicidal**.  

### Generative (Gemma-3)
Format input as a chat template (system + user message).
Add system prompt / domain knowledge
Use the fine-tuned Gemma-3 model with .generate().
The model produces an empathetic, counselor-style response in Arabic.
You can adjust generation parameters (max_new_tokens, temperature, top_p, top_k) for response length and creativity.












