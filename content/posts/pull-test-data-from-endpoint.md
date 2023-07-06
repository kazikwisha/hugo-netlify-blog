---
title: Pull JSON Data From Endpoint and Flatten it to CSV
date: 2020-11-18
tags: [how-to]
description: an example of json flattening script
draft: false
---

Sometimes as a QA Engineer,you need to pull test data from endpoints from
third parties.That is clients you are integrating you system with.

This is usually vital when the developers are working on the integration.
You can start preparing the tests early enough.

### Example script shows how to pull credit score data in json and flatten it to csv.

{{<gist jaymutuku 38ff8a1d9f26ea3be5009d9cc2e41c36>}}


### Better Example Now Using Pandas

```python
import pandas as pd
from requests.auth import HTTPBasicAuth
import requests
import json
from pandas.io.json import json_normalize

# import specific column
# measure time taken to import big CSV
df = pd.read_csv('farmers_identification.csv',usecols=['farmer_national_id'],verbose=True)

# print(df)
token = ''

def get_auth_token(token):
  endpoint='https://test-gateway.tulaa.io/uaa-server/oauth/token'

  payload = {
    'username':'<my-email>',
    'password':'<my-password>',
    'grant_type':'password'
  }

  response = requests.post(endpoint,auth=HTTPBasicAuth('<web_client>','<client_secret>'),data=payload)

  if(response.ok):

    jData = json.loads(response.content)

    for key in jData:
      if key == 'access_token' in jData:
        token='Bearer'+' '+str(jData[key])
        # print(token)

      return token
  else
    # my_logger.debug('a debug message')
    raise ApiError('Cannot fetch access token:{}'.format(response.status_code))

def get_credit_score(row):

  token = get_auth_token(token)

  headers ={
    'Authorization':token
  }

  try:
    url = 'https://test-cogency-service.tulaa.io/credit/score/str[row]'

    response = (requests.get(url).text)
    response_json = json.loads(response)

    return response_json


  except Exception as e:
    raise e


  df['API_response'] = df.apply(get_credit_score,axis=1)
  df['API_response'].head()

  new_df = json_normalize(df['API_response'])
  new_df = new_df[['metropol_credit_score','id_number']]
  new_df

  new_df.to_csv(path_or_buf='./farmers-with-score.csv',index=False)


if __name__ == '__main__':
  get_credit_score()

```





