
from util import *
import yaml
import sys
from connect import create_service


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def main():
  

    if sys.argv[1] == None:
        print('To create and send email, include details in YAML file and specify it as an argument')
        exit(0)
    with open(sys.argv[1], 'r') as f:
        email = yaml.load(f, Loader=yaml.FullLoader)
    service = create_gmail_service()
    message = create_message(email["sender"], email["to"], email["subject"], email["message_text"])
    send_message(service, 'me', message)

if __name__ == '__main__':
    main()