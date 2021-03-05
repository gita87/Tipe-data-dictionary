import requests

url = 'https://detik.com'
try :
    response = requests.get(url)
    if response.status_code == 200:
        print(f'success! response == {response.status_code}')
        print(f'Content {response.text}')
except Exception as e :
    print('there is an error', e)
print('Program Ended!')