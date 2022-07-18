import os
import py_compile
import sys
from string import Template

class CreadorHtml:
    def _init_(self, nombreArchivo, transacciones, cliente):
        self.nombreArchivo = nombreArchivo
        self.transacciones = transacciones
        self.cliente = cliente

    def crearHtml(self):
        content = self.obtenerContenidoHtml()
        self.reemplazarHtml(content)

    def obtenerContenidoHtml(self):
        contentHtml = ''
        for transaccion in self.transacciones:
            row = '<tr><td>'+transaccion['fecha']+'</td><td>' + transaccion['tipo']+'</td><td>' + transaccion['estado']+'</td><td>' + str (transaccion['monto'])+'</td><td>' + transaccion['razon']+'</td></tr>'
            contentHtml += row
        return contentHtml
    
    def reemplazarHtml(self, content):
        filein = open('template/listadoop.html')
        src = Template(filein.read())
        d = {'content': content}
        result = src.substitute(d)
        try:
            os.mkdir("output")
            filein2 = open('output/'+"File"+'.html','a')
            filein2.writelines(result)
            print("creando carpeta")
            print("guardando archivos")
        except OSError:
            if os.path.exists('output'):
                filein2 = open('output/'+"Archivo"+'.html','a')
                filein2.writelines(result)
                print("guardando archivo")
        while True:
            pregunta = input("presione N si quiere continuar y S si quiere salir ")
            if pregunta == "N":
                os.system(r"output.py")
            elif pregunta == "S":
                sys.exit()