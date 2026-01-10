# Indian Kanoon API Demo (All Official Endpoints)

This repository contains a Jupyter Notebook demo that demonstrates how to use the official Indian Kanoon API endpoints to search for court decisions, retrieve documents, fetch original court copies, extract document fragments (snippets), and obtain document metadata.

The notebook is intended as a stakeholder-friendly demo: it shows how to authenticate with an API token, call endpoints, convert HTML responses to plain text, save responses to disk, and extract short evidence snippets for human review.

**Files**

- [indian_kanoon_api_demo.ipynb](indian_kanoon_api_demo.ipynb) — primary demo notebook. It contains runnable Python cells that call the API, parse responses, save results, and print concise previews.

**Key Endpoints Covered**

- `GET/POST /search/` — search by `formInput` and other filters (pagenum, doctypes, date ranges, etc.).
- `POST /doc/<docid>/` — fetch processed document content.
- `POST /origdoc/<docid>/` — fetch the original court copy (HTML/plaintext).
- `POST /docfragment/<docid>/` — fetch fragments/snippets for a query within a document.
- `POST /docmeta/<docid>/` — fetch document metadata (title, court, date, judges, citation, etc.).

Note: The notebook attempts `POST` by default (as the API expects), and gracefully falls back to `GET` for `/search/` if the server rejects `POST` with 405.

Getting Started
---------------

Prerequisites

- Python 3.8+ (recommended)
- Jupyter / JupyterLab or another IPython-compatible environment

Install the lightweight Python dependencies used in the notebook (the notebook also installs them automatically):

```bash
pip install requests pandas lxml beautifulsoup4
```

Configure your API token

1. Open `indian_kanoon_api_demo.ipynb` in Jupyter.
2. Locate the cell that defines `IK_TOKEN` and replace the placeholder with your API token:

```python
IK_TOKEN = "<input your token here, and remove the angle brackets>"
```

The notebook uses `HEADERS` with `Authorization: Token <IK_TOKEN>` for all API calls.

Running the demo
----------------

1. Start Jupyter and open `indian_kanoon_api_demo.ipynb`.
2. Run cells sequentially. The notebook demonstrates:
	- Installing dependencies (first cell)
	- Helper functions (`ik_get`, `ik_post`, `ik_request`, HTML to text)
	- Searching cases with `search_cases()` and auto-extracting `docid`s
	- Fetching `/doc/`, `/origdoc/`, `/docfragment/`, and `/docmeta/`
	- Saving JSON and plain-text outputs to the working directory

The notebook contains example queries (e.g., `Article 21 privacy`) and shows how to preview saved outputs.

Output files
------------

When run, the notebook saves JSON and text artifacts using descriptive names like:

- `search_response.json`
- `doc_<docid>.json`
- `doc_<docid>_plain.txt`
- `origdoc_<docid>_plain.txt`
- `docfragment_<docid>.json`
- `docmeta_<docid>.json`

Examples and usage notes
------------------------

- To run a search: call `search_cases("your query", pagenum=0)` from the notebook. The function accepts additional filters (`doctypes`, `fromdate`, `todate`, `maxcites`, `maxpages`, etc.).
- To fetch a document: use `get_document(docid)`; to fetch the original court copy use `get_origdoc(docid)`.
- To extract evidence snippets for a stakeholder question, use `get_doc_fragments(docid, query)` and then convert HTML to text using the notebook helper `html_to_text()`.

Security and token handling
--------------------------

- Keep your `IK_TOKEN` secret. Do not commit it to git or share it publicly.
- The notebook asserts that `IK_TOKEN` is set before making calls.

Troubleshooting
---------------

- HTTP 401 Unauthorized: verify your token and that it is active.
- HTTP 405 on `/search/` POST: the notebook will fallback to a `GET` request automatically. If you see other HTTP errors, inspect the printed response (the notebook prints the first part of the response on error).
- Slow responses / timeouts: the notebook uses a 60-second timeout for requests; increase `timeout` where necessary in helper functions.
