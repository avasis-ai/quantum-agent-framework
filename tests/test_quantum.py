"""Tests for Quantum Agent Framework."""

import pytest
import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from quantum_agent_framework.qiskit_bridge import (
    QiskitBridge,
    QuantumCircuit,
    QuantumGate,
    QubitConfiguration
)
from quantum_agent_framework.agent import (
    QuantumAgent,
    QuantumAgentFramework,
    QuantumSkill,
    AgentState,
    AgentTask
)


class TestQuantumGate:
    """Tests for QuantumGate enum."""
    
    def test_gate_values(self):
        """Test quantum gate enum values."""
        assert QuantumGate.H.value == "h"
        assert QuantumGate.CNOT.value == "cx"


class TestQubitConfiguration:
    """Tests for QubitConfiguration."""
    
    def test_config_creation(self):
        """Test creating a qubit configuration."""
        config = QubitConfiguration(
            qubit_id="q0",
            initial_state="|0>",
            connected_qubits=["q1"],
            measurement_order=0
        )
        
        assert config.qubit_id == "q0"
        assert config.initial_state == "|0>"


class TestQuantumCircuit:
    """Tests for QuantumCircuit."""
    
    def test_circuit_creation(self):
        """Test creating a quantum circuit."""
        circuit = QuantumCircuit(
            circuit_id="circuit_001",
            name="Test Circuit",
            num_qubits=2,
            num_clbits=2,
            gates=[],
            measurement_ops=[],
            optimized=False,
            confidence_score=1.0,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        assert circuit.circuit_id == "circuit_001"
        assert circuit.num_qubits == 2
        assert not circuit.optimized
    
    def test_to_dict(self):
        """Test converting circuit to dictionary."""
        circuit = QuantumCircuit(
            circuit_id="circuit_002",
            name="Another Circuit",
            num_qubits=3,
            num_clbits=3,
            gates=[{"gate": "h", "qubits": [0]}],
            measurement_ops=[],
            optimized=True,
            confidence_score=0.95,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        data = circuit.to_dict()
        
        assert data['circuit_id'] == "circuit_002"
        assert data['optimized'] is True


class TestQuantumAgent:
    """Tests for QuantumAgent."""
    
    def test_agent_initialization(self):
        """Test agent initialization."""
        agent = QuantumAgent("test_agent")
        
        assert agent._agent_name == "test_agent"
        assert agent.get_state() == AgentState.IDLE
        assert len(agent._skills) == 0
    
    def test_set_state(self):
        """Test setting agent state."""
        agent = QuantumAgent()
        
        result = agent.set_state(AgentState.PLANNING)
        
        assert result is True
        assert agent.get_state() == AgentState.PLANNING
    
    def test_register_skill(self):
        """Test registering a skill."""
        agent = QuantumAgent()
        
        skill = QuantumSkill(
            skill_id="skill_001",
            name="Test Skill",
            description="Test description",
            skill_type="gate_operation",
            capabilities=["hadamard"],
            confidence=0.95,
            version="1.0.0",
            created_at=datetime.now()
        )
        
        result = agent.register_skill(skill)
        
        assert result is True
        assert agent.get_skill("skill_001") is not None
    
    def test_get_skill(self):
        """Test getting a skill."""
        agent = QuantumAgent()
        
        skill = QuantumSkill(
            skill_id="skill_002",
            name="Another Skill",
            description="Another description",
            skill_type="optimization",
            capabilities=["circuit_simplify"],
            confidence=0.9,
            version="1.0.0",
            created_at=datetime.now()
        )
        
        agent.register_skill(skill)
        
        retrieved = agent.get_skill("skill_002")
        
        assert retrieved is not None
        assert retrieved.name == "Another Skill"
    
    def test_execute_task(self):
        """Test executing a task."""
        agent = QuantumAgent()
        
        task = agent.execute_task(
            description="Test task",
            target_problem="quantum_simulation",
            num_qubits=2
        )
        
        assert task is not None
        assert task.success is True
        assert task.num_qubits == 2
        assert len(agent.get_tasks()) == 1
    
    def test_execute_task_failure(self):
        """Test executing task with failure."""
        agent = QuantumAgent()
        
        task = agent.execute_task(
            description="Failing task",
            target_problem="error_test",
            num_qubits=1
        )
        
        assert task is not None
    
    def test_get_tasks_success_only(self):
        """Test getting tasks with success filter."""
        agent = QuantumAgent()
        
        agent.execute_task("Task 1", "problem_1", 2)
        agent.execute_task("Task 2", "problem_2", 3)
        
        success_tasks = agent.get_tasks(success_only=True)
        
        assert len(success_tasks) == 2
    
    def test_get_statistics(self):
        """Test getting agent statistics."""
        agent = QuantumAgent()
        
        agent.execute_task("Task 1", "problem_1", 2)
        agent.execute_task("Task 2", "problem_2", 3)
        
        stats = agent.get_statistics()
        
        assert stats['total_tasks'] == 2
        assert 'success_rate' in stats


class TestQuantumAgentFramework:
    """Tests for QuantumAgentFramework."""
    
    def test_framework_initialization(self):
        """Test framework initialization."""
        framework = QuantumAgentFramework("test_framework")
        
        assert framework._framework_name == "test_framework"
        assert len(framework._agents) == 0
    
    def test_create_agent(self):
        """Test creating an agent."""
        framework = QuantumAgentFramework()
        
        agent = framework.create_agent("quantum_researcher")
        
        assert agent._agent_name == "quantum_researcher"
        assert framework.get_agent("quantum_researcher") is not None
    
    def test_list_agents(self):
        """Test listing agents."""
        framework = QuantumAgentFramework()
        
        framework.create_agent("agent_1")
        framework.create_agent("agent_2")
        
        agents = framework.list_agents()
        
        assert len(agents) == 2
    
    def test_execute_experiment(self):
        """Test executing an experiment."""
        framework = QuantumAgentFramework()
        
        framework.create_agent("quantum_researcher")
        
        task = framework.execute_experiment(
            agent_name="quantum_researcher",
            description="Test experiment",
            target_problem="quantum_simulation",
            num_qubits=2
        )
        
        assert task is not None
        assert task.success is True
    
    def test_execute_experiment_invalid_agent(self):
        """Test executing experiment with invalid agent."""
        framework = QuantumAgentFramework()
        
        task = framework.execute_experiment(
            agent_name="nonexistent_agent",
            description="Test experiment",
            target_problem="quantum_simulation",
            num_qubits=2
        )
        
        assert task is None
    
    def test_get_statistics(self):
        """Test getting framework statistics."""
        framework = QuantumAgentFramework()
        
        framework.create_agent("agent_1")
        framework.create_agent("agent_2")
        
        framework.execute_experiment("agent_1", "Task 1", "problem_1", 2)
        framework.execute_experiment("agent_2", "Task 2", "problem_2", 3)
        
        stats = framework.get_statistics()
        
        assert stats['total_agents'] == 2
        assert stats['total_tasks'] == 2
        assert 'overall_success_rate' in stats
