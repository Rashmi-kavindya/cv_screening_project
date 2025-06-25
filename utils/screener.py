# screener.py

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def score_cv(cv_text, job_desc):
    if not cv_text or not job_desc:
        return 0
    embeddings = model.encode([cv_text, job_desc])
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(similarity) * 100, 2)
