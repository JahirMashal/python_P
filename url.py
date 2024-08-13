from urllib.parse import urlparse

def exactUrlParts(url):
    
    parurl = urlparse(url)
    
    parurl = {
        "scheme": parurl.scheme,
        "host": parurl.netloc,
        "path": parurl.path
    } 
    return parurl
    
    

print(exactUrlParts('http://www.aurochssoftware.com/about_us'))
print(exactUrlParts('https://demo.incentius.com/about/our_team'))