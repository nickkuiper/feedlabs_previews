import time
import pandas as pd
from squaremoonpy import errors

#-1001651820041
#446561835
#base_telegram_id = '-446561835'
base_telegram_id = '-541398399'

feeds = {
    'Valk Kamers': {'url': 'https://storage.googleapis.com/fl-output-feeds/Q2gqNMw/9ar5Dze', 'fields' : ['hotel_id', 'name'], 'image_field' : ['image[0].url'], 'items' : 3, 'tid' : base_telegram_id},
    'FD News': {'url': 'https://storage.googleapis.com/fl-output-feeds/b9gNvgo/bmMaYMK', 'fields' : ['id', 'title'], 'image_field' : ['image[0].url'], 'items' : 3, 'tid' : base_telegram_id},
    'FD Dagkoers': {'url': 'https://storage.googleapis.com/fl-output-feeds/b9gNvgo/mVMVwzq', 'fields' : ['id', 'title'], 'image_field' : ['image[0].url', 'image[1].url', 'image[2].url'], 'items' : 2, 'tid' : base_telegram_id},
    #'FD Essay': {'url': 'https://storage.googleapis.com/fl-output-feeds/b9gNvgo/N4Me0gJ', 'fields' : ['id', 'title'], "image_field" : ['image[0].url'], 'items' : 2, 'tid' : base_telegram_id},
    #'Borzo Verticals': {'url': 'https://storage.googleapis.com/fl-output-feeds/62Md9zW/BEzpYrm', 'fields' : ['id', 'title'], 'image_field' : ['image[0].url'], 'items' : 3, 'tid' : base_telegram_id},
    'Borzo Hyperlocal': {'url': 'https://storage.googleapis.com/fl-output-feeds/62Md9zW/lvzL3Md', 'fields' : ['id', 'title'], 'image_field' : ['image[0].url'], 'items' : 3, 'tid' : base_telegram_id},
    'Henk Kuiper Autos': {'url': 'https://storage.googleapis.com/fl-output-feeds/e2MWarL/Q2gqNMw', 'fields' : ['merk', 'model', 'price'], 'image_field' : ['image[0].url'], 'items' : 3, 'tid' : '-446561835'},
    'SE - SV - BL': {'url': 'https://storage.googleapis.com/fl-output-feeds/4LMAaMl/l0zXLz2', 'fields' : ['vehicle_id', 'price'], 'image_field' : ['image[0].url'], 'items' : 2, 'tid' : base_telegram_id},
    'NO - NB - BL': {'url': 'https://storage.googleapis.com/fl-output-feeds/4LMAaMl/LJgZkM9', 'fields' : ['vehicle_id', 'price'], 'image_field' : ['image[0].url'], 'items' : 2, 'tid' : base_telegram_id},
    'PO - PO - BL': {'url': 'https://storage.googleapis.com/fl-output-feeds/4LMAaMl/xNrJQzR', 'fields' : ['vehicle_id', 'price'], 'image_field' : ['image[0].url'], 'items' : 2, 'tid' : base_telegram_id},
    'Ekar': {'url': 'https://storage.googleapis.com/fl-output-feeds/dNMjKzk/BPzOBMQ', 'fields' : ['vehicle_id', 'price'], 'image_field' : ['image[2].url'], 'items' : 2, 'tid' : base_telegram_id},
}


for feed in feeds:
    intro_text = F"Previews for feed: {feed}"
    info = feeds[feed]
    errors.telegram_bot_sendtext(intro_text,parse_mode='HTML',chat_id=info['tid'])
    df = pd.read_csv(info['url'])
    df = df.sample(info['items'])
    for index, row in df.iterrows():
        text = ''
        for field in info['fields']:
            #print(field)
            text = text + F"<b>{field.title()}</b>: {row[field]}"
            text = text + '\n'

        for field in info['image_field']:
            #print(img)
            extratext = text + F"<b>{field.title()}</b>"
            extratext = extratext + '\n'
            extratext = extratext + F"{row[field]}"
            extratext = extratext + '\n'
            #url
            try:
                extratext = extratext + "\n<a href='" + row['url'].split('?')[0]  +"'>Visit Product URL""</a>\n"
            except:
                extratext = extratext + "\n<a href='" + row['link'].split('?')[0]  +"'>Visit Product URL""</a>\n"
            time.sleep(1.8)
            errors.telegram_bot_sendtext(extratext,parse_mode='HTML',chat_id = info['tid'])
        time.sleep(1.8)
        #errors.telegram_bot_sendtext(text,parse_mode='HTML')
    time.sleep(2.8)
