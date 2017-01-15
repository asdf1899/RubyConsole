#-*- coding: UTF-8 -*-

def main():
    PATH = readConfig()


def readConfig():
    f = open("config.txt")
    for ff in f.readlines():
        file= ff.strip()
    if file != file + "/":
        file= file+ "/"
    return file

if __name__ == '__main__':
    main()
