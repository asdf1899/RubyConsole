#-*- coding: UTF-8 -*-
import shutil, os


def main():
    print("Portable Ruby Console v1.0")
    print(" ")
    print("Modify the config file to set your ruby path")
    PATH = readConfig()
    print("Current path: " + PATH)
    print(" ")
    print("Type '2' (help) for config information")
    print(" ")
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
                try:
                    execute(PATH, filename)
                except IOError:
                    print("Error: this path " + PATH + " doesn't exit")
                    print(" ")
            except IOError:
                print("Error: File not found - " + filename)
                print(" ")
        elif shell == "2":
            Help(PATH)
        elif shell == "3":
            break

def execute(PATH, filename):
    currentFile = os.path.realpath(filename)
    shutil.copy2(currentFile, PATH + "temp.rb")
    os.popen("start " + PATH+ "irb " + PATH+"temp.rb").read()
    #os.startfile(PATH +"ruby-console.bat")

def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

def Help(PATH):
    print(" ")
    print("Portable Ruby Console v1.0 Copyright 2016 Anas Araid")
    print(" ")
    print("Current path: " + PATH)
    print(" ")
    print("Set your ruby bin folder path in the config.txt ")
    print("The path MUST NOT have spaces or quotation marks. So move it somewhere else. ")
    print("Ex. wrong path --> 'C:/Program Files (x86)/ruby-version-mingw32/bin'")
    print("Ex. right path --> 'C:/ruby-version-mingw32/bin' ")
    print(" or C:/Users/YourNameWithoutSpaces/Desktop/ruby-version-mingw32")
    print(" ")
    print("Insert the script file name with the extension.")
    print("Ex. filename.rb")
    print(" ")
    

if __name__ == '__main__':
    main()
