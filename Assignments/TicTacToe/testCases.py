import unittest
from PyQt5.QtWidgets import QApplication
from your_tic_tac_toe_file import UI  # Replace 'your_tic_tac_toe_file' with the actual file name

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.ui = UI()

    def tearDown(self):
        self.ui.close()

    def simulate_clicks(self, *buttons):
        for button in buttons:
            button.click()

    def test_player_X_wins(self):
        # Simulate a winning scenario for Player X
        self.simulate_clicks(
            self.ui.button1,
            self.ui.button4,
            self.ui.button2,
            self.ui.button5,
            self.ui.button3,
        )
        self.assertEqual(self.ui.label.text(), "WINNER!!")
        self.assertEqual(self.ui.scoreX, 1)
        self.assertEqual(self.ui.scoreO, 0)

    def test_player_O_wins(self):
        # Simulate a winning scenario for Player O
        self.simulate_clicks(
            self.ui.button1,
            self.ui.button4,
            self.ui.button2,
            self.ui.button5,
            self.ui.button7,
            self.ui.button6,
        )
        self.assertEqual(self.ui.label.text(), "WINNER!!")
        self.assertEqual(self.ui.scoreX, 0)
        self.assertEqual(self.ui.scoreO, 1)

    def test_draw_game(self):
        # Simulate a draw game
        self.simulate_clicks(
            self.ui.button1,
            self.ui.button2,
            self.ui.button3,
            self.ui.button5,
            self.ui.button4,
            self.ui.button6,
            self.ui.button8,
            self.ui.button7,
            self.ui.button9,
        )
        self.assertEqual(self.ui.label.text(), "WINNER!!")  # Since you didn't specify a tie, the game declares a winner on a draw.
        self.assertEqual(self.ui.scoreX, 0)
        self.assertEqual(self.ui.scoreO, 0)

if __name__ == "__main__":
    unittest.main()
