from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

doc_loader = PyPDFLoader(
    "/Users/patel/MyDrive/Study/Langchain_Learning/Code/langchain-textsplitter/length_based_splitting/sample_fake_resume.pdf"
)

doc = doc_loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=""    
)

doc_chunks = text_splitter.split_documents(doc)

print(len(doc_chunks))

print(doc_chunks[0].page_content)