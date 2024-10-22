from unittest import TestCase
import pytest

from business_object.collection.abstract_collection import AbstractCollection
from business_objet.collection.collection_physique import CollectionPhysique

class TestCollectionPhysique(TestCase):
    import unittest

class TestCollectionPhysique(unittest.TestCase):

    class FakeManga(mangaPhysique):
        def __init__(self, title):
            self.title = title

        def __eq__(self, other):
            return self.title == other.title

    def setUp(self):
        self.manga1 = self.FakeManga("Manga 1")
        self.manga2 = self.FakeManga("Manga 2")
        self.manga3 = self.FakeManga("Manga 3")
        self.collection = CollectionPhysique("Ma Collection", 1, [self.manga1, self.manga2])

    def test_initialization(self):
        self.assertEqual(self.collection.titre, "Ma Collection")
        self.assertEqual(self.collection.id_utilisateur, 1)
        self.assertEqual(len(self.collection.list_manga), 2)

    def test_initialization_invalid_manga(self):
        with self.assertRaises(ValueError):
            CollectionPhysique("Collection Invalide", 1, ["not a manga"])

    def test_eq_same_collection(self):
        collection2 = CollectionPhysique("Ma Collection", 1, [self.manga1, self.manga2])
        self.assertTrue(self.collection == collection2)

    def test_eq_different_collection(self):
        collection2 = CollectionPhysique("Collection Différente", 2, [self.manga1])
        self.assertFalse(self.collection == collection2)

    def test_ajouter_manga(self):
        self.collection.ajouter_manga(self.manga3, [1, 2])
        self.assertEqual(len(self.collection.list_manga), 3)
        self.assertIn({"manga": self.manga3, "tomes_manquants": [1, 2]}, self.collection.list_manga)

    def test_supprimer_manga(self):
        self.collection.supprimer_manga(self.manga1)
        self.assertEqual(len(self.collection.list_manga), 1)
        self.assertNotIn({"manga": self.manga1, "tomes_manquants": []}, self.collection.list_manga)

    def test_supprimer_manga_not_found(self):
        self.collection.supprimer_manga(self.manga3)  
        self.assertEqual(len(self.collection.list_manga), 2)

if __name__ == "__main__":
    unittest.main()

