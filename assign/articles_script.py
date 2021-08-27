import json
import os

import pandas as pd
import requests

SOLR_ENDPOINT = None  # Add endpoint here

params = (
    ('q', '*:*'),
    ('rows', '100'),
    ('sort', 'date_published desc'),
    ('start', '240000'),
)

response = requests.get(
    SOLR_ENDPOINT, params=params)

docs = json.loads(response.text)['response']['docs']
print({i['source_name'] for i in docs})
dates = ({i['date_published'] for i in docs})
print(min(dates), max(dates))
##

df = pd.read_csv('~/Downloads/inaug_speeches.csv')
try:
    os.mkdir('docs3')
except FileExistsError:
    pass
for i, d in enumerate(df.text):
    with open(f'docs3/{i}', 'w') as f:
        f.writelines([d])
##

try:
    os.mkdir('docs2')
except FileExistsError:
    pass
for i, d in enumerate(docs):
    with open(f'docs2/{i}', 'w') as f:
        f.writelines([d['article_body']])
