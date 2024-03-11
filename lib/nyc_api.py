
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = 'https://web.archive.org/web/20180303155827/https://data.cityofnewyork.us/resource/uvks-tn5n.json'
    response = requests.get(URL)
    return response.content

programs = GetPrograms().get_programs()
print(programs)