#-*- coding: UTF-8 -*-
import shutil, os


def main():
    PATH = readConfig()
    while True:
        print("1) Run a ruby script")
        print("2) Help")
        print("3) Exit")
        shell = input(">> ")
        if shell == "1":
            try:
                print("Insert the file name with the extension")
                filename = input("$> ")
                open(filename)            
                execute(PATH, filename)
            except IOError:
                print("Error: File not found - " + filename)
        elif shell == "2":
            #Help(PATH)
            pass
        elif shell == "3":
            break

def execute(PATH, filename):
    currentFile = os.path.realpath(filename)
    shutil.copy2(currentFile, PATH + "temp.rb")
    os.popen("start " + PATH+ "irb " + PATH+"temp.rb").read()
    #os.startfile(PATH +"ruby-console")

def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

if __name__ == '__main__':
    main()
