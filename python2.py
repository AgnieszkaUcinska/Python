print ("Podaj x")
x=int(input())
#zmiana linijki
if x > 0 and x<50:
	print ("X jest mniejszy od 50")
elif x >=50 and x < 500:
	print ("x jest większy lub równy  50 ale mniejszy niż 500")
elif x>=500 and x<=5000:
	print ("x jest pomiędzy 500 a 5000")
else: print ("x jest większy niż 5000")