import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from gitter import gitter
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from github_analytics import retrieve_repo_data
from pprint import pprint as pp

if __name__ == '__main__':
    #Load in the credentials & authorize client
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
    client = gspread.authorize(creds)

    '''Indexed by 0
    Main 0
    Gitter 1
    Github 2
    Data Studio 3 '''

    #Sets gitter worksheet
    # gitter_worksheet = client.open("Buildly Analytics").get_worksheet(1)

    #Gets gitter chat metadata
    # gitter_meta_data = gitter.get_chat_meta()

    #Sets github worksheet
    github_worksheet = client.open("Buildly Analytics").get_worksheet(2)

    #Gets github chat data
    github_meta_data = retrieve_repo_data.get_github_meta()
    github_view_data = retrieve_repo_data.modularize_view_data()
    github_clone_data = retrieve_repo_data.modularize_clone_data()

    #Writes user by frame
    # by_user_frame = github_meta_data.groupby("user").size().to_frame().T


    # Writes to the gitter google sheet
    set_with_dataframe(gitter_worksheet, gitter_meta_data)

    #Writes to the github metadata google sheet
    github_worksheet.update_acell('A1', 'Github Meta Data')
    set_with_dataframe(github_worksheet, github_meta_data, row=2)

    github_worksheet.update_acell('M1', 'Github viewer Data')
    set_with_dataframe(github_worksheet, github_view_data, row=2, col=13)

    github_worksheet.update_acell('Q1', 'Github clone Data')
    set_with_dataframe(github_worksheet, github_clone_data, row=2, col=17)
