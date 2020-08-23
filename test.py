import requests
import time 
t1=time.time()
for _ in range(1000):
    requests.get('http://localhost:8080/api/post_office?id=1')
t2=time.time()
print(t2-t1)