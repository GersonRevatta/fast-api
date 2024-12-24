from consumers.user_consumer import publish_message
from unittest.mock import patch

def test_publish_message():
    with patch("pika.BlockingConnection") as mock_connection:
        publish_message("user.created", {"id": 1, "email": "user@example.com"})
        assert mock_connection.called
