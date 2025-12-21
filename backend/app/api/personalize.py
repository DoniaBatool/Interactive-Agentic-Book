"""
Personalization API - Adjusts chapter content based on user's skill level
"""
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI

from app.core.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/personalize", tags=["personalize"])

settings = get_settings()
openai_client = OpenAI(api_key=settings.openai_api_key)


class PersonalizeRequest(BaseModel):
    """Request to personalize content"""
    content: str = Field(..., description="Markdown content to personalize")
    software_level: str = Field(
        default="beginner",
        description="User's software experience level: beginner, intermediate, advanced"
    )
    hardware_level: str = Field(
        default="none",
        description="User's hardware experience level: none, some, extensive"
    )
    technologies: Optional[dict] = Field(
        default=None,
        description="Technologies the user knows (e.g., {'python': true, 'ros2': true})"
    )
    chapter_title: Optional[str] = Field(
        default=None,
        description="Title of the chapter being personalized"
    )


class PersonalizeResponse(BaseModel):
    """Response with personalized content"""
    content: str = Field(..., description="Personalized markdown content")
    level_summary: str = Field(..., description="Summary of personalization applied")
    success: bool = True


def get_personalization_prompt(
    software_level: str,
    hardware_level: str,
    technologies: Optional[dict],
    chapter_title: Optional[str]
) -> str:
    """Generate the system prompt for personalization based on user profile"""
    
    # Level descriptions
    software_desc = {
        "beginner": "new to programming, explain code step by step, avoid jargon",
        "intermediate": "comfortable with Python, can handle moderate complexity",
        "advanced": "professional developer, can handle complex concepts and optimizations"
    }.get(software_level, "beginner level")
    
    hardware_desc = {
        "none": "no robotics hardware experience, focus on simulation and concepts",
        "some": "basic Arduino/Raspberry Pi experience, can connect simple hardware",
        "extensive": "extensive experience with Jetson, RealSense, professional robots"
    }.get(hardware_level, "no hardware experience")
    
    # Known technologies
    known_tech = []
    if technologies:
        known_tech = [tech for tech, knows in technologies.items() if knows]
    tech_str = ", ".join(known_tech) if known_tech else "none specified"
    
    chapter_context = f"for the chapter '{chapter_title}'" if chapter_title else ""
    
    return f"""You are an expert educational content personalizer for a Physical AI & Humanoid Robotics textbook.

Your task is to adapt the provided content to match the reader's skill level while preserving all technical accuracy and key concepts.

READER PROFILE:
- Software Experience: {software_level} ({software_desc})
- Hardware Experience: {hardware_level} ({hardware_desc})
- Technologies Known: {tech_str}

PERSONALIZATION RULES:

For BEGINNER software level:
- Add explanatory comments to code
- Break down complex code into smaller steps
- Explain what each import/library does
- Add "Why this matters" explanations
- Include troubleshooting tips for common errors
- Use analogies to explain abstract concepts

For INTERMEDIATE software level:
- Keep code mostly as-is but add brief comments
- Focus on the "how" and "why" of robotics concepts
- Include optimization tips where relevant
- Reference related concepts they might know

For ADVANCED software level:
- Include advanced optimizations and best practices
- Add performance considerations
- Reference academic papers or advanced resources
- Include edge cases and production considerations
- Add sections on scaling and architecture

For hardware level adjustments:
- NONE: Focus on simulation (Gazebo, Isaac Sim), virtual environments
- SOME: Include basic hardware setup with safety warnings
- EXTENSIVE: Include advanced hardware configuration, calibration, real-world deployment

IMPORTANT RULES:
1. Keep the same markdown structure and headings
2. Preserve all code blocks (adjust complexity inside them)
3. Don't remove any critical technical information
4. Add helpful annotations and explanations as needed
5. If content references unknown technologies, add brief explanations
6. Maintain a friendly, encouraging tone
7. Keep the personalized content roughly the same length (+/- 30%)

Output the personalized markdown content directly, no explanations needed."""


@router.post("/content", response_model=PersonalizeResponse)
async def personalize_content(request: PersonalizeRequest) -> PersonalizeResponse:
    """
    Personalize chapter content based on user's skill level.
    
    This endpoint takes markdown content and adapts it to match the user's
    software and hardware experience levels.
    """
    try:
        # Validate content length
        if len(request.content) < 50:
            raise HTTPException(
                status_code=400,
                detail="Content too short to personalize"
            )
        
        if len(request.content) > 50000:
            raise HTTPException(
                status_code=400,
                detail="Content too long. Please personalize smaller sections."
            )
        
        # Generate personalization prompt
        system_prompt = get_personalization_prompt(
            request.software_level,
            request.hardware_level,
            request.technologies,
            request.chapter_title
        )
        
        logger.info(
            f"Personalizing content for level: sw={request.software_level}, "
            f"hw={request.hardware_level}, chapter={request.chapter_title}"
        )
        
        # Call OpenAI to personalize
        response = openai_client.chat.completions.create(
            model=settings.chat_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please personalize this content:\n\n{request.content}"}
            ],
            temperature=0.7,
            max_tokens=4000,
        )
        
        personalized_content = response.choices[0].message.content
        
        # Generate level summary
        level_summary = f"Content adapted for {request.software_level} software level"
        if request.hardware_level != "none":
            level_summary += f" with {request.hardware_level} hardware experience"
        
        logger.info(f"Successfully personalized content ({len(personalized_content)} chars)")
        
        return PersonalizeResponse(
            content=personalized_content,
            level_summary=level_summary,
            success=True
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Personalization error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to personalize content: {str(e)}"
        )


@router.get("/health")
async def personalize_health():
    """Health check for personalization service"""
    return {"status": "ok", "service": "personalize"}

