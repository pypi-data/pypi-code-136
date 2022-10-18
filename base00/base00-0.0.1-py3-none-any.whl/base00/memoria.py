def save(*names):
    """
    Function to save the names created in a txt file.
    """
    with open("names.txt", "a") as file:
        for name in names:
            file.write(name+"\n")