<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/3d68948e-963a-46f0-a261-d1c91d2efc15" />


## Objetivo:

O foco central deste projeto é o desenvolvimento de um algoritmo de Machine Learning para a precificação dinâmica de imóveis disponíveis para aluguel na plataforma Airbnb. O valor reside na construção e engenharia do sistema, com uma forte ênfase na implementação de um ciclo de MLOps (Machine Learning Operations) completo e robusto.

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

## Tecnologias utlizadas: 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Nota sobre a Análise de Dados (EDA):

A Análise Exploratória e o tratamento de dados foram realizados para informar o Feature Engineering. Por uma decisão de escopo, e visando maior clareza na documentação do ciclo de vida, esta seção foi intencionalmente resumida. Todo o processo detalhado de exploração, clean-up e feature selection está integralmente versionado nos Notebooks de Desenvolvimento (./notebooks) do repositório, garantindo rastreabilidade e foco na arquitetura de MLOps e no resultado final do pipeline.

## Modelagem: 

# Cluster: 

Conduzi uma clusterizaçao selecionando duas caracteristicas que separam os hosts em rating de avaliaçao e frequencia de avaliaçoes por mes. Para fazer bom separamento dos klusters, realizei o teste de cotovelo com os dados normalizados com min max scaler e validei com Davies Bouldin score. 
Segue o grafico do teste de cotovelo: 
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




