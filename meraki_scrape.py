from bs4 import BeautifulSoup
import requests
import sys
import os.path
import shutil
import zipfile

# change this
# url = 'http://merakiscans.com/runway-de-waratte/9/'
# url = 'http://merakiscans.com/mogusa-san/13/'
url = 'http://merakiscans.com/dokgo2/17/'

def scrape_html_for_data(url):
    html_response = requests.get(url).content
    soup = BeautifulSoup(html_response, "html.parser")
    main_imgs = soup.find_all('img')

    meta_info = main_imgs[2]['alt'][:-4].split(' - ', 1)
    series_title, chapter_name = meta_info[0], meta_info[1]
    chapter_number = url.split('/')[-2]
    folder_name = series_title + ' - ch ' + chapter_number + ' [Meraki Scans]/'
    
    return(main_imgs, series_title, chapter_name, chapter_number, folder_name)

def create_directory(folder_name):
    abs_path = os.path.abspath(sys.argv[0]) 
    current_dir = os.path.dirname(abs_path) # current script directory
    output_dir = current_dir + '/' + folder_name
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print("Folder created: ", folder_name)
    return(output_dir, current_dir)
    
def download_images(main_imgs, series_title, chapter_name):    
    for img_tag in main_imgs[3:-2]:
        img_url = img_tag['src']
        response = requests.get(img_url)
        page_num = img_tag['src'].split('/')[-1]
        filename = chapter_name + '_'+ page_num 
        
        if response.status_code == 200:
            with open(output_dir+'/'+filename, 'wb') as f:
                f.write(response.content)
        
        #print progress after img write
        print("Downloading page: " + page_num + " out of " + main_imgs[-3]['src'].split('/')[-1], end="\r")
        print("Download complete.", end="\r")


## method 1 - folder depth 1 ##
def create_zip_depth_one(output_dir, current_dir, folder_name):
    shutil.make_archive(output_dir, 'zip', current_dir, folder_name)
    print(folder_name+".zip created. \nDone.")


## method 2 folder depth 0 ##
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

main_imgs, series_title, chapter_name, chapter_number, folder_name = scrape_html_for_data(url)
output_dir, current_dir = create_directory(folder_name)
download_images(main_imgs, series_title, chapter_name)
create_zip_depth_one(output_dir, current_dir, folder_name)

# zipf = zipfile.ZipFile(folder_name[:-1]+'.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir(folder_name, zipf)
# zipf.close()