import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH = 340
HEIGHT = 340

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Tic-Tac-Toe")

# Set the colors that will be used in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the size of each square on the grid
SQUARE_SIZE = 100

# Set the margin between the squares
MARGIN = 10

# Set the initial player to X
player = "X"

# Create a list to store the positions of the X's and O's
positions = []

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Calculate the column and row that was clicked
            column = pos[0] // (SQUARE_SIZE + MARGIN)
            row = pos[1] // (SQUARE_SIZE + MARGIN)
            # Make sure the space is not already occupied
            if (column, row) not in positions:
                # Add the position to the list
                positions.append((column, row))
                # Switch the player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the grid
    for row in range(3):
        for column in range(3):
            color = WHITE
            if (column, row) in positions:
                if player == "X":
                    color = BLACK
                else:
                    color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN + SQUARE_SIZE) * column + MARGIN, (MARGIN + SQUARE_SIZE) * row + MARGIN, SQUARE_SIZE, SQUARE_SIZE])
    
    # Update the screen
    pygame.display.flip()
