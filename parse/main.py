import zipfile 

try: 
    with zipfile.ZipFile('examples/resources/pg8438-images-3.epub') as archive:
        archive.printdir()
except zipfile.BadZipFile as err:
    print (err) 

try: 
    with zipfile.ZipFile('/mnt/c/Users/anp/Downloads/Walter Isaacson - Elon Musk-Simon & Schuster (2023).epub') as archive:
        archive.printdir()
except zipfile.BadZipFile as err:
    print (err) 
