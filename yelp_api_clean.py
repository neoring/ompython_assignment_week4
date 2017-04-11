import json
import requests
import urllib
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from urllib.parse import urlencode

def yelp_search(location):

	# OAuth credential placeholders that must be filled in by users.
	CLIENT_ID = os.environ['YELP_CLIENT_ID']
	CLIENT_SECRET = os.environ['YELP_CLIENT_SECRET']

	# API constants, you shouldn't have to change these.
	API_HOST = 'https://api.yelp.com'
	SEARCH_PATH = '/v3/businesses/search'
	TOKEN_PATH = '/oauth2/token'
	GRANT_TYPE = 'client_credentials'

	#Sets variables to fetch the bearer_token
	token_url = '{0}{1}'.format(API_HOST, TOKEN_PATH)
	data = urlencode({
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'grant_type': GRANT_TYPE,
	})
	token_headers = {
		'content-type': 'application/x-www-form-urlencoded',
	}

	# Actually getting the token and filtering out the important part
	response = requests.request('POST', token_url, data=data, headers=token_headers)
	bearer_token = response.json()['access_token']

	# Set variables for search function and run search request
	search_url = '{0}{1}'.format(API_HOST, SEARCH_PATH)

	search_headers = {
		'Authorization': 'Bearer %s' % bearer_token,
	}

	params = {
		'term': 'food',
		'lang': 'en',
		'location': location,
		'limit': 3,
	}
	 
	# Actually running the search and filtering results
	response = requests.request('GET', search_url, headers=search_headers, params=params).json()	

	for business in response['businesses']:
		print(business['name'], business['display_phone'], business['location']['display_address'][0])

	return response