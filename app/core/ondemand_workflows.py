"""
On-Demand.io Workflow Integration - Hackathon Edition

3 Unique AI-Powered Workflows for Blockchain Security:

1. 🧬 SMART CONTRACT DNA PROFILER
   - Multi-agent collaborative analysis that creates a unique "DNA fingerprint" 
   - of any smart contract by analyzing code patterns, risk markers, and behavior

2. 🔮 PREDICTIVE EXPLOIT ORACLE
   - AI workflow that predicts potential future exploits by analyzing 
   - historical attack patterns and current contract vulnerabilities

3. 🌐 CROSS-CHAIN THREAT MESH
   - Multi-chain security analysis that identifies attack patterns 
   - spreading across different blockchain ecosystems

Uses On-Demand.io Workflow API for orchestrated multi-step AI analysis.
"""

import json
import os
import httpx
from typing import Optional, List, Dict, Any
from datetime import datetime
from app.config import get_settings


class OnDemandWorkflowManager:
    """
    Manages On-Demand.io Workflow executions for advanced blockchain analysis.
    
    Implements 3 unique workflow patterns that combine multiple AI agents
    in sophisticated analysis pipelines.
    """
    
    # On-Demand.io API Configuration
    WORKFLOW_BASE_URL = "https://api.on-demand.io/workflow"
    CHAT_BASE_URL = "https://api.on-demand.io/chat/v1"
    
    # Workflow IDs (to be created in On-Demand.io dashboard)
    WORKFLOW_IDS = {
        "dna_profiler": os.getenv("ONDEMAND_DNA_WORKFLOW_ID", ""),
        "exploit_oracle": os.getenv("ONDEMAND_ORACLE_WORKFLOW_ID", ""),
        "threat_mesh": os.getenv("ONDEMAND_MESH_WORKFLOW_ID", "")
    }
    
    # AI Model Endpoints
    ENDPOINTS = {
        "gpt4o": "predefined-openai-gpt4o",
        "claude": "predefined-anthropic-claude-sonnet",
        "grok": "predefined-xai-grok4.1-fast",
        "gemini": "predefined-google-gemini-2.0-flash"
    }
    
    # 3 Unique Workflow Definitions
    WORKFLOWS = {
        "dna_profiler": {
            "id": "dna_profiler",
            "name": "🧬 Smart Contract DNA Profiler",
            "tagline": "Genetic fingerprinting for blockchain code",
            "description": "Creates a unique genetic fingerprint of any smart contract by analyzing code patterns, vulnerability markers, gas efficiency genes, and behavioral DNA. Like 23andMe for smart contracts!",
            "icon": "🧬",
            "gradient": "linear-gradient(135deg, #00d4aa 0%, #00b894 50%, #00cec9 100%)",
            "steps": [
                {"agent": "Code Analyzer", "task": "Extract structural DNA"},
                {"agent": "Vulnerability Scanner", "task": "Identify risk markers"},
                {"agent": "Pattern Matcher", "task": "Match against known strains"},
                {"agent": "DNA Synthesizer", "task": "Generate unique fingerprint"}
            ],
            "output_format": {
                "dna_sequence": "string",
                "risk_markers": ["array"],
                "similarity_matches": ["array"],
                "mutation_probability": "number",
                "evolutionary_tree": "object"
            }
        },
        "exploit_oracle": {
            "id": "exploit_oracle",
            "name": "🔮 Predictive Exploit Oracle",
            "tagline": "See the future of smart contract attacks",
            "description": "AI-powered oracle that predicts potential future exploits by analyzing historical attack patterns, current vulnerabilities, and emerging threat vectors. Prevents attacks before they happen!",
            "icon": "🔮",
            "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)",
            "steps": [
                {"agent": "Historical Analyst", "task": "Analyze past exploits"},
                {"agent": "Vulnerability Mapper", "task": "Map current weaknesses"},
                {"agent": "Attack Simulator", "task": "Simulate attack vectors"},
                {"agent": "Future Predictor", "task": "Generate exploit predictions"}
            ],
            "output_format": {
                "predicted_exploits": ["array"],
                "attack_probability": "number",
                "time_to_exploit": "string",
                "prevention_steps": ["array"],
                "similar_past_attacks": ["array"]
            }
        },
        "threat_mesh": {
            "id": "threat_mesh",
            "name": "🌐 Cross-Chain Threat Mesh",
            "tagline": "Multi-dimensional blockchain security",
            "description": "Analyzes security across multiple blockchain ecosystems simultaneously, identifying attack patterns that spread across chains, bridge vulnerabilities, and cross-chain exploit vectors.",
            "icon": "🌐",
            "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ff6b6b 100%)",
            "steps": [
                {"agent": "Chain Analyzer", "task": "Scan multiple chains"},
                {"agent": "Bridge Inspector", "task": "Analyze cross-chain bridges"},
                {"agent": "Pattern Correlator", "task": "Correlate attack patterns"},
                {"agent": "Mesh Generator", "task": "Create threat mesh map"}
            ],
            "output_format": {
                "threat_map": "object",
                "chain_risk_scores": "object",
                "bridge_vulnerabilities": ["array"],
                "correlated_attacks": ["array"],
                "mesh_visualization": "object"
            }
        }
    }
    
    def __init__(self):
        """Initialize the workflow manager."""
        settings = get_settings()
        self.api_key = settings.ondemand_api_key
        self.sessions = {}
    
    async def _create_session(self) -> str:
        """Create a new chat session for workflow execution."""
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.CHAT_BASE_URL}/sessions",
                headers={"apikey": self.api_key},
                json={"pluginIds": [], "externalUserId": f"workflow-{datetime.now().timestamp()}"}
            )
            response.raise_for_status()
            data = response.json()
            return data["data"]["id"]
    
    async def _submit_query(self, session_id: str, query: str, endpoint: str = "gpt4o") -> Dict[str, Any]:
        """Submit a query to the AI model."""
        endpoint_id = self.ENDPOINTS.get(endpoint, self.ENDPOINTS["gpt4o"])
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{self.CHAT_BASE_URL}/sessions/{session_id}/query",
                headers={"apikey": self.api_key},
                json={
                    "endpointId": endpoint_id,
                    "query": query,
                    "pluginIds": ["plugin-1712327325", "plugin-1713962163"],
                    "responseMode": "sync"
                }
            )
            response.raise_for_status()
            return response.json()
    
    def get_all_workflows(self) -> List[Dict[str, Any]]:
        """Get all available workflow definitions."""
        return [
            {
                "id": w["id"],
                "name": w["name"],
                "tagline": w["tagline"],
                "description": w["description"],
                "icon": w["icon"],
                "gradient": w["gradient"],
                "steps": w["steps"]
            }
            for w in self.WORKFLOWS.values()
        ]
    
    def get_workflow(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific workflow definition."""
        return self.WORKFLOWS.get(workflow_id)
    
    async def execute_dna_profiler(self, contract_code: str, language: str = "move") -> Dict[str, Any]:
        """
        Execute the Smart Contract DNA Profiler workflow.
        
        Creates a unique genetic fingerprint of the contract by:
        1. Extracting structural patterns (code DNA)
        2. Identifying vulnerability markers (risk genes)
        3. Matching against known contract patterns
        4. Generating a unique DNA sequence
        """
        session_id = await self._create_session()
        workflow_data = self.WORKFLOWS["dna_profiler"]
        
        # Step 1: Extract Structural DNA
        step1_prompt = f"""You are a Smart Contract DNA Analyzer. Extract the structural DNA of this {language} smart contract.

Analyze and identify:
1. **Function Genes**: List all functions with their visibility and modifiers
2. **State Variables DNA**: All storage variables and their types
3. **Inheritance Chain**: Contract inheritance patterns
4. **Interaction Patterns**: External calls, events, modifiers
5. **Access Control Markers**: Permission patterns

Contract Code:
```{language}
{contract_code}
```

Respond in JSON format:
{{
    "function_genes": [...],
    "state_dna": [...],
    "inheritance_chain": [...],
    "interaction_patterns": [...],
    "access_markers": [...]
}}"""
        
        step1_result = await self._submit_query(session_id, step1_prompt, "gpt4o")
        
        # Step 2: Identify Risk Markers (Vulnerability Genes)
        step2_prompt = f"""You are a Vulnerability Gene Scanner. Based on the DNA extracted, identify RISK MARKERS (vulnerability genes) in this contract.

Previous DNA Analysis: {step1_result.get('data', {}).get('answer', '')}

Scan for these vulnerability genes:
1. **Reentrancy Gene (RG)**: Functions susceptible to reentrancy
2. **Overflow Gene (OG)**: Arithmetic without SafeMath
3. **Access Bypass Gene (ABG)**: Weak access controls
4. **Oracle Dependency Gene (ODG)**: External oracle risks
5. **Timestamp Gene (TG)**: Block timestamp dependencies
6. **Front-run Gene (FRG)**: MEV vulnerable patterns

Rate each gene: PRESENT (critical), LATENT (warning), ABSENT (safe)

Respond in JSON format:
{{
    "risk_markers": [
        {{"gene": "name", "status": "PRESENT|LATENT|ABSENT", "location": "...", "severity": 0-100}}
    ],
    "overall_risk_dna": 0-100
}}"""
        
        step2_result = await self._submit_query(session_id, step2_prompt, "claude")
        
        # Step 3: Pattern Matching (Find Similar Strains)
        step3_prompt = f"""You are a Contract Pattern Matcher. Match this contract's DNA against known contract patterns/strains.

Contract DNA Profile:
{step1_result.get('data', {}).get('answer', '')}

Risk Markers:
{step2_result.get('data', {}).get('answer', '')}

Identify similarities to:
1. **Known Safe Strains**: OpenZeppelin patterns, audited templates
2. **Known Exploit Strains**: Patterns from past hacks (DAO, Parity, etc.)
3. **DeFi Protocol Strains**: Uniswap, Compound, Aave patterns
4. **NFT Strains**: ERC721, ERC1155 patterns

Respond in JSON format:
{{
    "strain_matches": [
        {{"strain": "name", "similarity": 0-100, "type": "safe|risky|neutral", "description": "..."}}
    ],
    "closest_ancestor": "...",
    "mutation_from_standard": 0-100
}}"""
        
        step3_result = await self._submit_query(session_id, step3_prompt, "gemini")
        
        # Step 4: Generate Unique DNA Fingerprint
        step4_prompt = f"""You are a DNA Fingerprint Synthesizer. Generate a UNIQUE DNA FINGERPRINT for this smart contract.

Structural DNA: {step1_result.get('data', {}).get('answer', '')}
Risk Markers: {step2_result.get('data', {}).get('answer', '')}
Strain Matches: {step3_result.get('data', {}).get('answer', '')}

Create a unique DNA fingerprint that includes:
1. **DNA Sequence**: A unique hex-like sequence representing the contract (32 chars)
2. **Gene Map**: Visual representation of the contract's genetic makeup
3. **Risk Chromosome**: Summary of all risk genes
4. **Evolution Path**: Suggested improvements/mutations
5. **Compatibility Score**: How well it works with other contracts

Respond in JSON format:
{{
    "dna_sequence": "0xABCD1234...",
    "gene_map": {{
        "security": 0-100,
        "efficiency": 0-100,
        "complexity": 0-100,
        "standards_compliance": 0-100,
        "innovation": 0-100
    }},
    "risk_chromosome": {{
        "critical_genes": [...],
        "latent_genes": [...],
        "healthy_genes": [...]
    }},
    "evolution_recommendations": [...],
    "compatibility_score": 0-100,
    "overall_health": "HEALTHY|AT_RISK|CRITICAL"
}}"""
        
        step4_result = await self._submit_query(session_id, step4_prompt, "gpt4o")
        
        return {
            "workflow": workflow_data["name"],
            "workflow_id": "dna_profiler",
            "execution_time": datetime.now().isoformat(),
            "steps_completed": 4,
            "results": {
                "structural_dna": step1_result.get("data", {}).get("answer", ""),
                "risk_markers": step2_result.get("data", {}).get("answer", ""),
                "strain_matches": step3_result.get("data", {}).get("answer", ""),
                "dna_fingerprint": step4_result.get("data", {}).get("answer", "")
            },
            "session_id": session_id
        }
    
    async def execute_exploit_oracle(self, contract_code: str, language: str = "move") -> Dict[str, Any]:
        """
        Execute the Predictive Exploit Oracle workflow.
        
        Predicts potential future exploits by:
        1. Analyzing historical attack patterns
        2. Mapping current vulnerabilities
        3. Simulating attack vectors
        4. Generating exploit predictions
        """
        session_id = await self._create_session()
        workflow_data = self.WORKFLOWS["exploit_oracle"]
        
        # Step 1: Historical Attack Analysis
        step1_prompt = f"""You are a Blockchain Attack Historian. Analyze this {language} smart contract and identify patterns similar to HISTORICAL EXPLOITS.

Contract Code:
```{language}
{contract_code}
```

Compare against major historical exploits:
1. **The DAO Hack (2016)**: Reentrancy patterns
2. **Parity Wallet (2017)**: Library delegation issues
3. **bZx Flash Loan (2020)**: Flash loan attack vectors
4. **Cream Finance (2021)**: Oracle manipulation
5. **Wormhole Bridge (2022)**: Cross-chain vulnerabilities
6. **Ronin Bridge (2022)**: Validator compromise patterns
7. **FTX Collapse (2022)**: Centralization risks
8. **Euler Finance (2023)**: Donation attack patterns

Respond in JSON format:
{{
    "historical_similarities": [
        {{"exploit": "name", "similarity": 0-100, "matching_patterns": [...], "year": "YYYY"}}
    ],
    "high_risk_patterns": [...],
    "attack_surface_area": 0-100
}}"""
        
        step1_result = await self._submit_query(session_id, step1_prompt, "claude")
        
        # Step 2: Current Vulnerability Mapping
        step2_prompt = f"""You are a Vulnerability Cartographer. Create a detailed MAP of all current vulnerabilities in this contract.

Historical Analysis: {step1_result.get('data', {}).get('answer', '')}

Contract Code:
```{language}
{contract_code}
```

Map vulnerabilities by category:
1. **Access Control Vulnerabilities**: Missing checks, privilege escalation
2. **Arithmetic Vulnerabilities**: Overflow, underflow, precision loss
3. **Logic Vulnerabilities**: Business logic flaws, edge cases
4. **External Dependencies**: Oracle risks, external calls
5. **State Management**: Storage collisions, uninitialized storage
6. **Economic Vulnerabilities**: Flash loans, MEV, arbitrage

Respond in JSON format:
{{
    "vulnerability_map": [
        {{
            "id": "V001",
            "category": "...",
            "location": "function/line",
            "severity": "CRITICAL|HIGH|MEDIUM|LOW",
            "exploitability": 0-100,
            "description": "..."
        }}
    ],
    "total_vulnerabilities": 0,
    "exploitable_now": 0,
    "requires_conditions": 0
}}"""
        
        step2_result = await self._submit_query(session_id, step2_prompt, "gpt4o")
        
        # Step 3: Attack Simulation
        step3_prompt = f"""You are an Attack Simulator. Simulate potential attack scenarios against this contract.

Vulnerability Map: {step2_result.get('data', {}).get('answer', '')}
Historical Patterns: {step1_result.get('data', {}).get('answer', '')}

For each viable attack vector, simulate:
1. **Attack Preconditions**: What needs to be true for attack
2. **Attack Steps**: Step-by-step attack execution
3. **Required Resources**: Flash loans, gas, tokens needed
4. **Potential Profit**: Estimated extractable value
5. **Detection Difficulty**: How hard to detect in real-time

Respond in JSON format:
{{
    "simulated_attacks": [
        {{
            "attack_name": "...",
            "attack_type": "...",
            "preconditions": [...],
            "steps": [...],
            "required_capital": "...",
            "potential_profit": "...",
            "success_probability": 0-100,
            "detection_difficulty": "EASY|MEDIUM|HARD|STEALTH"
        }}
    ],
    "most_likely_attack": "...",
    "total_risk_value": "..."
}}"""
        
        step3_result = await self._submit_query(session_id, step3_prompt, "grok")
        
        # Step 4: Future Exploit Prediction
        step4_prompt = f"""You are the Predictive Exploit Oracle. Based on all analysis, PREDICT FUTURE EXPLOITS for this contract.

Historical Analysis: {step1_result.get('data', {}).get('answer', '')}
Vulnerability Map: {step2_result.get('data', {}).get('answer', '')}
Attack Simulations: {step3_result.get('data', {}).get('answer', '')}

Generate predictions for the next 30, 60, 90 days:

1. **Immediate Threats (0-30 days)**: High probability exploits
2. **Emerging Threats (30-60 days)**: Developing attack vectors
3. **Future Threats (60-90 days)**: Potential new techniques

Include:
- Probability of each exploit occurring
- Estimated time to exploit
- Prevention recommendations
- Monitoring suggestions

Respond in JSON format:
{{
    "predictions": {{
        "immediate": [
            {{
                "exploit": "...",
                "probability": 0-100,
                "estimated_date": "...",
                "impact": "CATASTROPHIC|SEVERE|MODERATE|LOW",
                "prevention": "..."
            }}
        ],
        "emerging": [...],
        "future": [...]
    }},
    "overall_forecast": {{
        "exploit_probability_30d": 0-100,
        "exploit_probability_60d": 0-100,
        "exploit_probability_90d": 0-100,
        "recommended_actions": [...],
        "monitoring_priority": "CRITICAL|HIGH|MEDIUM|LOW"
    }},
    "oracle_confidence": 0-100
}}"""
        
        step4_result = await self._submit_query(session_id, step4_prompt, "gpt4o")
        
        return {
            "workflow": workflow_data["name"],
            "workflow_id": "exploit_oracle",
            "execution_time": datetime.now().isoformat(),
            "steps_completed": 4,
            "results": {
                "historical_analysis": step1_result.get("data", {}).get("answer", ""),
                "vulnerability_map": step2_result.get("data", {}).get("answer", ""),
                "attack_simulations": step3_result.get("data", {}).get("answer", ""),
                "exploit_predictions": step4_result.get("data", {}).get("answer", "")
            },
            "session_id": session_id
        }
    
    async def execute_threat_mesh(self, contract_code: str, language: str = "move", chains: List[str] = None) -> Dict[str, Any]:
        """
        Execute the Cross-Chain Threat Mesh workflow.
        
        Analyzes security across multiple blockchain ecosystems by:
        1. Scanning contract across multiple chain contexts
        2. Analyzing bridge vulnerabilities
        3. Correlating cross-chain attack patterns
        4. Generating a threat mesh visualization
        """
        session_id = await self._create_session()
        workflow_data = self.WORKFLOWS["threat_mesh"]
        chains = chains or ["aptos", "ethereum", "solana", "sui", "arbitrum"]
        
        # Step 1: Multi-Chain Analysis
        step1_prompt = f"""You are a Multi-Chain Security Analyst. Analyze this contract in the context of MULTIPLE BLOCKCHAIN ECOSYSTEMS.

Contract Code ({language}):
```{language}
{contract_code}
```

Analyze for compatibility and risks on these chains: {', '.join(chains)}

For each chain context, evaluate:
1. **Native Compatibility**: How well it fits the chain's paradigm
2. **Chain-Specific Risks**: Unique vulnerabilities per chain
3. **Gas/Resource Costs**: Efficiency on each chain
4. **Security Model Fit**: Match with chain's security assumptions

Respond in JSON format:
{{
    "chain_analysis": {{
        "aptos": {{"compatibility": 0-100, "risks": [...], "efficiency": 0-100}},
        "ethereum": {{"compatibility": 0-100, "risks": [...], "efficiency": 0-100}},
        "solana": {{"compatibility": 0-100, "risks": [...], "efficiency": 0-100}},
        "sui": {{"compatibility": 0-100, "risks": [...], "efficiency": 0-100}},
        "arbitrum": {{"compatibility": 0-100, "risks": [...], "efficiency": 0-100}}
    }},
    "best_fit_chain": "...",
    "worst_fit_chain": "...",
    "cross_chain_deployment_risk": 0-100
}}"""
        
        step1_result = await self._submit_query(session_id, step1_prompt, "gpt4o")
        
        # Step 2: Bridge Vulnerability Analysis
        step2_prompt = f"""You are a Cross-Chain Bridge Security Expert. Analyze potential BRIDGE VULNERABILITIES if this contract were to interact with cross-chain bridges.

Multi-Chain Analysis: {step1_result.get('data', {}).get('answer', '')}

Contract Code:
```{language}
{contract_code}
```

Analyze bridge risks for:
1. **Message Passing Vulnerabilities**: How messages could be spoofed
2. **Validator Risks**: Centralization points in bridge validation
3. **Replay Attacks**: Cross-chain replay possibilities
4. **Liquidity Risks**: Bridge liquidity manipulation
5. **Oracle Bridge Risks**: Price oracle manipulation across chains

Major bridges to consider:
- LayerZero, Wormhole, Axelar, Multichain, Stargate

Respond in JSON format:
{{
    "bridge_vulnerabilities": [
        {{
            "bridge": "...",
            "vulnerability_type": "...",
            "risk_level": "CRITICAL|HIGH|MEDIUM|LOW",
            "attack_scenario": "...",
            "mitigation": "..."
        }}
    ],
    "safest_bridge": "...",
    "bridge_recommendations": [...],
    "cross_chain_risk_score": 0-100
}}"""
        
        step2_result = await self._submit_query(session_id, step2_prompt, "claude")
        
        # Step 3: Attack Pattern Correlation
        step3_prompt = f"""You are a Cross-Chain Attack Pattern Analyst. Identify CORRELATED ATTACK PATTERNS that could spread across chains.

Chain Analysis: {step1_result.get('data', {}).get('answer', '')}
Bridge Analysis: {step2_result.get('data', {}).get('answer', '')}

Identify:
1. **Coordinated Attacks**: Multi-chain synchronized exploits
2. **Chain Hopping**: Using one chain to attack another
3. **Arbitrage Exploits**: Cross-chain price manipulation
4. **Governance Attacks**: Voting across chains
5. **Liquidity Drain**: Multi-chain liquidity extraction

Reference real attacks:
- Wormhole ($320M), Ronin ($600M), Nomad ($190M), Multichain ($126M)

Respond in JSON format:
{{
    "correlated_patterns": [
        {{
            "pattern_name": "...",
            "chains_involved": [...],
            "attack_flow": [...],
            "historical_example": "...",
            "current_applicability": 0-100
        }}
    ],
    "highest_correlation": {{
        "chains": [...],
        "attack_type": "...",
        "probability": 0-100
    }},
    "multi_chain_risk_matrix": {{}}
}}"""
        
        step3_result = await self._submit_query(session_id, step3_prompt, "grok")
        
        # Step 4: Generate Threat Mesh Map
        step4_prompt = f"""You are a Threat Mesh Architect. Generate a comprehensive THREAT MESH MAP showing interconnected risks across all analyzed chains.

Chain Analysis: {step1_result.get('data', {}).get('answer', '')}
Bridge Vulnerabilities: {step2_result.get('data', {}).get('answer', '')}
Correlated Patterns: {step3_result.get('data', {}).get('answer', '')}

Create a threat mesh that shows:
1. **Nodes**: Each chain as a node with risk score
2. **Edges**: Connections between chains (bridges, protocols)
3. **Threat Flows**: How attacks could propagate
4. **Hot Spots**: Highest risk intersection points
5. **Safe Zones**: Recommended isolation points

Respond in JSON format:
{{
    "threat_mesh": {{
        "nodes": [
            {{"chain": "...", "risk_score": 0-100, "threats": [...], "color": "hex"}}
        ],
        "edges": [
            {{"from": "...", "to": "...", "bridge": "...", "risk": 0-100, "threat_flow": "..."}}
        ],
        "hotspots": [
            {{"location": "...", "severity": "...", "connected_chains": [...]}}
        ]
    }},
    "mesh_summary": {{
        "total_risk_score": 0-100,
        "most_vulnerable_path": [...],
        "recommended_isolation": [...],
        "monitoring_priorities": [...]
    }},
    "visualization_data": {{
        "center_node": "...",
        "layout": "force-directed",
        "color_scheme": {{}}
    }}
}}"""
        
        step4_result = await self._submit_query(session_id, step4_prompt, "gemini")
        
        return {
            "workflow": workflow_data["name"],
            "workflow_id": "threat_mesh",
            "execution_time": datetime.now().isoformat(),
            "steps_completed": 4,
            "chains_analyzed": chains,
            "results": {
                "chain_analysis": step1_result.get("data", {}).get("answer", ""),
                "bridge_vulnerabilities": step2_result.get("data", {}).get("answer", ""),
                "correlated_patterns": step3_result.get("data", {}).get("answer", ""),
                "threat_mesh": step4_result.get("data", {}).get("answer", "")
            },
            "session_id": session_id
        }
    
    async def execute_workflow(self, workflow_id: str, contract_code: str, language: str = "move", **kwargs) -> Dict[str, Any]:
        """Execute a workflow by ID."""
        if workflow_id == "dna_profiler":
            return await self.execute_dna_profiler(contract_code, language)
        elif workflow_id == "exploit_oracle":
            return await self.execute_exploit_oracle(contract_code, language)
        elif workflow_id == "threat_mesh":
            chains = kwargs.get("chains", ["aptos", "ethereum", "solana", "sui", "arbitrum"])
            return await self.execute_threat_mesh(contract_code, language, chains)
        else:
            raise ValueError(f"Unknown workflow: {workflow_id}")


# Global instance
workflow_manager = OnDemandWorkflowManager()
