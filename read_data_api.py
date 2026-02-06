
import pandas as pd
import requests
import os

token=os.getenv('api_token')
print(f"token: {token}")

if token=='1011':
    print("correct token")
else:
    print("invalid token")

# url="https://jsonplaceholder.typicode.com/users"

# response=requests.get(url)
# if response.status_code==200:
#     data=response.json()

# df=pd.DataFrame(data)
# df=df[['id','name']]
# print(df)