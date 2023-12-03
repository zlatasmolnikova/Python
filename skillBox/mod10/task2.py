import re
import requests

url = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(url)
html_text = response.text

all_tags = re.findall(r'<h3(.*?)>(.*?)</h3>', html_text)

result = []

for i in range(len(all_tags)):
  result.append(all_tags[i][1])

result
