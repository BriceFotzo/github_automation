import os
import requests
from dotenv import load_dotenv
from utils import *
from time import sleep 

#load the .env variables
load_dotenv()
#set the api link
GITHUB_API = os.getenv('GITHUB_API')
GITHUB_URL = os.getenv('GITHUB_URL')
#set your github account info 
GITHUB_USER = os.getenv('GITHUB_USER')
GITHUB_TOKEN= os.getenv('GITHUB_TOKEN')

print('-------------------- DATA SCIENCE PROJECT INIT --------------------\n')
#navigating to the directory where you want to save your project
os.chdir('..')
print('-------------------- Step 1. Creating a local repository for your project in {}! --------------------\n'.format(os.getcwd()))
# launch the project setting whith cookiecutter (messages will be prompted to set parameters)
os.system('cookiecutter https://github.com/drivendata/cookiecutter-data-science')
print('-------------------- Project created in {}! --------------------\n'.format(os.getcwd()))
# show directories and files
for x in os.listdir('.'):
    print(x)
print('-------------------- Step 2. Creating a github repository to host your local project! --------------------\n')
if __name__=="__main__":
    #set your github repository name. It has to be the same you use previously for the local repository.
    repo_name=input("Type the repository name(please use the same name as your local repo.): ")
    #do you want your repo public or private?
    is_public=input("The repository msut be public? Y/N: ")
    if str.lower(is_public)=="y" or str.lower(is_public)=="yes":
        is_public=True
    else :
        is_public=False
    #creating a github repository using the function create_repo
    create_repo(GITHUB_API,repo_name,is_public,GITHUB_USER,GITHUB_TOKEN)
    #navigating to the local repository to push it to the hosted one.
    os.chdir(repo_name)
    print('-------------------- Step 3. Pushing local repo to the github one! --------------------\n') 
    os.system("git init")
    os.system("git remote add origin https://oauth2:"+GITHUB_TOKEN+"@github.com/"+GITHUB_USER+"/"+repo_name+".git")
    os.system("git add .")
    os.system('git commit -m "Initial commit"')
    os.system("git push --set-upstream origin master")
    print("-------------------- Done! You're now ready to start coding. --------------------")

