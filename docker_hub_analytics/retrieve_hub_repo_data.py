import requests
import pandas as pd

hub_api_url = "https://hub.docker.com/v2/repositories/buildly/"

def get_hub_analytics_df():
    return pd.DataFrame(requests.get(hub_api_url).json()['results'])

def get_hub_analytics_json():
    return request.sget(hub_api_url).json()['results']

