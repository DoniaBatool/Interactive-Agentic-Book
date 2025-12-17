---
id: gazebo-unity
slug: /modules/gazebo-unity
title: Chapter 3: Gazebo & Unity Digital Twin
description: Physics simulation, URDF/SDF, sensor simulation, and Unity visualization for humanoid workflows.
---

# Chapter 3: Gazebo & Unity Digital Twin

## Overview
Gazebo provides physics-accurate simulation; Unity provides high-fidelity visualization and interaction. Together they form the digital twin for humanoid development.

## Gazebo Setup & Physics
- Configure gravity, solver, and collision parameters suitable for biped stability.
- Use realistic masses/inertias to avoid unstable simulations.

## URDF/SDF for Humanoids
- Define links/joints for limbs, torso, head, and sensors; ensure proper inertias.
- Use SDF for advanced world configuration; URDF for robot kinematics.

## Sensor Simulation (LiDAR/Depth/IMU)
- LiDAR: structure mapping and obstacle detection.
- Depth/RGB: perception and VSLAM inputs.
- IMU: balance/orientation; tune noise models to reflect hardware.

## Unity Visualization & HRI
- Use Unity for human-robot interaction demos and polished visuals.
- Mirror Gazebo state into Unity for presentations and UX testing.

## ROS Interfaces / Bridge
- Expose topics/services/actions that match the ROS 2 stack (e.g., `/cmd_vel`, `/joint_states`, camera/IMU topics).
- Keep consistent namespaces for sim vs. real (e.g., `/sim/robot/...`).

## Workflow & Tips
- Iterate in Gazebo for physics correctness; present in Unity for HRI.
- Version parameter files (PID gains, friction, contact properties).

## Pitfalls & Safety
- Validate TF tree and collision geometry; bad inertias destabilize bipeds.
- Use simulation-first testing; apply limits and watchdogs when moving to real hardware.

## Recap / Key Outcomes
- You can configure a humanoid digital twin with Gazebo physics and Unity visualization.
- You know how to simulate sensors and expose ROS interfaces.
- You understand common pitfalls and safety steps before real-world trials.

## Next Steps
- Move to NVIDIA Isaac integration and perception pipelines.

