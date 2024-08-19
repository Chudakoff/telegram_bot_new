import time
import requests

offset = -2
counter = 0
chat_id: 6630116092


api_url = 'https://api.telegram.org/bot'
bot_token = '6630116092:AAG284aMjZ2agdP_nflp3SkYG-ULWXEWT2Y'
text = 'Wow, this is a real magic!'
max_counter = 15

while counter < max_counter:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')
            time.sleep(1)
    counter += 1
print("finished")