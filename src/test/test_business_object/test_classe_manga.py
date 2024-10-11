from unittest import TestCase

from business_object.manga import Manga


class TestManga(Manga):

    def test_manga_ok(self):
    #GIVEN
        titre = "mettre un titre d'un manga de notre BDD"

    #WHEN
    res = Manga().manga("mettre un titre d'un manga de notre BDD")

    #THEN
