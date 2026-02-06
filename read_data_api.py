
import pandas as pd
import requests

url="https://jsonplaceholder.typicode.com/users"

response=requests.get(url)
if response.status_code==200:
    data=response.json()

df=pd.DataFrame(data)
df=df[['id','name']]
print(df)