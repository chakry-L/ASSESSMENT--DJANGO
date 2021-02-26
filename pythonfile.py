import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'fileconversion'
resp = requests.get(BASE_URL+ENDPOINT)


import convertapi
import os
import io
import tempfile
convertapi.api_secret = os.environ['CONVERT_API_SECRET'] # your api secret
# Example of using content stream to convert to pdf
# https://www.convertapi.com/txt-to-pdf


upload_io = convertapi.UploadIO(resp, 'test.txt')
result = convertapi.convert('pdf', { 'File': upload_io })
saved_files = result.save_files(tempfile.gettempdir())
print("The PDF saved to %s" % saved_files)

