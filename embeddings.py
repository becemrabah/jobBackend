from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    sections = text.split("\n\n")
    embeddings = [embed_model.encode(s) for s in sections]
    return sections, np.array(embeddings)

def get_relevant_sections(cv_text, job_text, top_k=3):
    cv_sections, cv_emb = embed_text(cv_text)
    job_sections, job_emb = embed_text(job_text)

    index = faiss.IndexFlatL2(cv_emb.shape[1])
    index.add(cv_emb)

    D, I = index.search(job_emb, top_k)
    relevant = [cv_sections[i] for i in I.flatten() if i < len(cv_sections)]
    return " ".join(relevant[:3])  # simple summary
