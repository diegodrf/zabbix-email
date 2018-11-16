import datetime
import requests

def test():
    itemname = 'CPU Total'
    period = 3600 # 1h
    width = 800
    height = 600
    stime = str(datetime.datetime.now() - datetime.timedelta(hours=1)).replace('-', '').replace(' ','').replace(':', '').split('.')[0]
    itemid = '96488'
    color = '218910'

    server = 'YOUR SERVER'
    url = server + f"/chart3.php?name={itemname}&period={period}&width={width}&height={height}&stime={stime}&items[0][itemid]={itemid}&items[0][drawtype]=5&items[0][color]={color}"


    user = 'YOUR USER'
    password = 'YOUR PASSWORD'
    payload = {'name': user, 'password': password, 'enter': 'Sign in'}

    with requests.Session() as s:
        s.post(server + '/index.php', data=payload)
        img = s.get(url)
        return img.content
        # with open ('img.png', 'wb') as f:
        #     for chunk in img.iter_content(100000):
        #         f.write(chunk)

if __name__ == '__main__':
    print(test())