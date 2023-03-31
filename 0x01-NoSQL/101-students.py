#!/usr/bin/env python3
"""
10. Change school topics

Write a Python function that returns the list of school
having a specific topic:
    - Prototype: `def schools_by_topic(mongo_collection, topic):`
    - `mongo_collection` will be the `pymongo` collection object
    - `topic` (string) will be topic searched
"""


def top_students(mongo_collection):
    '''
    # Define the pipeline to calculate the average score and sort by it
    # Execute the pipeline and return the results
    '''
    pipeline = [
        {
            '$project': {
                'name': 1,
                'scores': 1,
                'averageScore': { '$avg': '$scores' }
            }
        },
        {
            '$sort': { 'averageScore': -1 }
        }
    ]
    return mongo_collection.aggregate(pipeline)