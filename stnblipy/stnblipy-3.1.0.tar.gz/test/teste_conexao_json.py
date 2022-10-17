
import sys
sys.path.append('..')

from blipy.conexao_bd import ConexaoBD


from blipy.job import Job
from blipy.enum_tipo_col_bd import TpColBD as tp
import blipy.func_transformacao as ft
trim = ft.Trim()

class LookupConverteHTML():
    """
    Faz uma transformação específica de primeiro fazer um lookup e depois
    realizar uma operação com o resultado do lookup.
    """
 
    def __init__(self, 
            conexao, 
            tabela_lookup, 
            campo, 
            chave,
            filtro, 
            qtd_bytes,
            operacao):
        """
        Args:
        operacao: ação a ser realizada com o retorno do lookup. Valores
        possíveis: 'html' ou 'trim'.

        Os demais argumentos são Idênticos aos das classes LookupViaTabela e
        HTMLParaTxt.
        """

        self.__conexao = conexao
        self.__tabela_lookup = tabela_lookup
        self.__campo = campo
        self.__chave = chave
        self.__filtro = filtro
        self.__qtd_bytes = qtd_bytes
        self.__operacao = operacao
 
    def transforma(self, entradas):
        """
        Retorna a string buscada na lookup truncado na quantidade de bytes
        informada ou com trim.

        Args:
            entradas : tupla contendo a string a ser transformada
        """

        if len(entradas) != 1:
            raise RuntimeError(
                "Não pode haver mais de um dado de entrada para essa "
                "transformação.")

        if entradas[0] is None:
            return None

        ret = ft.LookupViaTabela(
                self.__conexao, 
                self.__tabela_lookup, 
                self.__campo, 
                self.__chave, 
                self.__filtro).transforma(entradas)
        
        if self.__operacao == "html":
            return ft.HTMLParaTxt(self.__qtd_bytes).transforma((ret, ))
        else:
            return trim.transforma((ret, ))

class GetCriticidade_3Pro():
    def __init__(self, conn_stg, conn_prd):
        self.__conn_stg = conn_stg
        self.__conn_prd = conn_prd

    def transforma(self, entradas):
        nome_criticidade = ft.LookupViaTabela(
            self.__conn_stg,
            "MVW_CRITICIDADE_SOLUCAO",
            "CRITICIDADE3PRO",
            "ID_SOLUCAO").transforma(entradas)

        if nome_criticidade is None:
            ret = None
        elif nome_criticidade == "NÃO CALCULADO":
            ret = -9
        else:
            # obtém o ID através do nome
            # como só deve haver um registro ativo para cada nome, esse
            # select só deve retornar uma linha
            cursor = self.__conn_prd.executa("select ID_TIPO_CRITICIDADE "
                "from COSIS_CORPORATIVO.TIPO_CRITICIDADE@DL_APEX_PRODUCAO "
                "where SN_ATIVO = 'S' and "
                "NO_TIPO_CRITICIDADE = '" + nome_criticidade + "'")

            ret = next(cursor)[0] 
        
        return ret



if __name__ == "__main__":
    job = Job("Teste Carga")

    try:
        conn_stg, conn_prd, conn_corp = ConexaoBD.from_json()
    except:
        sys.exit()

    # print(conn_stg)
    # print(conn_prd)
    # print(conn_corp)

    # dimensão LOCAL_HOSPEDAGEM
    # cols_entrada = ["ID_LOCAL_HOSPEDAGEM",
    #                 "NO_LOCAL_HOSPEDAGEM"]
    # cols_saida = [  ["ID_LOCAL_HOSPEDAGEM", tp.NUMBER],
    #                 ["NO_LOCAL_HOSPEDAGEM", tp.STRING]]
    # job.importa_tabela_por_nome(   
    #         conn_stg, 
    #         conn_prd, 
    #         "MVW_LOCAL_HOSPEDAGEM", 
    #         "LOCAL_HOSPEDAGEM",
    #         cols_entrada, 
    #         cols_saida)
    # 
    # 
    # # dimensão API
    # cols_entrada = ["ID_SOLUCAO", 
    #                 "ID_ROTINA", 
    #                 "NO_ROTINA", 
    #                 "DS_ROTINA", 
    #                 "NO_VERSAO", 
    #                 "DT_VERSAO", 
    #                 "ID_TIPO_PERIODICIDADE_ROTINA", 
    #                 "TX_PERIODICIDADE", 
    #                 "NO_HOSPEDAGEM", 
    #                 "TX_LEGILACAO_ASSOCIADA", 
    #                 "TX_LINK_DOCUMENTACAO", 
    #                 "SN_INICIATIVA_PRIVADA",
    #                 "TX_PUBLICO_ALVO", 
    #                 "TX_MODELO_OFERTA",
    #                 "TX_ROTEIRO_CONCESSAO", 
    #                 "TX_CONTROLE_ACESSO",
    #                 "TX_DETALHAMENTO_ACESSO", 
    #                 "TX_DISPONIBILIDADE", 
    #                 "TX_DETALHAMENTO",
    #                 "TX_PROTOCOLO_SEGURANCA",
    #                 "TX_DETALHAMENTO_SEGURANCA", 
    #                 "TX_DETALHAMENTO_FUNCIONALIDADE", 
    #                 "TX_ENDPOINT_PRODUCAO", 
    #                 "TX_ENDPOINT_SANDBOX", 
    #                 "TX_SWAGGER", 
    #                 "TX_TECNOLOGIA",
    #                 "TX_TAGS"]
    # cols_saida = [  ["ID_SOLUCAO", tp.NUMBER], 
    #                 ["ID_API", tp.NUMBER], 
    #                 ["NO_API", tp.STRING], 
    #                 ["DS_API", tp.STRING, 
    #                    ft.HTMLParaTxt(500)], 
    #                 ["NO_VERSAO", tp.STRING], 
    #                 ["DT_VERSAO", tp.DATE], 
    #                 ["ID_TIPO_PERIODICIDADE", tp.NUMBER], 
    #                 ["TX_PERIODICIDADE", tp.STRING], 
    #                 ["NO_HOSPEDAGEM", tp.STRING], 
    #                 ["TX_LEGISLACAO_ASSOCIADA", tp.STRING], 
    #                 ["TX_LINK_DOCUMENTACAO", tp.STRING,
    #                     ft.TruncaStringByte(500)], 
    #                 ["SN_OFERTA_INICIATIVA_PRIVADA", tp.STRING, trim],
    #                 ["TX_PUBLICO_ALVO", tp.STRING], 
    #                 ["TX_MODELO_OFERTA", tp.STRING, 
    #                     ft.DePara({
    #                         "G": "Gratuito",
    #                         "V": "Gratuito até volume",
    #                         "P": "Pago"})],
    #                 ["TX_ROTEIRO_CONCESSAO", tp.STRING, 
    #                    ft.HTMLParaTxt(500)], 
    #                 ["TX_FORMA_AUTENTICACAO", tp.STRING, 
    #                     ft.DePara({
    #                         "L": "Livre",
    #                         "H": "HTTP Basic",
    #                         "O": "OAuth",
    #                         "C": "Certificado Digital",
    #                         "A": "API Key",
    #                         "S": "SAML",
    #                         "T": "Outros"})],
    #                 ["TX_DETALHAMENTO_ACESSO", tp.STRING, 
    #                    ft.HTMLParaTxt(500)], 
    #                 ["TX_DISPONIBILIDADE", tp.STRING], 
    #                 ["TX_NIVEL_SERVICO", tp.STRING],
    #                 ["TX_PROTOCOLO_SEGURANCA", tp.STRING, 
    #                     ft.DePara({
    #                         "S": "SSL",
    #                         "W": "WS-SECURITY",
    #                         "N": "Nenhum",
    #                         "O": "Outro"})],
    #                 ["TX_DETALHAMENTO_SEGURANCA", tp.STRING, 
    #                    ft.HTMLParaTxt(500)], 
    #                 ["TX_DETALHAMENTO_FUNCIONALIDADE", tp.STRING, 
    #                    ft.HTMLParaTxt(500)], 
    #                 ["TX_ENDPOINT_PRODUCAO", tp.STRING], 
    #                 ["TX_ENDPOINT_SANDBOX", tp.STRING], 
    #                 ["TX_SWAGGER", tp.STRING], 
    #                 ["TX_FORMATO_RESPOSTA", tp.STRING],
    #                 ["TX_TAGS", tp.STRING]]
    # job.importa_tabela_por_nome(   
    #         conn_stg, 
    #         conn_prd, 
    #         "MVW_ROTINA",
    #         "API",
    #         cols_entrada, 
    #         cols_saida,
    #         filtro_entrada="ID_TIPO_ROTINA = 3")



    # fago SOLUCAO
    cols_entrada = [ "ID_SOLUCAO ",
                     "NO_SOLUCAO",
                     "DS_SOLUCAO",
                     "SG_SOLUCAO",
                     "ID_SOLUCAO", 
                     "ID_SOLUCAO",
                     "HR_TEMPO_DADOS_SIS_PERDIDO",
                     "HR_TEMPO_SIS_INDISPONIVEL",
                     "AN_TEMPO_HIST_DADOS_MANTIDO",
                     "TX_LINK_ACESSO",
                     "TX_TERCEIRIZADO_DM",
                     "TX_VIDEO_DATAMART",
                     "NO_DEV_DATAMART",
                     "NO_PRD_DATAMART",
                     "DT_ULTIMA_VERIF_DATAMART",
                     "SN_SISTEMA_ESTRUTURANTE",
                     "SN_ESTRATEGICO",
                     "SN_DESENV_DESCENTRALIZADO",
                     "SN_INFORMACAO_SIGILOSA_LAI",
                     "SN_INFORMACAO_PESSOAL_LGPD",
                     "SN_EXISTE_CONTING_SISTEMA",
                     "SN_SIGILOSO_DATAMART",
                     "SN_LGPD_DATAMART",
                     "ID_IMPACTO_FINANCEIRO",
                     "ID_IMPACTO_NA_IMAGEM_JUNTO_A",
                     "ID_RISCO_PROCESSO_NEGOCIO",
                     "ID_ETAPA_SOLUCAO",
                     "ID_LOCAL_HOSPEDAGEM",
                     "ID_ABRANGENCIA",
                     "ID_UNIDADE_DESENVOLVEDORA",
                     "ID_TIPO_PERIODICIDADE_ROTINA",
                     "ID_UNIDADE_DEMANDANTE",
                     "ID_USUARIO",
                     "ID_SOLUCAO",
                     "ID_SOLUCAO"]
    cols_saida = [  ["ID_SOLUCAO ", tp.NUMBER],
                    ["NO_SOLUCAO", tp.STRING], 
                    ["DS_SOLUCAO", tp.STRING, ft.TruncaStringByte(500)],
                    ["SG_SOLUCAO", tp.STRING], 
                    ["DS_SOLUCAO_DETALHADA", tp.STRING, 
                         LookupConverteHTML(
                            conn_stg, 
                            "MVW_BLOCO_INFO_SOLUCAO",
                            "TX_INFORMACAO",
                            "ID_SOLUCAO", 
                            "ID_TIPO_BLOCO_INFORMAC = 31",
                            500,
                            "html")],
                    ["DS_RESUMO_EXECUTIVO", tp.STRING, 
                         LookupConverteHTML(
                            conn_stg, 
                            "MVW_BLOCO_INFO_SOLUCAO",
                            "TX_INFORMACAO",
                            "ID_SOLUCAO", 
                            "ID_TIPO_BLOCO_INFORMAC = 69",
                            500,
                            "html")],
                    ["HR_TEMPO_DADOS_SIS_PERDIDO", tp.NUMBER],
                    ["HR_TEMPO_SIS_INDISPONIVEL", tp.NUMBER],
                    ["AN_TEMPO_HIST_DADOS_MANTIDO", tp.NUMBER],
                    ["TX_LINK_ACESSO", tp.STRING], 
                    ["TX_TERCEIRIZADO_DATAMART", tp.STRING], 
                    ["TX_VIDEO_DATAMART", tp.STRING], 
                    ["NO_ESQUEMA_DEV_DATAMART", tp.STRING], 
                    ["NO_ESQUEMA_PRD_DATAMART", tp.STRING], 
                    ["DT_ULTIMA_VERIFICACAO_DATAMART", tp.DATE],
                    ["SN_SISTEMA_ESTRUTURANTE", tp.STRING, trim], 
                    ["SN_ESTRATEGICO", tp.STRING, ft.DeParaSN(inverte=True)],
                    ["SN_DESENV_DESCENTRALIZADO", tp.STRING, trim], 
                    ["SN_INFORMACAO_SIGILOSA_LAI", tp.STRING, trim], 
                    ["SN_INFORMACAO_PESSOAL_LGPD", tp.STRING, trim], 
                    ["SN_EXISTE_CONTINGENCIA_SISTEMA", tp.STRING, trim], 
                    ["SN_SIGILOSO_DATAMART", tp.STRING, trim], 
                    ["SN_LGPD_DATAMART", tp.STRING, trim], 
                    ["ID_IMPACTO_FINANCEIRO", tp.NUMBER],
                    ["ID_IMPACTO_IMAGEM", tp.NUMBER],
                    ["ID_RISCO_PROCESSO_NEGOCIO", tp.NUMBER],
                    ["ID_SITUACAO", tp.NUMBER],
                    ["ID_LOCAL_HOSPEDAGEM", tp.NUMBER],
                    ["ID_ABRANGENCIA", tp.NUMBER],
                    ["ID_UNIDADE_DESENVOLVEDORA", tp.NUMBER],
                    ["ID_PERIODICIDADE_ATUALIZACAO", tp.NUMBER],
                    ["ID_UNIDADE_DEMANDANTE", tp.NUMBER],
                    ["ID_RESPONSAVEL_TECNICO", tp.NUMBER],
                    ["ID_CRITICIDADE_3PRO", tp.NUMBER, 
                        GetCriticidade_3Pro(conn_stg, conn_prd)],
                    ["TX_CRITICIDADE_SOLUCAO", tp.STRING, 
                        LookupConverteHTML(
                            conn_stg,
                            "MVW_CRITICIDADE_SOLUCAO",
                            "CRITICIDADESOLUCAO",
                            "ID_SOLUCAO",
                            "",
                            None,
                            "trim")]]

    job.importa_tabela_por_nome(   
            conn_stg, 
            conn_prd, 
            "MVW_SOLUCAO", 
            "SOLUCAO",
            cols_entrada, 
            cols_saida)

