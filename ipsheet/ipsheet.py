import netifaces as ni
import json
import gspread
import threading
from oauth2client.client import SignedJwtAssertionCredentials
import yaml

config = yaml.load(open("./config.yml"))

# connect to spreadsheet
json_key = json.load(open(config['key_file']))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'],
                                            scope)
gc = gspread.authorize(credentials)

wks = gc.open(config['spreadsheet']).sheet1

# get ip address
neti = ni.ifaddresses(config['network_interface'])
ip_address = neti[2][0]['addr']

# check if this ip address is already in the spreadsheet,
# if it's not append it to the column
try:
    wks.find(ip_address)
    # this is fine ip adress is already there
except:
    # append the address
    wks.update_cell(len(wks.col_values(1)) + 1, 1, ip_address)

# need to querry spreadsheet(for example every 10s)
# when key is pasted pick it up and stop queries
def fetch_key():
    cell = wks.find(ip_address)
    key = wks.cell(cell.row, 2).value
    if (key == ""):
        # querry again
        threading.Timer(1, fetch_key).start()
    else:
        # add the key
        with open(config['target_file'], 'a') as target:
            target.write(key)
        wks.update_cell(cell.row, 3, "success")

fetch_key()
