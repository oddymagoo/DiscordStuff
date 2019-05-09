import requests
import json


url = 'https://discordapp.com/api/guilds/212528597443936256/widget.json'
r = requests.get(url)


print (r.json())