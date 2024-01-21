import express from 'express';
var app = express();
app.use(express.static('public'));
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
app.get("/", (req, res) => {
    res.send('Hello World!')
});