import os
import shutil

from_dir="c:\Users\asian\Downloads"
to_dir= "c:\Users\asian\Documents\Document_Files"

list_of_files=os.listdr(from_dir)
print(list_of_files)

for file_name in list_of_files:


    name,extension = os.path.splittext(file_name)


    if extension == '':
        continue
    if extension in ['.txt','.pdf', '.doc', '.docx']:


        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document Files"
        path3 = to_dir + '/' + "Document Files" + '/' + file_name


        if os.path.exists(path2):
            print("Moving" + file_name + "...")

            shutil.move(path1,path3)


        else:
            os.makedirs(path2)
            print("Moving" + file_name + "...")
            shutil.move(path1,path2)








    


    
    