import os

def Arrangefiles(path):
    files=os.listdir(path)
    extension=[]
    for file in files:
        ext = os.path.join(path,os.path.splitext(file)[1][1:])       # ----> extensions  ex: pdf,exe, jpg,mp3,zip
        if ext not in extension:
            extension.append(ext)

    for folder in extension:
        try:
             os.mkdir(folder)
        except:pass
        for file in files:
            if os.path.split(folder)[1] == os.path.splitext(file)[1][1:]:
                os.rename(os.path.join(path,file),os.path.join(folder,file))

if __name__=="__main__":
    path=r"D:\Logith project\Nivas"
    Arrangefiles(path)