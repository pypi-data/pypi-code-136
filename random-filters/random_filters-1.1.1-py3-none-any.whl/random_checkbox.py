from random import randint, choice


def checkbox():
    """
        It is a function with the equivalent values of the present checkboxes in the question.

        :return: A random checkbox between the present checkboxes.
        :rtype: str

        :Example:
            >>> checkbox()
    """
    random_choice = randint(1, 2)
    if random_choice == 1:
        checkbox = ['almoco', 'jantar', 'final de semana', 'dia de semana']
        return choice(checkbox)
    else:
        return ''
