// project imports
const { WebSocketServer } = require("ws");
const cors = require('cors');
const { metacall, metacall_load_from_file } = require('metacall')
const express = require('express')
const fs = require("fs");

// load python script 
metacall_load_from_file('py', ['analysis.py'])

const app = express();
const port = 8080;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

const server = app.listen(port, () =>
    console.log(`ws server is listening on http://localhost:${port}`)
);

const wss = new WebSocketServer({ server });

console.log(`WebSocket server running on ws://localhost:${port}`);

wss.on("connection", (ws, req) => {
    console.log("Client connected");
    ws.on("error", console.error);
    ws.on("message", async (message) => {
        try {
            const data = message.toString();
            const res = metacall('process_message', data);
            const imagePath = "./output/analysis_visualization.png";

            fs.readFile(imagePath, (err, image) => {
                if (err) {
                    console.error(`Error reading image: ${err.message}`);
                    return;
                }

                ws.send([image, res], (err) => {
                    if (err) {
                        console.error(`Error sending image: ${err.message}`);
                    } else {
                        console.log("Image sent successfully.");
                    }
                });
            })

        } catch (error) {
            ws.send(JSON.stringify({ error: "Processing failed", details: error }));
        }
    });

    ws.on("close", () => {
        console.log("Client disconnected");
    });
});