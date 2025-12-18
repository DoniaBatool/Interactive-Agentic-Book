---
id: course-overview
title: Physical AI & Humanoid Robotics
description: Quarter overview, learning outcomes, weekly progression, and hardware expectations for the Physical AI & Humanoid Robotics textbook.
---

# Course Overview

The future of AI extends into the physical world. This course bridges digital intelligence to embodied systems using ROS 2, Gazebo/Unity, NVIDIA Isaac, and Vision-Language-Action pipelines so learners can control humanoid-capable robots in simulation and real environments.

## Why Physical AI Matters

Humanoid robots thrive in human-centered spaces by sharing our form factor and leveraging abundant interaction data. Physical AI trains agents that respect physics, interact safely, and collaborate with people.

## Learning Outcomes

- Understand Physical AI principles and embodied intelligence
- Master ROS 2 for robotic control and messaging
- Simulate humanoid systems with Gazebo and Unity
- Develop perception and navigation with NVIDIA Isaac (Sim + ROS)
- Design humanoid kinematics, locomotion, and manipulation strategies
- Integrate GPT-based conversational and planning capabilities for robots

## Weekly Breakdown (Quarter)

- **Weeks 1-2:** Foundations of Physical AI; sensors (LiDAR, cameras, IMUs, F/T)
- **Weeks 3-5:** ROS 2 architecture (nodes, topics, services, actions), launch files, packages
- **Weeks 6-7:** Gazebo simulation, URDF/SDF, physics + sensor simulation, Unity visualization
- **Weeks 8-10:** NVIDIA Isaac SDK/Sim, AI perception, RL for control, sim-to-real transfer
- **Weeks 11-12:** Humanoid development: kinematics/dynamics, bipedal locomotion, manipulation
- **Week 13:** Conversational robotics with GPT + speech; multimodal interaction

## Hardware Requirements

This course is computationally heavy (physics + vision + LLM):

- **Digital Twin Workstation (per student):** RTX 4070 Ti or better (24 GB VRAM ideal), Intel i7/Ryzen 9, 64 GB RAM, Ubuntu 22.04
- **Edge Kit:** Jetson Orin Nano/NX, Intel RealSense D435i/D455, USB mic array, optional IMU
- **Robotics Options:** Budget proxy (Unitree Go2/arm), miniature humanoid (Unitree G1/Robotis OP3), or premium sim-to-real (Unitree G1 Humanoid)
- **Cloud Option:** GPU instances (e.g., AWS g5/g6e) for Isaac Sim with local Jetson for low-latency deployment

## Module Map

1. Introduction to Physical AI and embodied intelligence
2. ROS 2 nervous system
3. Gazebo/Unity digital twin
4. NVIDIA Isaac AI brain
5. Vision-Language-Action capstone (voice-to-action, planning, perception, manipulation)

## Chat with the Textbook Assistant

import RagChatPanel from '@site/src/components/RagChatPanel';

<RagChatPanel chapter="Course Overview" />


