import requests 
from datetime import datetime
from bs4 import BeautifulSoup
from telebot import TeleBot
from time import sleep
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

TELEGRAM_BOT = '6579017739:AAFX5hszm_QiWchK6Bi6HivFjvYmvc6DpOw'

bot = TeleBot(TELEGRAM_BOT)

url = 'https://pro.firpo.ru/meropriyatiya/itogi/'


while True:
    response = requests.get(url)

    logging.info(f'SEND REQUEST | {datetime.now()}')

    if response.status_code == 200:

        logging.info(f'GET RESPONSE SUCCESSFULL | {datetime.now()}')

        soup = BeautifulSoup(response.content, 'lxml')
        data = soup.find_all('a', class_='doc-item')
        for s in data:

            href = f"https://pro.firpo.ru{s.get('href')}"
            text = s.find('div', class_="doc-item__title").text
            text_lower = s.find('div', class_="doc-item__title").text.lower()
            
            date_create = s.find('div', class_="doc-item__info").text.lower().split(':')[1]
            message = f"""{text}\n\n{href}\n\n{date_create}"""
        
            type = ('веб'.lower() in text_lower) and not ('Юниоры'.lower()  in text_lower)

            

            if type:
                logging.info(f'SEARCH ITEM SUCCESS | {datetime.now()}')
                bot.send_message(1807334234, message)
                break
                
    else:
        logging.warning(f'ERROR SEND REQUEST {response.status_code} | {datetime.now()}')

    sleep(60)
        
        
    
    
    



# if __name__ == "__main__":
#     bot.infinity_polling()