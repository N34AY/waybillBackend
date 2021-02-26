from application import app
from config import DEBUG, HOST, PORT


app.run(host=HOST, port=PORT, debug=DEBUG)
