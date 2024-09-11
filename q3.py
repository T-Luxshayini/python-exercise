def temperature_advice(temperature):
    if temperature > 30:
        return "Hot"
    elif 15 <= temperature <= 30:
        return "Warm"
    else:
        return "Cold"


print(temperature_advice(34))  
print(temperature_advice(20))  
print(temperature_advice(10))  
