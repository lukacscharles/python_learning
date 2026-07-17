"""✍️ IV. HÁZI FELADAT
Az alábbi feladatok végrehajtásával tovább erősítheted a fentiekben ismertetett számelmélet és számok-szövegek kombinálásának megértését. A berögződés menete a gyakorlás, ezért nagyon ajánlott mindenkinek elkezdeni a gondolatokat önállóan is kivitelezni.

1.feladat: 

Írj Python-szkriptet a következő matematikai műveletekhez és futtasd le őket:

a). 8+20
b). 40-17
c). 15*2
d). 81/9

2. feladat: 

Tegyük fel, hogy munkaadód azt kéri, hogy írj az ügyfelei részére személyre szabott jókívánságokat születésnapjuk alkalmából. A neveknek és az életkoruknak hozz létre külön változókat, majd egy általad megfogalmazott jókívánsággal írasd ki az egész mondatokat a konzolban.

 András, 39 éves
 Judit, 42 éves
 Gery, 24 éves
Fontos!

A feladatok a gyakorlásra vannak. A gyakorlással pedig tapasztalatot szerzel. Mindenképp javasolt, hogy a feladatokat önállóan oldd meg. Javaslom, hogy ha végeztél, csak akkor nézz rá a megoldásra. Erősen ajánlott, hogy előtte mindenképp szánj rá időt és próbáld önállóan végiggondolni, hogy mit is kellene és hogyan lehetséges megvalósítani."""

math_op=input("Which function would you like to use? (a +; b -; c ×; d /)\n")

a=int(input("Adja meg az egyik számot\n"))
b=int(input("Adja meg a másik számot\n"))
def my_f(an,bn,mop):
	if math_op=="a":
		print(a+b)
	elif math_op=="b":
		print(a-b)
	elif math_op=="c":
		print(a*b)
	elif math_op=="d":
		print(a/b)
	else:
		print("nem értem, tolmácsot szeretnék kérni!")

my_f(an=a,bn=b,mop=math_op)
	
