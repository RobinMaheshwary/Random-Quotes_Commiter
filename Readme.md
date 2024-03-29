# Random Quotes Writer/Commiter

This project is a Python script that fetches random quotes from an API and writes them to a text file and then it is commited to my github repository.


## How it works

The script uses the `requests` library to send a GET request to the API. The API returns a JSON response with a list of quotes. The script then extracts the first quote from the list and writes it to a file named `Quotes.txt`. Then `commiter.py` auto commit it my github repository.

The script runs in a loop, fetching a new quote and writing it to the file every 10 seconds.

## Usage

To run the script, you need Python 3 and the `requests` library installed on your machine. You can install `requests` using pip:

```bash
pip install requests
```

Then, you can run the script using the following command:

```bash
python codeGenerator.py
```
This will start the script and it will begin fetching quotes and writing them to the Quotes.txt file.

Then, open new terminal window and run following command:

```bash
python commiter.py
```

This command will auto commit the changes to github every 30 minutes.
