import requests

filename = ''
url = ''

image_file_descriptor = open(filename, 'rb')

files = {'media': image_file_descriptor}

r = requests.post(url, files=files)

print(r.status_code)

image_file_descriptor.close()