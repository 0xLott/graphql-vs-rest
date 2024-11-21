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
    id: ID
    postId: Int
    score: Float
    text: String
    creationDate: String
    userId: Int
  }

  type Query {
    allComments: [Comment]
    commentById(id: ID!): Comment
    commentsByUserId(userId: Int!): [Comment]
    commentsByMinScore(minScore: Float!): [Comment]
  }
`;

const resolvers = {
  Query: {
    allComments: async () => {
      return await loadData();
    },
    commentById: async (_, { id }) => {
      const data = await loadData();
      return data.find((comment) => comment.id == id) || null;
    },
    commentsByUserId: async (_, { userId }) => {
      const data = await loadData();
      return data.filter((comment) => comment.userId == userId);
    },
    commentsByMinScore: async (_, { minScore }) => {
      if (minScore < 0 || minScore > 10) {
        throw new Error("Score values should be between 0 and 10.");
      }
      const data = await loadData();
      return data.filter((comment) => comment.score >= minScore);
    },
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen({ port: 3001 }).then(({ url }) => {
  console.log(`GraphQL Server is running at ${url}`);
});
