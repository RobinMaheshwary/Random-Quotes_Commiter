import requests
import base64
import time
import json
from token_1 import api_ninja_key


# Define a function to get a random quote and write it to a file
def get_random_quote_and_write_to_file():
    api_key = api_ninja_key  # Replace with your actual API key
    api_url = 'https://api.api-ninjas.com/v1/quotes'

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        quote_data = response.json()

        # Check if the response is a list and contains at least one item
        if isinstance(quote_data, list) and len(quote_data) > 0:
            # Access the first item in the list
            first_quote = quote_data[0]

            # Check if the expected keys are present in the item
            if 'quote' in first_quote and 'author' in first_quote:
                quote = f'"{first_quote["quote"]}" - {first_quote["author"]}'
                
                # Write the quote to a file
                with open('Quotes.txt', 'a') as file:
                    file.write(quote + '\n')
            else:
                print('Unexpected response format from the API')
        else:
            print('Empty or unexpected response format from the API')
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # No return statement needed as we're writing directly to a file

while True:
    get_random_quote_and_write_to_file()
    print('Random quote written to file')
    time.sleep(8640)
