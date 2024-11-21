# JavaScript Stack Exchange Comments API

## Description

This project is a JavaScript API built using Node.js and Express.js to fetch comments data from the Stack Exchange Language Learning forum.

This project is part of a controlled study to assess the advantages of using GraphQL for web APIs versus REST in terms of performance. The REST API will be compared with an equivalent GraphQL implementation to measure and analyze performance differences.

## Pre-requisites

- Install the latest version of [Node.js](https://nodejs.org/en/).

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/0xLott/graphql-vs-rest.git
   ```

2. Install dependencies:

   ```bash
   cd graphql-vs-rest/code/javascript
   npm install
   ```

3. Build the project and start the server:

   ```bash
    # On /code/javascript directory
    npm start
   ```

4. Navigate to `http://localhost:3001` to access the API.

## Endpoints

- `GET /comments`: Returns all comments
- `GET /comment/:id`: Returns a specific comment by id
- `GET /comment/user/:id`: Returns comments made by specific user id
- `GET /comments/min-score/:score`: Returns comments with at least the specified score value between 0 and 10

## License

This project is licensed under the Apache License
Version 2.0. See the [LICENSE](https://github.com/0xLott/graphql-vs-rest/blob/main/LICENSE) file for more details.
