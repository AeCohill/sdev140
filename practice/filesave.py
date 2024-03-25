import urllib.request
def SaveFile():
    filename = input('enter a file name to save to: ')
    URL = input('input a url: ')

    urllib.request.urlretrieve(URL, filename)

SaveFile()
