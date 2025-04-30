

correo_usuario = input("Ingrese su correo electronico: ")
def correo_electronico(variable):
 email = False
 for x in variable: 
  if x == "@":
   email = True

 if email == True:
  print(f"Correo Electronico {variable} valido ")
 else:
  print("El correo Electronico no es valido")

correo_electronico(correo_usuario)