const readJsonFile = require("../jsonLoader");

const express = require("express");
const app = express();
const port = 3000;

filePath = "data/comments.json";

async function loadData() {
  try {
    const data = await readJsonFile(filePath);
    return data;
  } catch (err) {
    throw err;
  }
}

app.get("/comments", async (req, res) => {
  try {
    const data = await loadData();
    res.send(data);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error: Couldn't load comments.");
  }
});

// app.get("/comments/:id", async (req, res) => {
//   commentId = req.params.id;
// });

app.listen(port, () => {
  console.log(`Running on localhost:${port}`);
});
