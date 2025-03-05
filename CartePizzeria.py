class CartePizzeriaException(Exception):
    """Exception levée lorsque l'on tente de supprimer une pizza qui n'existe pas."""
    pass

class Pizza:
    def __init__(self, nom: str, ingredients: list, prix: float):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
    
    def __str__(self):
        return f"Pizza {self.nom}: {', '.join(self.ingredients)} - {self.prix:.2f}€"

class CartePizzeria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)
    
    def remove_pizza(self, name: str):
        for pizza in self.pizzas:
            if pizza.nom == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")
    
    def __str__(self):
        if self.is_empty():
            return "La carte est vide."
        return "\n".join(str(pizza) for pizza in self.pizzas)

# Exemple d'utilisation
if __name__ == "__main__":
    carte = CartePizzeria()
    pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
    pizza2 = Pizza("Reine", ["tomate", "mozzarella", "jambon", "champignons"], 10)
    
    carte.add_pizza(pizza1)
    carte.add_pizza(pizza2)
    
    print(carte)
    print("Nombre de pizzas:", carte.nb_pizzas())
    
    carte.remove_pizza("Margherita")
    print("Après suppression:")
    print(carte)
    
    try:
        carte.remove_pizza("Quatre Fromages")
    except CartePizzeriaException as e:
        print("Erreur:", e)
