"""This module conatin all route method"""

import json
from flask import request, redirect
from Database import db
from url_shortner import app, domain_name
from url_shortner.shorten_url import get_long_url, generate_decoded_hashed_key


@app.route('/', methods=['POST'])
def create_shorten_url():

    """Create long url"""

    long_url = json.loads((request.data).decode('utf-=8'))

    if db.is_document_existed(long_url['long_url']):
        return {"Already document exist for url": long_url['long_url']}

    decoded_hashed_key = generate_decoded_hashed_key(long_url['long_url'])

    db.insert_document(long_url['long_url'], decoded_hashed_key)

    short_url = domain_name + decoded_hashed_key

    return {"message": short_url}


@app.route("/<hash>/", methods=['GET'])
def long_url(hash):

    """api for long_url"""

    long_url = get_long_url(hash)

    if long_url.startswith("http") or long_url.startswith("https"):
        return redirect(long_url)

    url = f'http://{long_url}'

    return redirect(url)
