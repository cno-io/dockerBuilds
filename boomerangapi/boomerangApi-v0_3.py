import boto3
import re
import datetime

# BoomerangAPI.py
# @TweekFawkes
# Ref: https://github.com/RhinoSecurityLabs/IPRotate_Burp_Extension/blob/master/IPRotate.py

# aws configure --profile apigateway
#
# AKIA.............BAR
# VnM..................................1Im
# us-east-2
# json
#
# aws --profile apigateway sts get-caller-identity
#

print("""
                                                               ___                  
_-_ _,,                                                       -   -_, -__ /\\  _-_, 
   -/  )                                     _           _   (  ~/||    ||  \\   // 
  ~||_<    /'\\  /'\\ \\/\\/\\  _-_  ,._-_  < \, \\/\\  / \\ (  / ||   /||__||   || 
   || \\  || || || || || || || || \\  ||    /-|| || || || ||  \/==||   \||__||  ~|| 
   ,/--|| || || || || || || || ||/    ||   (( || || || || ||  /_ _||    ||  |,   || 
  _--_-'  \\,/  \\,/  \\ \\ \\ \\,/   \\,   \/\\ \\ \\ \\_-| (  - \\, _-||-_/  _-_, 
 (                                                      /  \            ||          
                                                       '----`                       
    """)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

sDirtyAwsAccessKeyId = input("AWS Access Key ID, e.g. AKIA... [None]: ")
sAwsAccessKeyId = str(sDirtyAwsAccessKeyId).strip()
print("[+] sAwsAccessKeyId: " + str(sAwsAccessKeyId) + "")

sDirtyAwsSecretAccessKey = input("AWS Secret Access Key [None]: ")
sAwsSecretAccessKey = str(sDirtyAwsSecretAccessKey).strip()
print("[+] sAwsSecretAccessKey: " + str(sAwsSecretAccessKey)[0:4] + "...<REDACTED>..." + str(sAwsSecretAccessKey)[0:-4] + "")

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

sDirtyAwsRegionName = input("Region to Deploy API Gateway into, e.g. us-east-2 [None]: ")
sAwsRegionName = str(sDirtyAwsRegionName).strip()
print("[+] sAwsRegionName: " + str(sAwsRegionName) + "")

sDirtyTargetUrl = input("Target URL to redir traffic to, e.g. http://ip.on.the.internet:1080/ [None]: ")
sTargetUrl = str(sDirtyTargetUrl).strip()
print("[+] sTargetUrl: " + str(sTargetUrl) + "")

# sProfileName = "apigateway"
# sRegion = "us-east-2"
#sTargetUrl = "http://18.189.188.205:1080/"
sUniqueString = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
sApiName = "BoomerangAPI" + sUniqueString
sStageName = "v1"
sUsage = "boomerangusage"

#print("[*] sProfileName: " + str(sProfileName))
#print("[*] sRegion: " + str(sRegion))
print("[*] sTargetUrl: " + str(sTargetUrl))
print("[*] sUniqueString: " + str(sUniqueString))
print("[*] sApiName: " + str(sApiName))
print("[*] sStageName: " + str(sStageName))
print("[*] sUsage: " + str(sUsage))

#session = boto3.Session(profile_name=sProfileName)
session = boto3.Session(aws_access_key_id=sAwsAccessKeyId, aws_secret_access_key=sAwsSecretAccessKey, region_name=sAwsRegionName)

awsclient = session.client('apigateway', region_name=sAwsRegionName)

create_api_response = awsclient.create_rest_api(
				name=sApiName,
				endpointConfiguration={
					'types': [
						'REGIONAL',
					]
				}
			)

get_resource_response = awsclient.get_resources(restApiId=create_api_response['id'])

restAPIId = create_api_response['id']
print("[~] restAPIId: " + str(restAPIId))

create_resource_response = awsclient.create_resource(
    restApiId=create_api_response['id'],
    parentId=get_resource_response['items'][0]['id'],
    pathPart='{proxy+}'
)

awsclient.put_method(
    restApiId=create_api_response['id'],
    resourceId=get_resource_response['items'][0]['id'],
    httpMethod='ANY',
    authorizationType='NONE',
    requestParameters={
        'method.request.path.proxy':True
                    }
)

awsclient.put_integration(
    restApiId=create_api_response['id'],
    resourceId=get_resource_response['items'][0]['id'],
    type='HTTP_PROXY',
    httpMethod='ANY',
    integrationHttpMethod='ANY',
    uri=sTargetUrl,
    connectionType='INTERNET',
    requestParameters={
        'integration.request.path.proxy':'method.request.path.proxy'
    }
)

awsclient.put_method(
    restApiId=create_api_response['id'],
    resourceId=create_resource_response['id'],
    httpMethod='ANY',
    authorizationType='NONE',
    requestParameters={
        'method.request.path.proxy':True
    }
)

awsclient.put_integration(
    restApiId=create_api_response['id'],
    resourceId=create_resource_response['id'],
    type= 'HTTP_PROXY', 
    httpMethod= 'ANY',
    integrationHttpMethod='ANY',
    uri= sTargetUrl+'{proxy}',
    connectionType= 'INTERNET',
    requestParameters={
        'integration.request.path.proxy':'method.request.path.proxy'
    }
)

deploy_response = awsclient.create_deployment(
    restApiId=restAPIId,
    stageName=sStageName
)

sEndpoint = str(restAPIId+'.execute-api.'+sAwsRegionName+'.amazonaws.com')
print("[~] sEndpoint: " + str(sEndpoint))

usage_response = awsclient.create_usage_plan(
    name=sUsage,
    description=restAPIId,
    apiStages=[
        {
        'apiId': restAPIId,
        'stage': sStageName
        }
    ]
)

print("[~] usage_response: " + str(usage_response))

print("[+] Redirect URL: https://" + sEndpoint + '/' + sStageName)