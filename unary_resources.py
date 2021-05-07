import json
import unary_pb2

def read_database():
    feature_list = []
    with open("book_db.json") as db:
        for item in json.load(db):
            feature = unary_pb2.Book(
                    id=item["id"],
                    title=item["title"],
                    author=item["author"],
                    first_sentence=item["first_sentence"],
                    year_published=item["year_published"])
            feature_list.append(feature)
    return feature_list