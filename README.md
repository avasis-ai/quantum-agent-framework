# README.md - Quantum Agent Framework

## Autonomous Agents Orchestrating Quantum Computing Experiments

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/quantum-agent-framework.svg)](https://pypi.org/project/quantum-agent-framework/)

**Quantum Agent Framework** equips an AI agent with Quantum-SKILL.md, teaching it how to construct quantum circuits, interface with IBM's Qiskit API, and autonomously optimize qubit configurations to solve specific chemistry or cryptographic problems.

## 🎯 What It Does

This represents the absolute bleeding edge of technology (AI + Quantum). It generates massive academic and research appeal and prepares developers for the upcoming quantum hardware boom.

### Example Use Case

```python
from quantum_agent_framework.qiskit_bridge import QiskitBridge, QuantumGate
from quantum_agent_framework.agent import QuantumAgent, QuantumAgentFramework, QuantumSkill

# Initialize framework
framework = QuantumAgentFramework("quantum_lab")

# Create quantum agent
agent = framework.create_agent("quantum_researcher")

# Create quantum circuit
bridge = QiskitBridge()

circuit_id = bridge.create_circuit(
    name="quantum_coin_flip",
    num_qubits=2,
    description="Quantum coin flip experiment"
)

# Add gates
bridge.add_gate(circuit_id, QuantumGate.H, [0])
bridge.add_gate(circuit_id, QuantumGate.CNOT, [0, 1])

# Execute circuit
results = bridge.execute_circuit(circuit_id, shots=1024)

# Run quantum experiment
task = framework.execute_experiment(
    agent_name="quantum_researcher",
    description="Test quantum circuit",
    target_problem="quantum_simulation",
    num_qubits=2
)

# Get statistics
stats = framework.get_statistics()
print(f"Success rate: {stats['overall_success_rate']:.1%}")
```

## 🚀 Features

- **Quantum Circuit Construction**: Build and manage quantum circuits
- **Gate Operations**: Support for all basic quantum gates
- **Agent Orchestration**: Autonomous quantum computing agents
- **Qiskit Integration**: Interface with Qiskit simulators and backends
- **Circuit Optimization**: Automatically optimize quantum circuits
- **Experiment Tracking**: Track quantum experiments and results
- **Skill Management**: Register and manage quantum skills
- **Statistics & Analytics**: Detailed quantum computing statistics

### Core Components

1. **QiskitBridge**
   - Quantum circuit creation and management
   - Gate operations (H, X, Y, Z, CNOT, etc.)
   - Circuit optimization
   - Execution simulation

2. **QuantumAgent**
   - Autonomous quantum computing agent
   - State management (IDLE, PLANNING, EXECUTING, etc.)
   - Task execution and tracking
   - Skill registration

3. **QuantumAgentFramework**
   - Multi-agent orchestration
   - Experiment execution
   - Statistics aggregation
   - Resource management

4. **Quantum Gates**
   - H (Hadamard)
   - X, Y, Z (Pauli gates)
   - CNOT, CZ, SWAP
   - T, S (Phase gates)
   - Identity

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Qiskit, PyYAML, Click

### Install from PyPI

```bash
pip install quantum-agent-framework
```

### Install from Source

```bash
git clone https://github.com/avasis-ai/quantum-agent-framework.git
cd quantum-agent-framework
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
pip install pytest pytest-mock black isort
```

## 🔧 Usage

### Command-Line Interface

```bash
# Check version
quantum-agent --version

# Initialize framework
quantum-agent init --name quantum_lab

# Run quantum experiment
quantum-agent experiment --agent quantum_researcher --qubits 2

# View statistics
quantum-agent stats

# Run demo
quantum-agent demo
```

### Programmatic Usage

```python
from quantum_agent_framework.qiskit_bridge import QiskitBridge, QuantumGate
from quantum_agent_framework.agent import QuantumAgent, QuantumAgentFramework, QuantumSkill

# Initialize quantum agent framework
framework = QuantumAgentFramework("research_lab")

# Create quantum agent
agent = framework.create_agent("quantum_researcher")

# Initialize Qiskit bridge
bridge = QiskitBridge()

# Create quantum coin flip circuit
circuit_id = bridge.create_circuit(
    name="quantum_coin_flip",
    num_qubits=2,
    description="Create superposition and entanglement"
)

# Add Hadamard gate to create superposition
bridge.add_gate(circuit_id, QuantumGate.H, [0])

# Add CNOT gate to create entanglement
bridge.add_gate(circuit_id, QuantumGate.CNOT, [0, 1])

# Execute circuit
results = bridge.execute_circuit(circuit_id, shots=1024)

# Register quantum skills
hadamard_skill = QuantumSkill(
    skill_id="hadamard_001",
    name="Hadamard Skill",
    description="Create quantum superposition",
    skill_type="gate_operation",
    capabilities=["create_superposition", "quantum_fourier_transform"],
    confidence=0.95,
    version="1.0.0"
)

agent.register_skill(hadamard_skill)

# Execute quantum experiment
task = framework.execute_experiment(
    agent_name="quantum_researcher",
    description="Test quantum coin flip",
    target_problem="quantum_simulation",
    num_qubits=2
)

# Get results
task_results = task.result
print(f"Solution: {task_results['solution']}")
print(f"Confidence: {task_results['confidence']}")

# Get statistics
stats = framework.get_statistics()
print(f"Total agents: {stats['total_agents']}")
print(f"Success rate: {stats['overall_success_rate']:.1%}")
```

### Advanced Usage

```python
from quantum_agent_framework.qiskit_bridge import QiskitBridge, QuantumGate
from quantum_agent_framework.agent import QuantumAgent, QuantumAgentFramework, QuantumSkill

# Create multiple agents
framework = QuantumAgentFramework("quantum_research_lab")

agent1 = framework.create_agent("quantum_scientist_1")
agent2 = framework.create_agent("quantum_scientist_2")

# Create complex quantum circuits
bridge1 = QiskitBridge()
circuit1_id = bridge1.create_circuit("bell_state", 2, "Create Bell state")
bridge1.add_gate(circuit1_id, QuantumGate.H, [0])
bridge1.add_gate(circuit1_id, QuantumGate.CNOT, [0, 1])

bridge2 = QiskitBridge()
circuit2_id = bridge2.create_circuit("quantum_fourier", 3, "QFT circuit")
bridge2.add_gate(circuit2_id, QuantumGate.H, [0])
bridge2.add_gate(circuit2_id, QuantumGate.CNOT, [0, 1])
bridge2.add_gate(circuit2_id, QuantumGate.T, [2])

# Optimize circuits
bridge1.optimize_circuit(circuit1_id)
bridge2.optimize_circuit(circuit2_id)

# Register specialized skills
skill = QuantumSkill(
    skill_id="quantum_optimization",
    name="Quantum Optimization",
    description="Optimize quantum circuits",
    skill_type="optimization",
    capabilities=["circuit_simplification", "gate_removal"],
    confidence=0.98,
    version="2.0.0"
)

agent1.register_skill(skill)

# Execute experiments with different qubits
for num_qubits in [2, 3, 4]:
    task = framework.execute_experiment(
        agent_name="quantum_scientist_1",
        description=f"QFT with {num_qubits} qubits",
        target_problem="quantum_fourier_transform",
        num_qubits=num_qubits
    )
    print(f"Task {task.task_id}: {task.success}")

# Get statistics
bridge_stats = bridge1.get_statistics()
agent_stats = agent1.get_statistics()
framework_stats = framework.get_statistics()

print(f"Circuits: {bridge_stats['total_circuits']}")
print(f"Agent tasks: {agent_stats['total_tasks']}")
print(f"Framework success: {framework_stats['overall_success_rate']:.1%}")
```

## 📚 API Reference

### QiskitBridge

Bridge between quantum agent and Qiskit.

#### `create_circuit(name, num_qubits, description)` → str

Create a new quantum circuit.

#### `execute_circuit(circuit_id, shots)` → Dict

Execute a quantum circuit.

### QuantumAgent

Autonomous agent for quantum computing.

#### `execute_task(description, target_problem, num_qubits)` → AgentTask

Execute a quantum computing task.

#### `register_skill(skill)` → bool

Register a quantum skill.

## 🧪 Testing

Run tests with pytest:

```bash
python -m pytest tests/ -v
```

## 📁 Project Structure

```
quantum-agent-framework/
├── README.md
├── pyproject.toml
├── LICENSE
├── AGENTS.md
├── src/
│   └── quantum_agent_framework/
│       ├── __init__.py
│       ├── qiskit_bridge.py
│       └── agent.py
├── tests/
│   └── test_quantum.py
└── .github/
    └── ISSUE_TEMPLATE/
        └── bug_report.md
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: `python -m pytest tests/ -v`
5. **Submit a pull request**

### Development Setup

```bash
git clone https://github.com/avasis-ai/quantum-agent-framework.git
cd quantum-agent-framework
pip install -e ".[dev]"
pre-commit install
```

## 📝 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## 🎯 Vision

Quantum Agent Framework represents the absolute bleeding edge of technology (AI + Quantum). It generates massive academic and research appeal and prepares developers for the upcoming quantum hardware boom.

### Key Innovations

- **Quantum Circuit Construction**: Build and manage quantum circuits
- **Agent Autonomy**: Autonomous quantum computing agents
- **Qiskit Integration**: Interface with IBM's Qiskit API
- **Circuit Optimization**: Automatically optimize qubit configurations
- **Problem Solving**: Solve chemistry and cryptographic problems
- **Skill-Based Architecture**: Extensible quantum skills
- **Statistics & Analytics**: Detailed quantum computing insights

### Impact on Quantum Computing

This tool enables:

- **Automated Experimentation**: Autonomous quantum experiments
- **Circuit Design**: Automated quantum circuit construction
- **Problem Solving**: Solve complex chemistry and cryptography
- **Research Acceleration**: Speed up quantum research
- **Education**: Learn quantum computing through automation
- **Hardware Prep**: Prepare for quantum hardware boom
- **Bridging Gap**: Connect natural language to quantum mechanics

## 🛡️ Security & Trust

- **Trusted dependencies**: qiskit (9.2), pyyaml (7.4), click (8.8) - [Context7 verified](https://context7.com)
- **MIT License**: Open source, permissive
- **Local Simulation**: No external dependencies
- **Open Source**: Community-reviewed quantum logic
- **Educational**: Learn quantum computing
- **Safe**: Controlled environment

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/avasis-ai/quantum-agent-framework/wiki)
- **Issues**: [GitHub Issues](https://github.com/avasis-ai/quantum-agent-framework/issues)
- **Email**: quantum-agent@avasis.ai

## 🙏 Acknowledgments

- **Qiskit**: Quantum computing framework inspiration
- **OpenClaw**: Agent framework inspiration
- **IBM Quantum**: Quantum hardware inspiration
- **Quantum Researchers**: Theoretical foundations
- **Deep Tech Community**: Real-world requirements
- **Academic Community**: Daily feedback

---

**Made with ⚛️ by [Avasis AI](https://avasis.ai)**

*The essential open-source quantum agent framework. Autonomous agents orchestrating quantum computing experiments.*
