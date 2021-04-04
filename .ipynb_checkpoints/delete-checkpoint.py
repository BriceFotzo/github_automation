import os
import requests
from dotenv import load_dotenv
from utils import get_repos
load_dotenv()

#set the api link
GITHUB_URL = os.getenv('GITHUB_URL')
#set your github account info 
GITHUB_USER = os.getenv('GITHUB_USER')
GITHUB_TOKEN= os.getenv('GITHUB_TOKEN')

if __name__=="__main__":
    #get the repositories using your credentials
    repos_dict=get_repos(GITHUB_URL,GITHUB_USER,GITHUB_TOKEN)
    #set an input variable to choose the repositories to delete
    to_del=input("Type the repositories id to delete (spare them with a comma): ")    
    #split the input to create a list of repo to delete
    repo_to_del=to_del.split(',')
    #loop over the list of repo to delete
    for i in repo_to_del:
        #set the api link for deleting repo
        url = GITHUB_URL+"/repos/"+GITHUB_USER+"/"+repos_dict[int(i)]
        try:
            #delete the repositories
            response = requests.delete(url, auth=(GITHUB_USER,GITHUB_TOKEN))
            if response.status_code==204:
                print("The repository {} has been deleted".format(repos_dict[int(i)]))
            else :
                print("Error: Not Found")

        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

    