import requests
import sys
import os
import argparse
import errno
from os import path
import socket


def main(url):
	try :
		response = requests.head(url)
		#response = str(response.status_code)
		return response
	except requests.ConnectionError:
		return "[Failed to Connect]"

def fetch_Contentlength(url):
	try:
		r = requests.get(url)
		content_length = r.headers['Content-Length']	
		return content_length	
	except requests.ConnectionError:
		return"Failed to Connect"
def find_ip(url):
	try:
		if "https://" in url or "http://" in url:
			url = url.strip("https://")
			ip_addr = socket.gethostbyname(url)
			return ip_addr
		else :
			ip_addr = socket.gethostbyname(url)
			return ip_addr
	except socket.gaierror:
		return "[Failed to Connect]"

def file_read(filename):
	urls = []
	with open(filename) as f:
		for url in f:
			if "https://" in url or "http://" in url:
				urls.append(url.strip('\n'))
			else:
				urls.append("http://"+url.strip('\n'))
				urls.append("https://"+url.strip('\n'))
	return urls
def file_write(filename, out):
	f_out = open(filename, "a")
	f_out.write(out)
	f_out.write("\n")

	f_out.close()


if __name__ == '__main__':
	urls = []
	
	try:
		parser = argparse.ArgumentParser(description='Test')
		parser.add_argument('-l', '--urls', help = 'urls')
		parser.add_argument('-o', '--output', help =  'save to a file')
		parser.add_argument('-c', '--content_length', help = 'capture content length', action="store_true")
		parser.add_argument('-i','--ip', help = 'Find ip', action="store_true")
		args =  parser.parse_args()
		if os.name=="nt":
			os.system("cls")

        	
		banner = """\033[34m
		    __    __  __       
		   / /_  / /_/ /_____  _         _ 
		  / __ \/ __/ __/ __ \  \      /  /
		 / / / / /_/ /_/ /_/ /\  \    /  /
		/_/ /_/\__/\__/ .___/  \  \  /  /
       			     /_/        \  \/  /
        	    			 \_  _/ ALIDATOR
            			 							v1.0


           		   \033[36m
           		   """
        
        
        
		if args.urls:
			print(banner)
			filename = args.urls
			urls = file_read(filename)
			for url in urls:
				response = str(main(url)).strip("<Response").strip(">")
				if response:
					if response == "[200]":
						out = url+"		"+'\033[92m'+response+'\033[0m'
						out1 = url+"		"+response
					elif response == "[301]":
						out = url + "	"+'\033[92m'+response+'\033[0m'
						out1 = url+"		"+response
					else :
						out = url + "	" + '\033[92m'+response+'\033[0m'
						out1 = url+"		"+response
				if response != "[Failed to Connect]":
					if args.content_length:
						out = out+"		"+"["+str(fetch_Contentlength(url))+"]"
						out1= out1+"		"+"["+str(fetch_Contentlength(url))
					elif args.ip:
						out = out+"		"+str(find_ip(url))
						out1 = out1+"		"+str(find_ip(url))
				if args.output:
					out_file = args.output
					file_write(out_file,out1)


				print(out)




	except KeyboardInterrupt:
		print("\n\u001b[31m[EXIT]KeyBoard Interrupt Encountered \u001b[0m")