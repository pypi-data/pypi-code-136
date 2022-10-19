"""
Gerencia a carga dos dados de uma planilha do Excel.
"""

# módulo usado para  implementar method overloading
# ATENÇÃO: este módulo *não é* thread safe
# (https://stackoverflow.com/questions/6434482/python-function-overloading)
# ATENÇÃO: métodos que usam o decorator dispatch e que contenham argumentos
# nomeados com valores default: se o valor default for alterado na chamada do
# método, precisa ser por meio de argumento nomeado, não pode se basear na
# posição do argumento
# (https://stackoverflow.com/questions/54132640/how-to-use-default-parameter-with-multipledispatch)

import pandas as pd

import blipy.erro as erro


class Planilha():
    """
    Planilha a ser carregada no banco de dados.
    """

    # tratamento de erro
    # este atributo é um atributo de classe, portanto pode ser alterado pora
    # todas as instâncias dessa classe, se se quiser um tipo de tratamento de
    # erro diferente de imprimir mensagem no console.
    # Para alterá-lo, usar sintaxe "Planilha.e = <novo valor>"
    e = erro.console

    def carrega_dados(self, 
            io=None, sheet_name=0, header=0, skipfooter=0, 
            names=None, index_col=None, usecols=None,
            skiprows=None, nrows=None, na_values=None, engine='openpyxl'):
        """
        Lê uma aba de uma planilha de Excel e carrega em um Data Frame do
        Pandas.

        Referência: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html

        Args:
        io:         caminho (path) do arquivo, com nome do arquivo incluso ou
                    uma URL
        sheet_name: aba ou guia do Excel, pode ser o nome ou número 0-indexed
        header:     linhas de cabeçalho a serem ignoradas, 0-indexed
        skipfooter: linhas de rodapé (final arquivo) a serem ignoradas,
                    0-indexed.
        names:      lista de nomes de colunas. Se arquivo não contém header,
                    deve-se obrigatoriamente setar header=None
        index_col:  coluna a ser usada como label das linhas
        usecols:    seleção de colunas. Tipos de seleção: 'A,B,C', [0,1,2],
                    ['ID','Coluna_1','Coluna_4']
        skiprows:   linhas a serem ignoradas no início do arquivo, 0-indexed
        nrows:      número de linhas a serem carregadas
        na_values:  lista de strings a serem consideradas como dados não
                    disponívels (NaN)
        engine:     o padrão é openpyxl. Existem outras para outros formatos,
                    por ex .odf
        """

        self.__tabela_data_frame = None  # Data Frame da planilha carregada
        self.__cursor            = None  # Iterável para função le_prox_registro()

        # Verificações de possíveis erros
        if io is None:
            self.e._("O argumento 'io' é o mínimo para funcionamento da função. \n"
                     "Este é o caminho (path) para a planilha com o nome do arquivo incluso ao final e com a extensão .xlsx ou .xls. \n"
                     "Formato esperado: C:/.../planilha.xlsx")
            raise RuntimeError

        if io.endswith('.xlsx') and engine != 'openpyxl':
            self.e._("Parâmetro 'engine' não adequado para o tipo de arquivo.\n"
                     "O argumento 'io' caminho (path) para a planilha deve terminar com: .xlsx ou .xls.\n"
                     "Para cada formato de arquivo existe uma engine adequada.\n"
                     "Engine 'openpyxl' para .xlsx e 'xlrd' para .xls.\n"
                     "Exemplos de parâmetro 'io' esperados:\n"
                     "\tC:/.../planilha.xlsx\n"
                     "\tC:/.../planilha.xls\n")
            raise RuntimeError

        if io.endswith('.xls') and engine != 'xlrd':
            self.e._("Parâmetro 'engine' não adequado para o tipo de arquivo.\n"
                     "O argumento 'io' caminho (path) para a planilha deve terminar com: .xlsx ou .xls.\n"
                     "Para cada formato de arquivo existe uma engine adequada.\n"
                     "Engine 'openpyxl' para .xlsx e 'xlrd' para .xls.\n"
                     "Exemplos de parâmetro 'io' esperados:\n"
                     "\tC:/.../planilha.xlsx\n"
                     "\tC:/.../planilha.xls\n")
            raise RuntimeError

        if not io.endswith(('.xlsx','.xls')):
            self.e._("O argumento 'io' caminho (path) para a planilha deve terminar com: .xlsx ou .xls.\n"
                     "Para cada formato de arquivo existe uma engine adequada.\n"
                     "Engine 'openpyxl' para .xlsx e 'xlrd' para .xls.\n"
                     "Exemplos de parâmetro 'io' esperados:\n"
                     "\tC:/.../planilha.xlsx\n"
                     "\tC:/.../planilha.xls\n")
            raise RuntimeError

        # Carregamento da tabela para a memória
        self.__tabela_data_frame = pd.read_excel(io=io,sheet_name=sheet_name, 
                header=header, skipfooter=skipfooter,
                names=names, index_col=index_col, usecols=usecols, 
                skiprows=skiprows, nrows=nrows, na_values=na_values, 
                engine=engine)

        self.__nome_planilha = io

    # getter; instancia.nome vai retornar __nome_planilha
    @property
    def nome(self):
        return self.__nome_planilha
    @nome.setter
    def nome(self, nome):
        raise NotImplementedError

    def recarrega_dados(self):
        """
        Faz o reset do cursor para o ponto inicial a partir do data frame
        carregado.

        Ret:
        Iterável com os registros de una tabela do Excel
        se a tabela ainda não foi carregada em um data frame retorna erro.
        """
        if self.__tabela_data_frame is None:
            self.e._("A planilha não pode ser recarregada pois ainda não "
                     "foi carregada pela primeira vez.\n"
                     "Necessário executar a função carrega_dados() primeiro.")
            raise RuntimeError

        # Reset do cursor para o index 0.
        self.__cursor = None
        self.__cursor = self.__tabela_data_frame.itertuples(index=False)

    def le_prox_registro(self):
        """
        Lê a próximo registro da tabela.

        Ret:
            tupla com o registro lido ou None se não houver mais registros a
            serem lidos.
        """

        if self.__cursor is None:
            self.__cursor = self.__tabela_data_frame.itertuples(index=False)

        try:
            registro = next(self.__cursor)
            registro = tuple(registro)
        except StopIteration:
            registro = None

        return registro

    def formata_colunas(self, cols):
        """
        Altera a estrutura (colunas) da planilha. Colunas podem ser suprimidas,
        duplicadas ou trocadas de ordem.

        Arg:
        cols:   lista com o índice (zero-based) das colunas finais da planilha.
                Por exemplo, para duplicar a primeira coluna como última coluna
                numa planilha original de 3 colunas, esse parâmetro deve ser
                [0, 1, 2, 0]
        """

        df_original = self.__tabela_data_frame.copy()
        df_original_cols = list(df_original.columns)
        self.__tabela_data_frame = pd.DataFrame()

        i = 0
        for col in cols:
            self.__tabela_data_frame.insert(
                    i, 
                    df_original_cols[col], 
                    df_original[df_original_cols[col]],
                    allow_duplicates=True)
            i += 1

