
from mcp.server.fastmcp import FastMCP

# 创建第二个 MCP Server
mcp = FastMCP("Information Server")


# 模拟一个简单的知识库
KNOWLEDGE_BASE = {
    "Agent": (
        "Agent 是能够感知环境、理解任务、制定计划，"
        "并调用工具执行任务的智能系统。"
    ),
    "LLM": (
        "LLM 是大语言模型，通过大量文本数据训练，"
        "具备语言理解、文本生成和推理等能力。"
    ),
    "MCP": (
        "MCP 是模型上下文协议，"
        "用于标准化 AI 应用与外部工具、数据源之间的连接。"
    )
}


# 工具一：搜索知识
@mcp.tool()
def search_knowledge(query: str) -> str:
    """根据关键词搜索知识库中的相关内容。"""

    results = []

    for topic, content in KNOWLEDGE_BASE.items():

        if query.lower() in topic.lower() or query.lower() in content.lower():
            results.append(f"{topic}：{content}")

    if not results:
        return "知识库中没有找到相关内容。"

    return "\n".join(results)


# 工具二：获取主题详细信息
@mcp.tool()
def get_information(topic: str) -> str:
    """查询指定主题的详细信息。"""

    for name, content in KNOWLEDGE_BASE.items():

        if topic.lower() == name.lower():
            return content

    return f"暂时没有找到关于 {topic} 的信息。"


# 启动 MCP Server
if __name__ == "__main__":
    mcp.run(transport="stdio")
