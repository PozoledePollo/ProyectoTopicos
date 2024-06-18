from .Conexion import *

class BDClientes(object):
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if(r != None):
            sql = "SELECT * FROM clientes WHERE activo = 1"
            resp = objCon.query_all(r, sql)
            r.close()
            return resp 
        else:
            return False
        
    def borrarLogico(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if(r != None):
            sql = "UPDATE clientes SET activo = 0 WHERE id = "+str(id)
            resp= objCon.exec_query(r, sql)
            r.close()
            return resp
        else: 
            return False
        
    def guardar(self, nom, pa, sa, tel, calle, col, num, cp, sal):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if(c != None):
            #VERIFICAR SI EXISTE EL REGISTRO EN LA BASE
            #SI NO EXISTE SE INSERTA
            sql = "select id from clientes  where nombre = \'"+nom+"\' "
            sql +="and primer_apellido =\'"+pa+"\' and segundo_apellido =\'"+sa+"\';"
            existe = objCon.exist(c, sql)
            sql =""
            if(existe != False):
                #NO EXISTE POR LO TANTO SE INSERTA
                sql = "SELECT max(id) FROM clientes;"
                n = objCon.getNextID(c, sql)
                sql =""
                sql ="INSERT INTO clientes VALUES("+str(n)+", "
                sql += "\'"+nom+"\', \'"+pa+"\', \'"+sa+"\', "
                sql += "\'"+tel+"\', \'"+calle+"\', \'"+col+"\', "
                sql += str(num)+", "+str(cp)+", "+str(sal)+", 1);"  
                ok = objCon.exec_query(c, sql)
                c.close()
                return ok
            else:
                return False