from flask import Flask, jsonify, render_template, request
import logging

# create globals
app = Flask(__name__)
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='$%', # was {%
    block_end_string='%$', # was %}
    variable_start_string='${', # was {{
    variable_end_string='}$', # was }}
    comment_start_string='$#', # was {#
    comment_end_string='#$', # was #}
))
app.jinja_options = jinja_options

#add logging
log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.DEBUG)

# index
@app.route('/')
def index():
    return render_template(
        'index.html', 
        flask_template_var='{}'.format(request.remote_addr)
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
