# Trafilatura Website Loader

This loader is a web scraper that fetches the text from static websites using the `trafilatura` Python package.

## Usage

To use this loader, you need to pass in an array of URLs.

```python
from gpt_index import download_loader

TrafilaturaWebReader = download_loader("TrafilaturaWebReader")

loader = TrafilaturaWebReader()
documents = loader.load_data(urls=['https://google.com'])
```

## Examples

This loader is designed to be used as a way to load data into [GPT Index](https://github.com/jerryjliu/gpt_index/tree/main/gpt_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent.

### GPT Index

```python
from gpt_index import GPTSimpleVectorIndex, download_loader

TrafilaturaWebReader = download_loader("TrafilaturaWebReader")

loader = TrafilaturaWebReader()
documents = loader.load_data(urls=['https://google.com'])
index = GPTSimpleVectorIndex(documents)
index.query('What language is on this website?')
```

### LangChain

Note: Make sure you change the description of the `Tool` to match your use-case.

```python
from gpt_index import GPTSimpleVectorIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory

TrafilaturaWebReader = download_loader("TrafilaturaWebReader")

loader = TrafilaturaWebReader()
documents = loader.load_data(urls=['https://google.com'])
index = GPTSimpleVectorIndex(documents)

tools = [
    Tool(
        name="Website Index",
        func=lambda q: index.query(q),
        description=f"Useful when you want answer questions about the text on websites.",
    ),
]
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")
agent_chain = initialize_agent(
    tools, llm, agent="zero-shot-react-description", memory=memory
)

output = agent_chain.run(input="What language is on this website?")
```
