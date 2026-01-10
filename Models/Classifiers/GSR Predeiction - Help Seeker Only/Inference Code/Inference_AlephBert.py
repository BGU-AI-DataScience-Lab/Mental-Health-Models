from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Define the model name and load the tokenizer
model_name = 'onlplab/alephbert-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the base model architecture
bert_model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Load your saved weights (replace 'path_to_weights.pth' with the actual path)
state_dict = torch.load('load the path of the model_weights_anon_original.pth')

# Load the weights into the model
bert_model.load_state_dict(state_dict)  # Set strict=False to ignore mismatched keys

# Move the model to the appropriate device (GPU if available)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
bert_model = bert_model.to(device)

# Set the model to evaluation mode
bert_model.eval()

# Start a while loop to check sentences
print("Enter a sentence to check (or type 'סיים' to quit):")

while True:
    sentence = input("Sentence: ")
    if sentence.lower() == 'סיים':
        break

    # Tokenize the input
    inputs = tokenizer(sentence, return_tensors="pt")

    # Move inputs to the same device as the model
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Get the model's predictions
    with torch.no_grad():
        outputs = bert_model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()

    # Interpret the result (assuming binary classification: 0 = Not Suicidal, 1 = Suicidal)
    result = "Suicidal" if prediction == 1 else "Not Suicidal"
    print(f"The model predicts: {result}\n")