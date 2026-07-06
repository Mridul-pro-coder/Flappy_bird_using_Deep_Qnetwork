# 🐦 Flappy Bird AI using Deep Q-Network (DQN)

An AI agent that learns to play **Flappy Bird** using **Deep Reinforcement Learning**. The project implements a **Deep Q-Network (DQN)** that interacts with the game environment, learns from experience, and gradually improves its gameplay without any human intervention.

---

# ✨ Features

- 🧠 Deep Q-Network (DQN) implementation
- 🎮 Learns to play Flappy Bird autonomously
- 🔄 Experience Replay for stable learning
- 🎯 Target Network to improve convergence
- 📈 Training reward visualization
- 💾 Save and load trained models
- ⚡ GPU support with PyTorch (if available)

---

# 🛠️ Tech Stack

### Language
- Python

### Deep Learning
- PyTorch

### Reinforcement Learning
- Deep Q-Network (DQN)

### Environment
- Flappy Bird Game Environment (Pygame)

### Other Libraries
- NumPy
- Matplotlib
- OpenCV (if used)

---

# 🧠 DQN Algorithm

The agent learns by repeatedly interacting with the environment.

1. Observe the current game state.
2. Choose an action using an ε-greedy policy.
3. Execute the action.
4. Receive a reward and the next state.
5. Store the transition in the replay buffer.
6. Sample a random mini-batch from memory.
7. Update the Q-network using the Bellman equation.
8. Periodically update the target network.
9. Repeat until the agent learns an optimal policy.

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flappy-bird-dqn.git

cd flappy-bird-dqn
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train the agent

```bash
python train.py
```

---

### 5. Test the trained model

```bash
python test.py
```

---

# 🚀 Training Pipeline

```text
Game Environment
        │
        ▼
Current State
        │
        ▼
DQN Agent
        │
        ▼
Choose Action (ε-Greedy)
        │
        ▼
Environment Step
        │
        ▼
Reward + Next State
        │
        ▼
Replay Buffer
        │
        ▼
Mini-batch Sampling
        │
        ▼
Neural Network Update
        │
        ▼
Target Network Update
```

---

# 📦 Requirements

- Python 3.10+
- PyTorch
- NumPy
- Pygame
- Matplotlib

---

# 📊 Results

After sufficient training, the agent learns to:

- Avoid obstacles effectively
- Maximize cumulative rewards
- Improve survival time over episodes
- Develop a successful gameplay strategy without manual programming

---

# 🔮 Future Improvements

- Double DQN (DDQN)
- Dueling DQN
- Prioritized Experience Replay
- Noisy Networks
- Rainbow DQN
- PPO implementation
- TensorBoard integration
- Hyperparameter tuning

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📚 References

- Playing Atari with Deep Reinforcement Learning (DeepMind, 2013)
- Human-Level Control Through Deep Reinforcement Learning (Nature, 2015)

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub.
