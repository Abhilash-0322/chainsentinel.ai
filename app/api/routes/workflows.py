"""
Workflow API Routes - On-Demand.io Workflow Integration

Provides endpoints for executing the 3 unique AI workflows:
1. Smart Contract DNA Profiler
2. Predictive Exploit Oracle
3. Cross-Chain Threat Mesh
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from app.core.ondemand_workflows import workflow_manager

router = APIRouter(prefix="/api/workflows", tags=["workflows"])


class WorkflowExecuteRequest(BaseModel):
    """Request model for workflow execution."""
    contract_code: str
    language: str = "move"
    chains: Optional[List[str]] = None  # For threat_mesh workflow


class WorkflowResponse(BaseModel):
    """Response model for workflow results."""
    success: bool
    workflow_id: str
    workflow_name: str
    execution_time: str
    steps_completed: int
    results: dict
    error: Optional[str] = None


@router.get("/")
async def list_workflows():
    """
    List all available AI workflows.
    
    Returns the 3 unique On-Demand.io powered workflows:
    - DNA Profiler: Genetic fingerprinting for smart contracts
    - Exploit Oracle: Predictive future exploit analysis
    - Threat Mesh: Cross-chain security analysis
    """
    workflows = workflow_manager.get_all_workflows()
    return {
        "success": True,
        "workflows": workflows,
        "total": len(workflows)
    }


@router.get("/{workflow_id}")
async def get_workflow(workflow_id: str):
    """Get details of a specific workflow."""
    workflow = workflow_manager.get_workflow(workflow_id)
    if not workflow:
        raise HTTPException(status_code=404, detail=f"Workflow '{workflow_id}' not found")
    return {
        "success": True,
        "workflow": workflow
    }


@router.post("/{workflow_id}/execute")
async def execute_workflow(workflow_id: str, request: WorkflowExecuteRequest):
    """
    Execute a specific AI workflow on the provided smart contract.
    
    Workflows:
    - dna_profiler: Creates a unique DNA fingerprint of the contract
    - exploit_oracle: Predicts potential future exploits
    - threat_mesh: Analyzes cross-chain security risks
    
    Each workflow uses multiple AI agents in sequence for deep analysis.
    """
    workflow = workflow_manager.get_workflow(workflow_id)
    if not workflow:
        raise HTTPException(status_code=404, detail=f"Workflow '{workflow_id}' not found")
    
    if not request.contract_code or len(request.contract_code.strip()) < 10:
        raise HTTPException(status_code=400, detail="Contract code is required and must be substantial")
    
    try:
        result = await workflow_manager.execute_workflow(
            workflow_id=workflow_id,
            contract_code=request.contract_code,
            language=request.language,
            chains=request.chains
        )
        
        return {
            "success": True,
            "workflow_id": workflow_id,
            "workflow_name": workflow["name"],
            "execution_time": result["execution_time"],
            "steps_completed": result["steps_completed"],
            "results": result["results"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow execution failed: {str(e)}")


@router.post("/dna-profiler")
async def run_dna_profiler(request: WorkflowExecuteRequest):
    """
    🧬 Smart Contract DNA Profiler
    
    Creates a unique genetic fingerprint of any smart contract by analyzing:
    - Code patterns (Function Genes)
    - Vulnerability markers (Risk Genes)
    - Pattern matching (Strain Identification)
    - Unique DNA sequence generation
    """
    try:
        result = await workflow_manager.execute_dna_profiler(
            contract_code=request.contract_code,
            language=request.language
        )
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DNA Profiler failed: {str(e)}")


@router.post("/exploit-oracle")
async def run_exploit_oracle(request: WorkflowExecuteRequest):
    """
    🔮 Predictive Exploit Oracle
    
    AI-powered oracle that predicts potential future exploits by:
    - Analyzing historical attack patterns
    - Mapping current vulnerabilities
    - Simulating attack vectors
    - Generating time-based exploit predictions
    """
    try:
        result = await workflow_manager.execute_exploit_oracle(
            contract_code=request.contract_code,
            language=request.language
        )
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exploit Oracle failed: {str(e)}")


@router.post("/threat-mesh")
async def run_threat_mesh(request: WorkflowExecuteRequest):
    """
    🌐 Cross-Chain Threat Mesh
    
    Multi-dimensional security analysis across blockchain ecosystems:
    - Scans contract for multi-chain compatibility
    - Analyzes bridge vulnerabilities
    - Correlates cross-chain attack patterns
    - Generates threat mesh visualization data
    """
    chains = request.chains or ["aptos", "ethereum", "solana", "sui", "arbitrum"]
    
    try:
        result = await workflow_manager.execute_threat_mesh(
            contract_code=request.contract_code,
            language=request.language,
            chains=chains
        )
        return {"success": True, **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Threat Mesh failed: {str(e)}")


@router.get("/health")
async def workflows_health():
    """Check workflow system health."""
    return {
        "status": "healthy",
        "workflows_available": 3,
        "api_connected": True
    }
