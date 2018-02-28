from bs4 import BeautifulSoup
import requests
import sys
import os.path
import shutil
import zipfile


url = 'http://merakiscans.com/runway-de-waratte/9/'
response = requests.get(url)
# html = response.content
# soup = BeautifulSoup(html, "html.parser")
# main_imgs = soup.find_all('img')

# # print(main_imgs[2]['alt'][:-3])

abs_path = os.path.abspath(sys.argv[0]) 
current_dir = os.path.dirname(abs_path) # current script directory
output_dir = current_dir+'/'+ '_ch_'.join(url.strip('/').split('/')[-2:])
# print(output_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# for img_tag in main_imgs[3:-2]:
    # img_url = img_tag['src']
    # response = requests.get(img_url)
    # filename = main_imgs[2]['alt'][:-3].replace(' ','_')+img_tag['src'].split('/')[-1]
    
    # if response.status_code == 200:
        # with open(output_dir+'/'+filename, 'wb') as f:
            # f.write(response.content)
    
    # print(img_tag['src'], img_tag['src'].split('/')[-1]) #print progress after write

# C:\Users\Zeng\PycharmProjects\meraki_scrape_test/runway-de-waratte_ch_9    
print(output_dir)
# shutil.make_archive("C:\Users\Zeng\PycharmProjects\meraki_scrape_test/runway-de-waratte_ch_9", 'zip', "C:\Users\Zeng\PycharmProjects\meraki_scrape_test\", 'runway-de-waratte_ch_9')
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            
zipf = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('runway-de-waratte_ch_9', zipf)
zipf.close()