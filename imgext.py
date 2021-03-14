#####################################################################################
##              Simple program to download images from web                         ##
##              All images will be downloaded from stocksnap.io                    ##
##              Author: Anom Chakravorty | Github: anomic30                        ##
#####################################################################################
import requests
import bs4

print("*MAKE SURE TO CREATE A FOLDER BEFORE DOWNLOADING*")
type = input("\nWhat type of images do you want to download: ")
address = "https://stocksnap.io/search/" + type
drive_letter = input("Enter the drive letter: ").upper()
folder_name = input("Enter the folder name: ")
path=drive_letter+":/"+folder_name+"/"

source=requests.get(address,headers={'User-Agent': 'Mozilla/5.0'})

soup = bs4.BeautifulSoup(source.text, 'lxml')
# print(soup.prettify())
Images = []
img_links = soup.select('.photo-grid-item')
img_links = soup.select('img')
img_links=img_links[3:]
# print(img_links)
for i in range(len(img_links)):
    link=img_links[i]['src']
    Images.append(link)
# print(Images)
for i in range(len(Images)):
    print("Downloading "+Images[i])
    name = path+str(i)+".jpg"
    image_data = requests.get(Images[i], 'lxml')
    f = open(name, 'wb')
    f.write(image_data.content)
    f.close()
    
