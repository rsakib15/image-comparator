# Image Comparator

A lightweight Python tool for **comparing two images** to detect differences using the **Structural Similarity Index (SSIM)** from `scikit-image`. Perfect for image processing, quality assurance, and computer vision projects.

## Features

- Computes a similarity score (SSIM) between two images.
- Classifies images as **identical**, **similar**, or **different** based on a customizable threshold.
- Saves a **difference image** (`diff.png`) to highlight changes.
- Simple **command-line interface (CLI)** for easy use.
- Supports all **OpenCV-compatible** image formats (e.g., PNG, JPG, BMP).
- Lightweight and extensible for integration into larger workflows.

---

## Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/) for dependency installation
- [Git](https://git-scm.com/downloads) for cloning the repository

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/image-comparator.git
   cd image-comparator


2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt

3. **Required packages**:

    ```bash
    opencv-python
    scikit-image
    numpy
    ```
