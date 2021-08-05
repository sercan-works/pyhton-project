liste = []
sayı=0
count1 = 0
count2 = 1
while sayı <55:

  if liste == []:
      liste.append(1)

  elif liste == [1]:
      liste.append(1)

  else:
      sayı = liste[count2] + liste[count1]   
      liste.append(sayı)
      count1 = count1 + 1
      count2 = count1 + 1
print(liste)