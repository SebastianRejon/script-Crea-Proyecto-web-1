import os
def generaProyecto():
    """
    Crea la estrucuta base de un proyecto web.
    WebProyecName
        |
        +---css
        +---img
        +---js
        +---pages
        +---recursos
        +---index.html

    Args:
        str: (WebProyecName) nombre carpeta contenedora proyecto

    Returns:
        estructura arbol de directorios base
    """
    ruta=os.getcwd()
    nombres=["css","js","img","pages","recursos"]
    nombreProy=input("nombre proyecto [carpeta contenedora]: ")
    os.mkdir(nombreProy)
    ruta=ruta+'\\'+nombreProy
    nombreIndex=ruta+'\\'+"index.html"
    os.chdir(ruta)
    for i in nombres:
        os.mkdir(i)
    open(nombreIndex,"w")

if __name__ == "__main__":
    generaProyecto()
input()
