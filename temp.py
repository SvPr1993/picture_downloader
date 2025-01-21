import requests

link_download = "https://cs15.pikabu.ru/post_img/2025/01/21/10/1737477652178649338.jpg"

link_clear = link_download.split("/")

print(link_clear)
print(link_clear[-1])


#response = requests.get(link_download)
#
#print(response)
#
#with open("image.jpg", "wb") as file:
#    file.write(response.content)
