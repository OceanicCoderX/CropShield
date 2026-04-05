#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

import random
import requests

# ðŸ” Static values
phone_number = "9373757906"  # OTP à¤‡à¤¸à¥€ à¤¨à¤‚à¤¬à¤° à¤ªà¤° à¤œà¤¾à¤à¤—à¤¾
api_key = "dfGbQk6v8LAMwNSq4DyVRXxhaUE7W5eFB1OYtTjncp9ugJlszHSQ5rGmDp8lLaFh4vkMtZoUVCHW1s7f"  # à¤¯à¤¹à¤¾à¤ à¤…à¤ªà¤¨à¤¾ Fast2SMS API key à¤¡à¤¾à¤²à¥‹

# ðŸ”¢ OTP Generate
otp = str(random.randint(100000, 999999))

# ðŸ“¤ Send OTP via Fast2SMS
url = "https://www.fast2sms.com/dev/bulkV2"
headers = {
    'authorization': api_key,
    'Content-Type': "application/x-www-form-urlencoded"
}
payload = {
    'variables_values': otp,
    'route': 'otp',
    'numbers': phone_number
}

response = requests.post(url, data=payload, headers=headers)
print("ðŸ“¨ OTP Sent to", phone_number)
print("ðŸ”§ API Response:", response.json())
