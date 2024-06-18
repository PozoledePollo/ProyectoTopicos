import pyodbc

class Conexion(object):
    def  __init__(self):
        pass

    def conexionMariaDB(self):
        try:
            #print(pyodbc.drivers())
            txt = "DRIVER={MariaDB ODBC 3.1 Driver}; SERVER=localhost; "
            txt += "UID=root; PWD=admin; DATABASE=python; PORT=3306"
            conn = pyodbc.connect(txt)
        except Exception as err:
            conn = None
        return conn
    
    def query_all(self, con, sql):
        cur = con.cursor()
        cur.execute(sql)
        r = cur.fetchall()
        #RECUPERAR LOS HEADERS O NOMBRES DE LOS ATRIBUTOS
        nom = [column[0] for column in cur.description]
        resp = [nom, r]
        cur.close()
        return resp
    
    def exec_query(self, con, sql):
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        cur.close()
        return True
    
    def exist(self,c, sql):
        cur = c.cursor()
        cur.execute(sql)
        r = cur.fetchone()
        cur.close()
        if(r != None):
            return False
        else:
            return True
        
    def getNextID(self,c, sql):
        cur = c.cursor()
        cur.execute(sql)
        r = cur.fetchone()
        n = r[0] + 1
        cur.close()
        return n