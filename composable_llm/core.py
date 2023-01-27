"""."""
import argparse
from document_search import DocumentLoader, LSASearchEngine
from chatbot import GPT3Model


def core(search, chatbot, question):
    context = search.search(question)
    response = chatbot.ask(context, question)
    return response


def main():
    """Main functionality of core module"""
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('-s', '--api_secret', help='secret api key for openai', required=True)
    parser.add_argument('-d', '--documents_path', help='path to a directory of documents', default=None)
    parser.add_argument('-f', '--file_path', help='path to a document file', default=None)
    parser.add_argument('-u', '--url_path', help='path to a url for a document', default=None)
    parser.add_argument('-q', '--question', help="question for the model", default=None)

    # Parse the arguments
    args = parser.parse_args()

    # Create the models
    doc_loader = DocumentLoader()
    doc_loader.load_documents(documents_path=args.documents_path,
                              file_path=args.file_path, url_path=args.url_path)
    search = LSASearchEngine(docs=doc_loader.docs[0], n_components=5)
    search.fit()
    chatbot = GPT3Model(args.api_secret)

    # Use the model
    if args.question is None:
        question = input("What question do you have for the model? (Type Q or Quit to quit)\n").lower()
        while question not in ("q", "quit"):
            core(search, chatbot, question)
    else:
        core(search, chatbot, args.question.lower())


if __name__ == '__main__':
    main()
