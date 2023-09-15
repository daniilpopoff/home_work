
batken = int(input("Введите температуру в области Баткен: "))
jalal_abad = int(input("Введите температуру в  области Джалал-Абад: "))
issyk_kul = int(input("Введите температуру в  области Иссы-Куль: "))
naryn = int(input("Введите температуру в  области Нарын: ")) 
osch = int(input("Введите температуру в  области Ош: "))
talas = int(input("Введите температуру в  области Талас: "))
chui = int(input("Введите температуру в  области Чуй: "))
bishkek = int(input(f"Введите температуру в  области Бишкек: "))

media_temp = (batken + jalal_abad + issyk_kul + naryn + osch + talas + chui + bishkek) / 8

print(f"Средний показатель температуры воздуха по КР на сегодня {round(media_temp, 1)} °C")



