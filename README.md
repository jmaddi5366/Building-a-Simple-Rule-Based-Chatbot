# Building-a-Simple-Rule-Based-Chatbot
# Simple Rule-Based Chatbot

Welcome! I’m excited to share my prototype rule-based chatbot built with Python and the Microsoft Bot Framework. This README will guide you through setting it up, running it locally, and understanding how it works.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Running the Bot](#running-the-bot)  
6. [Usage](#usage)  
7. [Testing](#testing)  
8. [Extending the Bot](#extending-the-bot)  
9. [Troubleshooting](#troubleshooting)  
10. [License](#license)  

---

## Project Overview

In this project, I built a simple rule-based chatbot that understands three basic interactions:

- **Echo**: When you type `echo <your message>`, the bot repeats exactly what follows.  
- **Help**: When you type `help` or `?`, the bot lists its available commands.  
- **Fallback**: For any other input, the bot reverses your text as a demonstrative fallback response.

I walk through every phase—from requirements gathering to deployment planning—and include the complete code in `app.py`.

---

## Prerequisites

Before you begin, make sure you have:

- **Anaconda** or **Miniconda** installed  
- **Python 3.8.2** (managed via Conda)  
- **Git** (optional, for cloning this repo)  
- **Bot Framework Emulator** (for local testing)  

---

## Installation

1. **Clone this repository** (or download the ZIP):

   ```bash
   git clone https://github.com/your-username/simple-rulebot.git
   cd simple-rulebot
Create and activate a Conda environment:

bash
Copy
Edit
conda create --name chatbot_env python=3.8.2 -y
conda activate chatbot_env
Install required Python packages:

bash
Copy
Edit
pip install botbuilder-core aiohttp
Configuration
For local testing, you don’t need Azure credentials—leave the app ID and password empty. If you later deploy to Azure, set these two environment variables:

bash
Copy
Edit
export MicrosoftAppId="<YOUR_APP_ID>"
export MicrosoftAppPassword="<YOUR_APP_PASSWORD>"
On Windows PowerShell:

powershell
Copy
Edit
setx MicrosoftAppId "<YOUR_APP_ID>"
setx MicrosoftAppPassword "<YOUR_APP_PASSWORD>"
Running the Bot
With your environment active and dependencies installed, start the bot:

bash
Copy
Edit
python app.py
You should see:

csharp
Copy
Edit
======== Running on http://localhost:3978 ========
Usage
Open the Bot Framework Emulator.

Click “Open Bot” and point the endpoint URL to:

bash
Copy
Edit
http://localhost:3978/api/messages
Type messages in the Emulator chat window:

help → lists available commands

echo Hello, world! → replies “Hello, world!”

foobar → replies “(reversed) raboof”

Enjoy experimenting with the simple rule engine!

Testing
I created basic unit tests in tests/ (if included) to verify each command’s output:

bash
Copy
Edit
pytest
I also manually verified behavior in the Emulator and captured screenshots for reference in my project report.

Extending the Bot
I designed this prototype for easy extension. To add new commands:

Update the on_turn logic in app.py.

Add corresponding unit tests.

Rerun and verify in the Emulator.

Possible enhancements include a time command, richer error handling, or even integrating an LLM for natural-language understanding.

Troubleshooting
“ModuleNotFoundError: No module named ‘aiohttp’”
Make sure you ran pip install aiohttp botbuilder-core.

Multiple Python installs on Windows
Use python -m pip install ... to ensure you’re installing into the right interpreter.

Port already in use
Stop any process listening on 3978 or change the port in app.py.

