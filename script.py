import http.client
import json

conn = http.client.HTTPSConnection("localhost", 8000)
payload = json.dumps({
   "path": "D:/Projects/Python/voice/webserver/examples/customer.wav",
   "speaker": "customer"
})
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/register", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))