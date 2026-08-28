"""Step 4: Store chunk embeddings in FAISS so we can search them later."""

import os

from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model


# ============================================================
# Build Vector Store
# ============================================================

def build_vector_store(chunks):
    """Embed every chunk and build a searchable FAISS index in memory."""
    
    embeddings_model = get_embeddings_model()

    return FAISS.from_documents(
        chunks,
        embeddings_model
    )


# ============================================================
# Save Vector Store
# ============================================================

def store_vector_store(
    vector_store,
    path: str = config.VECTOR_STORE_PATH
) -> None:
    """Save the FAISS index to disk."""
    
    vector_store.save_local(path)


# ============================================================
# Load Vector Store
# ============================================================

def load_vector_store(
    path: str = config.VECTOR_STORE_PATH
):
    """Load a previously saved FAISS index from disk."""
    
    embeddings_model = get_embeddings_model()

    return FAISS.load_local(
        path,
        embeddings_model,
        allow_dangerous_deserialization=True
    )


# ============================================================
# Check if Vector Store Exists
# ============================================================

def vector_store_exists(
    path: str = config.VECTOR_STORE_PATH
) -> bool:
    """Check if a FAISS index already exists on disk."""
    
    return os.path.exists(
        os.path.join(path, "index.faiss")
    )


# ============================================================
# Get Retriever
# ============================================================

def get_retriever(
    vector_store,
    k: int = config.TOP_K_RESULTS
):
    """Turn a vector store into a retriever that returns top-k chunks."""
    
    return vector_store.as_retriever(
        search_kwargs={"k": k}
    )