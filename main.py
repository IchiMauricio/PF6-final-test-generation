import requests

def dish_fetch(num):
    try:
        url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
        response = requests.get(url, timeout=10)
        return response.json()
    except:
        return {"error": "Dish not found"}

def main():
    print("Hello, students!")
    print("\n Choose a typical Colombian dish:")
    print("1 Bandeja Paisa")
    print("2 Ajiaco") 
    print("3 Sancocho")
    print("4 Arepas")
    print("5 Empanadas")
    
    while True:
        try:
            number = input("\nEnter a number (1-5): ")
            number = int(number)
            break
        except ValueError:
            print("Please enter a valid number!")
    
    dish = dish_fetch(number)
    print("\nYour dish:")
    print(dish)

if __name__=="__main__":
    main()

