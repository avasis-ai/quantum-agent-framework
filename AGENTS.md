# AGENTS.md - Quantum Agent Framework

## Your Quantum Computing Agent

This is **Quantum Agent Framework** - autonomous agents orchestrating quantum computing experiments. Here's what you need to know:

### What It Does

- **Quantum Circuit Construction**: Build and manage quantum circuits
- **Gate Operations**: Support for all basic quantum gates
- **Agent Orchestration**: Autonomous quantum computing agents
- **Qiskit Integration**: Interface with Qiskit simulators and backends
- **Circuit Optimization**: Automatically optimize quantum circuits

### Key Components

1. **QiskitBridge** - Quantum circuit construction
2. **QuantumAgent** - Autonomous quantum computing agent
3. **QuantumAgentFramework** - Multi-agent orchestration
4. **Quantum Gates** - H, X, Y, Z, CNOT, CZ, SWAP, T, S, etc.

### Usage

```bash
# Check version
quantum-agent --version

# Initialize framework
quantum-agent init --name quantum_lab

# Run quantum experiment
quantum-agent experiment --agent quantum_researcher --qubits 2

# Run demo
quantum-agent demo
```

### Development Notes

- **Dependencies**: qiskit (9.2), pyyaml (7.4), click (8.8) - Context7 verified
- **License**: MIT
- **Tests**: `pytest tests/ -v`
- **CLI Entry Point**: `quantum-agent`

### Vision

Represents the absolute bleeding edge of technology (AI + Quantum). Generates massive academic and research appeal. Prepares developers for the upcoming quantum hardware boom.

### Quick Start

```python
from quantum_agent_framework.qiskit_bridge import QiskitBridge, QuantumGate
from quantum_agent_framework.agent import QuantumAgentFramework

framework = QuantumAgentFramework()
agent = framework.create_agent("quantum_researcher")

bridge = QiskitBridge()
circuit_id = bridge.create_circuit("coin_flip", 2, "Test")
bridge.add_gate(circuit_id, QuantumGate.H, [0])
bridge.add_gate(circuit_id, QuantumGate.CNOT, [0, 1])
```

---

*The essential open-source quantum agent framework. Autonomous agents orchestrating quantum computing experiments.*
