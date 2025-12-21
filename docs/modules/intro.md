---
id: intro
slug: /modules/intro
title: "Chapter 1: Introduction to Physical AI"
description: Foundations of embodied intelligence, sensors, safety, and course roadmap.
---

# Chapter 1: Introduction to Physical AI

## Overview
Physical AI bridges digital intelligence with the physical world so robots can perceive, plan, and act safely alongside humans. This course focuses on humanoid-capable systems using ROS 2, Gazebo/Unity, NVIDIA Isaac, and Vision-Language-Action (VLA) pipelines.

## Why Physical AI Matters
- Humanoid form fits human environments (doors, stairs, tools).
- Embodied systems must respect physics: balance, contact, friction, inertia.
- Data-rich interactions enable safer, more capable assistants.

## Scope
- Control stack: ROS 2 nodes, topics, services, actions.
- Simulation: Gazebo physics + Unity visualization.
- AI brain: NVIDIA Isaac Sim/ROS for perception, navigation, sim-to-real.
- VLA: natural language to robot action (voice-to-action, planning).

## Prerequisites
- Comfortable with Python/TypeScript basics.
- Linux development workflow (terminal, package management).
- Intro linear algebra and basic kinematics (helpful, not mandatory).

## Sensor Stack
- LiDAR: environment structure and ranging.
- Depth/RGB cameras: perception, object detection, and SLAM input.
- IMU: orientation and balance cues.
- Force/torque: contact awareness and safer manipulation.

## Safety & Ethics
- Human-robot interaction: clear intent, collision avoidance, fall-safety.
- Data and privacy: handle voice/vision responsibly.
- Operational safety: test in simulation first; apply limits in real hardware.

## Module Roadmap
- Foundations: embodied intelligence principles, constraints of physics.
- Sensors primer: LiDAR, cameras, IMUs, F/T; how they feed the stack.
- Safety and ethics baseline for all later labs.
- Forward links into ROS 2, Gazebo/Unity, NVIDIA Isaac, and VLA modules.

## Key Outcomes
- Explain why embodiment changes AI design.
- Identify the core sensors and their roles.
- Understand how the course modules connect from control to perception to VLA.

## Lab Preview
- Install and validate dev environment (Node + Docusaurus docs).
- Run the course site locally and explore the module map.
- Optional: inspect sample sensor data (bag files or ROS topics) to connect theory to practice.

