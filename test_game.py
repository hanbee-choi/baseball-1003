from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def setUp(self) -> None:
        self.game = Game()
        super().setUp()

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_exception_when_input_length_is_unmatched(self):
        guessNumber = "12"
        self.assert_illegal_argument(guessNumber)

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess("%s" % guessNumber)
            self.fail()
        except TypeError:
            pass
