import requests

response = requests.get('http://naver.com')
print(response)

response1 = requests.get('http://naver.com').text
print(response1)

response2 = requests.get('http://naver.com').status_code
print(response2)