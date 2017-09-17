from flask import Flask, jsonify, render_template

# in order for view and flask to play nice, we need new tokens 
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='$%', # was {%
        block_end_string='%$', # was %}
        variable_start_string='${', # was {{
        variable_end_string='}$', # was }}
        comment_start_string='$#', # was {#
        comment_end_string='#$', # was #}
    ))

# create globals
app = CustomFlask("Flask-Vue")

# index
@app.route('/')
def index():
    return render_template(
        'index.html', 
        flask_template_var='Welcome to the jinja n vue example application.'
    )

# an api route
@app.route('/api/data/<parameter>')
def api_data(parameter):
    return jsonify(
        apiData="This is data returned from the api. The parameter was '{}'".format(parameter)
    )

# if called directly, launch our application
if __name__ == '__main__':
    app.run(debug=True)
