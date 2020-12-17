from bullet import Password  
def menu_login():
  nom = []
  ape = []
  movi = []
  email = ['andres@gmail.com','fabian@gmail.com']
  nick = []
  pasww = [123,543]
  estado = []
  print("### Ingreso a la administracion ###")
  print("[1]. Ingresar")
  print("[2]. Crear cuenta")
  print("[3]. salir")
  opt=input("digite una opcion: ")

  if opt =='1': 
   emailp=input("E-mail: ")
   contraseña=input("Contraseña: ") 
   if emailp in email or contraseña in pasww :
    print("ingreso exitoso")
    print("***MENU DE ADMINISTRACION***")
    categorias = []
    proveedores = []
    productos = []
    clientes=[]
    reportes=[]
    print("[1]. categorias")
    print("[2]. proveedores")
    print("[3]. productos")
    print("[4]- clientes")
    print("[5]. reportes")
    opt1=input("digite una opcion")
    if opt1 == '1' : 
      print("[1]. ingresar nueva categoria")
      print("[2]. listar categorias")
      print("[3]. buscar categoria")
      print("[4]- eliminar categoria")
      print("[5]. modificar categoria")
      print("[6]. volver al menu principal")
      opt1=input("digite una opcion")

      if opt1 =='1':
       categoria1=input("ingresar nueva categoria")
       categorias.append(categoria1)
      
      elif opt1 == '2':
       print (categorias)

      elif opt1 =='3' :
       buscar=input("buscar en la lista")
       if buscar in categorias:
        print(buscar)   
       else :
         print("no se encuentra en la lista de categoria")
      elif opt1 =='4':
       print(categorias)
       elim=input("seleccione la posicion que desea eliminar")
       categorias.pop(elim-1)
      elif opt1 =='5':
       
       for x in range(len(categorias)):
         a=input("digite la posicion a modificar") 
         if categorias[x]== a :
            b=input("")  
            categorias[x] =b
      elif opt1 =='6':
       print("[1]. categorias")
       print("[2]. proveedores")
       print("[3]. productos")
       print("[4]- clientes")
       print("[5]. reportes")
       opt1=input("digite una opcion")
    if opt=='2':
      print("[1]. ingresar nuevo proveedor")
      print("[2]. listar proveedores")
      print("[3]. buscar proveedor")
      print("[4]- eliminar proveedor")
      print("[5]. modificar proveedor")
      print("[6]. volver al menu principal")
      opt1=input("digite una opcion")

      if opt1 =='1':
       proveedor1=input("ingresar nuevo proveedor")
       proveedores.append(proveedor1)
      
      elif opt1 == '2':
       print (proveedores)

      elif opt1 =='3' :
       buscar=input("buscar en la lista")
       if buscar in proveedores:
        print(buscar)   
       else :
         print("no se encuentra en la lista de categoria")
      elif opt1 =='4':
       print(proveedores)
       elim=input("seleccione la posicion que desea eliminar")
       proveedores.pop(elim-1)
      elif opt1 =='5':
       
       for x in range(len(proveedores)):
         a=input("digite la posicion a modificar") 
         if proveedores[x]== a :
            b=input("")  
            proveedores[x] =b
      elif opt1 =='6':
       print("[1]. categorias")
       print("[2]. proveedores")
       print("[3]. productos")
       print("[4]- clientes")
       print("[5]. reportes")
       opt1=input("digite una opcion")
    if opt=='3':
      print("[1]. ingresar nueva producto")
      print("[2]. listar productos")
      print("[3]. buscar productos")
      print("[4]- eliminar producto")
      print("[5]. modificar producto")
      print("[6]. volver al menu principal")
      opt1=input("digite una opcion")

      if opt1 =='1':
       producto1=input("ingresar nueva categoria")
       productos.append(producto1)
      
      elif opt1 == '2':
       print (productos)

      elif opt1 =='3' :
       buscar=input("buscar en la lista")
       if buscar in productos:
        print(buscar)   
       else :
         print("no se encuentra en la lista de categoria")
      elif opt1 =='4':
       print(productos)
       elim=input("seleccione la posicion que desea eliminar")
       productos.pop(elim-1)
      elif opt1 =='5':
       
       for x in range(len(productos)):
         a=input("digite la posicion a modificar") 
         if productos[x]== a :
            b=input("")  
            productos[x] =b
      elif opt1 =='6':
       print("[1]. categorias")
       print("[2]. proveedores")
       print("[3]. productos")
       print("[4]- clientes")
       print("[5]. reportes")
       opt1=input("digite una opcion")



    if opt=='4':
      print("[1]. ingresar nuevo cliente")
      print("[2]. listar clientes")
      print("[3]. buscar clientes")
      print("[4]- eliminar clientes")
      print("[5]. modificar clientes")
      print("[6]. volver al menu principal")
      opt1=input("digite una opcion")

      if opt1 =='1':
       cliente1=input("ingresar nueva categoria")
       clientes.append(cliente1)
      
      elif opt1 == '2':
       print (clientes)

      elif opt1 =='3' :
       buscar=input("buscar en la lista")
       if buscar in clientes:
        print(buscar)   
       else :
         print("no se encuentra en la lista de clientes")
      elif opt1 =='4':
       print(clientes)
       elim=input("seleccione la posicion que desea eliminar")
       clientes.pop(elim-1)
      elif opt1 =='5':
       
       for x in range(len(clientes)):
         a=input("digite la posicion a modificar") 
         if clientes[x]== a :
            b=input("")  
            clientes[x] =b
      elif opt1 =='6':
       print("[1]. categorias")
       print("[2]. proveedores")
       print("[3]. productos")
       print("[4]- clientes")
       print("[5]. reportes")
       opt1=input("digite una opcion")



    if opt=='5':
       print("reportes")
    if opt=='6':
       exit()     




   else : 
     print("datos invalidos")
     emailp=input("E-mail: ")
     contraseña=input("Contraseña: ")
  elif opt == '2' :
   print("formulario de registro")
   nombre = input("ingrese su primer nombre: " ) 
   apellido = input("ingrese su primer apellido: ")
   celular = input("digite su numero de celular: ")
   email1=input("digite su correo: ")
   while email1 in email :
     print ("el correo ya se encuentra registrado")
     email1=input("digite su correo: ")
   nickname = input("ingrese su nickname: ")
   while email1 in email :
     print ("el nickname ya se encuentra registrado")
     nick=input("digite su nickname: ")
   contraseña = Password("Contraseña: ")
   p= contraseña.launch()
   
   
   nom.append(nombre)
   ape.append(apellido)
   movi.append(celular)
   email.append(email1)
   nick.append(nickname)
   pasww.append(contraseña)
   estado.append(True)

  else  :
    print("vuelve pronto, ¡chao!")  

  ##print(nom,"\n",ape,"\n",movi,"\n",email,"\n",nick,"\n",pasww,"\n",estado)
  