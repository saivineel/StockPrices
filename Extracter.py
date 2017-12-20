import time,shutil,zipfile,os

rawdate=str(time.strftime("%d%m%y"))

file_name = "EQ"+rawdate+"_CSV.ZIP"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
simple_task=os.path.join(BASE_DIR,"SimpleTask")
exact_path=os.path.join(simple_task,file_name)

zip = zipfile.ZipFile(exact_path)

zip.extractall(simple_task)

print("CSV File is Extracted")




