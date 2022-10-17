class CellTemplate:
    # {{{
    """
    Um template para a implementação de regras. Também define uma série de funções úteis
    que serão herdadas. Tem um monte de pylint: disable aí porque isso deve servir
    somente como uma classe template, ela não deve ser diretamente instanciada.
    """
    # pylint: disable=no-self-use, unused-argument

    def __init__(self, val, pos, cell_args=None):
        # {{{
        """
        Durante a inicialização, cada célula precisa saber a sua
        posição na matriz (para saber quais são seus vizinhos) e
        seu valor inicial. Esse __init__ é o absoluto mínimo, mas
        é claro que é possível sobrescrever esse init para
        implementar mais coisa.
        """

        self.lin, self.col = pos
        self.value = val

    # }}}

    def update(self, state_matrix, cell_args=None):
        # {{{
        """
        É aqui que a célula recebe o estado do tabuleiro. e
        atualiza seu próprio estado. Este é o método que é
        executado em cada célula a cada iteração.
        """
        ...

    # }}}

    @classmethod
    def simulation_start(cls, state_matrix, cell_args=None):
        # {{{
        """
        Método executado somente uma vez no começo da simulação, antes da primeira
        geração. Por padrão não faz nada.
        """
        ...

    # }}}

    @classmethod
    def generation_start(cls, state_matrix, cell_args=None):
        # {{{
        """
        Método executado somente uma vez no começo de cada geração. Por padrão não faz
        nada.
        """
        ...

    # }}}

    @classmethod
    def generation_end(cls, state_matrix, cell_args=None):
        # {{{
        """
        Método executado somente uma vez por geração, depois do update. Por padrão não
        faz nada.
        """
        ...

    # }}}

    @property
    def pos(self):
        return (self.lin, self.col)

    @property
    def neighbors(self):
        # {{{
        """
        Aqui se implementa uma vizinhança arbitrária para o tipo
        de célula. Também se pode usar uma das vizinhanças
        padrão. Confira o exemplo rules/game_of_life.py.
        """

        raise NotImplementedError("Implementado na classe derivada")

    # }}}

    @property
    def moore_neighborhood(self):
        # {{{
        """
        Vizinhança de Moore. Retorna um array de numpy com 8
        elementos; a ordem é da esquerda para direita, de cima
        para baixo.
        """
        # pylint: disable=no-member

        # Provavelmente há uma maneira mais elegante de fazer
        # isso, mas essa é de longe a mais rápida e eficiente
        # que encontrei
        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        prev_lin, next_lin = lin - 1, lin + 1
        prev_col, next_col = col - 1, col + 1
        try:
            # Primeiro tenta acessar os elementos normalmente
            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[next_lin, prev_col],
                state_matrix[lin, prev_col],
            ]
        except IndexError:
            # Isso vai falhar para células nas beiradas da
            # matriz. Neste caso, acessa-se os elementos fazendo
            # o 'wrapping' ao redor da matriz.
            prev_lin %= m
            next_lin %= m
            prev_col %= n
            next_col %= n

            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[next_lin, prev_col],
                state_matrix[lin, prev_col],
            ]

        return neighbors

    # }}}

    @property
    def neumann_neighborhood(self):
        # {{{
        """
        Vizinhança de Von Neumann. Retorna um array numpy com 4
        elementos, começando com o de cima no sentido horário.
        """
        # pylint: disable=no-member

        # Sim, esse código é quase todo copiado e colado da
        # moore_neighborhood. Fazer o que? Isso precisa ser
        # rápido.
        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        prev_lin, next_lin = lin - 1, lin + 1
        prev_col, next_col = col - 1, col + 1
        try:
            # Primeiro tenta acessar os elementos normalmente
            neighbors = [
                state_matrix[prev_lin, col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[lin, prev_col],
            ]
        except IndexError:
            # Isso vai falhar para células nas beiradas da
            # matriz. Neste caso, acessa-se os elementos fazendo
            # o 'wrapping' ao redor da matriz.
            prev_lin %= m
            next_lin %= m
            prev_col %= n
            next_col %= n

            neighbors = [
                state_matrix[prev_lin, col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[lin, prev_col],
            ]
        return neighbors

    # }}}

    @property
    def triangular_edges_neighborhood(self):
        # {{{
        """
        Vizinhança triangular de arestas. Os vizinhos são, para células ímpares,
        respectivamente, as células da esquerda, cima e direita, e para células pares,
        as da esquerda, de baixo e da direita.
        """
        # pylint: disable=no-member

        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        parity = -1 if (lin + col) & 1 else 1
        parity_lin = lin + parity
        prev_col, next_col = col - 1, col + 1
        try:
            neighbors = [
                state_matrix[lin, prev_col],
                state_matrix[parity_lin, col],
                state_matrix[lin, next_col],
            ]
        except IndexError:
            parity_lin %= m
            prev_col %= n
            next_col %= n

            neighbors = [
                state_matrix[lin, prev_col],
                state_matrix[parity_lin, col],
                state_matrix[lin, next_col],
            ]
        return neighbors

    # }}}

    @property
    def triangular_vertices_neighborhood(self):
        # {{{
        """
        Vizinhança triangular de vértices. Retorna as 12 células que, num ladrilhamento
        triangular, compartilham ao menos 1 vértice com a célula. Células pares tem suas
        vizinhanças apontando 'para cima', e ímpares tem suas vizinhanças apontando
        'para baixo'.
        """
        # pylint: disable=no-member

        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        parity = -1 if (lin + col) & 1 else 1
        parity_lin = parity + lin
        prev_lin, next_lin = lin - 1, lin + 1
        prev_col, next_col = col - 1, col + 1
        prev_2col, next_2col = col - 2, col + 2
        try:
            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[next_lin, prev_col],
                state_matrix[lin, prev_col],
                state_matrix[lin, prev_2col],
                state_matrix[lin, next_2col],
                state_matrix[parity_lin, next_2col],
                state_matrix[parity_lin, prev_2col],
            ]
        except IndexError:
            parity_lin %= m
            next_lin %= m
            prev_lin %= m
            prev_col %= n
            next_col %= n
            next_2col %= n
            prev_2col %= n

            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[next_lin, prev_col],
                state_matrix[lin, prev_col],
                state_matrix[lin, prev_2col],
                state_matrix[lin, next_2col],
                state_matrix[parity_lin, next_2col],
                state_matrix[parity_lin, prev_2col],
            ]
        return neighbors

    # }}}

    @property
    def triangular_1vertex_neighborhood(self):
        # {{{
        """
        Vizinhança triangular de vértices. Retorna as 9 células que, num ladrilhamento
        triangular, compartilham somente 1 vértice com a célula. Células pares tem suas
        vizinhanças apontando 'para cima', e ímpares tem suas vizinhanças apontando
        'para baixo'.
        """
        # pylint: disable=no-member, too-many-locals

        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        parity = -1 if (lin + col) & 1 else 1
        parity_lin = parity + lin
        rev_parity_lin = -parity + lin
        prev_lin, next_lin = lin - 1, lin + 1
        prev_col, next_col = col - 1, col + 1
        prev_2col, next_2col = col - 2, col + 2
        try:
            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, prev_2col],
                state_matrix[lin, next_2col],
                state_matrix[next_lin, prev_col],
                state_matrix[next_lin, next_col],
                state_matrix[parity_lin, prev_2col],
                state_matrix[parity_lin, next_2col],
                state_matrix[rev_parity_lin, col],
            ]
        except IndexError:
            parity_lin %= m
            next_lin %= m
            prev_lin %= m
            prev_col %= n
            next_col %= n
            next_2col %= n
            prev_2col %= n
            rev_parity_lin %= m

            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, next_col],
                state_matrix[lin, prev_2col],
                state_matrix[lin, next_2col],
                state_matrix[next_lin, prev_col],
                state_matrix[next_lin, next_col],
                state_matrix[parity_lin, prev_2col],
                state_matrix[parity_lin, next_2col],
                state_matrix[rev_parity_lin, col],
            ]
        return neighbors

    # }}}

    @property
    def hexagonal_neighborhood(self):
        # {{{
        """
        Vizinhança hexagonal. Semelhante à de Moore mas não conta os vizinhos do canto
        superior direito e inferior esquerdo.
        """
        # pylint: disable=no-member

        state_matrix = self.state_matrix
        m, n = state_matrix.shape
        lin, col = self.lin, self.col
        prev_lin, next_lin = lin - 1, lin + 1
        prev_col, next_col = col - 1, col + 1
        try:
            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[lin, prev_col],
            ]
        except IndexError:
            prev_lin %= m
            next_lin %= m
            prev_col %= n
            next_col %= n

            neighbors = [
                state_matrix[prev_lin, prev_col],
                state_matrix[prev_lin, col],
                state_matrix[lin, next_col],
                state_matrix[next_lin, next_col],
                state_matrix[next_lin, col],
                state_matrix[lin, prev_col],
            ]

        return neighbors

    # }}}

    @staticmethod
    def display(value):
        # {{{
        """
        Retorna um array numpy com os valores RGB, ou um intenro
        entre 0 e 255 para representar o autômato em função do
        value.

        O default é o caso binário, o mais simples.
        """
        return CellTemplate.display_binary(value)

    # }}}

    @staticmethod
    def from_display(rgb):
        # {{{
        """
        Retorna o valor da célula a partir do array RGB que o
        representa. É a operação inversa da função display.

        Novamente, o default é o caso binário.
        """

        return CellTemplate.from_binary(rgb)

    # }}}

    @staticmethod
    def display_binary(value):
        # {{{
        """
        Branco se o valor da célula for maior que zero, preto
        caso contrário.
        """

        return 255 if value > 0 else 0

    # }}}

    @staticmethod
    def from_binary(rgb):
        # {{{
        """
        1 caso o valor seja maior que 0, 0 caso contrário.
        """

        return 1 if (rgb > 123).all() else 0

    # }}}

    @classmethod
    def init_from_display(cls, rgb, *args, **kwargs):
        # {{{
        """
        Inicializa a célula a partir de um array RGB. Este é o
        método que de fato é chamado quando se carrega o estado
        do tabuleiro a partir de uma imagem.
        """

        return cls(cls.from_display(rgb), *args, **kwargs)

    # }}}

    def __repr__(self):
        return f"Cell({self.value}, ({self.lin}, {self.col}))"


# }}}
