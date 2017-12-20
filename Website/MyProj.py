import cherrypy,os,sys,redis
from mako.template import Template

##cherrypy.config.update({'server.socket_host': '0.0.0.0',
##                        'server.socket_port': int(os.environ.get('PORT',80))
##                        
##                       })


class StockAnalysis(object):

    # Setting up the configuration file
    
    conf_path = os.path.dirname(os.path.abspath(__file__))
    configfile = os.path.join(conf_path, "MyProj.conf")
    cherrypy.config.update(configfile)
    
  
    #To retrieve the 10 stocks data and load in to the web page
    
    @cherrypy.expose
    def index(self):
        conn = redis.Redis('localhost')
        x=[]
        y=[]
        s=[]
        for i in range(0,10):
            del y
            del x
            x=[]
            y=[]
            x.append(conn.lrange('top10stocks',i,i))
            z=x[0]
            z=''.join(z)
            print z 
            data = conn.hgetall(z)
            print data
            y.append(data['SC_CODE'])
            y.append(data['SC_NAME'])
            y.append(data['HIGH'])
            y.append(data['LOW'])
            y.append(data['CLOSE'])
            y.append(data['OPEN'])
            a=y
            s.append(a)
        return Template(filename='index.html').render(s=s)

    #To fetch the stock details entered by the user
    
    @cherrypy.expose
    def findstock(self,stockname = None):
        try:
         if stockname:
            conn = redis.Redis('localhost')
            data = conn.hgetall(stockname)
            row=[]
            row.append(data['SC_CODE'])
            row.append(data['SC_NAME'])
            row.append(data['HIGH'])
            row.append(data['LOW'])
            row.append(data['CLOSE'])
            row.append(data['OPEN'])
            return Template(filename='search.html').render(row=row)
        except:
            
            return Template(filename='error.html').render()
            

if __name__ == '__main__':        
    cherrypy.quickstart(StockAnalysis())
         


   

