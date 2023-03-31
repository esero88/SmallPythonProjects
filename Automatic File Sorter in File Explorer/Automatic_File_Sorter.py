# os stands for 'Operating System', shutil allows us to do high level operations on our files in file explorer
import os, shutil 

# r makes this a raw text without r it reads backslashes, colons
path = r"C:/Users/Eser/Desktop/Python/Files/" 

# os.listdir(path) show the path location files
file_name = os.listdir(path)

folder_names = ['csv files', 'excel files', 'json files', 'png files', 'text files']

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file , (path + "csv files/" + file))
    elif ".xlsx" in file and not os.path.exists(path + "excel files/" + file):
        shutil.move(path + file , (path + "excel files/" + file))
    elif ".json" in file and not os.path.exists(path + "json files/" + file):
        shutil.move(path + file , (path + "json files/" + file))
    elif ".png" in file and not os.path.exists(path + "png files/" + file):
        shutil.move(path + file , (path + "png files/" + file))
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file , (path + "text files/" + file))