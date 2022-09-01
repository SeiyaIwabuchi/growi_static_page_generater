"""
main.py
"""
import json
from typing import Dict
from flask import Flask, render_template, Markup
import requests
from markdown import markdown

from config_loader import ConfigLoader

app = Flask(__name__)
CONFIG = ConfigLoader.load()
base_url = CONFIG.rest_server_url + CONFIG.rest_url_prefix

def with_query_strings(url: str, query_strings: Dict[str, str]) -> str:
    string = ""
    for k,v in query_strings.items():
        string += f'{k}={v}&'
    
    return f'{url}?{string[:-1]}'

@app.route('/pages')
def pages():
    request_url = with_query_strings(f'{base_url}{CONFIG.endpoint_pages}', {'access_token':CONFIG.api_key, 'path':'/'})
    raw_json = requests.get(request_url).text
    enc_json = json.loads(raw_json)
    return render_template('pages.html', pages=enc_json['pages'])

@app.route('/v3/page/<page_id>')
def page(page_id):
    request_url = with_query_strings(f'{base_url}{CONFIG.endpoint_page}', {'access_token':CONFIG.api_key, 'pageId':page_id})
    raw_json = requests.get(request_url).text
    enc_json = json.loads(raw_json)
    print(enc_json)
    return render_template(
        'page.html',
        md_text=Markup(markdown(enc_json['page']['revision']['body'])),
        rest_server_url=CONFIG.rest_server_url,
        page_id=page_id
        )

if __name__ == '__main__':
    app.run(host=CONFIG.host_name, port=CONFIG.port)
