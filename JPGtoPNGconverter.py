import sys, osfrom PIL import Imagedef conversion(a, b):    entries = os.listdir(a + '/')    print(f"Folder '{a}' has some entries")        try:         os.mkdir(b + '/')        print(f"Creating new folder {b}")                for entry in entries:            try:                 img = Image.open(f"{a}/{entry}")                new_base = entry.split('.')[0]                                img.save(f"{b}/{new_base}.png", "png")            except:                continue                print('Conversion done.')                    except FileExistsError as err:         print(err)        print('Please use another foldername')arg1 = sys.argv[1]arg2 = sys.argv[2]print(arg1)print(arg2)conversion(arg1, arg2)#img = Image.open('Pokedek/pikachu.jpg')#print(img)        