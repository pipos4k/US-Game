import turtle
import pandas

# Sample DataFrame with States and their x, y coordinate
df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "states.gif"
screen.setup(width=740, height=515)
screen.bgpic(image)

# Set up the turtle for drawing
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Get user input
while len(guessed_states) < 50:
    user_input = screen.textinput(f"{len(guessed_states)}/50 States correct",
                                  "Enter a U.S. state name:").title()

    # Check if the user's input exists in the 'State' column
    if user_input in guessed_states:
        print("You already give that answer.")

    elif user_input in df['state'].values:
        # Find the corresponding row for the state
        guessed_states.append(user_input)
        row = df[df['state'] == user_input]

        # Retrieve the x and y axis values
        x_value = row['x'].values[0]
        y_value = row['y'].values[0]

        # Move the turtle to the state's location
        t.goto(x_value, y_value)

        # Write the state's name on the map at the coordinates
        t.write(user_input, align="center", font=("Arial", 7, "bold"))
    elif user_input == "Exit":
        turtle.bye()
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = pandas.DataFrame(missing_states)
        missing_states.to_csv("missing_states")
        break
    else:
        print(f"'{user_input}' does not exist in the list of states.")

    # Keep the window open until it's closed by the user
screen.mainloop()
