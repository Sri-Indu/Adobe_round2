from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('/app/local_model')
 # ~90MB, offline capable

def rank_sections(sections, persona_data):
    persona_job_text = persona_data["persona"] + " " + persona_data["job"]
    persona_embedding = model.encode([persona_job_text])[0]

    section_texts = [sec["section_title"] for sec in sections]
    section_embeddings = model.encode(section_texts)

    similarities = cosine_similarity([persona_embedding], section_embeddings)[0]
    ranked = sorted(
        [
            {
                "document": sec["document"],
                "page": sec["page"],
                "section_title": sec["section_title"],
                "importance_rank": int(rank + 1)
            }
            for sec, sim, rank in zip(
                sections,
                similarities,
                np.argsort(-similarities)
            )
        ],
        key=lambda x: x["importance_rank"]
    )
    return ranked[:10]  # top 10 sections
