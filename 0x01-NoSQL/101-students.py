def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    # Pipeline for the aggregation
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    # Perform the aggregation
    return list(mongo_collection.aggregate(pipeline))
