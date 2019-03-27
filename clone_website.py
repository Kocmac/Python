import urllib.request
url = urllib.request.Request (input('Paste the url you want to copy: '))
with urllib.request.urlopen(url) as response:
   char_set = response.headers.get_content_charset()
   html = response.read().decode(char_set)
file_name = input("Give the name of the file to be created: ")
file_format = input("Give the file formating (e.x. html, txt): ")
with open (file_name+"."+file_format, "w", encoding = char_set) as p:
   p.write(html)
