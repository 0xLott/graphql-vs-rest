# Análise comparativa da performance de web APIs GraphQL vs REST

## 1. Introdução

Neste trabalho, realizou-se um experimento controlado com o objetivo de comparar a performance de APIs web quando implementadas em GraphQL versus REST. A fim de nortear este estudo, foram estabelecidas as seguintes questões de pesquisa:

- **RQ 01**: Respostas às consultas GraphQL são mais rápidas que respostas às consultas REST?
- **RQ 02**: Respostas às consultas GraphQL tem tamanho menor que respostas às consultas REST?

## 2. Design do experimento

O experimento foi elaborado visando assegurar a validade dos resultados e responder às questões de pesquisa propostas. Para isso, foram definidos hipóteses claras, variáveis dependentes e independentes, além de tratamentos que representam as condições a serem comparadas (GraphQL e REST).

#### 1. Hipóteses Nula e Alternativa

|                           | RQ 01                                               | RQ 02                                                   |
| ------------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| Hipótese Nula (H₀)        | Não há diferença significativa no tempo de resposta | Não há diferença significativa no tamanho das respostas |
| Hipótese Alternativa (Hₐ) | GraphQL tem tempos de resposta menores              | GraphQL tem respostas menores                           |

#### 2. Variáveis Dependentes

- **RQ 01**: Tempo de resposta (em ms)
- **RQ 02**: Tamanho do `response body` (em bytes)

#### 3. Variáveis Independentes

| Fator                        | Níveis             |
| ---------------------------- | ------------------ |
| Tipo de implementação de API | `GraphQL` e `REST` |

#### 4. Tratamentos

1. API implementada a partir de GraphQL
2. API implementada a partir de REST

#### 5. Objetos Experimentais

#### 6. Tipo de Projeto Experimental

#### 7. Quantidade de Medições

#### 8. Ameaças à Validade

## 3. Metodologia

### 3.1. Criação do Dataset

A coleta de dados foi realizada a partir da API do GitHub e implementada via GraphQL, buscando os 200 repositórios com maior número de estrelas, filtrados a partir dos seguintes critérios de seleção:

- Repositórios com pelo menos 100 PRs (mergeados ou fechados).
- PRs com status de `MERGED` ou `CLOSED`, que passaram por pelo menos uma revisão (campo `review` com valor maior que zero).
- PRs cuja revisão tenha levado mais de uma hora, eliminando assim revisões automáticas (como bots ou ferramentas de CI/CD).

Exemplo de objeto JSON obtido após extração e manipulação de dados de Pull Requests e seus atributos, utilizados para cálculo das métricas:

```json
{
  "objectId": "8f17a2ca-039f-4a5d-934a-6189989fa56e",
  "repositoryName": "freeCodeCamp",
  "ownerName": "freeCodeCamp",
  "author": "ahs-atan",
  "state": "MERGED",
  "createAt": "2018-10-19T08:45:30Z",
  "closetAt": "2018-11-17T10:04:49Z",
  "mergedAt": "2018-11-17T10:04:49Z",
  "changedFiles": 1,
  "deletions": 0,
  "additions": 4,
  "description": "Some links I found useful for learning and understanding Java Inheritance:\r\n - https://www.codejava.net/java-core/the-java-language/12-rules-and-examples-about-inheritance-in-java\r\n - https://medium.com/java-for-absolute-dummies/inheritance-in-java-programming-39176e0016f3\r\n\r\n\r\n",
  "participantsCount": 3,
  "commentsCount": 0,
  "reviewsCount": 1
}
```

### 3.2. Definição de Métricas

Para cada pergunta de pesquisa, utilizamos as seguintes métricas para avaliar as correlações:

- **Tamanho do PR**: número de arquivos modificados e total de linhas adicionadas e removidas.
- **Tempo de Análise**: intervalo de tempo entre a criação do PR e sua última atividade (merge ou fechamento).
- **Descrição**: número de caracteres no 'body' da descrição do PR (em markdown).
- **Interações**: número de participantes no PR e o número de comentários feitos.

## 4. Resultados e análise

### 4.1. Tamanho dos PRs x Feedback final das revisões (RQ 01)

![Plotagem de dados referentes à RQ_01](./plots/RQ1.png)

A visualização de dados indica que PRs menores (tamanho 2) podem ter uma ligeira preferência em serem mergeados em relação a PRs mais longos. Ademais, no topo da escala (tamanhos 8-10), é possível visualizar um contraste maior entre PRs maiores, que tendem a ser mais mergeados do que fechados.

### 4.2. Tempo de análise dos PRs x Feedback final das revisões (RQ 02)

![Plotagem de dados referentes à RQ_02](./plots/RQ2_1.png)
![Plotagem de dados referentes à RQ_02](./plots/RQ2_2.png)

Os gráficos indicam que PRs que passam por longos períodos de análise (na ordem de 600.000 minutos) têm uma chance maior de serem fechados sem merge, enquanto PRs que são mergeados tendem a ter tempos de análise mais curtos, entre 0-200.000 minutos. Pode-se concluir, portanto, que há indícios de uma correlação entre PRs analisados rapidamente e uma maior chance de aprovação, confirmando a hipótese inicial de que PRs analisados por mais tempo tenderiam à rejeição.

### 4.3. Descrição dos PRs x Feedback final das revisões (RQ 03)

![Plotagem de dados referentes à RQ_03](./plots/RQ3.png)

É possível inferir, por meio da visualização de dados, que PRs cuja descrição é de até 1.000 caracteres possuem a tendência de serem fechados sem merge. Por outro lado, PRs que apresentam descrição de tamanho moderado (2.000 a 3.000 caracteres) têm maior chance de serem mergeados. Quanto aos PRs de descrições longas, não é possível identificar disparidade significativa quanto à sua tendência de merge.

### 4.4. Interações nos PRs x Feedback final das revisões (RQ 04)

![Plotagem de dados referentes à RQ_04](./plots/RQ4.png)

É evidente o contraste entre PRs cujas interações se encontram na ordem de 20 a 60, uma vez que estes possuem significativa tendência de serem mergeados, confirmando a hipótese inicial de que o processo colaborativo de revisão favorece aprovações. No entanto, é possível observar alguns outliers — PRs com elevado histórico de interações, porém com status de fechado.

### 4.5. Tamanho dos PRs x Número de revisões realizadas (RQ 05)

![Plotagem de dados referentes à RQ_05](./plots/RQ5.png)

O gráfico indica uma correlação aproximadamente linear entre o tamanho dos PRs e a quantidade de revisões, mostrando que, à medida que a quantidade de modificações cresce, o número de revisões também se eleva proporcionalmente. Essa tendência confirma a hipótese inicial de que PRs com maior quantidade de arquivos e linhas alteradas necessitariam de um número maior de revisões durante o processo de Code Review.

### 4.6. Tempo de análise dos PRs x Número de revisões realizadas (RQ 06)

![Plotagem de dados referentes à RQ_06](./plots/RQ6.png)

A visualização permite inferir que PRs com menor tempo de análise tendem a receber menos revisões, considerando a grande concentração de instâncias próximas aos eixos do gráfico. Também é possível perceber alguns outliers — PRs que, embora analisados por pouco tempo, passaram por uma quantidade alta de revisões.

### 4.7. Descrição dos PRs x Número de revisões realizadas (RQ 07)

![Plotagem de dados referentes à RQ_07](./plots/RQ7_1.png)
![Plotagem de dados referentes à RQ_07](./plots/RQ7_2.png)

Ao analisar os gráficos, percebe-se indícios de que PRs com menor descrição tendem a receber menos revisões, refutando a hipótese inicial de que PRs com descrições mais sucintas ou vagas poderiam ser mais propensos a enfrentar dificuldades durante o processo de revisão.

### 4.8. Interações nos PRs x Número de revisões realizadas (RQ 08)

![Plotagem de dados referentes à RQ_08](./plots/RQ8.png)

O gráfico indica uma correlação aproximadamente linear entre o número de interações e a quantidade de revisões, apontando uma relação de proporcionalidade. Essa tendência valida a hipótese inicial de que PRs com mais interações tendem a passar por um número maior de revisões, uma vez que discussões mais longas geralmente levam a ajustes e revisões adicionais.
