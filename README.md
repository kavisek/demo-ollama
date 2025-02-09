# Ollama Startup

You can start up with converations with

```bash
ollama run deepseek-r1
```

You can stop the conversation with the following commmand;

```bash
\bye 
```

# Ollama Startup via Docker

You can start up with converations with conversation. You can need spin the the container running the olamma server.

Then you can start the conversation with processeding command.

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run deepseek-r1
```

## Parameters Models

```bash
# These model will run quickly on a M3 Max with 128 Gb of RAM.

ollama run deepseek-r1:1.5b
# Model Size: 1.1GB
# 1.1GB
# 55% CPU Usage


ollama run deepseek-r1:7b
# Model Size: 4.7GB
# 1.27 GB
# 4% CPU Usage

ollama run deepseek-r1:8b
# Model Size: 5GB
# 1.27 GB
# 4% CPU Usage

ollama run deepseek-r1:14b
# Model Size: 7GB
# 1.74 GB
# 3% CPU Usage

ollama run deepseek-r1:32b
# Model Size: 19GB
# RAM: 2.3GB
# 3% CPU Usage

ollama run deepseek-r1:70b
# Model Size: 2.77GB
# RAM: 2.3GB
# 3% CPU Usage

```



