"""
Role Definitions and Permission Maps

Static role constants and placeholder permission mappings for RBAC framework.
All permissions are placeholders—no real enforcement logic.

TODO: Real permission enforcement will be implemented in a future feature.
"""

# Role Constants
ROLE_ADMIN = "admin"
ROLE_EDUCATOR = "educator"
ROLE_STUDENT = "student"

# Placeholder Permission Map
# Format: {role: [list of permissions]}
# Permission format: "{action}:{resource}"
permissions = {
    "admin": [
        "*"  # All permissions
    ],
    "educator": [
        "read:chapters",
        "write:content",
        "read:analytics",
        "manage:students"
    ],
    "student": [
        "read:chapters",
        "read:content",
        "read:own_progress"
    ]
}

# TODO: Real permission enforcement logic will:
# - Check if user_role has permission for action
# - Support wildcard permissions ("*")
# - Support permission inheritance
# - Support dynamic permission assignment
# - Support permission hierarchies

