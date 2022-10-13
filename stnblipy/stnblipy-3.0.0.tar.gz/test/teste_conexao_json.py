
import sys
sys.path.append('..')

from blipy.conexao_bd import ConexaoBD


from blipy.job import Job
from blipy.enum_tipo_col_bd import TpColBD as tp
import blipy.func_transformacao as ft
trim = ft.Trim()



if __name__ == "__main__":
    job = Job("Teste Carga")

    try:
        conn_stg, conn_prd, conn_corp = ConexaoBD.from_json()
    except:
        sys.exit()

    print(conn_stg)
    print(conn_prd)
    print(conn_corp)

    # dimensão LOCAL_HOSPEDAGEM
    cols_entrada = ["ID_LOCAL_HOSPEDAGEM",
                    "NO_LOCAL_HOSPEDAGEM"]
    cols_saida = [  ["ID_LOCAL_HOSPEDAGEM", tp.NUMBER],
                    ["NO_LOCAL_HOSPEDAGEM", tp.STRING]]
    job.importa_tabela_por_nome(   
            conn_stg, 
            conn_prd, 
            "MVW_LOCAL_HOSPEDAGEM", 
            "LOCAL_HOSPEDAGEM",
            cols_entrada, 
            cols_saida)



    # dimensão API
    cols_entrada = ["ID_SOLUCAO", 
                    "ID_ROTINA", 
                    "NO_ROTINA", 
                    "DS_ROTINA", 
                    "NO_VERSAO", 
                    "DT_VERSAO", 
                    "ID_TIPO_PERIODICIDADE_ROTINA", 
                    "TX_PERIODICIDADE", 
                    "NO_HOSPEDAGEM", 
                    "TX_LEGILACAO_ASSOCIADA", 
                    "TX_LINK_DOCUMENTACAO", 
                    "SN_INICIATIVA_PRIVADA",
                    "TX_PUBLICO_ALVO", 
                    "TX_MODELO_OFERTA",
                    "TX_ROTEIRO_CONCESSAO", 
                    "TX_CONTROLE_ACESSO",
                    "TX_DETALHAMENTO_ACESSO", 
                    "TX_DISPONIBILIDADE", 
                    "TX_DETALHAMENTO",
                    "TX_PROTOCOLO_SEGURANCA",
                    "TX_DETALHAMENTO_SEGURANCA", 
                    "TX_DETALHAMENTO_FUNCIONALIDADE", 
                    "TX_ENDPOINT_PRODUCAO", 
                    "TX_ENDPOINT_SANDBOX", 
                    "TX_SWAGGER", 
                    "TX_TECNOLOGIA",
                    "TX_TAGS"]
    cols_saida = [  ["ID_SOLUCAO", tp.NUMBER], 
                    ["ID_API", tp.NUMBER], 
                    ["NO_API", tp.STRING], 
                    ["DS_API", tp.STRING, 
                       ft.HTMLParaTxt(500)], 
                    ["NO_VERSAO", tp.STRING], 
                    ["DT_VERSAO", tp.DATE], 
                    ["ID_TIPO_PERIODICIDADE", tp.NUMBER], 
                    ["TX_PERIODICIDADE", tp.STRING], 
                    ["NO_HOSPEDAGEM", tp.STRING], 
                    ["TX_LEGISLACAO_ASSOCIADA", tp.STRING], 
                    ["TX_LINK_DOCUMENTACAO", tp.STRING,
                        ft.TruncaStringByte(500)], 
                    ["SN_OFERTA_INICIATIVA_PRIVADA", tp.STRING, trim],
                    ["TX_PUBLICO_ALVO", tp.STRING], 
                    ["TX_MODELO_OFERTA", tp.STRING, 
                        ft.DePara({
                            "G": "Gratuito",
                            "V": "Gratuito até volume",
                            "P": "Pago"})],
                    ["TX_ROTEIRO_CONCESSAO", tp.STRING, 
                       ft.HTMLParaTxt(500)], 
                    ["TX_FORMA_AUTENTICACAO", tp.STRING, 
                        ft.DePara({
                            "L": "Livre",
                            "H": "HTTP Basic",
                            "O": "OAuth",
                            "C": "Certificado Digital",
                            "A": "API Key",
                            "S": "SAML",
                            "T": "Outros"})],
                    ["TX_DETALHAMENTO_ACESSO", tp.STRING, 
                       ft.HTMLParaTxt(500)], 
                    ["TX_DISPONIBILIDADE", tp.STRING], 
                    ["TX_NIVEL_SERVICO", tp.STRING],
                    ["TX_PROTOCOLO_SEGURANCA", tp.STRING, 
                        ft.DePara({
                            "S": "SSL",
                            "W": "WS-SECURITY",
                            "N": "Nenhum",
                            "O": "Outro"})],
                    ["TX_DETALHAMENTO_SEGURANCA", tp.STRING, 
                       ft.HTMLParaTxt(500)], 
                    ["TX_DETALHAMENTO_FUNCIONALIDADE", tp.STRING, 
                       ft.HTMLParaTxt(500)], 
                    ["TX_ENDPOINT_PRODUCAO", tp.STRING], 
                    ["TX_ENDPOINT_SANDBOX", tp.STRING], 
                    ["TX_SWAGGER", tp.STRING], 
                    ["TX_FORMATO_RESPOSTA", tp.STRING],
                    ["TX_TAGS", tp.STRING]]
    job.importa_tabela_por_nome(   
            conn_stg, 
            conn_prd, 
            "MVW_ROTINA",
            "API",
            cols_entrada, 
            cols_saida,
            filtro_entrada="ID_TIPO_ROTINA = 3")

