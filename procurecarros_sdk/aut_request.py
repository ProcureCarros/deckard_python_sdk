


client_id = 'APP_ID'
secret = 'TOKEN'
url = b'http://localhost:3001/endpoint/discover/v1/dummy'

timestamp = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
msg = "application/json,,/endpoint/discover/v1/dummy,"+timestamp
signing = hmac.new(secret, msg, hashlib.sha1)

headers = {'Authorization': 'APIAuth '+client_id+":"+base64.b64encode(signing.digest()),
            'content-type':'application/json',
            'content-md5':'',
            'request-uri': '/endpoint/discover/v1/dummy',
            'TIMESTAMP': timestamp,
            'DATE': timestamp}
response = requests.get(url, headers=headers)
print(msg);
print(response.request.headers);
print(response);
