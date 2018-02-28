from bs4 import BeautifulSoup
import requests
import sys
import os.path
import shutil
import zipfile

# change this
# url = 'http://merakiscans.com/runway-de-waratte/9/'
url = 'http://merakiscans.com/mogusa-san/13/'

html_response = requests.get(url).content
soup = BeautifulSoup(html_response, "html.parser")
main_imgs = soup.find_all('img')

meta_info = main_imgs[2]['alt'][:-4].split(' - ', 1)
series_title, chapter_name = meta_info[0], meta_info[1]



abs_path = os.path.abspath(sys.argv[0]) 
current_dir = os.path.dirname(abs_path) # current script directory
folder_name = series_title + ' - ch ' + url.split('/')[-2] + ' [Meraki Scans]/'
output_dir = current_dir + '/' + folder_name
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
print("Creating folder: ", output_dir)

for img_tag in main_imgs[3:-2]:
    img_url = img_tag['src']
    response = requests.get(img_url)
    page_num = img_tag['src'].split('/')[-1]
    # filename = main_imgs[2]['alt'][:-3].replace(' ','_')+img_tag['src'].split('/')[-1]
    filename = chapter_name + '_'+ page_num 
    
    if response.status_code == 200:
        with open(output_dir+'/'+filename, 'wb') as f:
            f.write(response.content)
    
    #print progress after img write
    print("Downloading page: " + page_num + " out of " + main_imgs[-3]['src'].split('/')[-1], end="\r") 


## method 1##
shutil.make_archive(output_dir, 'zip', current_dir, folder_name)
print(folder_name+".zip created. Done.")
# shutil.make_archive(output_dir, 'zip', "C:/Users/Zeng/PycharmProjects/meraki_scrape_test/", 'runway-de-waratte_ch_9')

# ## method 2##
# def zipdir(path, ziph):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))
#            
# zipf = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('runway-de-waratte_ch_9', zipf)
# zipf.close()