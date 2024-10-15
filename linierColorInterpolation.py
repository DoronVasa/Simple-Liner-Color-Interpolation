import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display values
screen_width = 800
screen_height = 200

def get_two_colors():
    right = input("Input the right color RGB value separated by ', ': ").split(", ")
    left = input("Input the left color RGB value separated by ', ': ").split(", ")
    
    # Convert the values to integers and check if they are within the valid range
    try:
        right_color = [int(value) for value in right]
        left_color = [int(value) for value in left]
    except ValueError:
        raise ValueError("All RGB values must be integers.")

    # Check if all values are between 0 and 255
    for value in right_color + left_color:
        if value < 0 or value > 255:
            raise ValueError("RGB values must be between 0 and 255.")
    
    return right_color, left_color

def calculate_M_values(right_color, left_color, screen_width):
    return (right_color - left_color) / screen_width

def calculate_new_pixel_values(M, X, B):
    return M * X + B 

# Get inputs from user
right_color, left_color = get_two_colors()

# Calculate M for each color
redM = calculate_M_values(right_color[0], left_color[0], screen_width)
greenM = calculate_M_values(right_color[1], left_color[1], screen_width)
blueM = calculate_M_values(right_color[2], left_color[2], screen_width)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linier Color Interpolation")

for rowX in range(0, screen_width):
    new_pixel_red_value = calculate_new_pixel_values(redM, rowX, left_color[0])
    new_pixel_green_value = calculate_new_pixel_values(greenM, rowX, left_color[1])
    new_pixel_blue_value = calculate_new_pixel_values(blueM, rowX, left_color[2])
    
    # Draw all the pixels to the screen
    for pixel in range(0, screen_height):
        screen.set_at((rowX, pixel), (new_pixel_red_value, new_pixel_green_value, new_pixel_blue_value))    

# Draw everything to the screen
pygame.display.flip()

# Main game loop
running = True
while running:
    # Make the X button work so we can exit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()