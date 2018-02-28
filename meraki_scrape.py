from bs4 import BeautifulSoup
import requests
import sys
import os.path
import shutil

# change this url
url = 'http://merakiscans.com/runway-de-waratte/9/'

def scrape_html_for_data(url):
    # grab html response and get soup
    html_response = requests.get(url).content
    soup = BeautifulSoup(html_response, "html.parser")
    img_tags = soup.find_all('img')
    # grab relevant metadata
    meta_info = img_tags[2]['alt'][:-4].split(' - ', 1)
    series_title, chapter_name = meta_info[0], meta_info[1]
    chapter_number = url.split('/')[-2]
    folder_name = series_title + ' - ch ' + chapter_number + ' [Meraki Scans]/'
    
    return(img_tags, series_title, chapter_name, chapter_number, folder_name)

    
def create_directory(folder_name):
    abs_path = os.path.abspath(sys.argv[0]) 
    current_dir = os.path.dirname(abs_path) # current script directory
    output_dir = current_dir + '/' + folder_name
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print("Folder created: ", folder_name[:-1])
    return(output_dir, current_dir)
    
    
def download_images(img_tags, series_title, chapter_name):    
    for img_tag in img_tags[3:-2]:
        img_url = img_tag['src']
        response = requests.get(img_url)
        page_num = img_tag['src'].split('/')[-1]
        filename = chapter_name + '_'+ page_num 
        
        if response.status_code == 200:
            with open(output_dir+'/'+filename, 'wb') as f:
                f.write(response.content)
        
        #print progress after img write
        print("Downloading page: " + page_num + " out of " + img_tags[-3]['src'].split('/')[-1], end="\r")
        print("Download complete.", end="\r")

        
def create_zip_depth_one(output_dir, current_dir, folder_name):
    shutil.make_archive(output_dir, 'zip', current_dir, folder_name)
    print("Zip file created: "+folder_name[:-1]+".zip.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    try:
        img_tags, series_title, chapter_name, chapter_number, folder_name = scrape_html_for_data(url)
    except:
        sys.exit("HTML was invalid. Please use a valid Meraki chapter url. \nOtherwise Contact asdfblarg with details.")
        
    output_dir, current_dir = create_directory(folder_name)
    download_images(img_tags, series_title, chapter_name)
    create_zip_depth_one(output_dir, current_dir, folder_name)
    print(Done)
