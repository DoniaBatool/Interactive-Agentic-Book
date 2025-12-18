---
id: ros2
slug: /modules/ros2
title: "Chapter 2: ROS 2 Nervous System"
description: "Core ROS 2 concepts for humanoid control: nodes, topics, services, actions, launch files, URDF basics."
---

# Chapter 2: ROS 2 Nervous System

## Overview
ROS 2 is the “nervous system” for humanoid-capable robots. It coordinates sensing, planning, and actuation through nodes and message passing, enabling safe, modular control.

## Nodes
- Independent processes that encapsulate functions (e.g., perception, control, mapping).
- For humanoids: separate nodes for balance control, joint controllers, vision, and speech.

## Topics
- Publish/subscribe channels for streaming data (sensor feeds, state, commands).
- Examples: `/joint_states`, `/imu/data`, `/camera/color/image_raw`, `/cmd_vel`.
- Use QoS profiles appropriate to reliability vs. latency (e.g., sensor data best-effort).

## Services
- Request/response calls for on-demand actions (e.g., trigger calibration, reset posture).
- Good for discrete operations where immediate confirmation is needed.

## Actions
- Long-running goals with feedback and cancellation (e.g., walk to waypoint, pick/place).
- Essential for humanoid navigation and manipulation tasks.

## Launch Files
- Orchestrate multiple nodes with parameters and remaps.
- Humanoid example: bring up controllers, sensor bridges, state estimator, and navigation stack together.
- Keep parameters versioned and organized per environment (sim vs. real).

## URDF Essentials
- Defines links, joints, frames, inertias, and sensor mounts.
- Critical for kinematics, collision models, and accurate transforms.
- For humanoids: ensure foot frames, IMU placement, and hand/end-effector frames are correct.

## Humanoid Control Patterns
- Sensor fusion node → state estimator → controller nodes → actuators.
- Perception pipelines publish to planning/action servers.
- Use namespaced nodes for left/right limbs and for sim vs. real (e.g., `/sim/`, `/real/`).

## Pitfalls & Safety
- Always test in simulation first; enforce limits and watchdogs.
- Validate TF tree correctness; bad frames break planning and control.
- Manage QoS carefully to avoid dropped critical messages.

## Recap / Key Outcomes
- You understand nodes/topics/services/actions and when to use each.
- You know how launch files coordinate a humanoid bring-up.
- You grasp URDF essentials needed for humanoid kinematics and sensing.

## Next Steps
- Move to simulation workflows (Gazebo/Unity).
- Try a minimal graph: joint state publisher + controller + IMU + simple action server in sim.

