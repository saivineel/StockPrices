import shutil,os,time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

project_dir=os.path.join(base_dir,"SimpleTask")

rawdate=str(time.strftime("%d%m%y"))

zip_file_name = "EQ"+rawdate+"_CSV.ZIP"
csv_file_name = "EQ"+rawdate+".CSV"

zip_source=os.path.join(project_dir,zip_file_name)
csv_source=os.path.join(project_dir,csv_file_name)

destination=os.path.join(project_dir,'Archive')

shutil.move(zip_source,destination)
print("CSV File moved to archive")

shutil.move(csv_source,destination)

print("ZIP File moved to archive")
