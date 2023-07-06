---
title: Postman API  Testing
date: 2020-11-18
tags: [testing]
description: a sample postman api test
draft: false
---

### Example Postman Tests

{{< gist jaymutuku 0e0bbb7e4702aa4f1d59bc25ed9e378a >}}

### Notes

[Here](https://github.com/jaymutuku/postman-api-tests) is the detailed explanation of above script.


###  The Example below shows a Postman test-cript for automation the process of authentication(Basic Auth)

```js
let tokenUrl = 'https://test-gateway.tulaa.io/uaa-server/oauth/token'
let clientId='<client_id>'
let clientSecret='<client_secret>'

let getTokenRequest = {

    method:'POST',
    url:tokenUrl,
    auth: {
        type:'basic',
        basic: [
            {key:'username',value:clientId},
            {key:'password',value:clientSecret}

            ]
    },
    body: {
        mode:'urlencoded',
        urlencoded: [
            {key: 'username', value: '<USERNAME>'},
            {key: 'password', value: '<PASSWORD>'},
            {key: 'grant_type', value: 'password'}
            ]
    }
}

pm.sendRequest(getTokenRequest,(err,response) => {
    let jsonResponse = response.json(),
    newAccessToken = jsonResponse.access_token

    console.log({err,jsonResponse,newAccessToken})

    pm.globals.set('tulaa_token',newAccessToken)
});

```

### Another example using JSON payload

```js
let tokenUrl='<url>';

let getTokenRequest = {
    method:'POST',
    url:tokenUrl,
    header: 'Content-Type:application/json',
    body:{
        mode:'application/json',

       	raw: JSON.stringify({
 			username: '<USERNAME>',
 			password: '<PASSWORD>'
 		})
  }
};
pm.sendRequest(getTokenRequest,(err,response)=> {
    let jsonResponse = response.json(),
    newAccessToken = jsonResponse.data;

    console.log({err,jsonResponse,newAccessToken})

    pm.globals.set('accessToken',newAccessToken);
});

```