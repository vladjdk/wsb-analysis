import praw
import yaml

def getsession():
    with open("../config.yaml", 'r') as stream:
        try:
            conf = yaml.safe_load(stream)
            user = conf['reddit']['user']
            password = conf['reddit']['password']
            client_id = conf['reddit']['client_id']
            client_secret = conf['reddit']['client_secret']
            user_agent = conf['reddit']['user_agent']
        except yaml.YAMLError as exc:
            print(exc)

    return praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       username=user,
                       password=password,
                       user_agent=user_agent
                       )