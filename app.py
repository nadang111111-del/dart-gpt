from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DART_API_KEY = os.environ.get("DART_API_KEY")

@app.route("/financial", methods=["GET"])
def financial():
    corp_code = request.args.get("corp_code")
    bsns_year = request.args.get("bsns_year")
    reprt_code = request.args.get("reprt_code", "11011")

    url = "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"

    params = {
        "crtfc_key": DART_API_KEY,
        "corp_code": corp_code,
        "bsns_year": bsns_year,
        "reprt_code": reprt_code
    }

    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
