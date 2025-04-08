# Importando bibliotecas necessárias
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------
# Funções para conversão de tipos de dados em um DataFrame
#-----------------------------------------------------------------------

# Converte colunas especificadas para tipo de dado string
def converter_para_string(conjunto_dados, colunas):
    """Converte colunas especificadas para o tipo de dado string.
    Parâmetros:
        conjunto_dados (pd.DataFrame): O conjunto de dados contendo as colunas a serem convertidas.
        colunas (list): Lista com os nomes das colunas a serem convertidas.
    Retorno:
        None: Esta função não retorna um valor, pois faz as mudanças diretamente no conjunto de dados.
    """
    for coluna in colunas:
        conjunto_dados[coluna] = conjunto_dados[coluna].astype("string")

# Converte colunas especificadas para tipo de dado inteiro
def converter_para_inteiro(conjunto_dados, colunas):
    """Converte colunas especificadas para o tipo de dado inteiro.
    Parâmetros:
        conjunto_dados (pd.DataFrame): O conjunto de dados contendo as colunas a serem convertidas.
        colunas (list): Lista com os nomes das colunas a serem convertidas.
    Retorno:
        None: Esta função não retorna um valor, pois faz as mudanças diretamente no conjunto de dados.
    """
    for coluna in colunas:
        conjunto_dados[coluna] = conjunto_dados[coluna].astype("int64")

# Converte colunas especificadas para tipo de dado float
def converter_para_float(conjunto_dados, colunas):
    """Converte colunas especificadas para o tipo de dado float.
    Parâmetros:
        conjunto_dados (pd.DataFrame): O conjunto de dados contendo as colunas a serem convertidas.
        colunas (list): Lista com os nomes das colunas a serem convertidas.
    Retorno:
        None: Esta função não retorna um valor, pois faz as mudanças diretamente no conjunto de dados.
    """
    for coluna in colunas:
        # Converte a coluna para o tipo de dado float64
        conjunto_dados[coluna] = conjunto_dados[coluna].astype("float64")

# Converte colunas especificadas para tipo de dado datetime
def converter_para_datetime(conjunto_dados, colunas):
    """Converte colunas especificadas para o tipo de dado datetime.
    Parâmetros:
        conjunto_dados (pd.DataFrame): O conjunto de dados contendo as colunas a serem convertidas.
        colunas (list): Lista com os nomes das colunas a serem convertidas.
    Retorno:
        None: Esta função não retorna um valor, pois faz as mudanças diretamente no conjunto de dados.
    """
    for coluna in colunas:
        conjunto_dados[coluna] = pd.to_datetime(conjunto_dados[coluna])

# Multiplica colunas especificadas por um fator
def multiplicar_por_fator(conjunto_dados, colunas, fator):
    """Multiplica colunas especificadas por um fator.
    Parâmetros:
        conjunto_dados (pd.DataFrame): O conjunto de dados contendo as colunas a serem multiplicadas.
        colunas (list): Lista com os nomes das colunas a serem multiplicadas.
        fator (float): O fator pelo qual as colunas devem ser multiplicadas.
    Retorno:
        None: Esta função não retorna um valor, pois faz as mudanças diretamente no conjunto de dados.
    """
    for coluna in colunas:
        conjunto_dados[coluna] = conjunto_dados[coluna] * fator


#-----------------------------------------------------------------------
# Funções para lidar com valores ausentes em um conjunto de dados
#-----------------------------------------------------------------------

# Calcula a porcentagem de valores ausentes no conjunto de dados
def calcular_porcentagem_valores_ausentes(dados):
    """Calcula a porcentagem de valores ausentes no conjunto de dados.
    Este método calcula a porcentagem de valores ausentes no conjunto de dados recebido como entrada.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
    Retorno:
        None: Esta função imprime a porcentagem de valores ausentes e não retorna um valor.
    """
    # Calcula o total de células do dataset
    total_de_celulas = np.prod(dados.shape)
    # Conta o número de valores ausentes por coluna
    quantidade_ausentes_por_coluna = dados.isnull().sum()
    # Calcula o total de valores ausentes em todo o conjunto de dados
    total_ausentes = quantidade_ausentes_por_coluna.sum()
    # Calcula a porcentagem de valores ausentes em relação ao total de células
    porcentagem_ausentes = (total_ausentes / total_de_celulas) * 100
    # Exibe a porcentagem de valores ausentes no conjunto de dados
    print(f"O conjunto de dados tem {round(porcentagem_ausentes, 2)}% de valores ausentes.")

# Calcula a porcentagem de linhas que possuem valores ausentes
def calcular_porcentagem_ausentes_por_linha(dados):
    """Calcula a porcentagem de linhas com valores ausentes no conjunto de dados.
    Este método calcula a porcentagem de linhas no conjunto de dados que possuem pelo menos um valor ausente.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
    Retorno:
        None: Esta função imprime a porcentagem de linhas com valores ausentes e não retorna um valor.
    """
    # Conta o número de linhas com pelo menos um valor ausente
    linhas_com_ausencias = sum(1 for _, linha in dados.iterrows() if linha.isna().any())
    # Calcula o número total de linhas no conjunto de dados
    total_linhas = dados.shape[0]
    # Calcula a porcentagem de linhas com valores ausentes
    porcentagem_linhas_ausentes = (linhas_com_ausencias / total_linhas) * 100
    # Exibe a porcentagem de linhas com valores ausentes
    print(f"{round(porcentagem_linhas_ausentes, 2)}% das linhas possuem pelo menos um valor ausente.")

# Gera um relatório com informações sobre valores ausentes por coluna
def relatorio_valores_ausentes_por_coluna(dados):
    """Gera um relatório com informações sobre valores ausentes por coluna.
    Este método gera um relatório com a quantidade e porcentagem de valores ausentes em cada coluna do conjunto de dados.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
    Retorno:
        pd.DataFrame: Um DataFrame com um resumo das informações sobre valores ausentes por coluna.
    """
    # Calcula a quantidade de valores ausentes por coluna
    quant_valores_ausentes = dados.isnull().sum()
    # Calcula a porcentagem de valores ausentes por coluna
    percent_valores_ausentes = 100 * quant_valores_ausentes / len(dados)
    # Coleta o tipo de dado de cada coluna
    tipos_de_dados = dados.dtypes
    # Junta as informações de valores ausentes e tipos de dado em um DataFrame
    resumo_valores_ausentes = pd.concat([quant_valores_ausentes, percent_valores_ausentes, tipos_de_dados], axis=1)
    # Renomeia as colunas para tornar os nomes mais compreensíveis
    resumo_valores_ausentes.columns = ['Quantidade de Ausentes', 'Porcentagem de Ausentes', 'Tipo de Dado']
    # Remove as colunas sem valores ausentes e classifica em ordem decrescente por porcentagem de valores ausentes
    resumo_valores_ausentes = resumo_valores_ausentes[resumo_valores_ausentes['Quantidade de Ausentes'] > 0].sort_values('Porcentagem de Ausentes', ascending=False).round(2)
    # Exibe um resumo do relatório
    print(f"O conjunto de dados tem {dados.shape[1]} colunas. \nForam encontradas {resumo_valores_ausentes.shape[0]} colunas com valores ausentes.")
    # Retorna o DataFrame com informações sobre valores ausentes por coluna
    return resumo_valores_ausentes

# Preenchimento de valores ausentes usando preenchimento progressivo
def preencher_ausentes_progressivo(dados, coluna):
    """Preenche valores ausentes usando preenchimento progressivo.
    Este método preenche valores ausentes em uma coluna usando o valor anterior não nulo.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados contendo a coluna a ser preenchida.
        coluna (str): O nome da coluna a ser preenchida.
    Retorno:
        pd.Series: A coluna com valores ausentes preenchidos.
    """
    # Conta a quantidade de valores ausentes na coluna
    quantidade_ausentes = dados[coluna].isna().sum()
    # Preenche valores ausentes com o método de preenchimento progressivo (forward fill)
    dados[coluna] = dados[coluna].fillna(method='ffill')
    # Exibe quantos valores foram preenchidos
    print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos usando o método de preenchimento progressivo.")
    # Retorna a coluna com valores ausentes preenchidos
    return dados[coluna]

# Preenchimento de valores ausentes usando preenchimento reverso
def preencher_ausentes_reverso(dados, coluna):
    """Preenche valores ausentes usando preenchimento reverso.
    Este método preenche valores ausentes em uma coluna usando o valor posterior não nulo.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados contendo a coluna a ser preenchida.
        coluna (str): O nome da coluna a ser preenchida.
    Retorno:
        pd.Series: A coluna com valores ausentes preenchidos.
    """
    # Conta a quantidade de valores ausentes na coluna
    quantidade_ausentes = dados[coluna].isna().sum()
    # Preenche valores ausentes com o método de preenchimento reverso (backward fill)
    dados[coluna] = dados[coluna].fillna(method='bfill')
    # Exibe quantos valores foram preenchidos
    print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos usando o método de preenchimento reverso.")
    # Retorna a coluna com valores ausentes preenchidos
    return dados[coluna]

# Preenchimento de valores ausentes usando a mediana
def preencher_ausentes_com_mediana(dados, coluna):
    """Preenche valores ausentes usando a mediana.
    Este método preenche valores ausentes em uma coluna usando a mediana da coluna.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados contendo a coluna a ser preenchida.
        coluna (str): O nome da coluna a ser preenchida.
    Retorno:
        pd.Series: A coluna com valores ausentes preenchidos.
    """
    # Calcula a mediana da coluna
    mediana = dados[coluna].median()
    # Conta a quantidade de valores ausentes na coluna
    quantidade_ausentes = dados[coluna].isna().sum()
    # Preenche valores ausentes com a mediana
    dados[coluna] = dados[coluna].fillna(mediana)
    # Exibe quantos valores foram preenchidos e o valor da mediana usada
    print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos com a mediana {mediana}.")
    # Retorna a coluna com valores ausentes preenchidos
    return dados[coluna]

# Preenchimento de valores ausentes usando a média
def preencher_ausentes_com_media(dados, coluna):
    """Preenche valores ausentes usando a média.
    Este método preenche valores ausentes em uma coluna usando a média da coluna.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados contendo a coluna a ser preenchida.
        coluna (str): O nome da coluna a ser preenchida.
    Retorno:
        pd.Series: A coluna com valores ausentes preenchidos.
    """
    # Calcula a média da coluna
    media = dados[coluna].mean()
    # Conta a quantidade de valores ausentes na coluna
    quantidade_ausentes = dados[coluna].isna().sum()
    # Preenche valores ausentes com a mediana
    dados[coluna] = dados[coluna].fillna(media)
    # Exibe quantos valores foram preenchidos e o valor da mediana usada
    print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos com a média {media}.")
    # Retorna a coluna com valores ausentes preenchidos
    return dados[coluna]


# Preenchimento de valores ausentes com um valor específico
def preencher_ausentes_com_valor(dados, coluna, valor):
    """Preenche valores ausentes com um valor específico.
    Este método preenche valores ausentes em uma coluna com um valor específico fornecido.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados contendo a coluna a ser preenchida.
        coluna (str): O nome da coluna a ser preenchida.
        valor: O valor específico a ser usado para preencher valores ausentes.
    Retorno:
        pd.Series: A coluna com valores ausentes preenchidos.
    """
    # Conta a quantidade de valores ausentes na coluna
    quantidade_ausentes = dados[coluna].isna().sum()
    # Preenche valores ausentes com o valor específico
    dados[coluna] = dados[coluna].fillna(valor)
    # Exibe quantos valores foram preenchidos e o valor usado
    if isinstance(valor, str):
        print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos com '{valor}'.")
    else:
        print(f"{quantidade_ausentes} valores ausentes na coluna {coluna} foram preenchidos com {valor}.")
    # Retorna a coluna com valores ausentes preenchidos
    return dados[coluna]

# Remoção de linhas duplicadas
def remover_linhas_duplicadas(dados):
    """Remove linhas duplicadas no conjunto de dados.
    Este método remove linhas duplicadas no conjunto de dados.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
    Retorno:
        None: Esta função não retorna um valor, mas imprime a quantidade de linhas removidas.
    """
    # Armazena o número inicial de linhas no conjunto de dados
    linhas_iniciais = dados.shape[0]
    # Remove linhas duplicadas
    dados.drop_duplicates(inplace=True)
    # Armazena o número final de linhas após remoção
    linhas_finais = dados.shape[0]
    # Calcula o número de linhas removidas
    quantidade_removida = linhas_iniciais - linhas_finais
    # Exibe quantas linhas duplicadas foram removidas
    if quantidade_removida == 0:
        print("Nenhuma linha duplicada foi encontrada.")
    else:
        print(f"{quantidade_removida} linhas duplicadas foram removidas.")

# Remoção de linhas com valores ausentes
def remover_linhas_com_ausencias(dados):
    """Remove linhas com valores ausentes no conjunto de dados.
    Este método remove linhas com valores ausentes no conjunto de dados.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
    Retorno:
        None: Esta função não retorna um valor, mas imprime a quantidade de linhas removidas.
    """
    # Armazena o número inicial de linhas no conjunto de dados
    linhas_iniciais = dados.shape[0]
    # Remove linhas com valores ausentes
    dados.dropna(inplace=True)
    # Armazena o número final de linhas após remoção
    linhas_finais = dados.shape[0]
    # Calcula o número de linhas removidas
    quantidade_removida = linhas_iniciais - linhas_finais
    # Exibe quantas linhas com valores ausentes foram removidas
    print(f"{quantidade_removida} linhas com valores ausentes foram removidas.")

# Remoção de colunas específicas
def remover_colunas(dados, colunas):
    """Remove colunas específicas no conjunto de dados.
    Este método remove colunas específicas no conjunto de dados.
    Parâmetros:
        dados (pd.DataFrame): O conjunto de dados a ser analisado.
        colunas (list): Lista de colunas a serem removidas.
    Retorno:
        None: Esta função não retorna um valor, mas imprime a quantidade de colunas removidas.
    """
    # Remove as colunas especificadas
    dados.drop(colunas, axis=1, inplace=True)
    # Calcula a quantidade de colunas removidas
    quantidade_removida = len(colunas)
    # Exibe quantas colunas foram removidas
    if quantidade_removida == 1:
        print(f"{quantidade_removida} coluna foi removida.")
    else:
        print(f"{quantidade_removida} colunas foram removidas.")


#-----------------------------------------------------------------------
# Funções para tratamento de outliers em um DataFrame
#-----------------------------------------------------------------------

# Classe para lidar com outliers em um conjunto de dados
class ManipuladorDeOutliers:

    # Inicialização com um DataFrame (CONSTRUTOR)
    def __init__(self, conjunto_dados: pd.DataFrame) -> None:
        """Inicializa o manipulador com um DataFrame.
        Parâmetros:
            conjunto_dados (pd.DataFrame): O conjunto de dados para trabalhar.
        """
        self.conjunto_dados = conjunto_dados

    # Conta a quantidade de outliers em colunas específicas
    def contar_outliers(self, Q1, Q3, IQR, colunas):
        """Conta a quantidade de outliers nas colunas especificadas.
        Parâmetros:
            Q1 (pd.Series): O primeiro quartil das colunas.
            Q3 (pd.Series): O terceiro quartil das colunas.
            IQR (pd.Series): A diferença interquartil das colunas.
            colunas (list): As colunas a serem verificadas.
        Retorno:
            list: Lista com a quantidade de outliers em cada coluna.
        """
        margem_de_corte = IQR * 1.5
        dados_temp = (self.conjunto_dados[colunas] < (Q1 - margem_de_corte)) | (self.conjunto_dados[colunas] > (Q3 + margem_de_corte))
        return [len(dados_temp[dados_temp[col] == True]) for col in dados_temp]

    # Calcula a assimetria (skewness) das colunas
    def calcular_assimetria(self, colunas=None):
        """Calcula a assimetria (skewness) das colunas.
        Parâmetros:
            colunas (list, optional): Lista de colunas para calcular a assimetria. Se não fornecida, todas as colunas do DataFrame serão consideradas.
        Retorno:
            list: Lista com a assimetria de cada coluna.
        """
        if colunas is None:
            colunas = self.conjunto_dados.columns
        return [self.conjunto_dados[col].skew() for col in colunas]

    # Calcula a porcentagem de outliers
    def calcular_porcentagem_outliers(self, lista):
        """Calcula a porcentagem de outliers.
        Parâmetros:
            lista (list): Lista com a quantidade de outliers em cada coluna.
        Retorno:
            list: Lista com a porcentagem de outliers em cada coluna.
        """
        return [str(round(((valor / 150001) * 100), 2)) + '%' for valor in lista]

    # Remove outliers das colunas especificadas
    def remover_outliers(self, colunas):
        """Remove outliers das colunas especificadas.
        Parâmetros:
            colunas (list): Lista de colunas para remover outliers.
        """
        for col in colunas:
            Q1, Q3 = self.conjunto_dados[col].quantile(0.25), self.conjunto_dados[col].quantile(0.75)
            IQR = Q3 - Q1
            margem_de_corte = IQR * 1.5
            limite_inferior, limite_superior = Q1 - margem_de_corte, Q3 + margem_de_corte
            self.conjunto_dados = self.conjunto_dados.drop(self.conjunto_dados[self.conjunto_dados[col] > limite_superior].index)
            self.conjunto_dados = self.conjunto_dados.drop(self.conjunto_dados[self.conjunto_dados[col] < limite_inferior].index)

    # Substitui outliers pelas margens definidas
    def substituir_outliers_por_limites(self, colunas):
        """Substitui outliers pelas margens definidas.
        Parâmetros:
            colunas (list): Lista de colunas para substituir outliers.
        """
        for col in colunas:
            Q1, Q3 = self.conjunto_dados[col].quantile(0.25), self.conjunto_dados[col].quantile(0.75)
            IQR = Q3 - Q1
            margem_de_corte = IQR * 1.5
            limite_inferior, limite_superior = Q1 - margem_de_corte, Q3 + margem_de_corte

            self.conjunto_dados[col] = np.where(self.conjunto_dados[col] > limite_superior, limite_superior, self.conjunto_dados[col])
            self.conjunto_dados[col] = np.where(self.conjunto_dados[col] < limite_inferior, limite_inferior, self.conjunto_dados[col])

    # Gera uma visão geral do conjunto de dados com informações sobre outliers
    def gerar_visao_geral(self, colunas) -> None:
        """Gera uma visão geral do conjunto de dados com informações sobre outliers.
        Parâmetros:
            colunas (list): Lista de colunas para gerar visão geral.
        Retorno:
            pd.DataFrame: DataFrame com informações sobre outliers nas colunas.
        """
        minimo = self.conjunto_dados[colunas].min()
        Q1 = self.conjunto_dados[colunas].quantile(0.25)
        mediana = self.conjunto_dados[colunas].quantile(0.5)
        Q3 = self.conjunto_dados[colunas].quantile(0.75)
        maximo = self.conjunto_dados[colunas].max()
        IQR = Q3 - Q1
        assimetria = self.calcular_assimetria(colunas)
        outliers = self.contar_outliers(Q1, Q3, IQR, colunas)
        margem_de_corte = IQR * 1.5
        limite_inferior, limite_superior = Q1 - margem_de_corte, Q3 + margem_de_corte

        nomes_colunas = ['Nome da Coluna', 'Mínimo', 'Q1', 'Mediana', 'Q3', 'Máximo', 'IQR', 'Limite Inferior', 'Limite Superior', 'Assimetria', 'Num_Outliers', 'Percentual de Outliers']
        
        dados = zip([coluna for coluna in self.conjunto_dados[colunas]], minimo, Q1, mediana, Q3, maximo, IQR, limite_inferior, limite_superior, assimetria, outliers, self.calcular_porcentagem_outliers(outliers))

        df_visao_geral = pd.DataFrame(data=dados, columns=nomes_colunas)
        
        df_visao_geral.set_index('Nome da Coluna', inplace=True)
        
        return df_visao_geral.sort_values('Num_Outliers', ascending=False).transpose()

