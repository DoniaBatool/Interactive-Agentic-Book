"""
Chapter Access Control Map

Static chapter-to-role access mapping for RBAC-based chapter permissions.
All access rules are placeholders—no real enforcement logic.

TODO: Real access control enforcement will be implemented in a future feature.
"""

from typing import Dict, List

# Chapter Access Map
# Format: {chapter_number: [list of allowed roles]}
# Default: All roles allowed for all chapters (placeholder)
CHAPTER_ACCESS_MAP: Dict[int, List[str]] = {
    1: ["admin", "educator", "student"],
    2: ["admin", "educator", "student"],
    3: ["admin", "educator", "student"]
}

# TODO: Real access control logic will:
# - Check if user_role is in allowed roles for chapter_number
# - Support dynamic access assignment
# - Support user-specific overrides
# - Support time-based access
# - Support chapter subscription model
# - Support access inheritance

