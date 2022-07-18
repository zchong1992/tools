
import os
import sys
import codecs
import chardet

def getEncode(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        f_charInfo=chardet.detect(data)
        #print (f_charInfo)
        return f_charInfo['encoding']

def convert(filename,out_enc="UTF-8"):
    #print("deal file {0}".format(filename))
    encode=getEncode(filename)
    try:
        with open(filename, 'rb') as f:
            content = f.read()
            #print(filename+" is "+encode)
            if encode=="utf-8" or encode=="ascii":
                #print("pass")
                return 
            print(filename +" maybe "+encode)
            if encode=="GB2312":
                str=content.decode(encoding=encode)
                os.rename(filename,filename+"bak.java")
                codecs.open(filename,'w').write(str)
        return 
    except IOError as err:
        print("I/O error:{0}".format(err))
    

def explore(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            if os.path.splitext(file)[1]=='.java':
                #print (file)
                path=os.path.join(root,file)
                convert(path)

def main():
    if len(sys.argv) <2:
        print("need work dir ")
        return 
    print("work dir is {0}".format(sys.argv[1]))
    explore(sys.argv[1])


if __name__=="__main__":
    main()
