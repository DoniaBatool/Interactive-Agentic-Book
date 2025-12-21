# Data Model – Feature 011: Agents/ChatKit Integration

## OpenAI Tool Schema

```python
RETRIEVE_BOOK_CONTEXT_TOOL = {
    "type": "function",
    "function": {
        "name": "retrieve_book_context",
        "description": "Search the Physical AI & Humanoid Robotics textbook for relevant content. Use this tool when the user asks about course topics, ROS 2, Gazebo, Isaac Sim, VLA models, or any robotics concepts covered in the course.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to find relevant textbook content"
                },
                "chapter_filter": {
                    "type": "string",
                    "description": "Optional: specific chapter to prioritize in results"
                }
            },
            "required": ["query"]
        }
    }
}
```

## Agent System Prompt

```python
AGENT_SYSTEM_PROMPT = """You are an AI teaching assistant for the "Physical AI & Humanoid Robotics" course.

Your role:
- Help students understand course concepts
- Answer questions about ROS 2, Gazebo, Isaac Sim, VLA models, and robotics
- Provide accurate information from the textbook

When to use the retrieve_book_context tool:
- Questions about course topics or concepts
- Requests for explanations or examples from the textbook
- Any question that might be answered by course content

When NOT to use the tool:
- Simple greetings or conversational messages
- Questions clearly outside the course scope
- Follow-up clarifications that don't need new context

Always cite your sources when using textbook content."""
```

## Request/Response Models

### ChatRequest (unchanged)
```python
class ChatRequest(BaseModel):
    question: str
    filters: Optional[ChunkFilters] = None
    stream: bool = False
```

### ChatResponse (unchanged)
```python
class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    stream: bool = False
```

### Citation (unchanged)
```python
class Citation(BaseModel):
    path: str
    chapter: str
    section: Optional[str] = None
    score: Optional[float] = None
```

## Internal Agent Models

### ToolCall (internal)
```python
@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict
```

### ToolResult (internal)
```python
@dataclass
class ToolResult:
    tool_call_id: str
    content: str
    citations: List[Citation]
```

