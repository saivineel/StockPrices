import csv,redis,time,os

conn = redis.Redis('localhost')

#Generating the todays file name

rawdate=str(time.strftime("%d%m%y"))
file_name = "EQ"+rawdate+".CSV"


#Instead of hardcoing the path using the below to find the path of file name

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
simple_task=os.path.join(BASE_DIR,"SimpleTask")
file_path=os.path.join(simple_task,file_name)

#genearting a dictionary using the python library

input_file=csv.DictReader(open(file_path,'r'))

#Cleaning the database before insertion of todays data

conn.flushall()

count=0
top10='top10stocks'

#Loop to retrieve the data from the dictionary generated .

for row in input_file:

  required_fields=[]
		
  stock_name=row['SC_NAME'].strip()

  
  required_fields={"SC_NAME":stock_name, "SC_CODE":row['SC_CODE'], "OPEN":row['OPEN'], "HIGH":row['HIGH'],"LOW":row['LOW'],"CLOSE":row['CLOSE']}

  conn.hmset(stock_name, required_fields)
  print conn.hgetall(stock_name)
  
  if count <10:
      conn.rpush(top10,stock_name)

  count+=1

print "Total Count of Stocks is {stock_count}".format(stock_count = count)
