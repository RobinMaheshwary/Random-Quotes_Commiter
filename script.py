import requests
from github import Github
import base64
import time
import json

# GitHub credentials and repository information
github_token = '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'
repository_name = 'RobinMaheshwary/Random-Quotes_Commiter'
github_username = 'RobinMaheshwary'
file_path = 'Quotes.txt'

# Define a function to get a random quote
def get_random_quote():
    api_key = 's/SEANwQtPUycKnbT6+ZRg==UW3k1oltpploMPgP'  # Replace with your actual API key
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
                return quote
            else:
                print('Unexpected response format from the API')
        else:
            print('Empty or unexpected response format from the API')
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Return None in case of failure
    return None


# Define a function to get the current file content from GitHub
def get_file_content():
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(f'https://api.github.com/repos/{repository_name}/contents/{file_path}', headers=headers)

    if response.status_code == requests.codes.ok:
        # Decode the base64-encoded content retrieved from GitHub
        content = base64.b64decode(response.json()['content']).decode('utf-8')
        return content
    else:
        return f"Error: {response.status_code} - {response.text}"

# Define a function to get the SHA of the file on GitHub
def get_file_sha():
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(f'https://api.github.com/repos/{repository_name}/contents/{file_path}', headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()['sha']
    else:
        return None



# Define a function to update the file content on GitHub
def update_file_content(new_content):
    headers = {'Authorization': f'token {github_token}'}
    data = {
        'message': 'Add a new quote',
        'content': base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
        'sha': get_file_sha()
    }
    response = requests.put(f'https://api.github.com/repos/{repository_name}/contents/{file_path}', headers=headers, data=json.dumps(data))
    return response.status_code == 200

# In a loop, get a random quote, get the current file content, append the quote to the content, and update the file on GitHub



while True:
    quote = get_random_quote()
    print(quote)
    content = get_file_content()
    new_content = content + '\n' + quote
    if update_file_content(new_content):
        print(f'Random quote committed: {quote}')
    else:
        print('Failed to commit the quote')
    
    time.sleep(10) 
