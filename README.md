# UIKit MCP Server

This project is UIKits MCP Server for Flutter UI template.

## Project Setup

To set up the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/anoochit/uikits_mcp_server.git
    cd uikits_mcp_server
    ```

2. **Create a virtual environment and install dependencies using `uv`:**

    ```bash
    uv venv
    uv sync
    ```

## Install

Install a MCP server in MCP client applications. FastMCP currently supports the following clients:

- **Claude Code**: Installs via Claude Code’s built-in MCP management system

  ```bash
  fastmcp install claude-code main.py
  ```

- **Claude Desktop**: Installs via direct configuration file modification

  ```bash
  fastmcp install claude-desktop main.py
  ```

- **Cursor**: Installs via deeplink that opens Cursor for user confirmation

  ```bash
  fastmcp install cursor main.py
  ```

- **MCP JSON**: Generates standard MCP JSON configuration for manual use

  ```bash
  fastmcp install mcp-json main.py
  ```
