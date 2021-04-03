import requests

def get_repos(github_url,username,token):
    #the api link to list the repositories
    repo_url=github_url+"/user/repos"
    #get the repositories of the user with its credentials
    repos = requests.get(repo_url, auth=(username,token))
    #initialize a dictonary to store the repositories name
    repos_dict={}
    for i,x in enumerate(repos.json(),1):
        #store each repository name with an id number
        repos_dict.update({i:x['name']})
    #print the values so that you can choose the repositories to delete
    for key,value in repos_dict.items():
        print("{}- {}".format(key,value))
    return repos_dict