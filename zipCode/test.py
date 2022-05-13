import urllib3
import requests
url = "https://api.postalpincode.in/pincode/"+ "413736"

request_response = requests.head(url)
status_code = request_response.status_code
website_is_up = status_code == 200

print(website_is_up)