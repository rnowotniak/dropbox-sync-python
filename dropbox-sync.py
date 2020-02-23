#!/usr/bin/python
#
# Robert Nowotniak <rnowotniak@gmail.com>  2020
#

import sys
import dropbox
import os
import json

# File to upload to Dropbox (150 MB max)
FILE_TO_UPLOAD = 'dropbox-sync.py'

DROPBOX_AUTHORIZE_URL = 'https://www.dropbox.com/oauth2/authorize?client_id=%s' \
    '&response_type=token'\
        '&redirect_uri=https://www.dropbox.com/1/oauth2/display_token'

TOKEN_FILE = '%s/.token.json' % os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    
    write_token_file = False
    try:
        with open(TOKEN_FILE, 'r') as f:
             appid, token = [(x['appid'], x['token']) for x in [json.load(f)]][0]
    except:
        appid = input('Please provide Dropbox application ID (App key): ')
        print('Please visit below URL, authorize this application to access your Dropbox, and paste the token below.')
        print(DROPBOX_AUTHORIZE_URL % appid)
        token = input('Token: ')
        write_token_file = True

    dbx = dropbox.Dropbox(token)
    acc = dbx.users_get_current_account()
    print('Account: %s' % acc.name.display_name)

    with open(FILE_TO_UPLOAD, 'rb') as f:
        dbx.files_upload(f.read(), '/' + FILE_TO_UPLOAD, mode=dropbox.files.WriteMode.overwrite)

    print('Done!')
    if write_token_file:
        with open(TOKEN_FILE, 'w') as f:
             json.dump({'appid': appid, 'token':token}, f)
    

