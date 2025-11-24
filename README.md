# Mental Health Models

This repository contains generative and classification models for the mental-health and crisis-support domain, developed in collaboration with the [Sahar](https://sahar.org.il/) organization.

The models are fine-tuned large language models and classifiers designed for emotional support and risk detection in Hebrew. They are trained on fully anonymized Sahar chat data, with the goal of identifying emotional states, distress patterns, and indicators of suicidality in real conversations.

A complementary dataset used in this research, the [Help-Seeking-Corpus](https://resources.nnlp-il.mafat.ai/?search=help-seeking-corpus), is released independently and provides anonymized help-seeker/volunteer conversations (available in Hebrew and Arabic).

Together, these models form a research-oriented foundation for building safe, empathetic, and culturally adapted AI systems for mental-health support.

--- 

## Model Weights Access
The models are trained on unique datasets from Sahar.

**To gain access to the model weights, you must fill out a request form.**  
This ensures compliance with ethical guidelines & privacy requirements.

🔗 [Request Model Weights Access Form](https://forms.gle/8YEmXQiSvHxEJsmw8)

---

This repository contains two complementary components:  

1. **Classifiers** – Supervised models for detecting suicidality and subject prediction tasks using volunteer-anonymized mental health chat data.  
2. **Generative** – Fine-tuning large language models (Gemma-3 via Unsloth) to act as empathetic, supportive responders aligned with real counselor behavior.  

The repository provides code, training scripts, and evaluation pipelines for both tasks.



## ⚙️ Setup & Installation

### Prerequisites
Before setting up the repository, make sure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager) or **conda**
- **CUDA-enabled GPU** (recommended for training large models)

### Clone the Repository
```bash
git clone https://github.com/BGU-AI-DataScience-Lab/Mental-Health-models.git
cd Mental-Health-models
```

### Install Dependencies

We recommend creating a virtual environment before installing dependencies.

```
# Create virtual environment
python -m venv venv

# Activate environment
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### GPU Support
For optimal performance, ensure you have CUDA-compatible PyTorch installed if you plan to use GPU acceleration. The requirements.txt includes the basic PyTorch installation, but you may need to install the CUDA-specific version based on your system configuration.



---

##  Models

This repository provides both **classifier models** for risk detection and **generative models** for supportive response generation, all fine-tuned on Hebrew data.

### 🔍 Classifiers
- **Fine-tuned Hebrew models** to identify **multiple risk levels** in conversations.  
- Tasks include:
  - **GSR Prediction** (binary suicidality detection for General Suicide Risk)  
  - **IMSR Prediction** (binary suicidality detection for Immediate Suicide Risk)  
  - **Subject Prediction** (binary and multilabel classification for depression, self-harm, sexual harm)  
- Implemented using **AlephBERT** and **Gemma-2** models.  
- Trained on anonymized **help-seeker messages** 
- Support for **Differential Privacy (DP)** fine-tuning with customizable privacy thresholds.  

### 🧠 Generative
- **Trained Generative Model in Hebrew** based on **Gemma-3-12B**.  
- Fine-tuned on **Sahar’s volunteer support language** using progressive emotional support datasets.  
- Alignment with **Sahar’s principles** for empathetic, non-judgmental responses.  
- Supports **parameter-efficient fine-tuning (LoRA)** with quantization (`bitsandbytes`) for efficient training.  
- Produces natural, context-aware, and supportive responses in Hebrew.  

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
* anonymized (modified messages by Sahar volunteers)

**Conversation info** contains
* engagement_id
* gsr (suicide score assessment - 0 or 1)

### Flow of the model
We try to predict whether a help-seeker is suicidal based on a combination of the chat.

This model takes into account only the messages of the help seeker,

and it does not takes into account the counselor messages.

* We merge both datasets based on engagement_id.
* We tokenize every batch
* We train the model


## Fine-tuning the Generative Model

All generative fine-tuning experiments in this repository are based on the **Sahar progressive emotional support dataset**.  
The goal is to adapt a large Hebrew-capable model (Gemma-3-12B) to produce **empathetic, counselor-aligned responses** in crisis and support conversations.  

### Dataset
We use a **conversation dataset** structured as **pairs of turns**:
- **Input** – the help-seeker’s anonymized message.  
- **Output** – the counselor’s supportive response (written by Sahar volunteers).  

This ensures that the model learns **how to respond** to diverse, emotionally intense situations in a safe and non-judgmental way.  
The dataset is anonymized, cleaned, and formatted into a **chat-template format** that follows a user → assistant dialogue structure.

### Flow of the model
The generative fine-tuning follows these steps:

1. **Load pretrained base model**:  
   Gemma-3-12B in 4-bit precision (`unsloth/gemma-3-12b-it-unsloth-bnb-4bit`) is chosen for efficiency and strong Hebrew support.

2. **Parameter-efficient fine-tuning (PEFT)**:  
   We apply **LoRA adapters** with small rank (`r=8`, `lora_alpha=8`) to reduce GPU memory usage while keeping performance.

3. **Chat template formatting**:  
   Each training sample is converted into a structured dialogue:  
   - User message (help-seeker)  
   - Assistant response (counselor)  
   This standardization ensures consistent model conditioning.

4. **Supervised Fine-Tuning (SFT)**:  
   We train using Hugging Face’s `trl.SFTTrainer`, optimizing the model on counselor responses only (ignoring instructions in loss calculation).

5. **Evaluation and inference**:  
   After training, the model can be prompted with a help-seeker’s message and will generate a **supportive, empathetic response** aligned with Sahar’s principles.

### Alignment with Counselor Guidelines (Prompt)
The fine-tuning integrates **Sahar’s supportive communication principles**, emphasizing:
- Active listening and validation  
- Avoiding judgment or clinical advice  
- Allowing open discussion of suicidal thoughts  
- Encouraging sharing, presence, and gentle probing  
- Using **simple, warm, empathetic Hebrew language**  

##  Inference

After fine-tuning, you can run both **classifier** and **generative** models for predictions.

### Classifier (AlephBERT)
- Load the tokenizer and model (`onlplab/alephbert-base`).  
- Load your saved weights (`.pth` file).  
- Tokenize input text and run it through the model.  
- Output is **0 = Not Suicidal** or **1 = Suicidal**.  

### Generative (Gemma-3)
- Format input as a **chat template** (system + user message).  
- Use the fine-tuned Gemma-3 model with `.generate()`.  
- The model produces an **empathetic, counselor-style response in Hebrew**.  
- You can adjust generation parameters (`max_new_tokens`, `temperature`, `top_p`, `top_k`) for response length and creativity.  





