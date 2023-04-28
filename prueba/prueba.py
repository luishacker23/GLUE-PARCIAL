from unittest.mock import MagicMock, patch
import requests

def make_request(url):
    response = requests.get(url)
    return response.text

def test_make_request():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = 'Hola mundo!'

    
    mock_get = MagicMock()
    mock_get.return_value = mock_response

    # Aplicar el mock al módulo requests
    with patch('requests.get', mock_get):
                result = make_request('http://www.example.com')
    assert result == 'Hola mundo!'
