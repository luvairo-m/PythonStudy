import re
import requests

ref = input()
html = requests.get(ref).text

matches = [match for match in re.findall(r'<h3.*>(.*)</h3>', html) if match != ""]
print(matches)
