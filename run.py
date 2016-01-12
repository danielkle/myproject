#!flask/bin/python
from app import app
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)
app.run(debug=True)
