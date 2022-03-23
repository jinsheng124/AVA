def geturl(file):
    if file == "test.txt":
        begin_with = "https://s3.amazonaws.com/ava-dataset/test/"
    elif file == "trainval.txt":
        begin_with = "https://s3.amazonaws.com/ava-dataset/trainval/"
    with open(file,"r") as f:
        total_line = f.readlines()
    cur_line = ""
    for tl in total_line:
        cur_line+=(begin_with+tl)
    with open(file.split(".")[0]+"_url.txt","w") as f:
        f.write(cur_line)
if __name__=="__main__":
    geturl("test.txt")
    geturl("trainval.txt")



