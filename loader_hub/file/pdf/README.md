# PDF Loader

This loader extracts the text from a local PDF file using the `PyPDF2` Python package. Any non-text elements are ignored. A single local file is passed in each time you call `load_data`.

## Usage

To use this loader, you need to pass in a `Path` to a local file.

```python
from pathlib import Path
from gpt_index import download_loader

PDFReader = download_loader("PDFReader")

loader = PDFReader()
documents = loader.load_data(file=Path('./article.pdf'))
```

This loader is designed to be used as a way to load data into [GPT Index](https://github.com/jerryjliu/gpt_index/tree/main/gpt_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent. See [here](https://github.com/emptycrown/llama-hub/tree/main) for examples.
