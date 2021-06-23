indian=("Jalebi","Samosa","Pakoda","Dahi balle","Chhole Bhature")
Chinese=("Noodles","Fried rice","Momos","Egg Roll")
Italian=("Pizza","Pasta")
dish=input("Enter a dish name: ")
if dish in indian:
    print("Indian")
elif dish in Chinese:
    print("Chinese")
elif dish in Italian:
    print("Italian")
else:
    print("I dont know the dish u want")
