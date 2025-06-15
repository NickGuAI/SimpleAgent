from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum
from sqlalchemy import Column, String, JSON, DateTime, Boolean, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AgentStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    ARCHIVED = "archived"


class ActionType(str, Enum):
    NAVIGATE = "navigate"
    CLICK = "click"
    TYPE = "type"
    WAIT = "wait"
    EXTRACT = "extract"
    SCREENSHOT = "screenshot"
    EXECUTE_JS = "execute_js"
    CONDITIONAL = "conditional"
    LOOP = "loop"
    FILE_READ = "file_read"
    FILE_WRITE = "file_write"


class Agent(Base):
    __tablename__ = "agents"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default=AgentStatus.DRAFT)
    configuration = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    workflows = relationship("Workflow", back_populates="agent")
    executions = relationship("AgentExecution", back_populates="agent")


class Workflow(Base):
    __tablename__ = "workflows"
    
    id = Column(String, primary_key=True)
    agent_id = Column(String, ForeignKey("agents.id"))
    name = Column(String, nullable=False)
    description = Column(Text)
    actions = Column(JSON, default=[])
    variables = Column(JSON, default={})
    triggers = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    agent = relationship("Agent", back_populates="workflows")
    actions_list = relationship("WorkflowAction", back_populates="workflow")


class WorkflowAction(Base):
    __tablename__ = "workflow_actions"
    
    id = Column(String, primary_key=True)
    workflow_id = Column(String, ForeignKey("workflows.id"))
    action_type = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    selector = Column(JSON)
    value = Column(JSON)
    options = Column(JSON, default={})
    conditions = Column(JSON, default={})
    error_handling = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    workflow = relationship("Workflow", back_populates="actions_list")


class AgentExecution(Base):
    __tablename__ = "agent_executions"
    
    id = Column(String, primary_key=True)
    agent_id = Column(String, ForeignKey("agents.id"))
    workflow_id = Column(String, ForeignKey("workflows.id"))
    status = Column(String, default="pending")
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    error = Column(Text)
    results = Column(JSON, default={})
    logs = Column(JSON, default=[])
    screenshots = Column(JSON, default=[])
    
    # Relationships
    agent = relationship("Agent", back_populates="executions")
    steps = relationship("ExecutionStep", back_populates="execution")


class ExecutionStep(Base):
    __tablename__ = "execution_steps"
    
    id = Column(String, primary_key=True)
    execution_id = Column(String, ForeignKey("agent_executions.id"))
    action_id = Column(String, ForeignKey("workflow_actions.id"))
    status = Column(String, default="pending")
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    input_data = Column(JSON)
    output_data = Column(JSON)
    error = Column(Text)
    screenshot_path = Column(String)
    
    # Relationships
    execution = relationship("AgentExecution", back_populates="steps")


class FilePermission(Base):
    __tablename__ = "file_permissions"
    
    id = Column(String, primary_key=True)
    agent_id = Column(String, ForeignKey("agents.id"))
    directory_path = Column(String, nullable=False)
    permission_type = Column(String, nullable=False)  # read, write, list
    file_patterns = Column(JSON, default=["*"])
    max_depth = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)


class Schedule(Base):
    __tablename__ = "schedules"
    
    id = Column(String, primary_key=True)
    workflow_id = Column(String, ForeignKey("workflows.id"))
    cron_expression = Column(String)
    timezone = Column(String, default="UTC")
    enabled = Column(Boolean, default=True)
    next_run = Column(DateTime)
    last_run = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)