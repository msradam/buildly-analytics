import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from gitter import gitter

if __name__ == '__main__':
    #Load in the credentials & authorize client
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
    client = gspread.authorize(creds)

    #gitter sheet indexed by 0
    gs = client.open("Buildly Analytics").get_worksheet(1)



    #Gets chat metadata
    metaData = gitter.getChatMeta()

    #Prints metaData
    print(metaData)


    # TODO:
    #   Write to Google Sheets
