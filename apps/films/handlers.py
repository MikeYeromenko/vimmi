from typing import Dict, List

from pymongo import InsertOne

from apps.common.db import db
from apps.common.utils import export_to_csv


__all__ = ["films_handler"]


class FilmsHandler:
    """Handler for serving films requests."""

    def __init__(self, db_name: str = "vimmi"):
        self.col = "films"
        self.db = db[db_name]
        self.conn = self.db[self.col]

    def get_average_imb_rating_top_10(self) -> Dict:
        pipeline = [
            {"$sort": {"imDbRating": -1}},
            {"$limit": 10},
            {
                "$group": {
                    "_id": None,
                    "avg_rate": {"$avg": {"$toDouble": "$imDbRating"}},
                }
            },
            {"$project": {"_id": 0, "avg_rate": 1}},
        ]
        cursor = self.conn.aggregate(pipeline=pipeline)
        result = [item for item in cursor][0]
        return result

    def get_top50_films_ranges(self) -> Dict:
        pipeline = [
            {"$sort": {"imDbRating": -1}},
            {"$limit": 50},
            {
                "$group": {
                    "_id": None,
                    "min_year": {"$min": {"$toInt": "$year"}},
                    "max_year": {"$max": {"$toInt": "$year"}},
                }
            },
            {"$project": {"_id": 0, "min_year": 1, "max_year": 1}},
        ]
        cursor = self.conn.aggregate(pipeline=pipeline)
        result = [item for item in cursor][0]
        return result

    def _get_group_by_ten(self, skip: int) -> List[Dict]:
        quantity_docs = self.conn.count_documents({})
        result = []
        for i in range(0, quantity_docs, skip):
            pipeline = [
                {"$sort": {"imDbRating": -1, "year": -1}},
                {"$skip": i},
                {"$limit": 10},
                {
                    "$facet": {
                        "first": [{"$project": {"_id": 0, "title": 1}}, {"$limit": 1}],
                        "second": [
                            {
                                "$group": {
                                    "_id": None,
                                    "avg_rate": {"$avg": {"$toDouble": "$imDbRating"}},
                                    "avg_year": {"$avg": {"$toInt": "$year"}},
                                }
                            }
                        ],
                    }
                },
                {
                    "$addFields": {
                        "title": {"$first": "$first.title"},
                        "avg_rating": {"$first": "$second.avg_rate"},
                        "avg_year": {"$first": "$second.avg_year"},
                    }
                },
                {"$project": {"title": 1, "avg_rating": 1, "avg_year": 1}},
            ]
            cursor = self.conn.aggregate(pipeline=pipeline)
            result.append([item for item in cursor][0])
        return result

    def group_by_ten_and_export_to_csv(self, skip: int = 10) -> None:
        data = self._get_group_by_ten(skip=skip)
        export_to_csv(data=data)

    def _save_data_in_the_db(self, data: List[Dict], collection_name: str = "task_4"):
        write_operations = [InsertOne(document=document) for document in data]
        result = self.db[collection_name].bulk_write(requests=write_operations)
        print(result)

    def get_data_and_save(self, skip: int = 10):
        data = self._get_group_by_ten(skip=skip)
        self._save_data_in_the_db(data=data)


films_handler = FilmsHandler()
