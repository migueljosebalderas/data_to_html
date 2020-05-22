from mcore.html_data import data_to_html

datos = [["Nombre", "Apellidos", "Edad"],
         ["Juan", "Perez", 20],
         ["Licia", "Carrillo", 21],
         ["Carmen", "Gomez", 22],
         ["Alicie", "Smith", 23],
         ["Pedro", "Lopez", 24]
         ]

if __name__ == '__main__':
    data_to_html(datos, "Select * from datos where 1=1", "datos_p1.html")