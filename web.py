from flask import Flask, render_template, request
import weather
import os
import yelp_api_clean
app = Flask(__name__)

@app.route("/")
def index():
	location = request.values.get('location')
	if location:
		yelp_results = yelp_api_clean.yelp_search(location)
	else:
		yelp_results = None
	return render_template('index.html', yelp_results=yelp_results, location=location)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port)