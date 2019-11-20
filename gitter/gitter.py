from gitterpy.client import GitterClient
from pprint import pprint as pp
import pandas as pd

#Create instance
# token = GitterClient(open('gtoken.txt").readline().strip())

#Raw chat JSON Data
chat_data = gitter.messages.list('Buildly/community')

def check_ID():
    '''Checks to see if the correct user is signed in and prints'''

    print(gitter.auth.get_my_id)

def get_chat_raw_data():
    '''Prints the raw data from chat for testing purposes'''

    for meta in chat_data:
        pp(meta)

def get_chat_meta():
    '''Gets that gitter chat metadata and returns it as a dict'''

    chat_meta_data = []

    for meta in chat_data:
        chat_meta_dict = {}
        chat_meta_dict['username'] = meta['fromUser']['username']
        chat_meta_dict['readby'] = meta['readBy']
        chat_meta_dict['timestamp'] = meta['sent'].split('T')[0] # T represents the 00:00 time sent - split on T to get the date
        chat_meta_dict['text'] = meta['text']
        chat_meta_data.append(chat_meta_dict)

    df = pd.DataFrame(chat_meta_data)

    return df

def get_unique_users():
    '''Returns the unique users who has chatted in the room since creation'''

    #Gets usernames of people who have chatted from the beginning of time
    holder = [x['fromUser']['username'] for x in chatData]

    #Deletes duplicates to get unique users who have chat
    unique_users = list(dict.fromkeys(holder))

    return unique_users
