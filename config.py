import os

HOST = '0.0.0.0'
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
MONGO_URI = "mongodb://127.0.0.1:27017/waybill"
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2


# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "9665cffa12436b665cffa12431ca51c4b4f8665cffa12435d2adb9"

# Secret key for signing cookies
SECRET_KEY = "96665cffa1243b665cffa12431665cffa1243ca51c4b4f85d2adb9"

# JWT
JWT_SECRET_KEY = '96b665cffa12462431ca51c4b45a51c4b4f8cffa'
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
