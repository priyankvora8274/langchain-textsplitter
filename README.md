# LangChain Text Splitters 📄

A hands-on collection of examples exploring **text splitting (chunking)** in LangChain. Text splitters break large documents into smaller pieces that are easier to embed, retrieve, and pass to large language models (LLMs), especially in **Retrieval-Augmented Generation (RAG)** pipelines.

## 📂 Repository Structure

| Folder | Technique | Best for |
|---|---|---|
| `length_based_splitting/` | Length-based splitting | Predictable chunk sizes and general-purpose documents |
| `text_structure_based_splitting/` | Text-structure-based splitting | Documents with headings, sections, or other formatting |
| `language_structure_based_splitting/` | Language-structure-based splitting | Source code and language-aware boundaries |
| `sementic_meaning_based/` | Semantic-meaning-based splitting | Grouping sentences by related meaning |

*Folder names are preserved exactly as they appear in this repository.*

## 🧩 Text Splitting Concepts

- **Chunk size:** Maximum target length of each chunk, measured in characters, tokens, or another unit depending on the splitter.
- **Chunk overlap:** Repeated content between adjacent chunks to reduce loss of context at boundaries.
- **Separators:** Boundaries such as paragraphs, newlines, spaces, headings, or code constructs.
- **Metadata:** Information such as document source or section that can help trace retrieved chunks back to their origin.

Smaller chunks can improve retrieval precision but may lose context; larger chunks preserve more context but can include irrelevant material. Overlap helps with continuity but increases storage and embedding costs.

## 🔍 Splitting Techniques

### 1. Length-Based Splitting

**How it works:** Divides text into chunks based on a chosen length. A common LangChain option is `RecursiveCharacterTextSplitter`, which tries separators in order (such as paragraphs, lines, and spaces) to keep related text together while meeting a target size.

**Use cases:** General text documents, articles, logs, and basic RAG prototypes.

**Advantages:** Simple, fast, predictable, and easy to tune with `chunk_size` and `chunk_overlap`.

**Limitations:** A fixed length does not necessarily match complete ideas; poorly chosen boundaries may separate related information.

### 2. Text-Structure-Based Splitting

**How it works:** Uses document structure, such as Markdown headings or HTML sections, to identify meaningful boundaries. For example, a Markdown header splitter can group text under its corresponding headings.

**Use cases:** Markdown documentation, HTML pages, reports, and manuals.

**Advantages:** Preserves section context and can attach heading information as metadata, improving interpretability during retrieval.

**Limitations:** Depends on consistent formatting; some sections may still be too large and require a second splitting pass.

### 3. Language-Structure-Based Splitting

**How it works:** Uses separators suited to a programming language, such as class or function boundaries, rather than splitting code purely by character count. LangChain offers language-aware recursive splitting options.

**Use cases:** Code search, repository question-answering, coding assistants, and code documentation.

**Advantages:** Better chance of keeping related code together; more useful chunks for code retrieval.

**Limitations:** Language-specific separators are not full syntax parsers, so complex or very long functions can still split awkwardly. Results depend on language support and settings.

### 4. Semantic-Meaning-Based Splitting

**How it works:** Uses embeddings to compare the meanings of nearby sentences and places boundaries where semantic similarity changes substantially. LangChain's semantic chunking approach typically requires an embedding model.

**Use cases:** Concept-heavy articles, research material, and documents where topic changes matter more than formatting.

**Advantages:** Can group conceptually related text even when paragraphs or lengths vary.

**Limitations:** More computationally expensive; chunk sizes are less predictable; quality depends on the embedding model and boundary thresholds.

## ⚖️ Quick Comparison

| Approach | Main strength | Main trade-off |
|---|---|---|
| Length-based | Easy and efficient | May cut through ideas |
| Text-structure-based | Retains document sections | Requires useful formatting |
| Language-structure-based | Respects code-oriented boundaries | Not a complete syntax-aware parser |
| Semantic-based | Follows changes in meaning | Higher embedding cost and complexity |

**Choosing a method:** Start with recursive length-based splitting for general text; prefer structure-aware splitting for well-formatted documents, language-aware splitting for code, and semantic splitting when topic boundaries are particularly important.

## 🛠️ Tech Stack

- Python
- LangChain and LangChain Text Splitters
- Embedding models (for semantic splitting)
- Optional model integrations including OpenAI, Anthropic, Google, and Hugging Face, as listed in `requirements.txt`

## 🚀 Getting Started

```bash
git clone https://github.com/priyankvora8274/langchain-textsplitter.git
cd langchain-textsplitter
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Explore the Python examples in each folder and run the desired script with `python path/to/script.py`. If an example uses a hosted embedding or chat model, configure the corresponding API key in your environment first. **Do not commit API keys or `.env` files containing secrets.**

## 💡 Example: Recursive Character Splitting

This is an **illustrative example**, not a transcription of a repository script.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "LangChain helps developers build LLM applications. " * 20

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40,
)

chunks = splitter.split_text(text)
print(f"Total chunks: {len(chunks)}")
print(chunks[0])
```

For RAG, a typical workflow is **load documents → split into chunks → create embeddings → store in a vector database → retrieve relevant chunks → generate an answer**.

## 🎯 Learning Objectives

Understand how chunking affects retrieval quality, compare length-, structure-, language-, and meaning-based strategies, and choose chunk sizes and overlap settings appropriate for different data types.

---

**Documentation note:** This README is based on the repository's verified folder structure and dependency list plus general LangChain concepts. Individual Python code comments were not accessible for review, so no specific script behavior is claimed beyond what the folder names indicate.
