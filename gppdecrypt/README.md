## gppdecrypt
Simple script to decrypt GPP passwords found in groups.xml files in the sysvol folders. Microsoft publishes the key on MSDN so this becomes straightforward.

Needs pycrypto (pip install pycrypto).
Windows users [https://twitter.com/riyazwalikar/status/844953786376474626](https://twitter.com/riyazwalikar/status/844953786376474626)

#### Usage
C:\> python gppdecrypt.py j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw


#### Credits
Inspired from: https://pentestlab.blog/2017/03/20/group-policy-preferences/
