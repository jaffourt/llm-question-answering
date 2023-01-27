# llm-question-answering
llm-question-answering is a simple Python project that answers questions using a LLM, with an added feature 
that it uses semantic search across user provided documents used to provide specific context to the LLM.

This python project uses the following technologies by default:
- openai, beautifulsoup, and scikit-learn for the core features of the model
- MkDocs for documentation
- GitHub Actions for continuous integration
- flake8, mypy, and pylint for linting
- pytest for unit testing and integration testing
- Docker for creating containerized applications

## Installation
To install [PROJECT_NAME], run the following command:

```shell
python setup.py install
```

## Usage
An example of using the python API:

```python
import os
from composable_llm import DocumentLoader, LSASearchEngine, GPT3Model

question = "What is a commonality of wealth distribution between developed nations?"

# Create the models
doc_loader = DocumentLoader()
doc_loader.load_documents(file_path='.data/wiki-dow.html')
search = LSASearchEngine(docs=doc_loader.docs[0], n_components=5)
search.fit()
chatbot = GPT3Model(os.getenv("OPENAI_API_KEY"))

# Use the core features
context = search.search(question)
response = chatbot.ask(context, question)
print(response)
```

An example of interacting with the python module using a CLI
```shell
PYTHONPATH=./ python composable_llm/core.py -s $OPENAI_API_KEY -f ./data/wiki-dow.html
```

## Contributing
We welcome contributions to [PROJECT_NAME]! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

License
llm-question-answering is released under the [MIT License](LICENSE).

## Generating Documentation

From the root directory run:

```shell
mkdocs build
```