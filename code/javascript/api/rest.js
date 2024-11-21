const readJsonFile = require("../jsonLoader");

const express = require("express");
const app = express();
const port = 3000;

filePath = "data/comments.json";

async function loadData() {
  try {
    const data = await readJsonFile(filePath);
    return data.comments;
  } catch (err) {
    throw err;
  }
}

app.get("/comments", async (req, res) => {
  try {
    const comments = await loadData();
    res.send(comments);
  } catch (error) {
    console.errorerror(error);
    res.status(500).send("Error: Couldn't load comments.");
  }
});

app.get("/comments/:id", async (req, res) => {
  commentId = req.params.id;

  try {
    const data = await loadData();
  } catch (error) {
    console.error(error);
    res.status(500).send("Error: Couldn't load comments.");
  }

  try {
    const comment = data.rows.Id[commentId];
  } catch (error) {
    res.status(500).send(`Error: Couldn't find comment with id: ${commentId}`);
  }
});

app.listen(port, () => {
  console.log(`Running on localhost:${port}`);
});
