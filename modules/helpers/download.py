import urllib.request

def download(url, name):
    name=name+".mp4"
    try:
        print("Downloading starts...\n")
        urllib.request.urlretrieve(url, name)
        print("Download completed..!!")
    except Exception as e:
        print(e)