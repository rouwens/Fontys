import requests
 
url = 'http://192.168.219.53:3080/v2/projects/318da34a-b52c-40ba-8059-717ab8209dac/export'
 
# fetch file
response = requests.get(url, allow_redirects=True)
open('export.gns3project', 'wb').write(response.content)
 
# Get response status
print (response.status_code)
