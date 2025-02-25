import os
from flask import Flask, request, render_template, redirect, url_for
print(os.path)

from src.model.SearchApp import SearchTerm

# creates the flask
app = Flask(__name__)

# The view function index() is linked to the main route using the app.route() decorator.
# When the main route is requested, Flask will serve the request by calling index() and using its return value as the response.

@app.route("/", methods=['GET', 'POST']) # obviously the default page.
def index():
    # search request

    if request.method == 'POST':
        query = request.form['query'].lower()

        print('querying', query)
        # query here?
        search_results = SearchTerm(query)
        
        print(search_results)
        # currently only works as array?
        return render_template('results.html', search_results=search_results, num_results=len(search_results), query=query, page_no=0, total_results=len(search_results))
    

    return render_template('main.html')


@app.route('/search', methods=['POST'])
def search_results():
    return render_template('results.html')

"""
@app.route('/search', methods=['POST'])
def my_form_post():
    query = request.form['query'].lower()
    if len(query) == 0:
        return render_template('index.html')

    print('querying', query)

    #search_results = 
    #total_results = 
    return render_template('./src/website/results.html')
    #return render_template('./src/website/results.html', search_results=search_results, num_results=len(), query=query, page_no=page_no, total_results=total_results)
"""