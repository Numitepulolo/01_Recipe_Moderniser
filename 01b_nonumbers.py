# Get's recipe name and checks it is not blank

# Not Blank Function goes here
def not_blank(question):
    error= "Your recipe name has numbers in it."
    has_errors = ""

    valid = False
    while not valid:
        response = input(question)

        # look at each character in string and if it's a number, complain
        for letter in recipe_name:

            if letter.isdigit() == True:
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            break
        else:
            return response


        #Main Routine goes here

recipe_name = not_blank("What is the recipe name? ")

print("You are making {}" .format(recipe_name))

