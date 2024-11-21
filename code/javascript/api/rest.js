const readJsonFile = require("../jsonLoader");
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
    console.error("Error handling request:", error);
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.get("/comment/user/:id", async (req, res) => {
  const UserId = req.params.id;

  try {
    const data = await loadData();

    // JSONPath query
    const comment = jp.query(data, `$[?(@.UserId == ${UserId})]`);

    if (comment.length === 0) {
      return res.status(404).json({ error: `No comments made by ${UserId} were found.` });
    }
    return res.status(200).json({ success: true, data: comment });
  } catch (error) {
    console.error("Error handling request:", error);
    return res.status(500).json({ error: "Couldn't load comments." });
  }
});

app.listen(port, () => {
  console.log(`Running on localhost:${port}`);
});
