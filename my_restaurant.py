from tkinter import *



# iniciar ykinder

aplicacion = Tk()


# Operador

operador = ''


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
    
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)
    
def resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0,resultado)
    operador = ''
    
    


# Tamanño de Ventana
standard_size = '1120x630'
aplicacion.geometry(f'{standard_size}+30+30')

# prohibir maximizar
aplicacion.resizable(False, False)

# Titulo Aplicacion
titulo_personal = "OffiRe.staurant "
aplicacion.title(titulo_personal)

# Color de fondo
aplicacion.config(bg = 'coral1')


# Panel superior
panel_superio = Frame(aplicacion, bd = 1 , relief = FLAT)
panel_superio.pack(side = TOP)

# Etiqueta titulo panel superior
etiqueta_titulo = Label(panel_superio, text = "Sistema de Facturacion", fg = "cadet blue" ,
                        font=('Dosis', 58), bg='DarkSlateGray4', width = 23)


# Panel Izquierdo
panel_izq = Frame(aplicacion, bd = 1, relief = RAISED)
panel_izq.pack(side= LEFT)
# Etiquetas de panel Izquierdo



# Panel Costos
panel_costos = Frame(panel_izq, bd = 1 , relief= RAISED, bg = "cadet blue", padx = 50 )
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izq, text ='Comida', font = ('Dosis', 19 , 'bold'),
                           bd = 1 , relief = FLAT, fg = "cadet blue" )
panel_comidas.pack(side = LEFT)


# Panel bebidas
panel_bebidas = LabelFrame(panel_izq, text ='Bebidas', font = ('Dosis', 19 , 'bold'),
                           bd = 1 , relief = FLAT, fg = "cadet blue" )
panel_bebidas.pack(side = LEFT)


# panel Postres
panel_potres = LabelFrame(panel_izq, text ='Bebidas', font = ('Dosis', 19 , 'bold'),
                           bd = 1 , relief = FLAT, fg = "cadet blue" )
panel_potres.pack(side = LEFT)


# panel derecha
panel_der = Frame(aplicacion, bd = 1 , relief= FLAT)
panel_der.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_der, bd = 1, relief = FLAT, bg = 'DarkSlateGray4')
panel_calculadora.pack(side = RIGHT)

# panel recibo
panel_recibo = Frame(panel_der, bd = 1, relief = FLAT, bg = 'DarkSlateGray4')
panel_recibo.pack(side = RIGHT)

# panel botones
panel_boton = Frame(panel_der, bd = 1, relief = FLAT, bg = 'DarkSlateGray4')
panel_boton.pack(side = RIGHT)



# lista de  productos
platos_comida = ['Pollo', 'Cordero', 'Soya', 'Huevoaltom','Aguacates', 'Salmon', 'Merluza','Pizza']
bebidas_comida = ['agua','limonada','vino','cerveza', 'jugo de fruta', 'malteada', 'tes', 'kefir']
postre_comida = ['helado','fruta', 'browing','flan', 'stevia', 'panelas', 'merengones', 'trufas']






# Presentacion Comida
cuadro_entrada_comida = []
texto_entra_comida = []
variable_comida = []


contador = 0
for comida in  platos_comida:
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    cuadro_entrada_comida.append('')
    texto_entra_comida.append('')
    texto_entra_comida[contador] = StringVar()
    texto_entra_comida[contador].set('*')
    
    comida = Checkbutton(panel_comidas, 
                         text = comida.title(), 
                         font = ('Dosis', 19, 'bold'), 
                         onvalue = 1, 
                         offvalue = 0 , 
                         variable = variable_comida[contador])
    comida.grid(row = contador, 
                column = 0 ,
                sticky = W)
    
    # Cuadro de Entrada de datos comida

    cuadro_entrada_comida[contador] = Entry(panel_comidas, 
                                            font = ('Dosis', 18, 'bold'),
                                            bd = 1,
                                            width = 6,
                                            state = DISABLED,
                                            textvariable =  texto_entra_comida[contador]            
                                        
                                            )
    cuadro_entrada_comida[contador].grid(row = contador,
                                         column = 1)
    contador += 1 
    
    
    
    
    
    
# Presentacion Bebida
cuadro_entrada_bebida = []
texto_entrada_bebida = []
variable_bebidas = []


contador = 0
for bebida in  bebidas_comida:
    cuadro_entrada_bebida.append('')
    variable_bebidas.append('')
    texto_entrada_bebida.append('')
    variable_bebidas[contador] = IntVar()
    texto_entrada_bebida[contador] = StringVar()
    texto_entrada_bebida[contador].set('*')
    
    bebida = Checkbutton(panel_bebidas, text =  bebida.title(), font = ('Dosis', 19, 'bold'), 
                         onvalue = 1, 
                         offvalue = 0 , 
                         variable = variable_bebidas[contador])
    bebida.grid(row = contador, column = 0 , sticky = W)
    
    # Entrada de  datos bebida
    texto_entrada_bebida.append('')
    cuadro_entrada_bebida[contador] = Entry(panel_bebidas, 
                                            font = ('Dosis', 18, 'bold'),
                                            bd = 1,
                                            width = 6,
                                            state = DISABLED,
                                            textvariable =  texto_entrada_bebida[contador])        
                                        
    
    
    
    cuadro_entrada_bebida[contador].grid(row = contador,
                                         column = 1)
    contador += 1 
    

# Presentacion Postre
cuadro_entrada_postre = []
texto_entrada_postre = []
variable_postre = []


contador = 0
for postre in  postre_comida:
    variable_postre.append('')
    cuadro_entrada_postre.append('')
    texto_entrada_postre.append('')
    variable_postre[contador] = IntVar()
    texto_entrada_postre[contador] = StringVar()
    texto_entrada_postre[contador].set('*')
    
    postre = Checkbutton(panel_potres, text = postre.title(), font = ('Dosis', 19, 'bold'), 
                         onvalue = 1, offvalue = 0 , variable= variable_postre[contador])
    postre.grid(row = contador, column = 0 , sticky = W)   
    
    
    # Entrada de datos 
    cuadro_entrada_postre[contador] = Entry(panel_potres, 
                                            font = ('Dosis', 18, 'bold'),
                                            bd = 1,
                                            width = 6,
                                            state = DISABLED,
                                            textvariable =  texto_entrada_postre[contador])   
    
    
    cuadro_entrada_postre[contador].grid(row = contador,
                                         column = 1)
    contador += 1 
    


# Etiquetas dede costo y campos de entrada


# variables 
val_costo_comida = StringVar()
val_costo_bebida = StringVar() 
val_costo_postre = StringVar() 
val_subtotal = StringVar() 
val_impuesto = StringVar() 
val_total = StringVar() 



# Etiquetas Comida
label_cost_comida = Label(panel_costos,
                          text =  'Costo Comida',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_cost_comida.grid(row = 0, column = 0)

texto_costo_comida = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_costo_comida)

texto_costo_comida.grid(row = 0, column= 1, padx = 41)
# Etiquetas Bebida
label_cost_bebida = Label(panel_costos,
                          text =  'Costo Bebida',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_cost_bebida.grid(row = 1, column = 0)
texto_costo_bebida = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_costo_bebida)

texto_costo_bebida.grid(row = 1, column = 1, padx = 41)

# Etiqueta Postre
label_cost_postre = Label(panel_costos,
                          text =  'Costo Postre',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_cost_postre.grid(row = 2, column = 0)
texto_costo_postre = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_costo_postre)

texto_costo_postre.grid(row = 2, column = 1)


# Etiqueta SubTotal
label_subtotal = Label(panel_costos,
                          text =  'SubTotal',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_subtotal.grid(row = 0, column = 2)
texto_subtotal  = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_subtotal)

texto_subtotal.grid(row = 0, column = 3, padx = 41)


# Etiqueta Impuestos
label_impuestos = Label(panel_costos,
                          text =  'Impuestos',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_impuestos.grid(row = 1, column = 2)
texto_impuestos  = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_impuesto)

texto_impuestos.grid(row = 1, column = 3, padx = 41)


# Etiqueta Total
label_total = Label(panel_costos,
                          text =  'Total',
                          font =  ('Dosis', 12 , 'bold'),
                          bg = 'cadet blue',
                          fg = 'white')
label_total.grid(row = 2, column = 2)
texto_total  = Entry(panel_costos,
                           font = ('Dosis', 12 ,'bold'),
                           bd = 1,
                           width = 10 ,
                           state = 'readonly',
                           textvariable=val_total)

texto_total.grid(row = 2, column = 3,padx = 41 )

# Botones

botones = ['Total', 'Recibo', 'Guradar', 'Resetear']
columna = 0
for boton in botones:
    boton = Button(panel_boton,
                   text = boton.title(),
                   font = ('Dosis', 14, 'bold'),
                   fg = 'white',
                   bg = 'cadet blue',
                   bd = 1,
                   width = 9)
    
    boton.grid(row = 0, column = columna)
    columna += 1 



# Area Recibo

texto_recibo = Text(panel_recibo,
                    font = ('Dosis', 14, 'bold'),
                    bd = 1,
                    width = 42,
                    height = 10
                    )
texto_recibo.grid(row = 0, column= 0 )

# Calculadora

visor_calculadora = Entry(panel_calculadora,
                          font = ('Dosis', 14 , 'bold'),
                          width = 16,
                          bd = 1)
visor_calculadora.grid(row = 0, column = 0, columnspan = 4)

# Botones Calculadora

botones_calculadora = ['7','8','9','+', '4', '5', '6', '-', '1','2', '3', 'x',
                        'CE', 'B', '0', '/']

botones_generados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
            text = boton.title(),
            font = ('Dosis', 16, 'bold'),
            fg = 'white',
            bg = 'cadet blue',
            bd = 1,
            width = 5)
    
    botones_generados.append(boton)

    boton.grid(row = fila, column = columna)
    
    if columna == 3 :
        fila += 1
    
    columna +=1
    
    if columna == 4 :
        columna = 0
        
 
                        
botones_generados[0].config(command = lambda : click_boton('7'))
botones_generados[1].config(command = lambda : click_boton('8'))
botones_generados[2].config(command = lambda : click_boton('9'))
botones_generados[3].config(command = lambda : click_boton('+'))
botones_generados[4].config(command = lambda : click_boton('4'))
botones_generados[5].config(command = lambda : click_boton('5'))
botones_generados[6].config(command = lambda : click_boton('6'))
botones_generados[7].config(command = lambda : click_boton('-'))
botones_generados[8].config(command = lambda : click_boton('1'))
botones_generados[9].config(command = lambda : click_boton('2'))
botones_generados[10].config(command = lambda : click_boton('3'))
botones_generados[13].config(command =  lambda : borrar())
botones_generados[12].config(command = lambda : resultado())
botones_generados[11].config(command = lambda : click_boton('x'))
botones_generados[14].config(command = lambda : click_boton('0'))
botones_generados[15].config(command = lambda : click_boton('/'))



    
        
        





# Establecer cuatricula
etiqueta_titulo.grid(row = 0, column = 0)


# evitar cieere de patalla
aplicacion.mainloop()




