<p align="center">
	<img src="assets/image.png" alt="Teaching The Machine — Codeday Kashmir 2026" width="420" />
</p>

# Teaching The Machine (Codeday Kashmir 2026)

Workshop starter code for training and running a YOLOv8 model using the Ultralytics library.

## Quick setup

### Get the code
You need a local copy of this repo before running anything.

- **Option A : Clone with Git (Only If Git Is Installed, else Option B)**
	- `git clone https://github.com/mohsin-nasir/codeday-vision.git`
	- `cd codeday-vision`  

- **Option B: Download ZIP**
	- Download the ZIP, extract it, then open a terminal in the extracted folder.

### Windows
1. Install Python 3.10+ (from python.org) and make sure Python is added to PATH.
2. Double-click `setup_windows.bat` (it installs everything you need).
	- If you’re using a terminal, run: `setup_windows.bat`


### Linux/macOS (manual)
We recommend using a virtual environment (`.venv`) so installs don’t affect your global Python.

If `python3 -m venv .venv` fails:
- **macOS:** install Python 3 first (then retry — `venv` comes with Python 3)
	- Homebrew: `brew install python`
	- Or install from python.org
- **Ubuntu/Debian:** `sudo apt update && sudo apt install -y python3-venv`
- **Other Linux distros:** install your distro’s package that provides Python’s `venv` module, then retry.

1. Create + activate:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`

2. Install dependencies:
   - `python -m pip install -r requirements.txt`

   

## What each file does

- `capture.py`
	- Webcam image-capture tool for building a dataset.
	- Saves images into `dataset/<label>/...` when you press SPACE.

- `yolo_train.py`
	- Trains a YOLOv8 model using your dataset config.

- `yolo_live.py`
	- Runs real-time detection on your webcam feed using a trained model.
	- Currently points to `yolov8n.pt` (change if your run name differs).

- `yolo_single_image.py`
	- Runs detection on a single image (`bus.jpg`) and saves the result.
	- Currently points to `yolov8n.pt`.

- `setup_windows.bat`
	- One-click Windows setup: installs `requirements.txt`.
