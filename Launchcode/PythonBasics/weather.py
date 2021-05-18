temperature = int(input("What is the temperature today?\n"))
forecast = input("What is the forecast today?\n")

if temperature < 80 and forecast != "rain":
    print("Go outside!") 
else:
    print("Stay inside!")
