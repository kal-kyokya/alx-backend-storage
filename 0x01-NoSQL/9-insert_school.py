#!/usr/bin/env python
"""
'9-insert_school' contains a function inserting a document into a collection
"""


def insert_school(mongo_collection, **kwargs):
    """Adds a document to a MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection to be processed.
        **kwargs: The attributes constituting the to-be-added document

    Return:
        The new document's ID.
    """
    attributes = {key: value for key, value in kwargs.items()}
    doc = mongo_collection.insert_one(attributes)
    return (doc.inserted_id)
