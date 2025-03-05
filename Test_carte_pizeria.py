import unittest
from unittest.mock import patch
from CartePizzeria import CartePizzeria, Pizza, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        """Cette méthode est appelée avant chaque test."""
        self.carte = CartePizzeria()
        self.pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
        self.pizza2 = Pizza("Reine", ["tomate", "mozzarella", "jambon", "champignons"], 10)
        self.carte.add_pizza(self.pizza1)
        self.carte.add_pizza(self.pizza2)
    
    def test_nb_pizzas(self):
        """Test pour vérifier le nombre de pizzas dans la carte."""
        self.assertEqual(self.carte.nb_pizzas(), 2)

    def test_is_empty(self):
        """Test pour vérifier si la carte est vide."""
        self.assertFalse(self.carte.is_empty())
        carte_vide = CartePizzeria()
        self.assertTrue(carte_vide.is_empty())

    def test_add_pizza(self):
        """Test pour ajouter une pizza à la carte."""
        pizza3 = Pizza("4 Fromages", ["tomate", "mozzarella", "gorgonzola", "parmesan", "emmental"], 12)
        self.carte.add_pizza(pizza3)
        self.assertEqual(self.carte.nb_pizzas(), 3)

    def test_remove_pizza_success(self):
        """Test pour supprimer une pizza existante."""
        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 1)
        self.assertNotIn(self.pizza1, self.carte.pizzas)

    @patch.object(CartePizzeria, 'remove_pizza')
    def test_remove_pizza_mock(self, mock_remove_pizza):
        """Test avec mock pour simuler la suppression d'une pizza."""
        mock_remove_pizza.return_value = None  # On simule que la pizza a bien été supprimée
        self.carte.remove_pizza("Margherita")
        mock_remove_pizza.assert_called_with("Margherita")
    
    def test_remove_pizza_exception(self):
        """Test pour lever une exception si la pizza n'existe pas."""
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Quatre Fromages")

    def test_str_empty(self):
        """Test pour vérifier l'affichage quand la carte est vide."""
        carte_vide = CartePizzeria()
        self.assertEqual(str(carte_vide), "La carte est vide.")

    def test_str_non_empty(self):
        """Test pour vérifier l'affichage de la carte non vide."""
        self.assertIn("Pizza Margherita", str(self.carte))
 
