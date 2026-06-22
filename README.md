# Legal Assistant

A Qt/C++ legal assistant application with a Python agent backend for legal data ingestion, retrieval, and LLM-based analysis.

## Project Structure

- `src/` - Qt/C++ application source code
  - `main.cpp` - application entry point; creates `QApplication` and shows `MainWindow`
  - `ui/mainwindow.h/.cpp` - main window shell; hosts all Qt widgets and top-level layout
  - `bridge/AgentBridge.h/.cpp` - (stub) synchronous interface between the Qt UI and the Python agent process
  - `bridge/AgentWorker.h/.cpp` - (stub) `QThread` worker that runs agent calls off the UI thread
  - `renderer/GraphWidget.h/.cpp` - (stub) `QOpenGLWidget` subclass; the main OpenGL surface for graph drawing
  - `renderer/ShaderProgram.h/.cpp` - (stub) loads, compiles, and links GLSL vertex/fragment shaders
  - `renderer/GraphLayout.h/.cpp` - (stub) computes 2-D positions for nodes (e.g. force-directed layout)
  - `renderer/NodeRenderer.h/.cpp` - (stub) draws individual case/entity nodes on the OpenGL canvas
  - `renderer/EdgeRenderer.h/.cpp` - (stub) draws edges (citation links) between nodes
  - `renderer/Camera2D.h/.cpp` - (stub) pan and zoom state for the graph viewport
  - `shaders/` - GLSL source files loaded at runtime by `ShaderProgram`
- `agent/` - Python agent, data ingestion, and future retrieval/LLM logic
- `agent/data/` - CourtListener dataset scripts and sample data
- `scripts/` - helper scripts
- `tests/` - tests
- `third_party/nlohmann_json/` - bundled JSON parsing library (header-only)

## Qt / C++ Setup

### Prerequisites

- **Qt 6.5+** — download the open-source installer from [qt.io/download-open-source](https://www.qt.io/download-open-source)
  - During installation, select at minimum: **Qt 6.x** for your platform and the **Qt OpenGL / OpenGLWidgets** components
  - Pick whichever compiler kit matches your toolchain (MSVC, MinGW-w64, Clang, etc.)
- **CMake 3.21+** — bundled with Qt Creator, or install separately from cmake.org
- **A C++23-capable compiler**, for example:
  - Windows: MSVC (Visual Studio Build Tools 2022 or later) or MinGW-w64
  - macOS: Xcode / Apple Clang
  - Linux: GCC 13+ or Clang 17+
- **OpenGL drivers** — provided by your GPU driver; no separate install needed on most systems

### Building with Qt Creator (recommended)

1. Open Qt Creator and choose **File → Open File or Project**, then select `CMakeLists.txt` at the repo root.
2. Qt Creator will prompt you to configure a kit — select the **Desktop Qt 6.x** kit for your compiler and click **Configure Project**.
3. Click the **Build** button (hammer icon) or press `Ctrl+B`.
4. Click **Run** (green play button) or press `Ctrl+R` to launch the application.

### Building from the command line

```bash
# Adjust CMAKE_PREFIX_PATH to point at your Qt 6 installation
cmake -B build -S . -DCMAKE_PREFIX_PATH="/path/to/Qt/6.x.x/<compiler>"
cmake --build build
```

On Windows with MSVC you may prefer `-G "Ninja"` or `-G "Visual Studio 17 2022"` as the generator.

### Notes

- The `third_party/nlohmann_json` library is bundled — no extra install needed.
- GLSL shader files live in `src/shaders/` and are loaded at runtime from that path; do not move them relative to the source root.
- The bridge and renderer files are currently stubs — the app will compile and open a blank window until they are filled in.

---

## Python Agent Setup

From the project root:

1. Create a virtual environment:

python3 -m venv .venv

2. Activate the virtual environment:

source .venv/bin/activate

3. Install Python dependencies:

pip install -r agent/requirements.txt

4. Create a local `.env` file:

cp .env.example .env

5. Add your CourtListener API token inside `.env`:

TOKEN=your_actual_courtlistener_token_here

Do not commit `.env`.

## CourtListener Data Ingestion

The ingestion script downloads 100 contract-law related CourtListener search results using the query:

"breach of contract"

Run:

python3 agent/data/ingest.py

Output file:

agent/data/courtlistener_contract_opinions.jsonl

## Ollama Setup

Install Ollama locally, then pull the required models:

ollama pull llama3
ollama pull nomic-embed-text

Verify the Ollama API is running:

curl http://localhost:11434/api/tags

Verify llama3 text generation:

curl http://localhost:11434/api/generate -d '{"model":"llama3","prompt":"Summarize what a legal opinion is in one sentence.","stream":false}'

Verify embeddings:

curl http://localhost:11434/api/embeddings -d '{"model":"nomic-embed-text","prompt":"This case is about breach of contract and damages."}'

## Week 1 Partner Work Completed

- Python virtual environment setup documented
- Python requirements added
- CourtListener contract-law ingestion script added
- 100-row contract-law JSONL sample dataset added
- Ollama llama3 REST API verified
- Ollama nomic-embed-text REST API verified
- Databricks raw Delta table created manually from the JSONL dataset