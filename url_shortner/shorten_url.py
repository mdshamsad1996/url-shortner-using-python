"""shorten url method"""

import bcrypt
from Database import db


def get_long_url(hashed_key):

    """"Get short url by appending str"""

    long_url = db.retrieve_long_url(hashed_key)

    return long_url


def generate_hashed_key(long_url):

    """Generate hashed key of long url"""

    generate_hashed_key = bcrypt.hashpw(long_url.encode('utf-8'), bcrypt.gensalt())

    return generate_hashed_key


def get_hashed_key(long_url):

    """Get hashed key of provide url"""

    hashed_key = generate_hashed_key(long_url)

    return hashed_key


def generate_decoded_hashed_key(long_url):

    """Generate short url via a long url"""

    hashed_key = get_hashed_key(long_url)

    first_sev_digit_key = hashed_key[0:7]

    decoded_hashed_key = first_sev_digit_key.decode("utf-8")

    return decoded_hashed_key
