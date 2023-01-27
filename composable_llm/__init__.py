"""This is the main entry point of the module"""

# Import the required functions, classes, etc. from the module
from . import core
from .chatbot import GPT3Model
from .document_search import DocumentLoader, LSASearchEngine

# Define the API of the module
__all__ = ['core', 'GPT3Model', 'DocumentLoader', 'LSASearchEngine']
