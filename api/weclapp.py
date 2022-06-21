import http.client
import json

from pyparsing import line

conn = http.client.HTTPSConnection("amadeus.weclapp.com")

payload = ""

headers = {
    'cookie': "JSESSIONID=PiWCOyaNUdmmF0Y92DhZVNXG4fV9gfl68q1MWfrH.app; _sid_=3",
    'AuthenticationToken': "44dd4594-30aa-499c-b375-8e596ff0d99d"
    }

conn.request("GET", "/webapp/api/v1/customer?page=2&pageSize=1&properties=customerNumber%2Ccompany%2Ccompany2%2Cemail%2Cphone%2Ccontacts.firstName%2Ccontacts.lastName%2Ccontacts.email%2Ccontacts.firstName%2Ccontacts.fixPhone2%2Ccontacts.lastName%2Ccontacts.mobilePhone1%2Ccontacts.mobilePhone2%2Ccontacts.phone%2Ccontacts.phoneHome", payload, headers)

res = conn.getresponse()
jdata = res.read()
jdata = jdata.decode("utf-8")



pdata = json.loads(jdata)

for x in pdata:
    print(x)

print(pdata)