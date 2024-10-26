#!/usr/bin/env python3
"""
'8-all' Contains a function listing all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Arg:
        mongo_collection: NoSQL Collection to be processed.
    Return:
        A list of all contained documents.
    """
    docs = mongo_collection.find()
    return ([doc for doc in docs])
