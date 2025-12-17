---
id: vla-capstone
slug: /modules/vla-capstone
title: Chapter 5: Vision-Language-Action Capstone
description: Voice-to-action, intent parsing, planning, navigation, perception, and manipulation for the capstone humanoid project.
---

# Chapter 5: Vision-Language-Action Capstone

## Overview
This capstone ties voice, language, vision, and action to control a humanoid: voice input → intent → plan → navigation/manipulation with safety checks.

## Voice-to-Action Pipeline
- Voice capture → ASR (e.g., Whisper) → transcript.
- Intent parsing: map to goals and constraints; confirm critical actions.

## Intent Parsing & Planning
- Translate natural language into ROS 2 actions/waypoints/skills.
- Use planning layer to sequence navigation + manipulation with preconditions.

## Navigation & Manipulation Execution
- Nav2 for movement; ROS actions for arms/hands; coordinate frames and TF validation.
- Recovery behaviors for failures (replan, retry, or ask user).

## Perception Hooks
- Vision/LiDAR for object/scene grounding; confidence checks.
- Use perception outputs to validate goals before executing.

## Safety & Guardrails
- Confirmation for risky tasks; bounding areas; rate limits; watchdogs.
- Simulation-first testing before real hardware.

## Evaluation & Metrics
- Task success rate; time-to-complete; safety events; perception confidence.

## Demo Tips
- Start with simple voice commands (“go to table”, “pick the cup”).
- Show partial progress updates and safe stops.

## Recap / Key Outcomes
- You understand the end-to-end voice-to-action flow with planning and perception.
- You know how to wire Nav2, manipulation, and safety guardrails.
- You have metrics to evaluate and iterate on the capstone.

## Next Steps
- Integrate personalization and translation toggles; harden testing and demos.

