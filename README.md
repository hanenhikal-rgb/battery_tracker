# Windows Battery Monitor

A lightweight background script for Windows that monitors battery status and sends native desktop toast notifications when the battery drops to 40% or below while unplugged.

## Features

* Real-time monitoring of battery percentage and charging state.
* Native Windows toast alerts via `winotify`.
* Prevents spamming alerts by notifying only once per drop.

## Prerequisites

* Windows 10 or 11
* Python 3.8+

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python battery.py
```

> **Note:** Make sure your laptop is unplugged and below 41% to test the notification immediately. Press `Ctrl + C` in the terminal to stop the script.
