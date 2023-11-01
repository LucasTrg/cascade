from abc import abstractmethod
from typing import Any, List


class Lake:
    """Lakes are data sources abstraction. They aim at providing interfaces for links to build their RAG prompts with."""

    @abstractmethod
    def query(self, query: Any, **kwargs):
        raise NotImplementedError


class ChromaLake(Lake):
    """ChromaLake is a lake that uses ChromaDB as a data source."""

    # TODO auth for remote chromadb
    def __init__(self, path: str = None, host: str = None, port: int = 8000) -> None:

        if path and host:
            raise ValueError("Chroma is either local or remote, not both.")

        chromadb = __import__("chromadb")

        if path:
            try:
                self.client = chromadb.PersistentClient(path=path)
            except Exception as e:
                raise SystemError("Couldn't load local Chroma: " + repr(e))

        elif host:
            try:
                self.client = chromadb.HttpClient(host=host, port=port)
            except Exception as e:
                raise ConnectionAbortedError(
                    "Couldn't connect to remote Chroma: " + repr(e)
                )
        else:
            self.client = chromadb.Client()

    def query(
        self, query: List[str], n_results: int, collection_name: str, embedding_fn=None
    ):
        """Queries a chromadb collection and retrieves n results.

        Args:
            query (List[str]): List of strings to query
            n_results (int): Number of results to retrieve for each query
            collection_name (str): Name of the collection to query
            embedding_fn (fn, Callable[str, float]): Embeddings function to use. Defaults to None.

        Raises:
            FileNotFoundError: _description_
        """
        try:
            collection = self.client.get_collection(collection_name)
            collection.query(
                query_texts=query, n_results=n_results, embedding_fn=embedding_fn
            )
        except Exception as e:
            raise FileNotFoundError("Couldn't find collection: " + repr(e))

    ## TODO add method to populate the db from raw texts or from pre-computed embeddings
