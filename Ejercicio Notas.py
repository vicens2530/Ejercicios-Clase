nota= float(input("Dime que nota sacaste:\n"))
if nota < 0:
    print("es incorrecto")
elif nota < 5:
    print("es insuficiente")
elif nota < 6:
    print("es suficiente")
elif nota < 7:
    print("esta bien")
elif nota < 9:
    print("es notable")
elif nota <= 10:
    print("es sobresaliente")
else:
    print("es incorrecto")