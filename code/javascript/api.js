const readJsonFile = require("./util/jsonLoader");
const jp = require("jsonpath");
const express = require("express");

const app = express();
const port = 3000;

filePath = "data/comments.json";

async function loadData() {
  try {
    const data = await readJsonFile(filePath);
    const result = Object.assign({}, data.comments.row);
    return result;
  } catch (err) {
    throw err;
  }
}

app.get("/comments", async (req, res) => {
  try {
    const comments = await loadData();
    return res.status(200).json({ success: true, data: comments });
  } catch (error) {
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.get("/comment/:id", async (req, res) => {
  const commentId = req.params.id;

  try {
    const data = await loadData();

    // JSONPath query
    const comment = jp.query(data, `$[?(@.Id == ${commentId})]`);

    if (comment.length === 0) {
      return res.status(404).json({ error: `Comment with id ${commentId} was not found.` });
    }
    return res.status(200).json({ success: true, data: comment });
  } catch (error) {
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.get("/comment/user/:id", async (req, res) => {
  const userId = req.params.id;

  try {
    const data = await loadData();

    // JSONPath query
    const comment = jp.query(data, `$[?(@.UserId == ${userId})]`);

    if (comment.length === 0) {
      return res.status(404).json({ error: `No comments made by ${userId} were found.` });
    }
    return res.status(200).json({ success: true, data: comment });
  } catch (error) {
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.get("/comments/min-score/:score", async (req, res) => {
  const minScore = req.params.score;

  if (minScore < 0 || minScore > 10) return res.status(400).json({ error: `Score values should be between 0 and 10` });

  try {
    const data = await loadData();

    // JSONPath query
    const comments = jp.query(data, `$[?(@.Score >= ${minScore})]`);

    if (comments.length === 0) {
      return res.status(404).json({ error: `No comments with score >= ${minScore} were found.` });
    }
    return res.status(200).json({ success: true, data: comments });
  } catch (error) {
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.listen(port, () => {
  console.log(`Running on localhost:${port}`);
});