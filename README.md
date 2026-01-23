# 🎬 Nano Cinema AI Video Studio

**An open-source, end-to-end AI video production pipeline optimized for 8GB VRAM consumer GPUs.**

## 🚀 Workflow Overview

This project implements a complete generative AI pipeline orchestrated via a **Gradio Web UI**, allowing users to create short films from simple text prompts entirely locally (with API support for text).

> **Script** (Llama-3.3-70b via Groq) ➡️ **Images** (SDXL-Turbo) ➡️ **Audio** (EdgeTTS) ➡️ **Video** (LTX) ➡️ **Composition** (FFmpeg)

---

## 🌟 Background & Motivation

The 2025 Google I/O Developer Conference showcased groundbreaking advancements in AI, particularly the **Veo3 model** and **Flow platform**, demonstrating cinema-quality text-to-movie generation. While impressive, these proprietary tools often come with high costs or restricted access.

**Our Mission:**
The goal of **Nano Cinema AI Video Studio** is to **democratize AI video creation**. We aim to solve resource constraints by combining efficient open-source models to achieve a "free and unlimited" video production workflow that runs smoothly on consumer-grade hardware.

* ✅ **Hardware Tested:** NVIDIA GeForce RTX 4060 (8GB VRAM)
* ✅ **Result:** High-quality image and video generation without requiring enterprise-level GPUs.

---

## 🛠️ Technology Stack

We carefully selected components to balance **performance, cost, and speed**:

1.  **Script Generation: Llama-3.3-70b-versatile (via Groq)**
    * Utilizes Groq's LPU technology for lightning-fast, free inference. Llama-3.3 offers exceptional creative writing capabilities and multilingual support.

2.  **Image Generation: SDXL-Turbo**
    * Powered by Adversarial Diffusion Distillation (ADD), generating high-quality cinematic shots in just **1-4 steps**. Implemented via Hugging Face `diffusers`.

3.  **Audio Synthesis: EdgeTTS**
    * Accesses Microsoft Edge's natural-sounding speech synthesis. Requires **no API key**, no heavy downloads, and offers granular control over pitch and speed.

4.  **Video Generation: LTX (Image-to-Video)**
    * A breakthrough in local generative video. LTX offers low latency and high computational efficiency, making it possible to generate video clips on 8GB VRAM cards.

5.  **Interface: Gradio**
    * Provides a user-friendly Web UI for real-time preview, script editing, and partial re-rendering (inpainting/regeneration) support.

---

## 📦 Getting Started

*(Add your installation steps here, e.g., pip install -r requirements.txt)*
