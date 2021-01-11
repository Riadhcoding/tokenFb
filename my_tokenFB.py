import mechanize,os,sys,json,time
import requests
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
print('\033[1;36mcopy your user agent here >'.upper())
us = input('\033[1;31mENTER YOUR USER AGENT : ')
time.sleep(4)
os.system('xdg-open https://www.google.com/search?sxsrf=ALeKk03R0VfGqdiK2mGIpD1HBjaij2_iUA%3A1610395533327&source=hp&ei=ja_8X5yEEYOYlwSZ35DwBA&iflsig=AINFCbYAAAAAX_y9ncPHXDlZicWFBCxiCW4n-pgHsWUs&q=my+user+agent&oq=my+&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDJAxAnMgQIIxAnMgQIIxAnMgQIABBDMgQILhBDMgQILhBDMgIILjICCAAyAgguMgQIABAKOgcIIxDqAhAnOgUIABCRAlClBlj4FmC_I2gCcAB4AIABzQOIAZMMkgEJMC4zLjEuMS4xmAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab')
br.addheaders = [('User-Agent',us)]
print('\033[1;36mAccess Tokens - Facebook Login\n')
print('\033[1;31m[1] \033[1;35mGet Token Facebook')
print('\033[1;31m[2] \033[1;35mYouTube')
choose = input('\033[1;31m[?] \033[1;35mChoose : ')
if choose =='1':
    id = input('\033[1;31m\nENTER ID/Email :')
    pw = input('\033[1;32m\nENTER PASSWORD  : ')
    data = br.open(
        'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
    q = json.load(data)
    if 'access_token' in q:
        print('\033[1;32mLogin success')
        print('\033[1;36myour token is > \033[1;31m'+q['access_token'])
        print('\033[1;37m #'*41)
        print('\033[1;36m Email/id      |    Password ')
        print('\n\033[1;31m' + id + '\033[1;35m | \033[1;32m' + pw)
    else:
        if 'www.facebook.com' in q['error_msg']:
            print('\033[1;33mAccount Has Been Checkpoint')
            print(id + ' | ' + pw)
        else:
            print('\033[1;31mWorng Email/id Or Password')
else:
    os.system('xdg-open https://www.youtube.com/c/pythonlife')


