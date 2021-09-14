import turtle
import pandas

IMAGE_PATH = "./blank_states_img.gif"
STATE_DATA_PATH = "./50_states.csv"

# Get state data
states_data = pandas.read_csv(STATE_DATA_PATH)
states_list = states_data.state.to_list()

# Create quiz screen
screen = turtle.Screen()
screen.title("U.S. States Quiz!!!")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Start the quiz!
correctly_guessed_states = []
quiz_is_on = True
while quiz_is_on:
    # Ask user to type a State name
    answer = screen.textinput(title="Guess the State", prompt="Name a state!")
    answer = answer.title()
    # Check answer
    answer_is_correct = answer in states_list
    if answer_is_correct:
        if answer in correctly_guessed_states:
            print(f"You've already guessed {answer}.")
        else:
            print("Nice guess!")
            correctly_guessed_states.append(answer)
    else:
        print("That's not a state!")

# Exit program on click
turtle.mainloop()
