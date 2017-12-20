import shutil,os,time,urllib

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

project_dir=os.path.join(base_dir,"SimpleTask")

rawdate=str(time.strftime("%d%m%y"))

zip_file_name = "EQ"+rawdate+"_CSV.ZIP"

destination=os.path.join(project_dir,'Archive')

Bselocation='http://www.bseindia.com/download/BhavCopy/Equity/'+ zip_file_name

print( Bselocation )



required_file=os.path.join(project_dir,zip_file_name)

print(required_file) 

urllib.urlretrieve(Bselocation,required_file)

print(" Bhav file downloaded ")
