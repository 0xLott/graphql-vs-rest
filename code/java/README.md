# JavaScript Stack Exchange Comments API

This project contains two Java Spring Boot APIs to fetch comments data from the Stack Exchange Language Learning forum.

- **REST API**: built using Spring Web
- **GraphQL API**: built using Spring for GraphQL and Netflix DGS Library

> [!WARNING]  
> This API provides static data captured at a specific time for experimental purposes. It is not up-to-date and should not be used for real-time needs.

This project is part of a controlled study to assess the advantages of using GraphQL for web APIs versus REST in terms of performance. The REST API will be compared with an equivalent GraphQL implementation to measure and analyze performance differences.

## Endpoints

- `GET /comments`: Returns all comments
- `GET /comments/:id`: Returns a specific comment by id
- `GET /comments/user/:id`: Returns comments made by specific user id
- `GET /comments/min-score/:score`: Returns comments with at least the specified score value between 0 and 10

## Pre-requisites

- Install the latest version of Java
- Install the latest version of Maven

## Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/0xLott/graphql-vs-rest.git
   ```

2. Install dependencies:

   ```bash
   cd graphql-vs-rest/code/java/spring-graphql-rest-experiment
   mvn clean package
   ```

3. Build the project and start the **REST API** Express server:

   ```bash
    # On /code/java/spring-graphql-rest-experiment/target directory
    java -jar spring-graphql-rest-experiment-0.0.1-SNAPSHOT.jar
   ```

4. Send HTTP requests under the URI `http://localhost:8080/rest` to access the REST API.

5. Send GraphQL requests under the URI `http://localhost:8080/graphql` to access the GraphQL API.

## License

This project is licensed under the Apache License
Version 2.0. See the [LICENSE](https://github.com/0xLott/graphql-vs-rest/blob/main/LICENSE) file for more details.
