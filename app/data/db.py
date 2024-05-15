import json
import pprint
from app.settings import DB



def get_quotes(data_file=DB) -> list:
    try:
        with open(data_file) as f:
            quotes = json.load(f)
            return quotes
    except json.decoder.JSONDecodeError:
        print("db is empty")
        return None


def create_quote(quote: dict, data_file=DB):
    list_of_quotes: list = get_quotes(data_file)

    if list_of_quotes is None:
        list_of_quotes = []
    list_of_quotes.append(quote)

    with open(data_file, "w") as f:
        json.dump(list_of_quotes, f, indent=4)

    return True

if __name__ == "__main__":

    quote = {
        "quote": "Fault its nit wrong",
        "author": "Jeremu"
    }


    create_quote(quote, DB)

