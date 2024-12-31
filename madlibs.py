# Long Mad Libs Game in Python

def mad_libs():
    print("Welcome to the Mad Libs Game!")
    print("You will be asked to provide some words to complete a funny and adventurous story. Let's begin!\n")

    # Collecting inputs from the user
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    place = input("Enter a place: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    emotion = input("Enter an emotion: ")
    plural_noun = input("Enter a plural noun: ")
    profession = input("Enter a profession: ")
    color = input("Enter a color: ")

    # Story template
    story = f"""
    Once upon a time in the {adjective1} land of {place}, there lived a {profession} named {name}. 
    {name} was known far and wide for their {adjective2} ability to {verb1}. 
    One day, while {name} was {verb2} near a {color} {noun1}, they stumbled upon a mysterious {noun2}. 

    Suddenly, a {adjective3} {animal} appeared, blocking the path! The {animal} looked {emotion} and seemed 
    very interested in the {food} that {name} was carrying. Thinking quickly, {name} offered the {food} 
    to the {animal}, who happily ate it and disappeared into the {place}. 

    Relieved but curious, {name} picked up the {noun2} and discovered it was filled with magical {plural_noun}. 
    This discovery changed {name}'s life forever, and they became the hero of {place}, 
    spreading joy and {adjective2} adventures wherever they went!
    """

    # Output the completed story
    print("\nHere's your Mad Libs story:")
    print(story)

# Run the program
if __name__ == "__main__":
    mad_libs()
