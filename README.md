# create-qr-code-generator

- Created at: 2025-05-22
- Created by: `🐢 Arun Godwin Patel @ Code Creations`

## Table of contents

- [Setup](#setup)
  - [System](#system)
  - [Installation](#installation)
- [Walkthrough](#walkthrough)
  - [Code Structure](#code-structure)
  - [Tech stack](#tech-stack)
  - [Build from scratch](#build-from-scratch)
    - [1. Create a virtual environment](#1-create-a-virtual-environment)
    - [2. Activate the virtual environment](#2-activate-the-virtual-environment)
    - [3. Install the required packages](#3-install-the-required-packages)
    - [4. Create the QR code generating class](#4-create-the-qr-code-generating-class)
    - [5. Create the Python module](#5-create-the-python-module)

## Setup

### System

This code repository was tested on the following computers:

- Windows 11

At the time of creation, this code was built using `Python 3.13.3`

### Installation

1. Install `virtualenv`

```bash
# 1. Open a CMD terminal
# 2. Install virtualenv globally
pip install virtualenv
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

```bash
# Windows
.\venv\Scripts\activate
# Mac
source venv/bin/activate
```

4. Install the required packages

```bash
pip install -r requirements.txt
```

5. Run the module

```bash
python main.py
```

## Walkthrough

### Code Structure

The code directory structure is as follows:

```plaintext
create-qr-code-generator
└───algorithm
|   └──qr.py
│   __init__.py
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
```

The `main.py` file is a module that you can run to generate a QR code.

The `algorithm/` folder contains files for algorithms to generate QR codes.

The `.gitignore` file specifies the files and directories that should be ignored by Git.

The `requirements.txt` file lists the Python packages required by the application.

### Tech stack

**Image processing**

- Image generation: `Pillow`
- QR code: `qrcode`

### Build from scratch

This project was built using Python, `Pillow` and `qrcode`. A URL can be specified within the `main.py` file which when run, generates the corresponding QR code locally within the file system.

#### 1. Create a virtual environment

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

```bash
# Windows
.\venv\Scripts\activate
# Mac
source venv/bin/activate
```

#### 3. Install the required packages

```bash
pip install -r requirements.txt
```

#### 4. Create the QR code generating class

Create a file named `qr.py` in the `algorithm/` directory. This file will contain the code to generate a QR code.

```python
import io
import qrcode


class Generate:

    def __init__(self):
        pass

    def qr_code(self, link: str = None):

        if link is None:
            raise Exception("link cannot be None")

        # Create an instance of qrcode
        qr = qrcode.QRCode(version=1, box_size=10, border=1)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
```

#### 5. Create the Python module

Next, we will create the `main.py` file in the root directory. This file will be the entry point of the application and will contain the code to generate a QR code.

```python
from algorithm.qr import Generate

URL = "https://arungodwinpatel.com"
OUTPUT_FILE = "output.png"

if __name__ == "__main__":

    # Generate QR code
    generator = Generate()
    img_bytes = generator.qr_code(link=URL)

    # Write to local file
    with open(OUTPUT_FILE, "wb") as f:
        f.write(img_bytes)
```

This completes the setup of our QR code generator!

## Happy coding! 🚀

```bash
🐢 Arun Godwin Patel @ Code Creations
```
