#Backlog

import time
import pandas as pd
from tqdm import tqdm
from squaremoonpy import errors, google_cloud as gc, bannerwise as bw

feeds_input = gc.get_spreadsheet('FeedLabs Previews', 'Sheet1')
feeds = {x['Account']: x for x in feeds_input}

output_chat = 'tid'
#output_chat = 'dev_tid'

for feed in tqdm(feeds):
    #feed= 'FD Dagkoers'
    intro_text = F"Previews for feed: {feed}"
    info = feeds[feed]
    if info['Active'] == 'TRUE':
        errors.telegram_bot_sendtext(intro_text,parse_mode='HTML',chat_id=info[output_chat])
        #check the type
        if info['type'] == 'csv':
            df = pd.read_csv(info['url'])
        else:
            df = bw.bannerwise2csv(info['url'])
        if info['items'] > len(df):
            sample_rate = len(df)
        else:
            sample_rate = info['items']
        df = df.sample(sample_rate)
        for index, row in df.iterrows():
            text = ''
            for field in info['fields'].split(','):
                field = field.strip()
                text = text + F"<b>{field.title()}</b>: {row[field]}"
                text = text + '\n'

            for field in info['image_field'].split(','):
                field = field.strip()
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
                errors.telegram_bot_sendtext(extratext,parse_mode='HTML',chat_id = info[output_chat])
            time.sleep(1.8)
            #errors.telegram_bot_sendtext(text,parse_mode='HTML')
        time.sleep(2.8)
