from dotenv import load_dotenv
import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.file import PDFReader
from llama_index.core import Settings

load_dotenv()


# PDF Reader with `SimpleDirectoryReader`
parser = PDFReader()
file_extractor = {".pdf": parser}


# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader(
        "./data", file_extractor=file_extractor
    ).load_data(show_progress=True)

    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()

while True:
    query = input("Query: ")
    response = query_engine.query(query)
    print(response)
