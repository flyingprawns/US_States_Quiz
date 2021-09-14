import turtle

IMAGE_PATH = "./blank_states_img.gif"

# Create quiz screen
screen = turtle.Screen()
screen.title("U.S. States Quiz!!!")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Ask user to input state name
answer_state = screen.textinput(title="Guess the State", prompt="Name a state!")
print(answer_state)

# Exit program on click
turtle.mainloop()