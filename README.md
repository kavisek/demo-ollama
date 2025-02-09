# Ollama Startup

You can start conversations with:

```bash
ollama run deepseek-r1
```

You can stop the conversation with the following command:

```bash
\bye 
```

# Ollama Startup via Docker

To start conversations using Docker, you first need to spin up the container running the Ollama server.

Then you can start the conversation with the following commands:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run deepseek-r1
```

### Models

- https://ollama.com/search

## DeepSeek

```bash
# These models will run quickly on an M3 Max with 128 GB of RAM.

ollama run deepseek-r1:1.5b
# Model Size: 1.1GB
# RAM Usage: 1.1GB
# CPU Usage: 55%


ollama run deepseek-r1:7b
# Model Size: 4.7GB
# RAM Usage: 1.27 GB
# CPU Usage: 4%

ollama run deepseek-r1:8b
# Model Size: 5GB
# RAM Usage: 1.27 GB
# CPU Usage: 4%

ollama run deepseek-r1:14b
# Model Size: 7GB
# RAM Usage: 1.74 GB
# CPU Usage: 3%

ollama run deepseek-r1:32b
# Model Size: 19GB
# RAM Usage: 2.3GB
# CPU Usage: 3%

ollama run deepseek-r1:70b
# Model Size: 2.77GB
# RAM Usage: 2.3GB
# CPU Usage: 3%

```

# Qwen 2.5

```bash
ollama run qwen2.5:3b
```


## Vision Models

Vision Models on Ollama can read images.

They can complete the following tasks without any additional information:

- Optical Character Recognition (OCR)
- Interpretation of Charts & Tables
- Image Q&A
- Interpretation of Handwriting

```bash
ollama run llama3.2-vision
# Model Size: 6GB

>>> What's in this image? ./images/lava.jpg 
Added image './images/lava.jpg'
 The image you've provided appears to show an erupting volcano with lava flowing down the mountain. The background is dark, suggesting it may be nighttime or 
early morning, and there are smoke and steam rising from the eruption. Additionally, the ground around the eruption looks to be covered in snow or ice, which 
contrasts with the hot, molten lava from the volcano.
```
