def check_age_category(age):
    if age < 18:
        return "Minor"
    elif 18 <= age <= 64:
        return "Adult"
    else:
        return "Senior"


print(check_age_category(16))  
print(check_age_category(25))  
print(check_age_category(70))  