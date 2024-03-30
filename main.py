from flask import Flask
from configuration import configure_all

app = Flask(__name__)



app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = 'static'


configure_all(app)


app.run(debug=True)