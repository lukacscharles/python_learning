"""✍️ III. HÁZI FELADAT
1. feladat:

1. lépés: Hozz létre egy “name” karakterlánc-változót, és rendeld hozzá az “aRnOlD sChWaRzEnEgGer” értéket. A név szándékosan tartalmaz kis-és nagybetűket felváltva. Érdemes így bemásolnod (CTRL + C vagy az egér jobb klikk “másolás” és “beillesztés”), mert a következő pontban részletezett utasításokat végrehajtva látványosabb eredményeket fogsz látni.

2. lépés: Írasd ki úgy, hogy minden betű kisbetű legyen. Ha ez megvan, alakítsd át úgy, hogy csak a két szó első betűje kezdődjön nagybetűvel és a többi maradjon kicsi. Legvégül pedig írasd ki az összeset nagybetűvel.

2. feladat:

1. lépés: Legyen adott egy név: “Nagy Márk”. Bontsd le vezetéknév – és keresztnévre, majd rendeld hozzájuk a neveket. A Python szabályain belül tetszőleges neveket adhatsz a fenti változóknak.

2. lépés: Most pedig vezess be egy új változót “full_name” néven és kombináld össze a vezetéknevet és a keresztnevet.

3. lépés: Írasd ki teljes nevet.

4. lépés: Írasd ki a teljes nevet és fűzd hozzá, hogy “a legjobb középiskolás barátom volt”

5. lépés: Ismételd meg a fenti 1-4 lépést további két középiskolai barátoddal.

Látni fogod, hogy milyen egyszerű is a Python segítségével mondatokat formálnunk."""

name="aRnOlD sChWaRzEnEgGer"
name=name.lower()
print(name)
print("\n")
name=name.title()
print(name)
print("\n")
name=name.upper()
print(name)
print("\n")
input()
print("\n")

	
i=4
while i>0:
	name2=input("Legyen egy adott név:")
	family_name=name2.split( " ", 1)[0]
	print(family_name)
	print("\n")
	first_name=name2.split( " ",1)[1]
	print(first_name)
	print("\n")
	full_name=family_name + " " + first_name
	print(full_name)
	print("\n")
	print(full_name + " a legjobb Középiskolai barátom volt.")
	print("\n")
	input()
	i=i-1
