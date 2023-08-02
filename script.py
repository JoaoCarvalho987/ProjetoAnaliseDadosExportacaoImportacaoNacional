import csv
import os
path_imp = r"D:\pythonDSA\TurimProcessoSeletivo\IMP_2022.CSV"
path_exp = r"D:\pythonDSA\TurimProcessoSeletivo\EXP_2022.CSV"
path_resul = r"D:\pythonDSA\TurimProcessoSeletivo\resultado"


def process(imp: str, exp: str, resul: str) -> None:
    print (resul)
    estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    # Bloco de exportação
    with open(exp, "r") as exportacao:
        linhas_exportacao = exportacao.read().split('\n')
    atributos_produtos_exportacao = [
    [(linha.split(';'))[1],(linha.split(';'))[2], (linha.split(';'))[5], (linha.split(';'))[-1]]
    for linha in linhas_exportacao[1:-1]
    ]
    
    # Bloco de importação
    with open(imp, "r") as importacao:
        linhas_importacao = importacao.read().split('\n')
    atributos_produtos_importacao = [
    [(linha.split(';'))[1],(linha.split(';'))[2], (linha.split(';'))[5], (linha.split(';'))[-1]]
    for linha in linhas_importacao[1:-1]
    ]
    
    for i in estados:
            valores_estado_importacao = list(filter(lambda x: x[2]==f'"{i}"', [linha for linha in atributos_produtos_importacao]))
            valores_estado_exportacao = list(filter(lambda x: x[2]==f'"{i}"', [linha for linha in atributos_produtos_exportacao]))
            ids_importacao_exportacao = set([linha[1].strip('"') for linha in valores_estado_importacao]) | set([linha[1].strip('"') for linha in valores_estado_exportacao])
            with open(os.path.join(resul, i + ".csv"), "w") as arquivo_resultado_csv:
                escritor = csv.writer(arquivo_resultado_csv)

                escritor.writerow(['NCM'] + [acao.strip("',[]") for mes in meses for acao in [f'exp_{mes}', f'imp_{mes}', f'net_{mes}']] + ['exp_2022', 'imp_2022', 'net_2022'])              
                for id in list(ids_importacao_exportacao):
                    row_final = list()
                    soma_total_importacao = 0
                    soma_total_exportacao = 0
                    for mesAtual in range(1, 13):
                        row_importacao = list(filter(lambda x: (x[1].strip('"'))==id and int(x[0].strip('"')) == mesAtual, [linha for linha in valores_estado_importacao]))
                        row_exportacao = list(filter(lambda x: (x[1].strip('"'))==id and int(x[0].strip('"')) == mesAtual, [linha for linha in valores_estado_exportacao]))                        
                        soma_exportacao = sum([int(i[-1]) if i else 0 for i in row_exportacao])
                        soma_importacao = sum([int(i[-1]) if i else 0 for i in row_importacao])
                        row_final.append(soma_exportacao)
                        row_final.append(soma_importacao)
                        soma_total_importacao += soma_importacao
                        soma_total_exportacao += soma_exportacao
                        row_final.append(soma_exportacao-soma_importacao)
                    escritor.writerow([str(id)]+ [str(s).strip("',[]") for s in row_final] + [soma_total_exportacao, soma_total_importacao, (soma_total_exportacao-soma_total_importacao)]) 
    return None

def main() -> None:
    process(path_imp, path_exp, path_resul)

if __name__ == "__main__":
    main()