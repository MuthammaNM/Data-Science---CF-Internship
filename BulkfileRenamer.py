import os

def renamer():
    i=0
    path = "C:\\Users\\User\\Desktop\\rename\\img\\"
    for filename in os.listdir(path):
        names = f"image .{i}.jpg"
        src = path + filename
        dist = path +names

        os.rename(src,dist)
        i=i+1

if __name__ == "__main__":
    renamer()

        