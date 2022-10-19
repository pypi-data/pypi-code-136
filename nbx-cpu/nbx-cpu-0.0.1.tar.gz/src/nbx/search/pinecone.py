import os
from pathlib import Path
from typing import List, Tuple, Callable

import pinecone
from sentence_transformers import SentenceTransformer

from nbx.note import Note, Record

MODEL_CKPT = "flax-sentence-embeddings/all_datasets_v3_mpnet-base"
SEARCH_INDEX_NAME = "search"
TIMEOUT_SECONDS = 300


def find_match(
    query: str,
    pinecone_token: str,
    notes_dir: Path,
    fallback_func: Callable,
    top_k: int = 10
) -> Tuple[List[Record], List[Note]]:
    if pinecone_token == "":
        print("[Error] Pinecone token not set, please set with: nbx config pinecone")
        return fallback_func()

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    model = SentenceTransformer(MODEL_CKPT)
    xq = model.encode(query).tolist()

    pinecone.init(api_key=pinecone_token, environment='us-west1-gcp')
    try:
        index = pinecone.Index(SEARCH_INDEX_NAME)
        results = index.query(xq, top_k=top_k, includeMetadata=True)
    except Exception:
        print("[Warning] Indexing in progress, fall back to regex search")
        return fallback_func()

    record_ids = []
    for match in results["matches"]:
        record_ids.append(match['metadata']["record_id"])

    res_records = []
    res_notes = []
    for record_id in record_ids:
        timestamp = record_id.split("#")[0]
        record_idx = int(record_id.split("#")[1])
        note_file_path = Path(notes_dir, f"{timestamp}.json")
        note = Note(note_file_path)
        record = note.get_sections()[record_idx]
        res_records.append(record)
        res_notes.append(note)

    return res_records, res_notes


# https://www.pinecone.io/docs/examples/basic-hybrid-search/
def index_notes(notes: List[Note], pinecone_token: str) -> None:
    # get embeddings of each record
    encoder = SentenceTransformer(MODEL_CKPT)
    contents = []
    record_ids = []
    for note in notes:
        records = note.get_sections()
        for record in records:
            contents.append(record.content)
            record_ids.append(record.id)
    embeddings = encoder.encode(contents)
    # upsert to pinecone
    print("Connecting to Pinecone")
    pinecone.init(api_key=pinecone_token, environment='us-west1-gcp')
    if SEARCH_INDEX_NAME in pinecone.list_indexes():
        print("Deleting old search index")
        pinecone.delete_index(SEARCH_INDEX_NAME, timeout=TIMEOUT_SECONDS)
    print("Creating new search index")
    pinecone.create_index(
        name=SEARCH_INDEX_NAME,
        dimension=embeddings.shape[1],
        timeout=TIMEOUT_SECONDS
    )
    index = pinecone.Index(SEARCH_INDEX_NAME)
    upserts = []
    for idx, (embedding, record_id) in enumerate(zip(embeddings, record_ids)):
        upserts.append((str(idx), embedding.tolist(), {"record_id": record_id}))
    print("Upserting embeddings")
    status = index.upsert(vectors=upserts)
    upserted_count = status["upserted_count"]
    print(f"Indexed records: {upserted_count}")
