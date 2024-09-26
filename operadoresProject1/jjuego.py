"cuantos dias has vivido "

from datetime import datetime

import datetime

nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
nacimiento = datetime.strptime(nacimiento, "%d/%m/%y")

hoy = datetime.now()

vida = (hoy - nacimiento).days

print(f"Has vivido: {vida} dias")

