from bs4 import BeautifulSoup
import urllib.request
import requests

# url = 'http://merakiscans.com/runway-de-waratte/9/'
# response = requests.get(url)
# html = response.content
# soup = BeautifulSoup(html, "html.parser")

# out_file = open("out.txt", "w")
# main_imgs = soup.find_all('img')



url = "http://merakiscans.com/wp-content/manga/36/9/00.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("sample.jpg", 'wb') as f:
        f.write(response.content)

        
# opener.retrieve("http://merakiscans.com/wp-content/manga/36/9/00.jpg", 'KappaHD.png')




# for img_tag in main_imgs[3:-2]:
    # # print(img_tag['src'])
    # # out_file.write(img_tag['src']+'\n')
    # print(img_tag['src'], img_tag['src'].split('/')[-1])
    # # urllib.request.urlretrieve(img_tag['src'], img_tag['src'].split('/')[-1])
    