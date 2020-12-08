import os, sys, subprocess
import json
import requests
import gkeepapi

logfileurl = "log.log"
logFile = open(logfileurl,"w")

if(len(sys.argv)>1 and sys.argv[1] == "gen"):
	#os.system("./ngrok http 8011 & >> ngrok.log")
	p=subprocess.Popen(["./ngrok", "http", "8011"], stdout=logFile, stderr=subprocess.STDOUT)
	print("Generating ngrok process, see", logfileurl, "for more details")	

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    return res_json["tunnels"][0]["public_url"]

def login():
	success = keep.login('talaourarfr@gmail.com', '********') # app pass from google

keep = gkeepapi.Keep()
login()
print("logged in")

try:
	url = get_ngrok_url()
except:
	print("no ngrok launched")
	exit()
"""
note = keep.createNote('ngrokUrl', get_ngrok_url())
note.pinned = True
note.color = gkeepapi.node.ColorValue.Red
"""
print ("ngrok launched in",url 	)
gnotes = keep.find(query='ngrokUrl')
for gnote in gnotes : 
	if(url != gnote.text):
		gnote.text = get_ngrok_url()
		print("url updated to ",url)
		keep.sync()
