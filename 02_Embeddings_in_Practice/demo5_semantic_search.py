# Demo 5: Semantic Search using Cosine Similarity

from openai import OpenAI
from dotenv import load_dotenv
import math

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.

# TODO: Create an instance named "client" for the gpt model.
# Set the value for the api_key to the environment variable OPENAI_API_KEY defined in the .env file. 


# -----------------------------
# Step 1: Document Corpus
# -----------------------------
# TODO: Define a list named "documents" that has 4-5 documents to embed and search.


# -----------------------------
# Step 2: Generate Embeddings
# -----------------------------
# TODO: Invoke the LLM using client.embeddings.create() to embed the documents
# Set the parameters for model and input (documents).
# Use the text-embedding-3-small model from the environment variable.
# Capture the response in a variable named "response".


# Create vector store
vector_store = []

for i, emb in enumerate(response.data):
    # TODO: Append each embedding in the vector store.
    # Set: id, the original document text and the embedding.


# -----------------------------
# Step 3: Cosine Similarity Function
# -----------------------------
def cosine_similarity(vec1, vec2):
    # Dot product of two vectors
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    
    # Magnitude of vectors
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    
    # Cosine similarity formula
    return dot_product / (magnitude1 * magnitude2)

# -----------------------------
# Step 4: Query Input
# -----------------------------
query = "How does AI help in supply chain?"
# query = "inventory optimization using AI"
# query = "customer service automation with chatbots"
# query = "pricing strategy using analytics"

# TODO: Invoke the LLM using client.embeddings.create() to embed the query.
# Set the parameters for model and input (query).
# Use the text-embedding-3-small model from the environment variable.
# Capture the response in a variable named "query_response".



query_embedding = query_response.data[0].embedding

# -----------------------------
# Step 5: Compute Similarity
# -----------------------------
results = []

for item in vector_store:
    similarity = cosine_similarity(query_embedding, item["embedding"])
    
    results.append({
        "text": item["text"],
        "similarity": similarity
    })

# -----------------------------
# Step 6: Sort Results
# -----------------------------
results = sorted(results, key=lambda x: x["similarity"], reverse=True)

# -----------------------------
# Step 7: Display Results
# -----------------------------
print("\n Query:", query)
print("\nTop Matches:\n")

for result in results:
    print(f"Score: {result['similarity']:.4f}")
    print(f"Text: {result['text']}")
    print("-" * 50)

# TODO: Print the score and text for only the top 2 results.
