from random import choice


def date_partition(max_partition: int) -> str:
    """
        It is a function to generate a random date partition.

        :param: int max_partition: max partition to generate a date partition

        :return: A random date partition between the present date partitions.
        :rtype: str

        :Example:
            >>> date_partition(2)
            >>> date_partition(3)
    """
    date_partition = ['dia', 'semana', 'mês', 'trimestre', 'semestre', 'ano']
    return f'por {choice(date_partition[:max_partition])}'


for i in range(100):
    print(date_partition(3))
