import turtle
import pandas

IMAGE_PATH = "./blank_states_img.gif"
STATE_DATA_PATH = "./50_states.csv"
FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

# Get state data
states_data = pandas.read_csv(STATE_DATA_PATH)
states_list = states_data.state.to_list()

# Create quiz screen
screen = turtle.Screen()
screen.title("U.S. States Quiz!!!")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Start the quiz!
guesses_used = 0
score = 0
correctly_guessed_states = []
while guesses_used <= 50:
    # Ask user to type a State name
    your_answer = screen.textinput(title=f"Score: {score}/50", prompt="Name a state!")
    your_answer = your_answer.title()
    # Check answer
    answer_is_correct = your_answer in states_list
    if answer_is_correct:
        if your_answer in correctly_guessed_states:
            print(f"You've already answered {your_answer}.")
        else:
            print("You answered correctly!!!")
            correctly_guessed_states.append(your_answer)
            # Find the location of the state
            state_x_cor = int(states_data.x[states_data.state == your_answer])
            state_y_cor = int(states_data.y[states_data.state == your_answer])
            print(state_x_cor, state_y_cor)
            # Reveal the state name on the map
            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto(state_x_cor, state_y_cor)
            new_state.write(arg=your_answer, font=FONT, align=ALIGNMENT)
            # Increase score
            score += 1
    else:
        print("That's not a state!")
    # Increase loop counter
    guesses_used += 1

# Exit program on click
turtle.mainloop()
