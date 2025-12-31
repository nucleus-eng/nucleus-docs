import streamlit as st
import chromadb
from chromadb.config import Settings
import anthropic

client = anthropic.Anthropic()

def load_chroma():
    """Load the Chroma database."""
    chroma_client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_db",
        anonymized_telemetry=False
    ))
    return chroma_client.get_collection(name="docs")

def retrieve_chunks(query: str, collection, k: int = 5) -> list[dict]:
    """Find relevant chunks for a query."""
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    
    chunks = []
    if results and results['documents']:
        for i, doc in enumerate(results['documents'][0]):
            chunks.append({
                'text': doc,
                'source': results['metadatas'][0][i].get('source', 'unknown')
            })
    
    return chunks

st.set_page_config(page_title="Synthetic Cell Doc Agent", layout="wide")

st.title("📚 Synthetic Cell Documentation Agent")
st.markdown("Ask questions about the synthetic cell processes documentation.")

# Load database
with st.spinner("Loading documentation database..."):
    collection = load_chroma()

st.success("Documentation database loaded")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input("Ask a question about the documentation...")

if user_query:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Retrieve relevant chunks
    chunks = retrieve_chunks(user_query, collection, k=5)
    
    if not chunks:
        st.warning("No relevant documentation found.")
    else:
        # Build context from chunks
        context = "\n\n".join([
            f"[From {c['source']}]\n{c['text']}"
            for c in chunks
        ])
        
        # Get response from Claude
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                message = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=2000,
                    messages=[
                        {
                            "role": "user",
                            "content": f"""You are an expert on synthetic cell research. Answer the question based on this documentation:

{context}

Question: {user_query}"""
                        }
                    ]
                )
            
            response_text = message.content[0].text
            st.markdown(response_text)
            
            # Show sources
            with st.expander("📖 Sources"):
                for chunk in chunks:
                    st.write(f"- {chunk['source']}")
        
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This agent answers questions about synthetic cell research documentation.
    
    It retrieves relevant sections and generates answers based on your docs.
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()