from gitterpy.client import GitterClient
from pprint import pprint as pp
import pandas as pd

#Create instance
token = open('gtoken.txt').readline().strip()
gitter = GitterClient(token)

#Check ID
# print(gitter.auth.get_my_id)
#
# #Get a list of messages has usercout
# print(gitter.rooms_list)

#Raw chat JSON Data
chatData = gitter.messages.list('Buildly/community')

def getChatRawData():
    '''Gets the raw data from chat for testing purposes'''

    for x in chatData:
        pp(x)

def getChatMeta():
    '''Gets that gitter chat metadata and returns it as a dict'''

    chatMetaData = []

    for x in chatData:
        chatMetaDict = {}
        chatMetaDict['username'] = x['fromUser']['username']
        chatMetaDict['readby'] = x['readBy']
        chatMetaDict['timesent'] = x['sent'].split('T')[0] # T represents the time sent - split on T to get the date
        chatMetaDict['text'] = x['text']
        chatMetaData.append(chatMetaDict)

    df = pd.DataFrame(chatMetaData)
    df.set_index('timesent', inplace=True)

    return df

def getUniqueUsers():
    '''Returns the unique users who has chatted in the room since creation'''

    uniqueUsers = []
    holder = []

    #Gets usernames of people who have chatted
    [holder.append(x['fromUser']['username']) for x in chatData]

    #deletes duplicates to get unique users who have chat
    [uniqueUsers.append(i) for i in holder if i not in uniqueUsers]
    return uniqueUsers
