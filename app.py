import sys
import os
import json
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print("Get Request:")
	print(json.dumps(req, indent=4))

	res = processRequest(req)
	print("Request processed")

	res = json.dumps(res, indent=4)
	print(res)

	r = make_response(res)
	print(r)

	r.headers['Content-Type'] = 'application/json'

	return r


def processRequest(req):
	if req.get("result").get("action") != "echoAction":
		return {}
	res = makeEchoResponse(req);
	return res;


def makeEchoResponse(req):
	speech = req.get("result").get("resolvedQuery")
	return {
		"speech": speech,
		"displayText": speech,
		"source": "apiai-echo-sample"
	}


if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print("Starting app on port %d" % port)

	app.run(debug=False, port=port, host='0.0.0.0')
