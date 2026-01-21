from fastmcp import FastMCP
import requests

mcp = FastMCP("FlutterRepoServer")

REPO_BASE_URL = "https://raw.githubusercontent.com/anoochit/uikits/refs/heads/master"
MANIFEST_URL = f"{REPO_BASE_URL}/lib/pages/templates_manifest.json"

@mcp.tool()
def list_templates() -> str:
    """
    Fetch the latest list of Flutter templates from the GitHub repository.

    This tool retrieves the templates manifest file and returns
    a human-readable list including template ID, title, and description.
    """
    try:
        response = requests.get(MANIFEST_URL)
        response.raise_for_status()
        templates = response.json()
        
        output = "📦 Available Flutter Templates:\n"
        for t in templates:
            output += f"- ID: {t['id']} | {t['title']}\n  Detail: {t['description']}\n"
        return output
    except Exception as e:
        return f"Error: Unable to load template list ({str(e)})"

@mcp.tool()
def get_template_code(template_id: str) -> str:
    """
    Retrieve Dart source code for a specific Flutter template by ID.

    The template ID must match one from the templates manifest.
    The source code is fetched directly from the GitHub repository
    using the file path defined in the manifest.
    """
    try:
        # 1. Load manifest to find the template file path
        manifest_res = requests.get(MANIFEST_URL)
        templates = manifest_res.json()
        target = next((t for t in templates if t['id'] == template_id), None)
        
        if not target:
            return f"Template ID not found: {template_id}"

        # 2. Fetch the Dart code from the specified path
        file_url = f"{REPO_BASE_URL}/{target['path']}"
        code_res = requests.get(file_url)
        code_res.raise_for_status()
        
        return f"--- Code for {target['title']} ---\n\n{code_res.text}"
    except Exception as e:
        return f"Error: Unable to retrieve template code ({str(e)})"

if __name__ == "__main__":
    mcp.run()
