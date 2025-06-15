from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Optional
from datetime import datetime
import uuid

from app.models.agent import Agent, Workflow, AgentExecution
from app.core.browser_engine import BrowserAutomationEngine, BrowserAction
from app.schemas.agent import (
    AgentCreate,
    AgentUpdate,
    AgentResponse,
    WorkflowCreate,
    WorkflowResponse,
    ExecutionRequest,
    ExecutionResponse,
    ActionTestRequest,
    ActionTestResponse,
)

router = APIRouter()


@router.post("/agents", response_model=AgentResponse)
async def create_agent(agent: AgentCreate) -> AgentResponse:
    """Create a new agent"""
    agent_id = str(uuid.uuid4())
    new_agent = {
        "id": agent_id,
        "name": agent.name,
        "description": agent.description,
        "status": "draft",
        "configuration": agent.configuration,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    # TODO: Save to database
    return AgentResponse(**new_agent)


@router.get("/agents", response_model=List[AgentResponse])
async def list_agents(
    status: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
) -> List[AgentResponse]:
    """List all agents"""
    # TODO: Fetch from database with filters
    return []


@router.get("/agents/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: str) -> AgentResponse:
    """Get agent by ID"""
    # TODO: Fetch from database
    raise HTTPException(status_code=404, detail="Agent not found")


@router.put("/agents/{agent_id}", response_model=AgentResponse)
async def update_agent(agent_id: str, agent: AgentUpdate) -> AgentResponse:
    """Update agent"""
    # TODO: Update in database
    raise HTTPException(status_code=404, detail="Agent not found")


@router.delete("/agents/{agent_id}")
async def delete_agent(agent_id: str) -> dict:
    """Delete agent"""
    # TODO: Delete from database
    return {"message": "Agent deleted successfully"}


@router.post("/agents/{agent_id}/workflows", response_model=WorkflowResponse)
async def create_workflow(agent_id: str, workflow: WorkflowCreate) -> WorkflowResponse:
    """Create a workflow for an agent"""
    workflow_id = str(uuid.uuid4())
    new_workflow = {
        "id": workflow_id,
        "agent_id": agent_id,
        "name": workflow.name,
        "description": workflow.description,
        "actions": workflow.actions,
        "variables": workflow.variables,
        "triggers": workflow.triggers,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    # TODO: Save to database
    return WorkflowResponse(**new_workflow)


@router.get("/agents/{agent_id}/workflows", response_model=List[WorkflowResponse])
async def list_workflows(agent_id: str) -> List[WorkflowResponse]:
    """List workflows for an agent"""
    # TODO: Fetch from database
    return []


@router.post("/agents/{agent_id}/execute", response_model=ExecutionResponse)
async def execute_agent(
    agent_id: str,
    request: ExecutionRequest,
) -> ExecutionResponse:
    """Execute an agent workflow"""
    execution_id = str(uuid.uuid4())
    
    # Initialize browser engine
    engine = BrowserAutomationEngine()
    
    try:
        # Start browser session
        await engine.initialize()
        await engine.start_session(
            url=request.start_url,
            viewport=request.viewport,
            record_video=request.record_video,
        )
        
        # Execute workflow actions
        results = []
        for action_data in request.actions:
            action = BrowserAction(**action_data)
            result = await engine.execute_action(action)
            results.append(result.dict())
        
        return ExecutionResponse(
            id=execution_id,
            agent_id=agent_id,
            status="completed",
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow(),
            results=results,
        )
    
    except Exception as e:
        return ExecutionResponse(
            id=execution_id,
            agent_id=agent_id,
            status="failed",
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow(),
            error=str(e),
        )
    
    finally:
        await engine.close()


@router.get("/executions/{execution_id}", response_model=ExecutionResponse)
async def get_execution(execution_id: str) -> ExecutionResponse:
    """Get execution details"""
    # TODO: Fetch from database
    raise HTTPException(status_code=404, detail="Execution not found")


@router.post("/test-action", response_model=ActionTestResponse)
async def test_action(request: ActionTestRequest) -> ActionTestResponse:
    """Test a single browser action"""
    engine = BrowserAutomationEngine()
    
    try:
        await engine.initialize()
        await engine.start_session(url=request.url)
        
        action = BrowserAction(**request.action)
        result = await engine.execute_action(action)
        
        # Take screenshot after action
        screenshot_result = await engine.take_screenshot()
        
        return ActionTestResponse(
            success=result.success,
            result=result.data,
            error=result.error,
            screenshot=screenshot_result.screenshot if screenshot_result.success else None,
        )
    
    except Exception as e:
        return ActionTestResponse(
            success=False,
            error=str(e),
        )
    
    finally:
        await engine.close()


@router.post("/agents/preview")
async def preview_agent(request: dict) -> dict:
    """Preview agent in development mode"""
    agent = request.get("agent", {})
    mode = request.get("mode", "preview")
    
    engine = BrowserAutomationEngine()
    
    try:
        await engine.initialize()
        
        # Start browser session with target website
        if agent.get("targetWebsite"):
            await engine.start_session(url=agent["targetWebsite"])
        
        # Execute instructions sequentially
        results = []
        for instruction in agent.get("instructions", []):
            # Convert instruction to BrowserAction
            action_type = instruction["type"]
            action_data = {
                "type": action_type,
                "selector": instruction.get("selector"),
                "value": instruction.get("value"),
            }
            
            # Map instruction types to browser action types
            if action_type == "navigate":
                action_data["type"] = "navigate"
                action_data["url"] = instruction.get("value", agent.get("targetWebsite"))
            elif action_type == "wait":
                action_data["type"] = "wait"
                action_data["duration"] = instruction.get("value", 1000)
            
            action = BrowserAction(**action_data)
            result = await engine.execute_action(action)
            results.append({
                "instruction_id": instruction["id"],
                "success": result.success,
                "data": result.data,
                "error": result.error,
            })
        
        return {
            "success": True,
            "results": results,
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }
    
    finally:
        await engine.close()


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "version": "0.1.0",
    }