import chromadb
from chromadb.config import Settings
import re
from pathlib import Path

def extract_text_from_markdown(content: str) -> str:
    """Clean markdown to plain text."""
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '[CODE BLOCK]', content)
    # Remove links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    # Remove markdown formatting
    content = re.sub(r'[#*_`~-]+', ' ', content)
    return content.strip()

def split_into_chunks(text: str, chunk_size: int = 500) -> list[str]:
    """Split text into chunks by word count."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks

def ingest_docs():
    """Load files from files_to_review.txt, chunk them, and store in Chroma."""
    print("Loading files from files_to_review.txt...")
    
    # Read the file list
    with open("scripts/files_to_review.txt", "r") as f:
        file_paths = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(file_paths)} files to ingest")
    
    # Initialize Chroma with explicit persistence
    chroma_client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_db",
        anonymized_telemetry=False
    ))
    
    collection = chroma_client.get_or_create_collection(
        name="docs",
        metadata={"hnsw:space": "cosine"}
    )
    
    chunk_id = 0
    
    for file_path in file_paths:
        print(f"Processing {file_path}...")
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Clean and chunk
            text = extract_text_from_markdown(content)
            chunks = split_into_chunks(text, chunk_size=500)
            
            # Store in Chroma
            for chunk in chunks:
                collection.add(
                    ids=[f"chunk_{chunk_id}"],
                    documents=[chunk],
                    metadatas=[{"source": file_path}]
                )
                chunk_id += 1
            
            print(f"  Added {len(chunks)} chunks")
        
        except FileNotFoundError:
            print(f"  ERROR: File not found - {file_path}")
        except Exception as e:
            print(f"  ERROR: {e}")
    
    # Persist the database
    chroma_client.persist()
    
    print(f"\nDone! Stored {chunk_id} total chunks in Chroma database")
    print(f"Data persisted to ./chroma_db")

if __name__ == "__main__":
    ingest_docs()