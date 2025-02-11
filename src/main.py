from tkinter import Tk
from gui import GameGUI

def main():
    root = Tk()
    root.title("Mastermind Game")
    game_gui = GameGUI(root)
    game_gui.start_game()
    root.mainloop()

if __name__ == "__main__":
    main()