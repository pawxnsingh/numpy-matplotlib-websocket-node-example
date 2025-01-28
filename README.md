# Polyglot Data Analysis and Visualization API using METACALL

In this example we show how to use Numpy and Matplotlib (Python) from an WebSocket server (NodeJS) in order to build a **Polyglot Data Analysis and Visualization API**.

## Install

Clone the repository:

```sh
git clone https://github.com/pawxnsingh/numpy-matplotlib-websocket-node-example
```

Install MetaCall CLI:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
```

Navigate to the directory:

```sh
cd numpy-matplotlib-websocket-node-example
```

Install application dependencies:

```sh
metacall pip3 install -r requirements.txt 
metacall npm install
```

## Run the Application

```sh
metacall index.js
```

For testing it, in another terminal, let's visualize this data calculating the mean, median, standard deviation of this array 
[10, 12, 14, 15, 10, 11, 150] (you can change the values and size for experimenting)

```sh
use postman/hoppscotch(web)

URL: ws://localhost:8080
Message: {"numbers": [10, 12, 14, 15, 10, 11, 150]}
```

It should output something like:

```
output: look for the output folder for the visualized view
```

## Docker

An alternative version with Docker and automated testing is provided.

```sh
docker build -t metacall/numpy-matplotlib-websocket-node-example .
docker run --rm -v $(pwd)/output:/metacall/output -p 8080:8080 -it metacall/numpy-matplotlib-websocket-node-example
```

