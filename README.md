# 🤖 Build an Autonomous Transit Agent with Google ADK & MCP

## Executive Summary
Today, we are moving beyond standard chatbots. In this hands-on lab, you will build a deterministic, multi-reasoning **Agentic AI** system using Google's Agent Development Kit (ADK) and the Model Context Protocol (MCP).

Instead of an AI that just generates text, you will build an orchestrator. Our Transit Agent will dynamically fetch live data, read business policies, and execute transactional workflows completely on its own. Finally, we will serve it through a beautiful web UI!

### The Tech Stack:

**- Google ADK**: The "Brain" - Orchestrates the ReAct (Reason + Act) loop using Gemini.

**- FastMCP**: The "Muscle" - Exposes your backend APIs and logic to the AI.

**- Docker**: For reliable, instant deployment.

## ☁️ Google Cloud Setup (Do This First!)
Before we look at the code, we need a workspace. Follow these steps to set up your Google Cloud environment:

### Step 1: Create a Google Cloud Project
Open the [Google Cloud Console](http://console.cloud.google.com/).

Click the Project Selector dropdown at the top of the page.

Click **New Project**.

Name your project (e.g., ``gdg-mumbai-agent``) and click **Create**.

Once created, make sure your new project is selected in the top dropdown.

### Step 2: Enable billing and redeem the credits
Make sure that billing is enabled for your Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled). 

[Redeem Credits](https://codelabs.developers.google.com/codelabs/cloud-codelab-credits) following the setps mentioned in codelab.

### Step 3: Activate Cloud Shell
We will use Google Cloud Shell as our terminal so we don't have to install anything locally.

Look at the top right corner of the Google Cloud Console.

Click the Activate Cloud Shell icon (it looks like this: ``>_``).

A terminal will open at the bottom of your screen. Click **Continue** if prompted.

Once connected to Cloud Shell, you check that you're already authenticated and that the project is set to your project ID using the following command:

```bash
gcloud auth list
```
Run the following command in Cloud Shell to confirm that the gcloud command knows about your project.

```bash
gcloud config list project
```
If your project is not set, use the following command to set it:

```bash
gcloud config set project <YOUR_PROJECT_ID>
```

### Step 4: Enable the Required APIs
To use Google's generative models, we need to turn on the APIs for this project.

In the Google Cloud Console search bar at the top, type "Vertex AI API" and select it.

Click **Enable**.

Next, search for "Generative Language API" (used for Gemini API keys) and click Enable.

Alertnatively, run this command in cloud shell:
```bash
gcloud services enable aiplatform.googleapis.com generativelanguage.googleapis.com
```
__(Note: If prompted to authorize Cloud Shell, click Authorize).__

## 🚀 Quick Start: Google Cloud Shell
Still in your Cloud Shell open, simply paste this command into your terminal:

```Bash
git clone https://github.com/ruby-verma/transit-agent.git && cd transit-agent 
```

### 🔑 Set Up Your API Key
You will need a Gemini API key to give your agent a brain.

Get your API key from [Google AI Studio](https://aistudio.google.com/api-keys).

Once you have your key, choose one of the following methods to add it to your project:

***Option A: The Quick CLI Method (Recommended)***

Run this single command in your Cloud Shell terminal, making sure to replace the placeholder with your actual copied key:

In your Cloud Shell terminal, copy the example environment file:

```bash
echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env
```

***Option B: The Visual Editor Method***

Copy the template file:

```bash
cp .env.example .env
```

Use the Cloud Shell Editor's file explorer on the left side of your screen.

Open the .env file, paste your key inside, and save (Ctrl+S).

## 📂 Repository Structure
When you clone this project, your directory will look like this:
```
transit-agent/
├── .env.example            # Your injected API key
├── Dockerfile              # Container spec for the Agent & Server
├── docker-compose.yml      # Docker multi-container orchestration
├── README.md               # This documentation file
├── transit_server.py       # FastMCP Data Server code
└── agents/                 # The folder ADK Web scans for agents
    └── __init__.py         # The ADK Agent orchestration code
```

## 🧠 Architecture Overview
### 1. The Data Layer (``transit_server.py``)
This runs our **FastMCP** Server. It does not contain any AI logic. It simply exposes tools and resources. It simply exposes two types of endpoints to the agent:

Tools: Executable Python functions (e.g., fetching a delay, processing a refund).

Resources: Static text or context (e.g., the corporate refund policy).

### 2. The Intelligence Layer (``agents/__init__.py``)
This file uses **Google ADK**. It connects to the MCP server, discovers the tools, and uses Gemini to orchestrate a solution. We use the blazing-fast ``gemini-2.5-flash`` model for high rate limits, and we name our variable ``root_agent`` so the Web UI can auto-discover it. __We have enabled debug logging so you can watch the AI "think" step-by-step__.

## 🏃‍♂️ Task 1: Launch the Architecture
We have containerized the entire architecture so you don't have to worry about Python versions or dependency conflicts.

In your Cloud Shell terminal, build and run the multi-container application:

```bash
docker compose up --build
```
You will see the containers build and the server start. Keep this terminal running!

## 🗣️ Task 2: Talk to Your Agent via Web UI
Now for the magic! Let's open the built-in ADK Web UI to interact with our agent.

1. Look at the top right of your Google Cloud Shell window.
2. Click the Web Preview icon (it looks like a small eye or a window with an arrow).
3. Click Change port.
4. Type in ``8000`` and click Change and Preview.
5. A new browser tab will open. Ensure ``root_agent`` is selected in the top-left dropdown!

Try these prompts in the chat box:
### Level 1: Simple Data Retrieval
The agent will just use the ``check_transit_status`` tool.

__"What is the status of the Vande Bharat express from Mumbai to Ahmedabad?"__

### Level 2: Knowledge & Policy Extraction
The agent will realize it needs to read the ``policy://refunds`` resource.

__"My flight from Mumbai to Bengaluru is delayed. What is the official compensation policy for delays?"__

### Level 3: Full Autonomous Reasoning (The Magic)
The agent will string together a Tool call, a Resource read, and a final transactional Tool call.

__"I am travelling from Mumbai to Bengaluru today (User ID: 90210). Please check my flight status. If it is delayed, check the refund policy to see what I am eligible for, and if I am eligible for anything, autonomously process that compensation for me."__

### 🔍 Watch the Terminal Logs!

When you run the Level 3 prompt, look at the right side of your Web UI screen. You will see the agent's internal monologue as it autonomously calls the status tool, reads the policy, and triggers the final refund!

---
Built for the GDG Cloud Mumbai Community! Happy Building!

---

