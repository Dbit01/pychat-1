__author__ = 'andrew'
import re
from subprocess import call
call(["wget", "http://emoticons-hangulatjelek.blogspot.com/p/emoticons.html", "-O", "/tmp/smiles.html"])

p = re.compile(r'http:\/\/[^"]*\.gif')
html_file = open('/tmp/smiles.html', 'r')
file_content = html_file.read()
result_regex = re.findall(p, file_content)
call(["mkdir","-p", "/tmp/smiles"])
for url in result_regex:
	call(["wget", url, "-P", "/tmp/smiles"])
