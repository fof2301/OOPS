import json
import hashlib

with open("credentials.json") as creds:
    data=json.load(creds)    
names=data["login_name"]
passs=data["login_pass"]
a=input()
hashed_a=hashlib.sha256(a.encode('utf-8')).hexdigest()
b=input()
hashed_b=hashlib.sha256(b.encode('utf-8')).hexdigest()
try:
    c=int(names.index(hashed_a))
    d=int(passs.index(hashed_b))
except:
    pass    
if(c==d):
    print("SUCCESS")
else:
    print("fail")    
