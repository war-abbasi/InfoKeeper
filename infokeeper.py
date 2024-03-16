import datetime

def calculate_age(year_of_birth):
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    return age

def generate_receipt(info):
    print("\n------------------------------------")
    print("Receipt:")
    print("------------------------------------")
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Gender:", info["gender"])
    print("Father's Name:", info["father_name"])
    print("Email:", info["email"])
    print("Contact:", info["contact"])
    print("------------------------------------")

def main():
    print("Welcome to the Information Input System\n")

    name = input("Enter your Name: ")
    year_of_birth = int(input("Enter your Year of Birth: "))
    gender = input("Enter your Gender: ")
    father_name = input("Enter your Father's name: ")
    email = input("Enter your Email: ")
    contact = input("Enter your Contact Number: ")

    age = calculate_age(year_of_birth)

    info = {
        "name": name,
        "age": age,
        "gender": gender,
        "father_name": father_name,
        "email": email,
        "contact": contact
    }

    generate_receipt(info)


main()
