
# MCP Tool Simulation Project

A simple learning project demonstrating how to create a **multi-component (MCP) tool** that integrates basic tools and simulates their interaction using **LangChain** and **Groq**.

---

## Project Overview

This project combines:

1. **Weather Tool** – a dummy API returning placeholder weather data.
2. **Calculator Tool** – supports addition and multiplication.
3. **Integration & Simulation** – connects these tools and simulates a workflow using LangChain + Groq.

The project also demonstrates streaming responses using **`streamable-http`** and interactive input/output via **standard I/O**.

> ⚠️ This is a learning project and not intended for production use.

---

## Features

* Dummy weather API for simulation.
* Calculator for addition and multiplication.
* Tools connected in a workflow to demonstrate **multi-component interaction**.
* Streaming responses using `streamable-http`.
* Interactive input/output using standard I/O.
* Simulation orchestrated via **LangChain + Groq**.

---

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd mcp-tool-simulation
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---


## Tech Stack

* **Python 3.10+**
* **FastAPI + UVicorn** – API server and streaming support
* **LangChain + Groq** – for connecting and simulating tools
* **streamable-http** – for streaming responses
* **stdio** – for interactive input/output

---

## Contributing

This is a personal learning project. Feel free to fork, experiment, or suggest improvements.

---

## License

MIT License – free to use for learning purposes.

---
