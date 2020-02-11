# Get's recipe name and checks it is not blank

# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("Please enter a recipe name")
            continue
        else:
            return response

# Main Routine goes here

recipe_name = not_blank("What is the recipe name?")

print("you are making {}".format(recipe_name))
