import os

def renamer():
    i=0
    path = "C:\\Users\\Namratha Muthamma\\OneDrive\\Documents\\data analyst\\Vs code\\img\\"
    for filename in os.listdir(path):
        names = f"capture.{i}.jpg"
        src = path + filename
        dist = path +names

        os.rename(src,dist)
        i=i+1

if __name__ == "__main__":
    renamer()

        