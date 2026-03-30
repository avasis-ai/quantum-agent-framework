"""Quantum agent for orchestrating quantum computing experiments."""

from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import threading


class AgentState(Enum):
    """State of the quantum agent."""
    IDLE = "idle"
    PLANNING = "planning"
    EXECUTING = "executing"
    OPTIMIZING = "optimizing"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class QuantumSkill:
    """Represents a quantum skill for the agent."""
    skill_id: str
    name: str
    description: str
    skill_type: str
    capabilities: List[str]
    confidence: float
    version: str
    created_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "skill_id": self.skill_id,
            "name": self.name,
            "description": self.description,
            "skill_type": self.skill_type,
            "capabilities": self.capabilities,
            "confidence": self.confidence,
            "version": self.version,
            "created_at": self.created_at.isoformat()
        }


@dataclass
class AgentTask:
    """Represents a task for the quantum agent."""
    task_id: str
    description: str
    target_problem: str
    num_qubits: int
    success: bool
    duration_ms: float
    timestamp: datetime
    result: Optional[Dict[str, Any]]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "task_id": self.task_id,
            "description": self.description,
            "target_problem": self.target_problem,
            "num_qubits": self.num_qubits,
            "success": self.success,
            "duration_ms": self.duration_ms,
            "timestamp": self.timestamp.isoformat(),
            "result": str(self.result)[:100] if self.result else None
        }


class QuantumAgent:
    """Autonomous agent for quantum computing experiments."""
    
    def __init__(self, agent_name: str = "quantum_agent"):
        """
        Initialize quantum agent.
        
        Args:
            agent_name: Agent name
        """
        self._agent_name = agent_name
        self._state = AgentState.IDLE
        self._skills: Dict[str, QuantumSkill] = {}
        self._tasks: List[AgentTask] = []
        self._lock = threading.RLock()
        self._task_counter = 0
    
    def set_state(self, state: AgentState) -> bool:
        """
        Set agent state.
        
        Args:
            state: New state
            
        Returns:
            True if state changed
        """
        with self._lock:
            if self._state == state:
                return False
            
            self._state = state
            return True
    
    def get_state(self) -> AgentState:
        """
        Get current agent state.
        
        Returns:
            Current state
        """
        with self._lock:
            return self._state
    
    def register_skill(self, skill: QuantumSkill) -> bool:
        """
        Register a quantum skill.
        
        Args:
            skill: Skill to register
            
        Returns:
            True if registered successfully
        """
        with self._lock:
            self._skills[skill.skill_id] = skill
            return True
    
    def get_skill(self, skill_id: str) -> Optional[QuantumSkill]:
        """
        Get a skill by ID.
        
        Args:
            skill_id: Skill ID
            
        Returns:
            QuantumSkill or None
        """
        return self._skills.get(skill_id)
    
    def list_skills(self, skill_type: Optional[str] = None) -> List[QuantumSkill]:
        """
        List all skills.
        
        Args:
            skill_type: Optional type filter
            
        Returns:
            List of QuantumSkills
        """
        if skill_type:
            return [
                s for s in self._skills.values()
                if s.skill_type == skill_type
            ]
        return list(self._skills.values())
    
    def execute_task(
        self,
        description: str,
        target_problem: str,
        num_qubits: int,
        skill_id: Optional[str] = None
    ) -> Optional[AgentTask]:
        """
        Execute a quantum computing task.
        
        Args:
            description: Task description
            target_problem: Problem to solve
            num_qubits: Number of qubits
            skill_id: Optional skill to use
            
        Returns:
            AgentTask or None
        """
        with self._lock:
            self._task_counter += 1
            task_id = f"task_{self._task_counter}"
        
        import time
        start_time = time.time()
        
        try:
            with self._lock:
                self.set_state(AgentState.EXECUTING)
            
            # Simulate task execution
            result = {
                "solution": f"Quantum solution for {target_problem}",
                "num_qubits": num_qubits,
                "confidence": 0.9
            }
            
            duration_ms = (time.time() - start_time) * 1000
            
            task = AgentTask(
                task_id=task_id,
                description=description,
                target_problem=target_problem,
                num_qubits=num_qubits,
                success=True,
                duration_ms=duration_ms,
                timestamp=datetime.now(),
                result=result
            )
            
            with self._lock:
                self._tasks.append(task)
                self.set_state(AgentState.COMPLETED)
            
            return task
            
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            
            task = AgentTask(
                task_id=task_id,
                description=description,
                target_problem=target_problem,
                num_qubits=num_qubits,
                success=False,
                duration_ms=duration_ms,
                timestamp=datetime.now(),
                result={"error": str(e)}
            )
            
            with self._lock:
                self._tasks.append(task)
                self.set_state(AgentState.ERROR)
            
            return task
    
    def get_tasks(self, success_only: bool = False) -> List[AgentTask]:
        """
        Get task history.
        
        Args:
            success_only: Only successful tasks
            
        Returns:
            List of AgentTasks
        """
        with self._lock:
            if success_only:
                return [t for t in self._tasks if t.success]
            return self._tasks.copy()
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get agent statistics.
        
        Returns:
            Dictionary of statistics
        """
        total_tasks = len(self._tasks)
        successful_tasks = len([
            t for t in self._tasks
            if t.success
        ])
        
        avg_duration = 0.0
        if total_tasks > 0:
            avg_duration = sum(t.duration_ms for t in self._tasks) / total_tasks
        
        return {
            "agent_name": self._agent_name,
            "state": self._state.value,
            "total_skills": len(self._skills),
            "total_tasks": total_tasks,
            "successful_tasks": successful_tasks,
            "success_rate": successful_tasks / total_tasks if total_tasks > 0 else 0.0,
            "avg_duration_ms": avg_duration
        }


class QuantumAgentFramework:
    """Framework for orchestrating quantum agent experiments."""
    
    def __init__(self, framework_name: str = "quantum_framework"):
        """
        Initialize quantum agent framework.
        
        Args:
            framework_name: Framework name
        """
        self._framework_name = framework_name
        self._agents: Dict[str, QuantumAgent] = {}
        self._lock = threading.RLock()
    
    def create_agent(self, agent_name: str) -> QuantumAgent:
        """
        Create a new quantum agent.
        
        Args:
            agent_name: Agent name
            
        Returns:
            QuantumAgent
        """
        agent = QuantumAgent(agent_name)
        
        with self._lock:
            self._agents[agent_name] = agent
        
        return agent
    
    def get_agent(self, agent_name: str) -> Optional[QuantumAgent]:
        """
        Get an agent by name.
        
        Args:
            agent_name: Agent name
            
        Returns:
            QuantumAgent or None
        """
        return self._agents.get(agent_name)
    
    def list_agents(self) -> List[QuantumAgent]:
        """
        List all agents.
        
        Returns:
            List of QuantumAgents
        """
        return list(self._agents.values())
    
    def execute_experiment(
        self,
        agent_name: str,
        description: str,
        target_problem: str,
        num_qubits: int
    ) -> Optional[AgentTask]:
        """
        Execute a quantum experiment.
        
        Args:
            agent_name: Agent name
            description: Experiment description
            target_problem: Problem to solve
            num_qubits: Number of qubits
            
        Returns:
            AgentTask or None
        """
        agent = self.get_agent(agent_name)
        if not agent:
            return None
        
        return agent.execute_task(description, target_problem, num_qubits)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get framework statistics.
        
        Returns:
            Dictionary of statistics
        """
        all_stats = [a.get_statistics() for a in self._agents.values()]
        
        total_agents = len(self._agents)
        total_tasks = sum(s['total_tasks'] for s in all_stats)
        total_success = sum(s['successful_tasks'] for s in all_stats)
        
        return {
            "framework_name": self._framework_name,
            "total_agents": total_agents,
            "total_tasks": total_tasks,
            "total_success": total_success,
            "overall_success_rate": total_success / total_tasks if total_tasks > 0 else 0.0
        }
