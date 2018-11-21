import requests
import re
from time import time

start = time()

regex = re.compile(r"Item\sID:\s</strong>(.*)</td>")

with open('body.html', 'r') as f:
        body = f.read()

data = {'1': '',
        '2': '',
        '3': '',
        '4': 'smtp.gmail.com',
        '5': 587,
        '6': 'diego.rodrigues@solor.com.br',
        '7': 'Teste',
        '8': body}

res = requests.post('http://0.0.0.0', data=data)
print(res.json())

end = time()

print('Duração: {} s'.format(round(end - start, 2)))