import os
import requests
from dotenv import load_dotenv
from utils import *
load_dotenv()

#set the api link
GITHUB_API = os.getenv('GITHUB_API')
GITHUB_URL = os.getenv('GITHUB_URL')
#set your github account info 
GITHUB_USER = os.getenv('GITHUB_USER')
GITHUB_TOKEN= os.getenv('GITHUB_TOKEN')

if __name__=="__main__":
    repo_name=input("Type the repository name: ")
    is_public=input("The repository msut be public? Y/N: ")
    if str.lower(is_public)=="y" or str.lower(is_public)=="yes":
        is_public=True
    else :
        is_public=False
    create_repo(GITHUB_API,repo_name,is_public,GITHUB_USER,GITHUB_TOKEN)
sleep(2)
print('\n------------ Repos after delete ------------')
show_repos(get_repos(GITHUB_API,GITHUB_USER,GITHUB_TOKEN))