#!/usr/bin/env python3
"""
10. Change school topics

Write a Python function that returns the list of school
having a specific topic:
    - Prototype: `def schools_by_topic(mongo_collection, topic):`
    - `mongo_collection` will be the `pymongo` collection object
    - `topic` (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """creturns the list of school having a specific topic"""
    # Find all documents in the collection with the specified topic
    cursor =  mongo_collection.find({'topics': {'$in': [topic]}})
    
    # Create a list of school names from the cursor
    schools_list = [doc['name'] for doc in cursor]
    
    return schools_list