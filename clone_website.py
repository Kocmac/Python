import urllib.request
import urllib.error
import socket
timeout = 10
socket.setdefaulttimeout(timeout)
my_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
url = input('Paste the url you want to copy: ')
try:
   headers = {}
   headers['User-Agent'] = my_UA
   req = urllib.request.Request(url, headers = headers)
   with urllib.request.urlopen(req) as response:
      char_set = response.headers.get_content_charset()
      html = response.read().decode(char_set)
   file_name = input("Give the name of the file to be created: ")
   file_format = input("Give the file formating (e.x. html, txt): ")
   with open (file_name+"."+file_format, "w", encoding = char_set) as p:
      p.write(html)
except urllib.HTTPError as e:
      print(e.code)
      print("HTTP Error")
except urllib.error.URLError as e:
   if hasattr(e, 'reason'):
      print('Connection Server Error')
      print("Due to :", e.reason)
else:
   print("--- {} created ---".format(file_name+"."+file_format))
   

