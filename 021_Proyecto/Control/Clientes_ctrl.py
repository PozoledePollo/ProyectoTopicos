from Base_Datos.BDClientes import *
import re #EXPRESIONES REGULARES

class Clientes_ctrl(object):
    def __init__(self):
        pass

    def obtenerDatos(self):
        objBD = BDClientes()
        resp = objBD.obtenerDatos()
        return resp
    
    def borrarLogico(self, id):
        objBD = BDClientes()
        r = objBD.borrarLogico(id)
        return
    
    def validacionDatos(self, nom, pa, sa, tel, calle, col, num, cp, sal):
        # 1 txt | 2 tel | 3 num | 4 salario        
        ok = self.validTxt(nom)
        if(ok != True):
            return [1,"El Nombre"]
        
        ok = self.validTxt(pa)
        if(ok != True):
            return [1,"El Apellido Paterno"]
        
        ok = self.validTxt(sa)
        if(ok != True):
            return [1,"El Apellido Materno"]
        
        ok = self.validTel(tel)
        if(ok != True):
            return [2,"El Telefono"]
        
        ok = self.validTxt(calle)
        if(ok != True):
            return [1,"La Calle"]
        
        ok = self.validTxt(col)
        if(ok != True):
            return [1,"La Colonia"]
    
        ok = self.validNum(num)
        if(ok != True):
            return [3,"El Numero Exterior"]

        ok = self.validNum(cp)
        if(ok != True):
            return [3,"El Codigo Postal"]
        
        ok = self.validReal(sal)
        if(ok != True):
            return [4,"El Salario"]
        
        return [0, True]        


    def validReal(self, n):
        try:
            float(n)
            return True
        except ValueError:
            return False  

    def validNum(self, n):
        if(n.isdigit()):
            return True
        else:
            return False   
    
    def validTel(self, t):
        exp = r"^([\d]{3})\-?([\d]{3})\-?([\d]{4})$"
        resp = re.match(exp, t)
        if(resp is None):
            return False              
        else:
            return True


    def validTxt(self, n):
        lst = n.split(' ')
        k = 0
        for item in lst:
            if(item.isalpha()):
                k +=1

        if(k == len(lst)):
            return True
        else:
            return False
        
    def guardar(self, nom, pa, sa, tel, calle, col, num, cp, sal):
        db = BDClientes()
        si = db.guardar(nom, pa, sa, tel, calle, col, num, cp, sal)
        return si
