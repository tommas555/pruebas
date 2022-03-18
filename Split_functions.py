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
