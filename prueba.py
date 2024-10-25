import tkinter as tk
import customtkinter as ctk
import requests
import sqlite3

def create_db():
    conn = sqlite3.connect("./users/Pou/alimentos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alimento (
            nombre TEXT NOT NULL,
            calorias_100gr INTEGER,
            calorias_porcion INTEGER
        );
    ''')
    conn.commit()
    conn.close()

def search_food():
    query = entry.get().strip()

    if query:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['products']:
                options = [f"{product['product_name']} - {product['nutriments'].get('energy-kcal_100g', 'No disponible')} kcal por 100g"
                           for product in data['products'][:5]]
                food_combobox.configure(values=options)
                food_combobox.set("Selecciona un alimento")
            else:
                result_label.configure(text="No se encontraron productos.")
        else:
            result_label.configure(text="Error en la búsqueda.")
    else:
        result_label.configure(text="Por favor ingresa un alimento.")

def insert_selected_food():
    selected_food = food_combobox.get()

    if selected_food != "Selecciona un alimento":
        food_data = selected_food.split(" - ")
        nombre = food_data[0]
        calorias_100gr = food_data[1].split(" ")[0]

        conn = sqlite3.connect("./users/Pou/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alimento (nombre, calorias_100gr) VALUES (?, ?)", (nombre, calorias_100gr))
        conn.commit()
        conn.close()

        result_label.configure(text=f"{nombre} insertado en la base de datos.")
    else:
        result_label.configure(text="Por favor selecciona un alimento.")

root = ctk.CTk()
root.title("Búsqueda de Alimentos")
root.geometry("400x400")

create_db()

entry = ctk.CTkEntry(root, placeholder_text="Escribe el nombre del alimento")
entry.pack(pady=20)

search_button = ctk.CTkButton(root, text="Buscar", command=search_food)
search_button.pack(pady=10)

food_combobox = ctk.CTkComboBox(root, values=["Selecciona un alimento"])
food_combobox.pack(pady=10)

insert_button = ctk.CTkButton(root, text="Insertar en BD", command=insert_selected_food)
insert_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="Aquí aparecerán los resultados")
result_label.pack(pady=20)

root.mainloop()
