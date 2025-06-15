from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class AgentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    configuration: Dict[str, Any] = Field(default_factory=dict)


class AgentCreate(AgentBase):
    pass


class AgentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    configuration: Optional[Dict[str, Any]] = None
    status: Optional[str] = None


class AgentResponse(AgentBase):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class WorkflowBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    actions: List[Dict[str, Any]] = Field(default_factory=list)
    variables: Dict[str, Any] = Field(default_factory=dict)
    triggers: Dict[str, Any] = Field(default_factory=dict)


class WorkflowCreate(WorkflowBase):
    pass


class WorkflowResponse(WorkflowBase):
    id: str
    agent_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ExecutionRequest(BaseModel):
    workflow_id: Optional[str] = None
    actions: List[Dict[str, Any]] = Field(..., min_items=1)
    start_url: Optional[str] = None
    variables: Dict[str, Any] = Field(default_factory=dict)
    viewport: Optional[Dict[str, int]] = None
    record_video: bool = False


class ExecutionResponse(BaseModel):
    id: str
    agent_id: str
    workflow_id: Optional[str] = None
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    results: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None
    logs: List[str] = Field(default_factory=list)
    screenshots: List[str] = Field(default_factory=list)

    class Config:
        from_attributes = True


class ActionTestRequest(BaseModel):
    url: str
    action: Dict[str, Any]
    viewport: Optional[Dict[str, int]] = None


class ActionTestResponse(BaseModel):
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    screenshot: Optional[str] = None