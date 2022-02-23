import requests
import os
import json

def main():

    client_id = '6614f5155b588bda528c'
    client_secret = '454139ad199a4fb5707ff56a05e55865'
    data={
         "client_id": client_id,
         "client_secret": client_secret
         }            
    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",data=data)
    # разбираем ответ сервера
    j = json.loads(r.text)
    # достаем токен
    token = j["token"]
    inp_data = []
    headers = {"X-Xapp-Token" : token}
    current_dir = os.path.abspath(os.path.dirname(__file__))
    ans = []
    with open(os.path.join(current_dir, 'input.txt'), "r") as inp:
        for number in inp:
            inp_data.append(number.strip())

    with open(os.path.join(current_dir, 'output.txt'), "w", encoding='utf-8') as outp:
        for number in inp_data:
            res = requests.get(f"https://api.artsy.net/api/artists/{number}", headers=headers)
            j = json.loads(res.text)
            ans.append(f"{j['birthday']} {j['sortable_name']}\n")
        for line in sorted(ans):
            outp.write(line[5:])
if __name__ == "__main__":
    main()