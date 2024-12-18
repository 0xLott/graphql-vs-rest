# JavaScript Stack Exchange Comments API

This project contains two JavaScript-based APIs to fetch comments data from the Stack Exchange Language Learning forum.

- **REST API**: built using Node.js and Express
- **GraphQL API**: built using Apollo Server

> [!WARNING]  
> This API provides static data captured at a specific time for experimental purposes. It is not up-to-date and should not be used for real-time needs.

This project is part of a controlled study to assess the advantages of using GraphQL for web APIs versus REST in terms of performance. The REST API will be compared with an equivalent GraphQL implementation to measure and analyze performance differences.

## Endpoints

- `GET /comments`: Returns all comments
- `GET /comments/:id`: Returns a specific comment by id
- `GET /comments/user/:id`: Returns comments made by specific user id
- `GET /comments/min-score/:score`: Returns comments with at least the specified score value between 0 and 10

## Pre-requisites

- Install the latest version of [Node.js](https://nodejs.org/en/).

## Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/0xLott/graphql-vs-rest.git
   ```

2. Install dependencies:

   ```bash
   cd graphql-vs-rest/code/javascript
   npm install
   ```

3. Build the project and start the **REST API** Express server:

   ```bash
    # On /code/javascript directory
    npm run rest
   ```

   Or start the **GraphQL API** Apollo server

   ```bash
    # On /code/javascript directory
    npm run gql
   ```

4. Send requests to `http://localhost:3000/comments` to access the REST API.

5. Send requests to `http://localhost:3001/` to access the GraphQL API.

## License

This project is licensed under the Apache License
Version 2.0. See the [LICENSE](https://github.com/0xLott/graphql-vs-rest/blob/main/LICENSE) file for more details.
