import requests
import base64

def get_git_content(url):

  url = url.split('/')
  user = url[3]
  repo = url[4]
  path = "/".join(url[7:])
  api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
  
  r = requests.get(api_url)
  if r.status_code == 404:
    return 'not found', ''
  
  data = r.json()

  content = data["content"]
  extension = data["name"].split(".")[1]

  message_bytes = base64.b64decode(content)
  message = message_bytes.decode('utf-8')
  return message, extension


if __name__ == '__main__':
  a, c = get_git_content("https://github.com/Sancho41/academic/blob/master/2019_2/maratona/classroom/lista01/a.py")
  print(a)