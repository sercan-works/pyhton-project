while True:
  
  sayı = int(input("Bir sayı giriniz....:"))
  if (sayı > 2 and sayı % 2 == 0) or (sayı > 3 and sayı % 3 == 0) or (sayı > 5 and sayı % 5 == 0) :
    print(str(sayı)+" "+ "bir asal sayı değildir...")
  elif sayı == 0:
    print("0 sakıncalı bir sayıdır:)") 
  else:
    print(str(sayı)+" "+ "bir asal sayıdır...")