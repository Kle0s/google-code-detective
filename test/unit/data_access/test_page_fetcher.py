from requests import Response, HTTPError
from pytest import raises
from unittest.mock import Mock, patch
from gcd.data_access.page_fetcher import PageFetcher


def test_raise_for_status():
    response = Mock(Response)
    response.raise_for_status = lambda: (_ for _ in ()).throw(HTTPError('unit-test'))

    with patch("requests.get", return_value=response):
        fetcher = PageFetcher()
        with raises(HTTPError):
            fetcher.fetch("http://cnn.com")
