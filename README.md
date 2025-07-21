# 🎙️ Kokoro Mini Project

This project uses the **Kokoro Text-to-Speech (TTS)** library to generate audio files from text content (e.g., Reddit posts) using a variety of realistic voices.

---

## 🚀 Features

- ✅ Converts JSON-formatted text posts into `.wav` audio files  
- ✅ Cleans and preprocesses text for better TTS output  
- ✅ Supports multiple Kokoro voices and languages  
- ✅ Skips posts with insufficient content or already existing audio  
- ✅ Easy configuration for input file, output directory, and voice selection  

---

## 📦 Requirements

- Python **3.8+**
- Kokoro TTS (`pip install kokoro`)
- Other dependencies: `torch`, `soundfile`
- If using `uv`:  
  ```sh
  uv pip install pip
  ```

---

## ⚙️ Usage

### 1. Prepare your JSON file  
Ensure the JSON is a list of objects, each with at least the following fields:
```json
[
  {
    "title": "Post title",
    "content": "Full content of the post"
  },
  ...
]
```

### 2. Configure `main.py`  
Update these variables:
- `json_file`: Path to your JSON file  
- `output_directory`: Folder where audio will be saved  
- `selected_voice`: Pick a Kokoro-supported voice

### 3. Run the script  
```sh
python main.py
```

### 4. Find Your Output  
Generated `.wav` files will be saved in the specified `output_directory`.

---

## 🗣️ Example Kokoro Voices

| Voice Code | Description        |
|------------|--------------------|
| `af_bella` | American Female    |
| `af_sarah` | American Female    |
| `af_nicole`| American Female    |
| `am_adam`  | American Male      |
| `am_michael` | American Male    |
| `bf_emma`  | British Female     |
| `bf_isabella` | British Female  |
| `bm_lewis` | British Male       |
| `bm_george`| British Male       |

---

## 🎛️ Customization

- To use a different voice, change the `selected_voice` variable in `main.py`.
- To process only specific posts, pre-filter your JSON accordingly.

---

## 🛠️ Troubleshooting

### ❗ Module Errors
Ensure correct import of the generator:
```python
from kokoro.__main__ import generate_and_save_audio
```

### ❗ Missing Dependencies
Install the required packages:
```sh
pip install kokoro soundfile
```
Or using `uv`:
```sh
uv add kokoro soundfile
```

---

## 🔧 External Installations

### 🔹 1. eSpeak NG

Download and install from:  
👉 [https://github.com/espeak-ng/espeak-ng/releases](https://github.com/espeak-ng/espeak-ng/releases)

---

### 🔹 2. Required Build Tools for Windows

Download and install:  
👉 [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

During installation, ensure the following are checked:

- ✅ **C++ Build Tools**
- ✅ **Windows 10 SDK** or **Windows 11 SDK**

These are required to build packages like `numpy` from source.

---

## 📄 License

This project is for educational/demo purposes only.  
See the [Kokoro License](https://github.com/rany2/kokoro) for more details.

---

Feel free to ⭐ the repo if you found it useful!
