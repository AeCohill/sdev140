import tkinter as tk

# Create the chessboard GUI
class ChessboardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess")
        self.board = tk.Canvas(self.root, width=400, height=400)
        self.board.pack()
        self.draw_board()
        self.bind_clicks()

    def draw_board(self):
        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.board.create_rectangle(
                    col * 50,
                    row * 50,
                    (col + 1) * 50,
                    (row + 1) * 50,
                    fill=color
                )
                # Add the chess pieces to the board
                piece_image = self.get_piece_image(row, col)  # Get the appropriate piece image
                self.board.create_image(
                    col * 50 + 25,
                    row * 50 + 25,
                    image=piece_image
                )

    def get_piece_image(self, row, col):
        # Return the image for the chess piece at the given position
        # This is a placeholder, you'll need to implement your own logic
        # to determine the appropriate piece image based on the chessboard state
        # and the position (row, col).
        # Here's an example of returning a different image for black and white pawns:
        if row == 1 or row == 6:
            return self.get_image("pawn.png")
        else:
            return None

    def get_image(self, filename):
        # Load and return the image from file
        # This assumes that the image files are in the same directory as this script
        # Make sure to replace 'filename' with the actual path to your image files if needed
        return tk.PhotoImage(file=filename)

    def bind_clicks(self):
        # Bind click events on the chessboard
        self.board.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # Handle the click event
        col = event.x // 50
        row = event.y // 50
        print("Clicked:", col, row)

# Create the main application window
root = tk.Tk()

# Create the chessboard GUI object
chessboard_gui = ChessboardGUI(root)

# Start the Tkinter event loop
root.mainloop()
