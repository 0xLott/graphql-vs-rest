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
| Hipótese nula (H₀)        | Não há diferença significativa no tempo de resposta | Não há diferença significativa no tamanho das respostas |
| Hipótese alternativa (Hₐ) | GraphQL tem tempos de resposta menores              | GraphQL tem respostas menores                           |

#### 2. Variáveis Dependentes

- **RQ 01**: Tempo de resposta (em ms)
- **RQ 02**: Tamanho do `response body` (em bytes)

#### 3. Variáveis Independentes

| Fator                        | Níveis                |
| ---------------------------- | --------------------- |
| Tipo de implementação de API | `GraphQL` e `REST`    |
| Linguagem                    | `JavaScript` e `Java` |

#### 4. Tratamentos

1. API implementada em GraphQL com JavaScript
2. API implementada em REST com JavaScript
3. API implementada em GraphQL com Java
4. API implementada em REST com Java

#### 5. Objetos Experimentais

Os objetos experimentais consistem em:

- APIs: Quatro APIs criadas para o experimento, conforme detalhado na combinação de tratamentos.
- Dados: Uma base de dados simulada e representativa para as consultas, contendo dados de comentários do fórum Language Learning, do Stack Exchange.

#### 6. Tipo de Projeto Experimental

O experimento segue um projeto fatorial, com combinações de tratamento em desenho cruzado (crossing).

#### 7. Quantidade de Medições

#### 8. Ameaças à Validade

- _Validade interna_: pode ser comprometida por variações ambientais, como de rede ou de hardware. Para mitigar esses efeitos, os testes foram executados múltiplas vezes em um ambiente controlado.

- _Validade externa_: pode ter a generalização limitada pelo uso da base de dados simplificada, uma vez que os resultados podem ser drasticamente diferentes dependendo da complexidade do conjunto de dados utilizado para implementaçao das APIs.

## 3. Metodologia

### 3.1. Criação do Dataset

### 3.2. Definição de Métricas

## 4. Resultados e Análise
