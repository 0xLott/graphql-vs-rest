const { ApolloServer, gql } = require("apollo-server");
const readJsonFile = require("./util/jsonLoader");

const filePath = "data/comments.json";

async function loadData() {
  try {
    const data = await readJsonFile(filePath);
    return data.comments.row;
  } catch (err) {
    throw new Error("Failed to load data");
  }
}

// GraphQL schema
const typeDefs = gql`
  type Comment {
    Id: ID
    PostId: Int
    Score: Float
    Text: String
    CreationDate: String
    UserId: Int
  }

  type Query {
    comments: [Comment]
    commentById(id: ID!): Comment
    commentsByUserId(userId: Int!): [Comment]
    commentsByMinScore(minScore: Float!): [Comment]
  }
`;

const resolvers = {
  Query: {
    comments: async () => {
      return await loadData();
    },
    commentById: async (_, { id }) => {
      const data = await loadData();
      return data.find((comment) => comment.Id == id) || null;
    },
    commentsByUserId: async (_, { userId }) => {
      const data = await loadData();
      return data.filter((comment) => comment.UserId == userId);
    },
    commentsByMinScore: async (_, { minScore }) => {
      if (minScore < 0 || minScore > 10) {
        throw new Error("Score values should be between 0 and 10.");
      }
      const data = await loadData();
      return data.filter((comment) => comment.Score >= minScore);
    },
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen({ port: 3000 }).then(({ url }) => {
  console.log(`Server is running at ${url}`);
});
