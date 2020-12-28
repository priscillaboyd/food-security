"""Utility to grab list of food banks registered on GiveFood.org."""

import urllib.request
import json
import time

# declare output path
dir = 'data/'
current_dt = time.strftime("%Y%m%d_%H%M%S")
f = 'foodbanks_' + current_dt + '.json'

# retrieve data from givefood.org
with urllib.request.urlopen('https://www.givefood.org.uk/api/1/foodbanks/') as api_response:
   json_string = api_response.read()
   parsed_json = json.loads(json_string)

# format and write to file
with open(dir + f, 'w') as output:
   json.dump(parsed_json, output, skipkeys=True, ensure_ascii=False, indent=4)