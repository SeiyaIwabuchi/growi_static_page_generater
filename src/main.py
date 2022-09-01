"""
main.py
"""
import json
from typing import Dict
from flask import Flask, render_template
import requests

from config_loader import ConfigLoader

app = Flask(__name__)
CONFIG = ConfigLoader.config
base_url = CONFIG.rest_server_url

def with_query_strings(url: str, query_strings: Dict[str, str]) -> str:
    string = ""
    for k,v in query_strings.items():
        string += f'{k}={v}&'
    
    return f'{url}?{string[:-1]}'

@app.route('/pages')
def pages():
    request_url = with_query_strings(f'{base_url}{CONFIG.endpoint_pages}', {'access_token':CONFIG.api_key})
    raw_json = requests.get(request_url)
    enc_json = json.loads(raw_json)
    return render_template('pages.html', pages=enc_json['pages'])

app.run(host=CONFIG.host_name, port=CONFIG.port)

# @app.route('/page/<page_id>')
# def page(page_id):
#     # 本文を入れたうえでリダイレクトする
#     requests.get()
#     pass
