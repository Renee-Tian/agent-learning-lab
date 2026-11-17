# MCP Information Server

**A simple MCP Server providing knowledge search and topic information tools.**

一个基于 MCP Python SDK 实现的简单信息查询服务，通过两个 MCP 工具向 AI 应用提供知识搜索和主题信息查询能力。

## 1. Project Overview | 项目介绍

This project implements a simple MCP Server using `FastMCP`.

The server provides access to a small in-memory knowledge base containing introductory information about Agent, LLM, and MCP.

本项目使用 MCP Python SDK 中的 `FastMCP` 创建服务，通过标准化工具接口，让 AI 应用能够查询预设知识。

## 2. Features | 核心功能

The server provides two tools:

### `search_knowledge(query: str)`

- Searches the knowledge base using keywords.
- Supports matching both topic names and content.
- Returns relevant knowledge entries.

根据关键词搜索知识库，同时匹配主题名称和内容。

### `get_information(topic: str)`

- Retrieves information about a specific topic.
- Supports exact topic-name matching.

根据指定主题名称获取详细信息。

## 3. Knowledge Base | 知识库

The current knowledge base contains three topics:

- Agent
- LLM
- MCP

**Note:** The knowledge base is currently implemented as a Python dictionary. It is a simple demonstration, not an external database.

注意：当前知识库使用 Python 字典实现，属于基础功能演示，尚未连接外部数据库。

## 4. Project Structure | 项目结构

```text
mcp-servers/
├── info_server.py
├── requirements.txt
└── README.md
```

## 5. Installation | 安装依赖

Create and activate a Python virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Run the Server | 启动服务

```bash
python info_server.py
```

The server uses the STDIO transport.

该服务通过 STDIO 方式运行，需要由支持 MCP 的客户端或宿主应用启动并连接。

## 7. Technologies | 技术栈

- Python
- MCP Python SDK
- FastMCP
- STDIO Transport

## 8. Learning Objectives | 学习目标

Through this experiment, I practiced:

- Creating an MCP Server with FastMCP.
- Registering tools using `@mcp.tool()`.
- Defining tool parameters and return values.
- Understanding STDIO transport.
- Providing structured knowledge access through MCP tools.

通过本项目，我实践了 MCP Server 创建、工具注册、参数定义以及 STDIO 通信方式，加深了对 MCP 工具调用机制的理解。

## 9. Project Status | 项目状态

**Status: Learning & Experimenting**

This project is an ongoing learning experiment. More tools and capabilities may be added in the future.

