import requests

def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        print("Dowloading...")
        with open("C:/Users/Edi_CeM24/Desktop/" + local_filename, 'wb') as f:
            print("write data to file")
            for chunk in r.iter_content(chunk_size=9192):
                f.write(chunk)
        f.close()
        print("Download complete")
        print("File saved as" +  local_filename)

while 1:
    print("Welcome to the image downloader!")
    image_url = input(str('Image_url: '))
    #print(local_filename)
    download_files(image_url) 
    download_files(image_url)
    print("Thank you!")
    break