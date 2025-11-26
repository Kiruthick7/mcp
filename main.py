from mcp.server.fastmcp import FastMCP

app = FastMCP("Demo")

@app.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@app.resource("greeting//{name}")
def get_greeting(name: str) -> str:
    """Generate a greeting message."""
    return f"Hello, {name}!"

@app.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting message based on the style."""
    styles={
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting"
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."
