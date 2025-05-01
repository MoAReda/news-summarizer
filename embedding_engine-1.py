from sentence_transformers import SentenceTransformer
import chromadb

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Directory to store embeddings
collection = chroma_client.get_or_create_collection(name="news_articles")

def generate_embeddings(text):
    """
    Generate embeddings for a given text.
    """
    return embedding_model.encode(text)

def store_embeddings(articles):
    """
    Store article embeddings in Chroma.
    """
    for article in articles:
        title = article["title"]
        content = article["content"] or article["description"]
        embedding = generate_embeddings(content)
        collection.add(
            documents=[content],
            metadatas=[{"title": title}],
            ids=[title]  # Use title as ID for simplicity
        )