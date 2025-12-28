'''
This file saves the train-test-split into the disk to avoid leakage when doing pre-training and finetuning.
This file reads the conversations and messsages csv files and do random split stratified by label (GSR)
into: train, test, unlabeled, and pretrain (pretrain data is train+unlabeled). It saves each of these dataframes as pickle
'''
import pandas as pd
from sklearn.model_selection import train_test_split


conversations_path = "arabic_conversations.csv"
messages_path = "arabic_messages.csv"
ARABIC_LEXICON_PATH = "new_arabic_lexicon_17_07.csv"
TOTAL_LEXICON_CATEGORIES = 47
LEXICON_ARABIC_PHRASE_COLUMN = "Arabic Phrase (Linor Translation / Approval)"

MODEL_NAME = "aubmindlab/bert-large-arabertv02"


test_size = 0.3
seed = 358


lexicon_df = pd.read_csv(ARABIC_LEXICON_PATH)
needed_categories = ["Past suicidal history", "Family suicide history", "Suicidal ideation", "Hopelessness", "Deliberate self harm", "Perceived burdensomeness"]
lexicon_df = lexicon_df[lexicon_df.Category.isin(needed_categories)]


messages_df = pd.read_csv(messages_path)
messages_df = messages_df[messages_df['text'].notna()]

conversations_df = pd.read_csv(conversations_path)

labeled_ids = set(conversations_df.engagement_id.unique()) & set(messages_df.engagement_id.unique())

labeled_convs = conversations_df[conversations_df.engagement_id.isin(labeled_ids)]

train_conv, test_conv = train_test_split(
            labeled_convs,
            test_size=test_size,
            random_state=seed,
            stratify=labeled_convs['gsr']
)


# Split messages based on engagement_id from conversations splits
train_ids = set(train_conv['engagement_id'].values)
test_ids = set(test_conv['engagement_id'].values)


unlabeled_msgs = messages_df[~(messages_df['engagement_id'].isin(labeled_ids))]

train_msgs = messages_df[messages_df['engagement_id'].isin(train_ids)]
test_msgs = messages_df[messages_df['engagement_id'].isin(test_ids)]

pretrain_messages_df = pd.concat([unlabeled_msgs, train_msgs])

print(f"train convs: {len(train_conv)}, train msgs: {len(train_msgs)}")
print(f"test convs: {len(test_conv)}, test msgs: {len(test_msgs)}")
print(f"pretraining (unlabeled + train ) convs: {len(pretrain_messages_df.engagement_id.unique())}, pretraining (unlabeled + train ) msgs: {len(pretrain_messages_df)}")




import os
import pickle

save_dir = "./saved_objects"
os.makedirs(save_dir, exist_ok=True)

data_to_save = {
    "train_conv": train_conv,
    "test_conv": test_conv,
    "unlabeled_msgs": unlabeled_msgs,
    "train_msgs": train_msgs,
    "test_msgs": test_msgs,
    "pretrain_messages_df": pretrain_messages_df,
    
}

for name, data in data_to_save.items():
    with open(os.path.join(save_dir, f"{name}.pkl"), 'wb') as f:
        pickle.dump(data, f)