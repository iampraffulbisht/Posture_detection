# **Pose Detection with OpenCV and MediaPipe**





https://github.com/iampraffulbisht/Posture_detection/assets/114369813/f1cf325e-074d-4438-9225-9f6da71cfcf0



This project demonstrates real-time pose detection using OpenCV and MediaPipe in Python. The application processes video input, detects body landmarks, and overlays a pose skeleton on the detected body.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Pose detection involves recognizing and tracking body landmarks to map the human body's structure. This project uses MediaPipe's pose detection capabilities and OpenCV for video processing to provide a real-time demonstration of pose estimation.

## Features

- Real-time pose detection from video input.
- Overlay of body landmarks and pose skeleton on detected bodies.
- Display frames per second (FPS) on the video feed.

## Installation

### Prerequisites

- Python 3.6+
- pip package manager

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/pose-detection.git
   cd pose-detection
   
2. Install Dependencies
Install the required packages using pip:
   ```bash
     pip install opencv-python mediapipe
      
Usage

1. Run the pose_detection.py script:
   ```bash
    python pose_detection.py

3. The script will start processing video input, detect body landmarks, and display the pose skeleton along with the FPS on the video feed.

Acknowledgments

OpenCV
MediaPipe

