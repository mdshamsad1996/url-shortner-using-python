"""Module conatins all method for mongodb"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

mydb = client.mydb

url_col = mydb.url_col


def insert_document(long_url, short_url):

    """Insert document in url_col collection"""

    url = {
            "long_url": long_url,
            "short_url": short_url
        }
    result = mydb.url_col.insert_one(url)


def is_document_existed(long_url):

    """Is document already exist"""

    doc = url_col.find_one({"long_url": long_url})

    if doc is None:
        return False

    return True


def retrieve_long_url(short_url):

    """Retrieve long url via short url"""

    doc = url_col.find_one({"short_url": short_url})

    long_url = doc['long_url']

    return long_url
