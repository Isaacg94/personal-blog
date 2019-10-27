import urllib.request,json
from .models import Quote


# Getting the movie base url
base_url = None


def configure_request(app):
    base_url = app.config['QUOTE_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quote_results_list)


    return quote_results


def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []

    for quote_item in quote_list:
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')
    
        quote_object = Quote(author,id,quote,permalink)
        quote_results.append(quote_object)

    return quote_results