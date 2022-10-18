from random import randint, choice


def combobox(self):
    """
        It is a function with the equivalent values of the present combobox in the question.

        :return: A random combobox between the present combobox.
        :rtype: str

        :Example:
            >>> combobox()
    """
    random_choice = randint(1, 2)
    if random_choice == 1:
        combobox = ['crostata', 'antipasti', 'bebidas leves', 'bebidas alcoolicas', 'sobremesas', 'cafes']
        return choice(combobox)
    else:
        return ''
