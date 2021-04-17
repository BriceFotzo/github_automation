import requests

def get_repos(github_api,username,token):
    """This function is used to list github repositories for an authenticated user.
    Args:
        github_api (string): the github api url
        username (string): your github username
        token (string): your github personal access token
    Returns:
        dict: a collection of repositories {id:repository_name}
    """
    #the api link to list the repositories
    repo_url=github_api+"/user/repos"
    #get the repositories of the user with its credentials
    repos = requests.get(repo_url, auth=(username,token))
    #initialize a dictonary to store the repositories name
    repos_dict={}
    for i,x in enumerate(repos.json(),1):
        #store each repository name with an id number
        repos_dict.update({i:x['name']})
    return repos_dict
def show_repos(repos_dict):
    """A function to show the list of repositories

    Args:
        repos_dict (dict): a collection of repositories {id:repository_name}
    """
    #print the values so that you can choose the repositories to delete
    print("List of repositories:")
    for key,value in repos_dict.items():
        print("{}- {}".format(key,value))

def create_repo(github_api,repo_name,is_public,username,token):
    """A function to create a github repository from the local environment

    Args:
        github_api (string): the github api url
        repo_name (string): the name of the repository you want to create
        is_public (bool): the paramter to set your repository public or private
        username (string): your github username
        token (string): your github personal access token

    Raises:
        SystemExit: description

    Returns:
        type: description
    """
    if is_public:
        data = '{"name": "' + repo_name + '", "public": true }'
    else:
        data = '{"name": "' + repo_name + '", "public": false }'

    try:
        r = requests.post(github_api + "/user/repos", data=data, auth=(username,token))
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
    return r
    