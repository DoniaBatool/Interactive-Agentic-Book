"""
Runtime Registry

Registry mapping chapter IDs to runtime descriptions.
Provides centralized runtime lookup for routing decisions.

TODO: Phase 2 - Replace strings with runtime objects
TODO: Phase 2 - Add runtime object instantiation
TODO: Phase 2 - Add runtime configuration
"""

# Chapter Runtime Registry
# Maps chapter IDs to runtime descriptions (Phase 1: strings, Phase 2: objects)

CHAPTER_RUNTIMES = {
    1: "engine for Chapter 1",
    2: "engine for Chapter 2",
    3: "engine for Chapter 3"
}

# TODO: Phase 2 - Replace with runtime objects
# CHAPTER_RUNTIMES = {
#     1: Chapter1Runtime(),
#     2: Chapter2Runtime(),
#     3: Chapter3Runtime()
# }

# TODO: Phase 2 - Add runtime object instantiation
# TODO: from app.ai.runtime.ch1_runtime import Chapter1Runtime
# TODO: from app.ai.runtime.ch2_runtime import Chapter2Runtime
# TODO: from app.ai.runtime.ch3_runtime import Chapter3Runtime

# TODO: Phase 2 - Add runtime configuration
# TODO: Each runtime object can have its own configuration
# TODO: Runtime objects can have state and methods

