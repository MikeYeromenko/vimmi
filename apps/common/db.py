from pymongo import MongoClient

__all__ = ["db"]


db = MongoClient(username="root", password="password")
