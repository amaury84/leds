import pyfirmata                              # Librería para comunicarse con Arduino

# INICIO DEL PUERTO USB
puertoUSB = "COM3"                            # Define el puerto USB donde conecta Arduino
                                              # VARIABLE 1 = "COM3"

print("Conectando con Arduino por USB...")    # Habilita la comunicación con Arduino
controlArdu = pyfirmata.Arduino(puertoUSB)    # VARIABLE 2 = Librería.Arduino(VARIABLE 1)

print("Conexión Exitosa...")
pyfirmata.util.Iterator(controlArdu).start()  # Prepara la transmisión de datos...(VARIABLE 2)

# DEFINIR PINES Y VARIABLES
sensor = controlArdu.get_pin('d:2:i')         # Configura el pin de entrada
                                              # VARIABLE 3 = VARIABLE 2.get_pin('digital:pin:entrada')
                                              
sensor.enable_reporting()                     # Controla la cantidad de información
                                              # VARIABLE3.enable_reporting()  

actuador = controlArdu.get_pin('d:13:o')      # Configura el pin de salida
                                              # VARIABLE 4 = VARIABLE 2.get_pin('digital:pin:salida')

# INICIO DEL PROGRAMA
while True:                                   # Mientras que este en verdadero ejecute...
    # RECIBE DESDE ARDUINO POR EL USB
    if sensor.read():                         # if VARIABLE 3.read() ** Si hay Lectura datos del SENSOR ingrese
       print("Pulsado...")                    # print("Pulsado...")                 
       # TRANSMITE HACIA ARDUINO POR EL USB
       actuador.write(1)                      # VARIABLE 4 . write(1) ** Escriba 1 o HIGH en el ACTUADOR                       
       controlArdu.pass_time(0.5)             # VARIABLE 2 . pass_time(0.5) ** Espere medio segundo
       actuador.write(0)                      # VARIABLE 4 . write(0) ** Escriba 0 o LOW en el ACTUADOR                       
       controlArdu.pass_time(0.5)             # VARIABLE 2 . pass_time(0.5) ** Espere medio segundo
    else:                                     # De lo contrario...
        print("NO Pulsado...")                # print("NO Pulsado...")
        controlArdu.pass_time(1)              # VARIABLE 2 . pass_time(0.5) ** Espere medio segundo
        

