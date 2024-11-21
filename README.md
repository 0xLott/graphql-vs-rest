# Web APIs performance comparison: GraphQL vs REST

This repository contains the code and datasets for a controlled experiment comparing the performance of web APIs implemented in GraphQL and REST, using both Java and JavaScript. The goal of the experiment was to answer the following research questions:

- **RQ 01**: Are GraphQL responses faster than REST responses?
- **RQ 02**: Are GraphQL responses smaller than REST responses?

## Experiment overview

The experiment consists of four different treatments comparing the performance of REST and GraphQL APIs implemented in Java and JavaScript, using mocked data gathered from public data dumps of [Stack Exchange](https://archive.org/download/stackexchange/).

The full experimental design, including hypotheses, methodology, and results, can be found in the [**experiment report**](docs/report.md).

## Replicating this experiment

To replicate the experiment, follow the steps below:

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/0xLott/graphql-vs-rest.git
cd graphql-vs-rest
```

### 2. Set up the environment

#### Java

1. Navigate to the `code/java/` folder
2. Follow the instructions in the README.md file inside the folder to set up the Java environment

#### JavaScript

1.  Navigate to the `code/javascript/` folder
2.  Follow the instructions in the README.md file inside the folder to set up the JavaScript environment

## 4. Accessing the results

The results of the experiment (response times and response sizes) are stored in the [results](code/client/results) directory. It contains:

- **Plots:** Graphs showing the distribution and averages of response times and sizes.
- **Data files:** The raw data from the experiment in CSV format.

## 5. Experiment design and detailed report

The full experiment design, including hypotheses, variables, and treatments, is detailed in the [**experiment report**](docs/report.md).
