# Mental Health Models for Arabic and Hebrew

This repository contains a collection of generative and classification models for the mental health and crisis support domain, developed in collaboration with the [Sahar](https://sahar.org.il/) organization. The models are designed for emotional support and risk detection in both **Arabic** and **Hebrew**.

The models are fine-tuned large language models and classifiers trained on fully anonymized Sahar chat data. Their primary purpose is to identify emotional states, distress patterns, and suicidality in real conversations, and to generate empathetic and supportive responses.

## Table of Contents
- [Mental Health Models for Arabic and Hebrew](#mental-health-models-for-arabic-and-hebrew)
  - [Table of Contents](#table-of-contents)
  - [🤖 Models Overview](#-models-overview)
  - [📊 Results](#-results)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [🔑 Model Access](#-model-access)
  - [📂 Project Structure](#-project-structure)


## 🤖 Models Overview

This repository provides both **classifier models** for risk detection and **generative models** for supportive response generation.

| Language | Model Type         | Description                                                                                                                                                                                          | Models Used                      | Details                                                                                    |
|:---------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------|
| **Hebrew** | **Classifiers**      | Supervised models for detecting suicidality and predicting the subject of a conversation, with support for Differential Privacy (DP) fine-tuning. Includes GSR, IMSR, and Subject Prediction (depression, self-harm, sexual harm).           | `AlephBERT`, `Gemma-2`           | [Go to the Hebrew Models README](./Mental-Health-Models-Hebrew/README.md)       |
|            | **Generative Models**| A `Gemma-3-12B` model fine-tuned to act as an empathetic and supportive responder, aligned with real counselor behavior in Hebrew.                                                                   | `Gemma-3-12B`                    | [Go to the Hebrew Models README](./Mental-Health-Models-Hebrew/README.md)       |
| **Arabic** | **Classifiers**      | Semi-Supervised models for detecting suicidality and predicting the subject of a conversation                                       | `AraBERTv0.2 large`, `Gemma-3`, `Fanar` | [Go to the Arabic Models README](./Mental-Health-Models-Arabic/README.md)       |
|            | **Generative Models**| A fine-tuned `gemma-3` model that generates supportive and empathetic responses in Arabic, mimicking the behavior of a real counselor. and additional version that uses the lexicon domain knowledge while training.                                                 | `gemma-3`                        | [Go to the Arabic Models README](./Mental-Health-Models-Arabic/README.md)       |

## 📊 Results

Detailed performance metrics and analysis for the models can be found in the respective language directories:

*   ➡️ **[Arabic Models Results](./Mental-Health-Models-Arabic/results/Prediction.md)**
*   ➡️ **[Hebrew Models Results](./Mental-Health-Models-Hebrew/results/README.md)**

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.9+**
*   **pip** (Python package manager) or **conda**
*   **CUDA-enabled GPU** (recommended for training and running the larger models)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BGU-AI-DataScience-Lab/Mental-Health-Models.git
    cd Mental-Health-Models
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate environment
    # On Linux/Mac
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3.  **Install the required dependencies for each language:**
    *   **For Arabic models:**
        ```bash
        pip install -r Mental-Health-Models-Arabic/requirments.txt
        ```
    *   **For Hebrew models:**
        ```bash
        pip install -r Mental-Health-Models-Hebrew/requirments.txt
        ```

## 🔑 Model Access

The models were trained on unique and sensitive datasets from the Sahar organization. To gain access to the model weights, you must fill out a request form. This process ensures compliance with ethical guidelines and privacy requirements.

🔗 **[Request Model Weights Access Form](https://forms.gle/8YEmXQiSvHxEJsmw8)**


## 📂 Project Structure

This repository is organized into two main subdirectories, one for each language:

*   **`Mental-Health-Models-Arabic/`**: Contains all the code, models, and documentation for the Arabic language models.
*   **`Mental-Health-Models-Hebrew/`**: Contains all the code, models, and documentation for the Hebrew language models.
