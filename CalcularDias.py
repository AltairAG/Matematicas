from datetime import datetime, date  # Se importa la libreria para poder manejar cadenas como datatime.

def calcular_dias_navidad():
    try:
        # Fecha actual
        fecha_actual = datetime.now()
        año_actual = fecha_actual.year
        
        
        # Calcular la Navidad más cercana desde la fecha actual
        navidad_actual = datetime(año_actual, 12, 25)
        
        
        if fecha_actual > navidad_actual:
            # Si ya pasó la Navidad de este año, usar la del próximo año
            navidad_actual = datetime(año_actual + 1, 12, 25)
        
        
        # Pedir al usuario una fecha en formato día/mes/año
        fecha_usuario = input("Ingresa una fecha en el formato: (dd/mm/aaaa): ")          # Se ingresa la fecha en formato de cadena.
        fecha_usuario = datetime.strptime(fecha_usuario, "%d/%m/%Y")                      # Se analiza 2 parámetros(cadena, formato de la fecha que esperamos).
        
        
        # Calcular la diferencia de días.
        # Si se ingresa una fecha posterior.
        if fecha_usuario > navidad_actual:                                                                                   # Gracias a que ya las cadenas son datatime se pueden comparar. 
            fecha_ref = fecha_usuario
            año_ref = fecha_usuario.year
            navidad_ref = datetime(año_ref, 12, 25)
            
            if fecha_ref > navidad_ref:
                print("La fecha ingresada es superior a la fecha actual.")
                # Si ya pasó la Navidad de este año, usar la del próximo año
                navidad_ref = datetime(año_ref + 1, 12, 25)
                
                diferencia = navidad_ref - fecha_ref
                dias = diferencia.days
                print("De la fecha", fecha_usuario.strftime('%d/%m/%Y'), "a la próxima Navidad", navidad_ref.strftime('%d/%m/%Y'), "hay:", dias, "días.") # Se imprimir el resultado.
            
            else:
                diferencia = navidad_ref - fecha_ref
                dias = diferencia.days
                print("De la fecha", fecha_usuario.strftime('%d/%m/%Y'), "a la próxima Navidad", navidad_ref.strftime('%d/%m/%Y'), "hay:", dias, "días.") # Se imprimir el resultado.
            

            
            
        #Si se ingresa una fecha anterior.
        else:
            diferencia = navidad_actual - fecha_usuario                # Se resta la fecha de la navidad actual, a la fecha ingreso el usuario para sacar la diferencia y se guarda en la variable diferencia 
            dias = diferencia.days                                     # De esa variable se obtiene solo los dias guardados.
            print("De la fecha", fecha_usuario.strftime('%d/%m/%Y'), "a la próxima Navidad", navidad_actual.strftime('%d/%m/%Y'), "hay:", dias, "días.") # Se imprimir el resultado.

        # del fecha_actual, año_actual, navidad_actual, fecha_usuario, navidad_ref, 
    except ValueError:
        print("Formato de fecha inválido. Asegúrate de usar el formato dd/mm/aaaa.")            # Validar el formato de la fecha ingresada

    fecha_actual, año_actual, navidad_actual, fecha_usuario, fecha_ref, navidad_ref, año_ref, diferencia, dias = None, None, None, None, None, None, None, None, None # Se tienen quie reiniciar las variables ya que python nop se que chingados hace y si no se hace la proxima vez que se ejecuta el cod hace el calculo mal

# calcular_dias_navidad()


fechaf = datetime(2026, 1, 1)
fechai = datetime(2025, 1, 1)
dif = fechaf - fechai
print("el año: ", fechai.year, "Tiene: ",dif.days)