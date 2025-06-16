import requests
import json
from typing import Optional, Union, Dict, List

class GetRequester:
    """
    A class designed to send GET requests to a specified URL and handle the response.
    It is initialized with a URL.
    """

    def __init__(self, url: str):
        """
        Initializes the GetRequester with a specific URL.

        Args:
            url (str): The string URL to which the GET requests will be made.
        """
        self.url = url

    def get_response_body(self) -> Optional[bytes]:
        """
        Sends a GET request to the URL provided during initialization.

        Returns:
            Optional[bytes]: The raw body of the response as bytes if the request is successful,
                             otherwise None.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            # Return the raw bytes of the response, as required by the test
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

    def load_json(self) -> Optional[Union[Dict, List]]:
        """
        Retrieves the response body (as bytes), decodes it, and converts it from a
        JSON string into a Python dictionary or list.

        This method utilizes the get_response_body method to send the request.

        Returns:
            Optional[Union[Dict, List]]: A Python list or dictionary from the JSON response,
                                        or None if the request fails or is not valid JSON.
        """
        body_bytes = self.get_response_body()
        if body_bytes is not None:
            try:
                # Decode the bytes into a string (using UTF-8) before parsing
                body_string = body_bytes.decode('utf-8')
                return json.loads(body_string)
            except (json.JSONDecodeError, UnicodeDecodeError):
                print("Failed to decode or parse JSON from the response.")
                return None
        return None