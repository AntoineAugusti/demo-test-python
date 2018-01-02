# -*- coding: utf-8 -*-
import unittest

from animals import Animal


class TestDatasetParser(unittest.TestCase):
    def test_can_create_cat(self):
        cat = Animal('Kitten', Animal.CAT)

        self.assertEquals(cat.name, 'Kitten')
        self.assertTrue(cat.is_cat())
        self.assertFalse(cat.is_dog())

    def test_shortcut_for_cat(self):
        self.assertEquals(
            Animal('Kitten', Animal.CAT),
            Animal.create_cat('Kitten')
        )

    def test_can_create_dog(self):
        dog = Animal('Pluto', Animal.DOG)

        self.assertEquals(dog.name, 'Pluto')
        self.assertTrue(dog.is_dog())
        self.assertFalse(dog.is_cat())

    def test_shortcut_for_dog(self):
        self.assertEquals(
            Animal('Doggy', Animal.DOG),
            Animal.create_dog('Doggy')
        )

    def test_can_only_create_cats_and_dogs(self):
        regex = r'^Cannot create .*: `fish`$'
        with self.assertRaisesRegexp(ValueError, regex):
            Animal('Nemo', 'fish')

    def test_titleize_name(self):
        self.assertEquals(
            Animal.create_cat('foo bar').name,
            'Foo Bar',
        )
