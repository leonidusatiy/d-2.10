import os
import sentry_sdk

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://d99f829289d94ccdbe2936fb2a978e1c@o411989.ingest.sentry.io/5288035",
    integrations=[BottleIntegration()]
)

@route('/success')
def success():
    return "Hello!"

@route('/fail')  
def index():  
    raise RuntimeError("There is an error!")  
    return  
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)