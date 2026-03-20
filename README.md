# 🤖 Build an Autonomous Travel Agent with Google ADK & MCP

## Executive Summary
Today, we are moving beyond standard chatbots. In this hands-on lab, you will build a deterministic, multi-reasoning Agentic AI system using Google's Agent Development Kit (ADK) and the Model Context Protocol (MCP).

Instead of an AI that just generates text, you will build an orchestrator. Our Transit Agent will dynamically fetch live data, read business policies, and execute transactional workflows (like issuing refunds) completely on its own, based on the rules we set.

### The Tech Stack:

Google ADK: The "Brain" - Orchestrates the ReAct (Reason + Act) loop and manages state using Gemini.

FastMCP: The "Muscle" - A standardized protocol to expose your backend APIs and logic to the AI.

uv: Lightning-fast Python environment manager.

Docker: For reliable, instant deployment.

## 🚀 Quick Start: Open in Cloud Shell
To skip local setup and jump straight into the code, click the button below to launch this repository in Google Cloud Shell.

## 🚀 Quick Start: Google Cloud Shell
The fastest way to run this lab is directly in Google Cloud Shell.

### Option 1: The Magic Button
Click below to automatically launch Cloud Shell and clone this repository:
[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/ruby-verma/transit-agent.git)

### Option 2: The CLI Method
If you already have Cloud Shell open, simply paste this command into your terminal:

```Bash
git clone https://github.com/https://github.com/ruby-verma/transit-agent.git && cd transit-agent 
```
``
(Note: Don't forget to configure your .env file with your Google Gemini API key before running the containers!)``

## Folder Structure
```
transit-agent/
├── .env.example            # Template for the API key
├── Dockerfile              # Container spec
├── README.md               # The full lab guide we created
├── agent.py                # The ADK Agent code
├── docker-compose.yml      # Orchestration
└── transit_server.py       # FastMCP Server code
```

## 🧠 Architecture Overview
### 1. The Data Layer (transit_server.py)
This file runs our FastMCP Server. It does not contain any AI logic. It simply exposes two types of endpoints to the agent:

Tools: Executable Python functions (e.g., fetching a delay, processing a refund).

Resources: Static text or context (e.g., the corporate refund policy).

### 2. The Intelligence Layer (agent.py)
This file uses Google ADK. It connects to the MCP server, discovers the tools, and uses Gemini to orchestrate a solution. We have enabled debug logging so you can watch the AI "think" step-by-step.

## 🏃‍♂️ Task 1: Execute the Agentic Workflow
We have containerized the entire architecture so you don't have to worry about Python versions or dependency conflicts.

1. Source your environment variables (if running locally):

```bash
source .env
```

2. Build and run the multi-container application:

```bash
docker compose up --build
```

## 🗣️ Task 2: How to Talk to Your Agent
To truly see the difference between a standard chatbot and an Agentic system, try editing the prompt variable inside agent.py with these examples. Re-run the container after changing the prompt to see the agent's behavior change.

### Level 1: Simple Data Retrieval
The agent will just use the check_transit_status tool.

"What is the status of the Vande Bharat express from Mumbai to Ahmedabad?"

### Level 2: Knowledge & Policy Extraction
The agent will realize it needs to read the policy://refunds resource.

"My flight from Mumbai to Bengaluru is delayed. What is the official compensation policy for delays?"

### Level 3: Full Autonomous Reasoning (The Magic)
The agent will string together a Tool call, a Resource read, and a final transactional Tool call.

"I am travelling from Mumbai to Bengaluru today (User ID: 90210). Please check my flight status. If it is delayed, check the refund policy to see what I am eligible for, and if I am eligible for anything, autonomously process that compensation for me."

### 🔍 Watch the Terminal Logs!

When you run the Level 3 prompt, look at the terminal. You will see the ADK Debug logger reveal the agent's invisible workflow:

``DEBUG``: Calling ``check_transit_status`` -> Discovers the 120-minute delay.

``DEBUG``: Reading the ``policy://refunds resource`` -> Learns the 120-minute rule.

``DEBUG``: Calling ``process_compensation`` -> Autonomously finalizes the refund via the backend.

---
Built for the GDG Cloud Mumbai Community! Happy Building!

---

