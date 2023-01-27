import os
import re
import urllib.request

from bs4 import BeautifulSoup

from typing import List


# TODO: add context splitting on docs


def clean_text(func):
    """Remove punctuation and lowercase each word"""

    def wrapper(*args, **kwargs):
        documents = func(*args, **kwargs)
        cleaned_doc = []
        for doc in documents:
            doc = doc.strip()
            doc = re.sub(r'[^\w\s]', '', doc)
            doc = doc.lower()
            cleaned_doc.append(doc)
        return cleaned_doc

    return wrapper


class DocumentLoader:
    def __init__(self):
        self.docs = []

    def _add_document(self, file):
        if file.endswith(".csv"):
            self.docs.append(self.load_csv(file))
        elif file.endswith(".txt"):
            self.docs.append(self.load_txt(file))
        elif file.endswith(".html"):
            self.docs.append(self.load_html(file))

    def load_documents(self, documents_path=None, file_path=None, url_path=None):
        # TODO: confirm that files exist
        if documents_path is not None:
            for file in os.listdir(documents_path):
                self._add_document(file)
        elif file_path is not None:
            self._add_document(file_path)
        elif url_path is not None:
            self.docs.append(self._parse_html(url_path, is_url=True))

    @clean_text
    def load_txt(self, file_path: str) -> List[str]:
        """Load a .txt file and return a list of lines"""
        return self._parse_lines(file_path)

    @clean_text
    def load_csv(self, file_path: str) -> List[str]:
        """Load a .csv file and return a list of lines"""
        return self._parse_lines(file_path)

    @clean_text
    def load_html(self, file_path: str) -> List[str]:
        """Load a .html file and return a list of paragraphs"""
        return self._parse_html(file_path)

    @clean_text
    def parse_url(self, url: str) -> List[str]:
        """Load a webpage from an url and return a list of paragraphs"""
        return self._parse_html(url, is_url=True)

    @staticmethod
    def _parse_lines(file_path: str) -> List[str]:
        """parse lines of a text or csv file"""
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines

    @staticmethod
    def _parse_html(file_path: str, is_url=False) -> List[str]:
        """parse paragraph tags of a html file or url"""
        if is_url:
            with urllib.request.urlopen(file_path) as response:
                soup = BeautifulSoup(response, 'html.parser')
        else:
            with open(file_path, 'r') as file:
                soup = BeautifulSoup(file, 'html.parser')
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        return paragraphs
