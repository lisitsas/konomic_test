import pytest
import requests
import logging
import string

logger = logging.getLogger("test")

baseUrl = 'https://habr.com/kek/v2'


def test_get_habr_main_page():
    url = 'https://habr.com/'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=url, headers=headers, auth=None)
    logging.info(response.content)
    assert response.status_code == 200


def test_get_habr_search_page():
    url = 'https://effect.habr.com/a'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=url, headers=headers, auth=None)
    logging.info(response.content)
    assert response.status_code == 200


@pytest.mark.parametrize('searchInput', [string.ascii_letters,
                                         string.ascii_uppercase,
                                         string.ascii_lowercase,
                                         string.digits,
                                         string.hexdigits,
                                         string.octdigits,
                                         string.punctuation,
                                         string.printable,
                                         string.whitespace,
                                         '',
                                         ' ',
                                         '❤'])
@pytest.mark.parametrize('order', ['relevance', 'date', 'rating'])
def test_get_habr_search_by_articles(searchInput, order):
    url = f'/articles/?query={searchInput}&order={order}&fl=ru&hl=ru&page=1&perPage=20'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=(baseUrl+url), headers=headers, auth=None)
    assert response.status_code == 200
    logging.info(response.json())


@pytest.mark.parametrize('searchInput', [string.ascii_letters,
                                         string.ascii_uppercase,
                                         string.ascii_lowercase,
                                         string.digits,
                                         string.hexdigits,
                                         string.octdigits,
                                         string.punctuation,
                                         string.printable,
                                         string.whitespace,
                                         '',
                                         ' ',
                                         '❤'])
@pytest.mark.parametrize('order', ['relevance', 'date', 'rating'])
def test_get_habr_search_by_hubs(searchInput, order):
    url = f'/hubs/search?q={searchInput}&target_type=hubs&order={order}&page=1'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=(baseUrl+url), headers=headers, auth=None)
    assert response.status_code == 200
    logging.info(response.json())


@pytest.mark.parametrize('searchInput', [string.ascii_letters,
                                         string.ascii_uppercase,
                                         string.ascii_lowercase,
                                         string.digits,
                                         string.hexdigits,
                                         string.octdigits,
                                         string.punctuation,
                                         string.printable,
                                         string.whitespace,
                                         '',
                                         ' ',
                                         '❤'])
@pytest.mark.parametrize('order', ['relevance', 'date', 'rating'])
def test_get_habr_search_by_companies(searchInput, order):
    url = f'/companies/search?q={searchInput}&target_type=companies&order={order}&page=1'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=(baseUrl+url), headers=headers, auth=None)
    assert response.status_code == 200
    logging.info(response.json())


@pytest.mark.parametrize('searchInput', [string.ascii_letters,
                                         string.ascii_uppercase,
                                         string.ascii_lowercase,
                                         string.digits,
                                         string.hexdigits,
                                         string.octdigits,
                                         string.punctuation,
                                         string.printable,
                                         string.whitespace,
                                         '',
                                         ' ',
                                         '❤'])
@pytest.mark.parametrize('order', ['relevance', 'date', 'rating'])
def test_get_habr_search_by_users(searchInput, order):
    url = f'/users/search?q={searchInput}&target_type=users&order={order}&page=1'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=(baseUrl+url), headers=headers, auth=None)
    assert response.status_code == 200
    logging.info(response.json())


@pytest.mark.parametrize('searchInput', [string.ascii_letters,
                                         string.ascii_uppercase,
                                         string.ascii_lowercase,
                                         string.digits,
                                         string.hexdigits,
                                         string.octdigits,
                                         string.punctuation,
                                         string.printable,
                                         string.whitespace,
                                         '',
                                         ' ',
                                         '❤'])
@pytest.mark.parametrize('order', ['relevance', 'date', 'rating'])
def test_get_habr_search_by_comments(searchInput, order):
    url = f'/comments/search?q={searchInput}&target_type=comments&order={order}&fl=ru&hl=ru&page=1'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        url=(baseUrl+url), headers=headers, auth=None)
    assert response.status_code == 200
    logging.info(response.json())
