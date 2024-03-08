userNameDB = "hidro45"
userpasswordDB = "admin123"

userName = input("Ingrese su usuario ")
userPassword = input("Ingrese su contraseña: ")

#Comparando las variables
if userName==userNameDB and userPassword==userpasswordDB: 
    print("exito")
else:
    print("credenciales erroneas")