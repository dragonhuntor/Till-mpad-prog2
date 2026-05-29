import csv
import os

csv_file_path = "db_products.csv"
fieldnames = ["id", "name", "desc", "price", "quantity"]

def load_products():
    products = []
    if not os.path.exists(csv_file_path):
        print("Filen finns inte – en ny skapas.")
        return products
    try:
        with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    products.append({
                        "id": int(row["id"]),
                        "name": row["name"],
                        "desc": row["desc"],
                        "price": float(row["price"]),
                        "quantity": int(row["quantity"])
                    })
                except:
                    print("Fel i en rad – hoppar över den.")
    except:
        print("Kunde inte läsa filen.")
    return products

def save_products(products):
    try:
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)
        print("Ändringar sparade.")
    except:
        print("Fel vid sparning.")

def show_products(products):
    if not products:
        print("Inga produkter finns.")
        return
    print("\n=== PRODUKTER ===")
    for p in products:
        print(f"ID:{p['id']} | Namn:{p['name']} | Beskrivning:{p['desc']} | Pris:{p['price']} kr | Antal:{p['quantity']}")

def add_product(products):
    try:
        name = input("Namn: ")
        desc = input("Beskrivning: ")
        price = float(input("Pris: "))
        quantity = int(input("Antal: "))
        new_id = max((p["id"] for p in products), default=0) + 1
        products.append({"id": new_id, "name": name, "desc": desc, "price": price, "quantity": quantity})
        save_products(products)
        print("Produkt tillagd.")
    except:
        print("Felaktig inmatning.")

def remove_product(products):
    try:
        id_to_remove = int(input("ID att ta bort: "))
        for p in products:
            if p["id"] == id_to_remove:
                products.remove(p)
                save_products(products)
                print("Produkt borttagen.")
                return
        print("Ingen produkt med det ID:t.")
    except:
        print("Felaktigt ID.")

def edit_product(products):
    try:
        id_to_edit = int(input("ID att ändra: "))
        for p in products:
            if p["id"] == id_to_edit:
                print("1. Namn\n2. Beskrivning\n3. Pris\n4. Antal")
                val = input("Välj: ")
                if val == "1":
                    p["name"] = input("Nytt namn: ")
                elif val == "2":
                    p["desc"] = input("Ny beskrivning: ")
                elif val == "3":
                    p["price"] = float(input("Nytt pris: "))
                elif val == "4":
                    p["quantity"] = int(input("Nytt antal: "))
                save_products(products)
                print("Produkten uppdaterad.")
                return
        print("Ingen produkt med det ID:t.")
    except:
        print("Felaktig inmatning.")

def show_statistics(products):
    if not products:
        print("Inga produkter finns.")
        return
    total_qty = sum(p["quantity"] for p in products)
    total_value = sum(p["price"] * p["quantity"] for p in products)
    avg_price = sum(p["price"] for p in products) / len(products)
    print("\n=== STATISTIK ===")
    print(f"Totalt antal: {total_qty}")
    print(f"Totalt värde: {total_value:.2f} kr")
    print(f"Genomsnittspris: {avg_price:.2f} kr")
    for p in products:
        procent = (p["price"] * p["quantity"]) / total_value * 100
        print(f"{p['name']}: {procent:.1f}% av totalvärdet")

def main():
    products = load_products()
    while True:
        print("\n=== PRODUKTDATABAS ===")
        print("1. Visa produkter")
        print("2. Lägg till produkt")
        print("3. Ta bort produkt")
        print("4. Ändra produkt")
        print("5. Visa statistik")
        print("0. Avsluta")
        choice = input("Välj: ")
        if choice == "1":
            show_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            remove_product(products)
        elif choice == "4":
            edit_product(products)
        elif choice == "5":
            show_statistics(products)
        elif choice == "0":
            print("Avslutar.")
            break
        else:
            print("Fel val.")

if __name__ == "__main__":
    main()
