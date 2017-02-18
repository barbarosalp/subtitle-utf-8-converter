import sys,os,pathlib,io,cchardet

if len(sys.argv) <= 1:
    print("ERROR: You should provide Source Path")    
    quit()

sourcePath = sys.argv[1]

if not sourcePath or sourcePath.isspace():
    print("ERROR: Source Path can not be null or empty string")    
    quit()

for path, subdirs, files in os.walk(sourcePath):
    for name in files:
        
        if (name.endswith(".srt") == False):
            continue

        filename = pathlib.PurePath(path, name)
        print("INFO: Processing: " + str(filename))

        with io.open(filename,'rb') as f:
            data = f.read()
            encoding = cchardet.detect(data)
        
        if encoding["encoding"] == "UTF-8":
            print("INFO: ALREADY-UTF8: " + str(filename))
        else:
            with io.open(filename,'r') as f:
                datatowrite = f.read()            

            with io.open(filename,'w', encoding='utf8') as f:
                f.write(datatowrite)

        print("INFO: DONE: " + str(filename))
            

