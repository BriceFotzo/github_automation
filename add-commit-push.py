import os
import requests
from dotenv import load_dotenv
from utils import *
import argparse

parser = argparse.ArgumentParser(description='Get the commit message.')
parser.add_argument('--commit', type=str, nargs='+',
                    help='a message for the commit')


args = parser.parse_args()
# print(vars(args)['commit'][0])
if __name__=="__main__":
    print("-------------------- ADD --------------------")
    os.system("git add .")
    print("-------------------- COMMIT --------------------")
    os.system('git commit -m "{}"'.format(vars(args)['commit'][0]))
    print("-------------------- PUSH --------------------")
    os.system("git push")
    

