<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/3d68948e-963a-46f0-a261-d1c91d2efc15" />

## Problema de Negócio:

O Airbnb precisa ajustar os preços dinamicamente para maximizar reservas e receita, considerando características do imóvel, reputação do host e demanda do mercado.
Este projeto cria um modelo preditivo capaz de sugerir preços baseados em dados históricos, comportamento do host e métricas de avaliações, ajudando a tomar decisões mais assertivas e automatizadas.

O projeto está estruturado nas seguintes etapas:

- Entendimento do Problema

- Criação da Base de Dados

- Engenharia e Criação de Variáveis

- Análise Exploratória de Dados (EDA)

- Criação de Ciclos de Vida do Modelo

- Criação de Features para Modelagem

- Construção da ABT (Analytics Base Table)

- Implementação de Feature Store

- Treinamento e Otimização dos Modelos

- Deploy e Monitoramento com Práticas de MLOps

## Tecnologias utilizadas: 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Foco na Arquitetura MLOps:

<img width="1139" height="274" alt="image" src="https://github.com/user-attachments/assets/d46fafa0-f4d7-4cb2-8320-a38fdb9fb02d" />


A Análise Exploratória (EDA) e o tratamento de dados foram cruciais para a etapa de Feature Engineering. Para manter o foco deste README na arquitetura do pipeline, ciclo de vida do modelo e resultados, os notebooks detalhados de exploração e limpeza estão versionados e disponíveis na pasta /notebooks.
## Modelagem: 

# Cluster: 

Conduzi uma clusterização selecionando duas características que separam os hosts com base na nota das avaliações (review_scores_rating) e na frequência de avaliações por mês (reviews_per_month). Para obter um bom separamento dos clusters, realizei o método do cotovelo utilizando os dados normalizados com MinMaxScaler e validei os resultados com o Davies-Bouldin Score.

A seguir, apresenta-se o gráfico do teste do cotovelo:

<img width="755" height="425" alt="image" src="https://github.com/user-attachments/assets/21049820-3f15-4f07-8add-74cd9beecf9a" />

Segue a separação dos clusters:

<img width="758" height="420" alt="image" src="https://github.com/user-attachments/assets/6f71045e-2c31-401b-870d-577eb4ab0f34" />


Com base no gráfico de dispersão apresentado, que relaciona a métrica reviews_per_month (avaliações por mês) com a review_scores_rating (nota das avaliações), podemos ver que os tipos de hosts foram divididos em dois grupos (Cluster 0 e Cluster 1) da seguinte forma:

Os limites dos clusters indicam que a divisão principal ocorreu com base na frequência de avaliações (reviews_per_month), resultando em dois perfis de host distintos:

Como podemos ver graficamente, os tipos de hosts foram divididos quase de forma perfeita em dois grupos:

Cluster 1 (Laranja): Hosts com alta qualidade, mas baixo volume de avaliações.

Este grupo está concentrado na faixa de baixa frequência de avaliações por mês (aproximadamente até 3.0), mas com alta nota média das avaliações (principalmente acima de 80, chegando a 100).  Representa hosts com reputação excelente, mas que recebem poucas reservas (e, consequentemente, poucas avaliações).

Cluster 0 (Azul): Hosts com alta qualidade e alto volume de avaliações.

Este grupo apresenta uma alta frequência de avaliações por mês (acima de 3.0, chegando a 12.0 ou mais) e mantém alta nota média das avaliações (principalmente acima de 80, chegando a 100). Representa hosts com alta demanda, alta frequência de reservas e que, apesar do grande volume, conseguem manter uma excelente qualidade no serviço.

# Treinamento: 

A fase de modelagem foi iniciada utilizando a Analytics Base Table (ABT), gerada a partir da base HostLifeCycle.db. Esta ABT serviu de fonte primária para popular nossa Feature Store, que, por sua vez, garantiu o fornecimento consistente e versionado das features para o treinamento.

Por se tratar de um problema de precificação de imóveis (uma tarefa de previsão de valor contínuo), o desafio foi endereçado utilizando uma abordagem de Regressão.

A estratégia de treinamento consistiu na avaliação de um conjunto diversificado de modelos regressivos, visando identificar o algoritmo com o melhor desempenho e estabilidade para o deploy em produção. Os modelos avaliados foram: Regressão Linear, Árvore de Decisão, Random Forest, AdaBoost e XGBoost

# Métricas de Treinamento e Teste: 

[TREINO] Modelo: Regressao linear -> {'R²': 0.5824575956165494, 'MSE': 3373.5703233407417, 'MAE': 35.865842620240045}

[TESTE]  Modelo: Regressao linear -> {'R²': 0.5877863061831368, 'MSE': 3134.288847699121, 'MAE': 35.34109448637189}

[TREINO] Modelo: Arvore de decisao -> {'R²': 0.9991523080429326, 'MSE': 6.8490012024523255, 'MAE': 0.1991921552687735}

[TESTE]  Modelo: Arvore de decisao -> {'R²': 0.26029364623657325, 'MSE': 5624.396787271514, 'MAE': 44.95019788918206}

[TREINO] Modelo: Random forest -> {'R²': 0.9388035196790947, 'MSE': 494.4423075025393, 'MAE': 13.165682319225311}

[TESTE]  Modelo: Random forest -> {'R²': 0.5712379970360033, 'MSE': 3260.1148005632226, 'MAE': 34.507110739822416}

[TREINO] Modelo: AdaBoost -> {'R²': -0.0142394918126445, 'MSE': 8194.636555278094, 'MAE': 82.55610949684166}

[TESTE]  Modelo: AdaBoost -> {'R²': -0.2192972170031744, 'MSE': 9270.991542996833, 'MAE': 86.10647680744755}

[TREINO] Modelo: XGboost -> {'R²': 0.9729670846446976, 'MSE': 218.41480060137621, 'MAE': 9.789531707763672}

[TESTE]  Modelo: XGboost -> {'R²': 0.5725595318458785, 'MSE': 3250.066440019727, 'MAE': 33.93905085057885}

Observação: Árvores individuais tiveram overfitting evidente.

Random Forest e XGBoost apresentam melhor equilíbrio entre treino e teste.

Para discriminar qual era o melhor modelo com base a métricas e escolhas proprias, eu criei uma funçao discriminant.py que foi testada utilizando o pytest e herdada pelo laço de treinamento dos modelos

Apesar de eu esperar que a função discriminant.py apontasse para um modelo, tive minhas expectativas frustradas, pois as métricas obtidas no treinamento e nos testes não alcançaram os valores definidos na função. Isso se deve a alguns fatores, como a baixa quantidade de dados na amostra, o comportamento sazonal, que influencia na capacidade dos modelos de generalizar a variância explicada (R²) e a falta de bons hiperparâmetros nos modelos. 

# Analise de Multicolinearidade (VIF):

Para verificar se havia influência da paralelização das variáveis, realizei um estudo de VIF (Variance Inflation Factor), que indica o grau de multicolinearidade entre elas.

Costumo definir os seguintes limites de interpretação para o VIF:

0 – 6: baixa multicolinearidade

7 – 10: multicolinearidade média

10 – 15: multicolinearidade aceitável

> 16: alta multicolinearidade

Abaixo, apresento um gráfico para facilitar a visualização dos resultados, embora eu pessoalmente prefira analisá-los em formato de tabela.

VIF:

<img width="769" height="615" alt="image" src="https://github.com/user-attachments/assets/32fad7ca-20d3-47a5-945b-de7e6ca58ec5" />

Observa-se uma forte multicolinearidade entre as variáveis availability_90, availability_365 e mean_availability, o que explica o desempenho artificialmente elevado do modelo e a dependência excessiva da Regressão Linear em relação à correlação entre essas features.

# Função discriminant.py:

<img width="1172" height="938" alt="image" src="https://github.com/user-attachments/assets/1dfd4c0b-d36e-4854-bab7-c63f22c0e6a1" />

## SHAP VALUES:

O modelo Random Forest apresentou o melhor desempenho mesmo com os hiperparâmetros padrão. A partir disso, realizei uma análise com SHAP para investigar de forma interpretável como cada feature influenciou as decisões do modelo, reforçando a transparência e compreensão dos resultados.
Shap: 

<img width="776" height="920" alt="image" src="https://github.com/user-attachments/assets/c0518ad4-0b4f-4ee1-96ee-7f537abae970" />


## Optuna - Busca por Hiperparametros:

Para realizar uma busca otimizada dos hiperparâmetros dos modelos, utilizei a biblioteca Optuna (já aplicada em outros projetos).
Com ela, conduzi uma busca automatizada dentro de intervalos de parâmetros previamente definidos, com o objetivo de maximizar o desempenho dos modelos.

Os modelos escolhidos para essa otimização foram o XGBoost e o Random Forest, pois ambos apresentaram as melhores métricas com os parâmetros default.

As métricas obtidas após a busca foram:

XGBoost: {'R²': 0.6213, 'MSE': 2879.19, 'MAE': 32.20}

Random Forest: {'R²': 0.6021, 'MSE': 3024.77, 'MAE': 33.80}

O modelo XGBoost demonstrou uma ligeira vantagem em relação ao Random Forest, apresentando menores valores de MAE e MSE, além de um R² superior, o que indica uma melhor capacidade de explicar a variabilidade dos dados.

Por exemplo:

o modelo XGBoost apresentou um R² ≈ 0,62, o que significa que ele é capaz de explicar aproximadamente 62% da variância dos valores reais. Em outras palavras, caso o conjunto de dados sofra variações, o modelo consegue capturar e explicar cerca de 62% dessas mudanças.

Já o MAE (erro médio absoluto) representa a diferença média entre o valor previsto e o valor real. Assim, com um MAE de aproximadamente 32,20, o modelo apresenta um erro médio de cerca de 32 dólares em relação ao preço real. Esse valor pode variar conforme as características específicas do host e do quarto, podendo ser maior ou menor em alguns casos.

Por exemplo, se estivermos prevendo o preço de um quarto que custa $900, o modelo tenderia a errar, em média, cerca de $32 para mais ou para menos, ou seja, preveria aproximadamente entre $868 e $932.

- Ambos os modelos estão previstos para uso em produção, mas cada um será direcionado a uma finalidade específica dentro da aplicação.

- Para um melhor aproveitamento dos parâmetros otimizados, exportei os hiperparâmetros dos modelos para um arquivo .json, armazenado na pasta /optuna.




## Criação da aplicação e Deploy 

Na etapa de deploy da aplicação, a ideia é criar a arquitetura da API utilizando FastAPI, conteinerizar com Docker e Docker Compose e prover na AWS, usando o LocalStack.

A aplicação consistirá em dois gateways para inferência: 

## Predição em batch

O usuário fornecerá um arquivo CSV com dados dos hosts. A API coletará esses dados, fará o tratamento e os enviará para o modelo XGBoost, que realizará as predições. Para ilustrar o raciocínio, que por definição é simples, criei um desenho bem básico da ideia:

<img width="1454" height="486" alt="image" src="https://github.com/user-attachments/assets/434894c0-8ef0-4f47-8508-9530ecccff02" />

A estrutura da API ficou dessa forma:

<img width="1480" height="2230" alt="image" src="https://github.com/user-attachments/assets/c21a4ae4-a018-4de7-84fc-7c1bf0da9e91" />

Utilizei o conceito de assincronismo para lidar com requisições e processamentos de forma não bloqueante, otimizando o tempo de resposta e o uso dos recursos da aplicação. 

A saída do modelo consiste em uma matriz N×2, que logo é transformada em um dataframe e exportada para melhor visualização e análises dos hosts.

O arquivo .csv que contém as previsões está presente no diretório /data.

# Qual problema essa abordagem resolve?

Provendo uma API que faz previsões em batch, permite que setores que possuem arquivos históricos dos hosts possam precificar de forma assertiva, justa, com pouco tempo de processamento e de forma direta.











