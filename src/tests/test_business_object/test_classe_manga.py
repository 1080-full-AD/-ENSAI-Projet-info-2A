from unittest import TestCase
import pytest

from business_object.manga import Manga


class TestManga(TestCase):

    def test_manga_ok(self):
        # GIVEN
        titre = "mettre un titre d'un manga de notre BDD"

        # WHEN
        res = Manga().manga(titre)

        # THEN
        self.assertEqual(res, titre)

    def test_manga_erreur(self):
        # GIVEN
        titre_2 = "mettre un titre qui n'est pas dans la BDD"

        # WHEN
        res_2 = Manga().manga(titre_2)

        # THEN
        assert res_2 is None

    def test_manga_exeption(self):
        # GIVEN
        titre_3 = 5

        # WHEN/THEN
        with pytest.raises(TypeError):
            Manga().manga(titre_3)       