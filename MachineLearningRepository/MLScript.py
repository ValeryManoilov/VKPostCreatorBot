# import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from langchain.llms import huggingface_pipeline
# # from transformers import BertTokenizer, BertModel


# # dataset = pd.read_csv("dataset(test).csv")

# # dataset.columns = ["text"]

# # texts = dataset["text"].to_list()

# # train_texts, test_texts = train_test_split(texts, test_size=0.2)

# # print(len(train_texts))

from transformers import BertTokenizer, BertModel
import torch
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("dataset(test).csv")
df.columns = ["text"]
texts = df['text'].tolist()

tokenizer = BertTokenizer.from_pretrained('google-bert/bert-base-multilingual-cased')
model = BertModel.from_pretrained('google-bert/bert-base-multilingual-cased')

def get_embeddings(texts):
    inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

embeddings = get_embeddings(texts)

kmeans = KMeans(n_clusters=6) 
kmeans.fit(embeddings)
clusters = kmeans.labels_

df['cluster'] = clusters
print(df.head())

