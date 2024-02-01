import os, shutil as sh
def main():
    dir1 = os.getcwd()
    dir2 = str(input("Input the destination directory: "))   
    with os.scandir(dir1) as it:
        for entry in it:
            if (not entry.name.startswith('.') and entry.is_file()) and entry.name is not "Script.py":
                sh.copy(entry.path, dir2)




    return 0
if __name__ == "__main__":
    main()
