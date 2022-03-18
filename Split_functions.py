def Separar_grupos_1(Dic_pages,pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 1]
		value = value + 1
		key = key + 1
	return Dic_pages

def Separar_grupos_2(Dic_pages, pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 2]
		value = value + 2
		key = key + 1
	return Dic_pages

def Separar_grupos_3(Dic_pages, pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 3]
		value = value + 3
		key = key + 1
	return Dic_pages

def Separar_grupos_5(Dic_pages, pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 5]
		value = value + 5
		key = key + 1
	return Dic_pages

def Separar_grupos_10(Dic_pages, pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 10]
		value = value + 10
		key = key + 1
	return Dic_pages

def Separar_grupos_20(Dic_pages, pages, key, value):
	while  key < pages:
		Dic_pages[key] = [value, value + 20]
		value = value + 20
		key = key + 1
	return Dic_pages

def error():
	return 'fuera de rango'

switch_semana = {
	1: Separar_grupos_1,
	2: Separar_grupos_2,
	3: Separar_grupos_3,
	4: Separar_grupos_5,
	5: Separar_grupos_10,
	6: Separar_grupos_20
}

# menu = """Presionar un número para separar el PDF:
# 1: Separar en grupos de (1)
# 2: Separar en grupos de (2) 
# 3: Separar en grupos de (3) 
# 4: Separar en grupos de (5) 
# 5: Separar en grupos de (10) 
# 6: Separar en grupos de (20) 
# 7: Salir/Cancelar
# """
# print(menu)
# option = int(input())

# Dic_pages = {} 
# pages = 20
# key = 0
# value = 0


# print(switch_semana.get(option, error)(Dic_pages, pages, key, value))


""" class Vivienda:
	temperatura_maxima = -100

	def __init__(self, temperatura):
		self.temperatura_actual = temperatura
		print('recorriendo el constructor')
		self.registrar_temperatura(temperatura)
		print(f'temp_actual: {self.temperatura_actual}')
	
	def registrar_temperatura(self, nueva_temperatura):
		self.temperatura_actual = nueva_temperatura
		print('recorriendo el metodo')
		if self.temperatura_actual > self.temperatura_maxima:
			self.__class__.temperatura_maxima = self.temperatura_actual


v1 = Vivienda(13)
v2 = Vivienda(11)
v3 = Vivienda(12)

v1.registrar_temperatura(25)
v2.registrar_temperatura(22)
v3.registrar_temperatura(21)

print(f'la temperatura máxima es: {Vivienda.temperatura_maxima}') """