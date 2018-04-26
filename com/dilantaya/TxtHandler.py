#


def split_file(fileName,keyWord):
    f=open(fileName)
    for each_line in f:
        if  keyWord in each_line:
            print(each_line)
    
    f.close()
    return



split_file("g://logs/exceptionLog.txt",'ClassNotFoundException')
            