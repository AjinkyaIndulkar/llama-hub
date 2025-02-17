# Unstructured.io File Loader

This loader extracts the text from a variety of unstructured text files using [Unstructured.io](https://github.com/Unstructured-IO/unstructured). Currently, the file extensions that are supported are `.txt`, `.docx`, `.pptx`, `.jpg`, `.png`, `.eml`, `.html`, and `.pdf` documents. A single local file is passed in each time you call `load_data`.

Check out their documentation to see more details, but notably, this enables you to parse the unstructured data of many use-cases. For example, you can download the 10-K SEC filings of public companies (e.g. [Coinbase](https://www.sec.gov/ix?doc=/Archives/edgar/data/0001679788/000167978822000031/coin-20211231.htm)), and feed it directly into this loader without worrying about cleaning up the formatting or HTML tags.

## Usage

To use this loader, you need to pass in a `Path` to a local file. Optionally, you may specify `split_documents` if you want each `element` generated by Unstructured.io to be placed in a separate document. This will guarantee that those elements will be split when an index is created in GPT Index, which, depending on your use-case, could be a smarter form of text-splitting. By default this is `False`.

```python
from pathlib import Path
from gpt_index import download_loader

UnstructuredReader = download_loader("UnstructuredReader")

loader = UnstructuredReader()
documents = loader.load_data(file=Path('./10k_filing.html'))
```

You can also easily use this loader in conjunction with `SimpleDirectoryReader` if you want to parse certain files throughout a directory with Unstructured.io.

```python
from pathlib import Path
from gpt_index import download_loader

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

loader = SimpleDirectoryReader()
documents = loader.load_data('./data', file_extractor={
  ".pdf": "UnstructuredReader",
  ".html": "UnstructuredReader",
  ".eml": "UnstructuredReader",
  ".pptx": "PptxReader"
})
```

This loader is designed to be used as a way to load data into [GPT Index](https://github.com/jerryjliu/gpt_index/tree/main/gpt_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent. See [here](https://github.com/emptycrown/llama-hub/tree/main) for examples.

## Troubleshooting

**"failed to find libmagic" error**: Try `pip install python-magic-bin==0.4.14`. Solution documented here: https://github.com/Yelp/elastalert/issues/1927#issuecomment-425040424.