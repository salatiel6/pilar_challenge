import json
import pytest
import sys
sys.path.insert(1, "../")

from controllers import app # noqa
from controllers.exceptions import BodyKeysError, WordsListError, \
    KeysValuesTypesError, OrderValueError # noqa


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_vowel_count_with_missing_keys(client):
    """
    Testing the vowel_count route with an invalid body
    It must throw BodyError exception
    """
    url = "/vowel_count"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "asdf": 1234
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": BodyKeysError("words").message}


def test_vowel_count_with_invalid_words(client):
    """
    Testing the vowel_count route with invalid words
    It must throw WordsListError exception
    """
    url = "/vowel_count"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", 1, 2]
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": WordsListError().message}


def test_vowel_count_with_empty_word(client):
    """
    Testing the vowel_count route with empty word
    It must throw WordsListError exception
    """
    url = "/vowel_count"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", "empty", "", "word"]
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": WordsListError().message}


def test_vowel_count_with_invalid_type(client):
    """
    Testing the vowel_count route with invalid types
    It must throw WordsListError exception
    """
    url = "/vowel_count"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ""
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": KeysValuesTypesError("words").message}


def test_sort_with_missing_words_key(client):
    """
    Testing the sort route with an invalid body
    It must throw BodyError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "asdf": ["test", "case"]
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": BodyKeysError("words").message}


def test_sort_with_missing_order_key(client):
    """
    Testing the sort route missing order key
    It must throw BodyError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", "case"]
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": BodyKeysError("order").message}


def test_sort_with_invalid_words(client):
    """
    Testing the sort route with invalid words
    It must throw WordsListError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", 1, 2],
        "order": "asc"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": WordsListError().message}


def test_sort_with_empty_word(client):
    """
    Testing the sort route with empty word
    It must throw WordsListError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", "empty", "", "word"],
        "order": "desc"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": WordsListError().message}


def test_sort_with_invalid_words_type(client):
    """
    Testing the sort route with invalid types
    It must throw KeysValuesTypesError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": "",
        "order": "asc"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": KeysValuesTypesError("words").message}


def test_sort_with_invalid_order_type(client):
    """
    Testing the sort route with invalid types
    It must throw KeysValuesTypesError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", "case"],
        "order": 1
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": KeysValuesTypesError("order").message}


def test_sort_with_invalid_order_value(client):
    """
    Testing the sort route with invalid order value
    It must throw OrderValueError exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["test", "case"],
        "order": "asdf"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": OrderValueError().message}


def test_vowel_count_with_valid_input(client):
    """
    Testing the vowel_count route with valid input
    It must pass without throwing any exception
    """
    url = "/vowel_count"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["batman", "robin", "joker"]
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {
        "batman": 2,
        "robin": 2,
        "joker": 2
    }


def test_sort_asc_with_valid_input(client):
    """
    Testing the sort route with valid input
    It must pass without throwing any exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["batman", "robin", "joker"],
        "order": "asc"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {
        "result": [
            "batman",
            "joker",
            "robin"
        ]
    }


def test_sort_desc_with_valid_input(client):
    """
    Testing the sort route with valid input
    It must pass without throwing any exception
    """
    url = "/sort"
    mimetype = "application/json"

    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }

    body = {
        "words": ["batman", "robin", "joker"],
        "order": "desc"
    }

    result = client.post(url, data=json.dumps(body), headers=headers)

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {
        "result": [
            "robin",
            "joker",
            "batman"
        ]
    }
