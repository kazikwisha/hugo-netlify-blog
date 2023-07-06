---
title: REST API  Testing
date: 2020-11-19
tags: [testing]
description: REST API Test using Python Request Library & Unittest
draft: false
---

### Example:API testing Using Selenium

{{<gist jaymutuku 499235d0f098dcc97451e9637e7a9080 >}}

### Notes

[Here](https://github.com/jaymutuku/python-api-tests) is the detailed explanation of above script.

### Sample API Mock Test

Below test script demos the simplest api test using python `unittest` and `request` libraries.

```python {hl_lines=[11,"13-14"]}

import requests
import unittest
from pytest_httpserver import HTTPServer
import json

class APITest(unittest.TestCase):
    def test_my_client(self):
        with HTTPServer() as httpserver:
            # set up the server to serve "/content"  with the json
            httpserver.expect_request('/content').respond_with_json({'result': 30})
            # check that the request is served
            response = requests.get(httpserver.url_for('/content')).json()
            self.assertEqual(response, {"result":31})

if __name__ == "__main__":

    unittest.main()

## Expected Output
#
# $ python simple-test.py
#127.0.0.1 - - [11/Dec/2020 13:04:35] "GET / HTTP/1.1" 200 -
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.004s
#
#OK
#$
#$ python simple-test.py
#127.0.0.1 - - [11/Dec/2020 13:28:11] "GET /content HTTP/1.1" 200 -
#F
#======================================================================
#FAIL: test_my_client (__main__.APITest)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "simple-test.py", line 13, in test_my_client
#    self.assertEqual(response, {"result":31})
#AssertionError: {'result': 30} != {'result': 31}
#- {'result': 30}
#?             ^
#
#+ {'result': 31}
#?             ^
#
#
#----------------------------------------------------------------------
#Ran 1 test in 0.004s
#
#FAILED (failures=1)
#$
```
