# Ejemplo de una expresion 42//6+7*3-39
resultado0 = 42//6+7*3-39
resultado1 = (42//6)+7*3-39 #//Prioridad 3}
resultado2 = (42//6)+(7*3)-39 # *Es la prioridad 3
resultado3 = ((42//6)+(7*3))-39 # + prioridad 4
resultado4 = (((42//6)+(7*3))-39) # - prioridad 5

print(resultado4)