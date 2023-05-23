name="salem"
lastname = "jose"
fullname = (name + " "+ lastname)
age = 2
print(fullname)
print(name + " " + lastname)

#format
template = "hola, soy " + name + " y mi apellido es " + lastname + " y mi edad es ❤️  " + str(age) + " añitos"
print("v1 "+template)

template = "Hola, soy {} y mi apellido es {} y mi edad es 🌸 {} añitos".format(name, lastname,age)
print("v2 "+ template)

template=f"Hola, soy {name} y mi apellido es {lastname} y mi edad es 🎉 {age} añitos"
print("v3 " + template)