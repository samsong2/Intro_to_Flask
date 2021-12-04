import os
from flask import Flask 

# creates the flask
template_dir = os.path.abspath('./src')
app = Flask(__name__, template_folder=template_dir)

# The view function index() is linked to the main route using the app.route() decorator.
# When the main route is requested, Flask will serve the request by calling index() and using its return value as the response.

@app.route("/") # obviously the default page.
def index():
    return render_template('./src/website/main.html')

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