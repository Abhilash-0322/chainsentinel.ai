'use client';

import { useState } from 'react';
import Navbar from '@/components/ui/Navbar';
import './workflows.css';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Workflow definitions
const WORKFLOWS = [
  {
    id: 'dna_profiler',
    name: '🧬 Smart Contract DNA Profiler',
    tagline: 'Genetic fingerprinting for blockchain code',
    description: 'Creates a unique genetic fingerprint of any smart contract by analyzing code patterns, vulnerability markers, gas efficiency genes, and behavioral DNA. Like 23andMe for smart contracts!',
    icon: '🧬',
    gradient: 'linear-gradient(135deg, #00d4aa 0%, #00b894 50%, #00cec9 100%)',
    accentColor: '#00d4aa',
    steps: [
      { agent: 'Code Analyzer', task: 'Extract structural DNA', icon: '🔬' },
      { agent: 'Vulnerability Scanner', task: 'Identify risk markers', icon: '⚠️' },
      { agent: 'Pattern Matcher', task: 'Match against known strains', icon: '🧪' },
      { agent: 'DNA Synthesizer', task: 'Generate unique fingerprint', icon: '🧬' }
    ],
    outputSections: ['Structural DNA', 'Risk Markers', 'Strain Matches', 'DNA Fingerprint']
  },
  {
    id: 'exploit_oracle',
    name: '🔮 Predictive Exploit Oracle',
    tagline: 'See the future of smart contract attacks',
    description: 'AI-powered oracle that predicts potential future exploits by analyzing historical attack patterns, current vulnerabilities, and emerging threat vectors. Prevents attacks before they happen!',
    icon: '🔮',
    gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)',
    accentColor: '#764ba2',
    steps: [
      { agent: 'Historical Analyst', task: 'Analyze past exploits', icon: '📜' },
      { agent: 'Vulnerability Mapper', task: 'Map current weaknesses', icon: '🗺️' },
      { agent: 'Attack Simulator', task: 'Simulate attack vectors', icon: '⚔️' },
      { agent: 'Future Predictor', task: 'Generate exploit predictions', icon: '🔮' }
    ],
    outputSections: ['Historical Analysis', 'Vulnerability Map', 'Attack Simulations', 'Exploit Predictions']
  },
  {
    id: 'threat_mesh',
    name: '🌐 Cross-Chain Threat Mesh',
    tagline: 'Multi-dimensional blockchain security',
    description: 'Analyzes security across multiple blockchain ecosystems simultaneously, identifying attack patterns that spread across chains, bridge vulnerabilities, and cross-chain exploit vectors.',
    icon: '🌐',
    gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ff6b6b 100%)',
    accentColor: '#f5576c',
    steps: [
      { agent: 'Chain Analyzer', task: 'Scan multiple chains', icon: '⛓️' },
      { agent: 'Bridge Inspector', task: 'Analyze cross-chain bridges', icon: '🌉' },
      { agent: 'Pattern Correlator', task: 'Correlate attack patterns', icon: '🔗' },
      { agent: 'Mesh Generator', task: 'Create threat mesh map', icon: '🌐' }
    ],
    outputSections: ['Chain Analysis', 'Bridge Vulnerabilities', 'Correlated Patterns', 'Threat Mesh']
  }
];

const SAMPLE_CONTRACT = `module vulnerable_vault::vault {
    use std::signer;
    use aptos_framework::coin;
    use aptos_framework::aptos_coin::AptosCoin;
    
    struct Vault has key {
        balance: u64,
        owner: address,
    }
    
    // VULNERABILITY: No reentrancy guard
    public entry fun withdraw(account: &signer, amount: u64) acquires Vault {
        let addr = signer::address_of(account);
        let vault = borrow_global_mut<Vault>(addr);
        
        // VULNERABILITY: Check after external call
        coin::transfer<AptosCoin>(account, addr, amount);
        
        assert!(vault.balance >= amount, 1);
        vault.balance = vault.balance - amount;
    }
    
    // VULNERABILITY: No access control
    public entry fun set_owner(new_owner: address) acquires Vault {
        let vault = borrow_global_mut<Vault>(@vulnerable_vault);
        vault.owner = new_owner;
    }
    
    // VULNERABILITY: Integer overflow possible
    public entry fun deposit(account: &signer, amount: u64) acquires Vault {
        let addr = signer::address_of(account);
        let vault = borrow_global_mut<Vault>(addr);
        vault.balance = vault.balance + amount; // No overflow check
    }
}`;

interface WorkflowResult {
  workflow: string;
  workflow_id: string;
  execution_time: string;
  steps_completed: number;
  results: {
    [key: string]: string;
  };
}

export default function WorkflowsPage() {
  const [selectedWorkflow, setSelectedWorkflow] = useState(WORKFLOWS[0]);
  const [contractCode, setContractCode] = useState(SAMPLE_CONTRACT);
  const [language, setLanguage] = useState('move');
  const [loading, setLoading] = useState(false);
  const [currentStep, setCurrentStep] = useState(-1);
  const [result, setResult] = useState<WorkflowResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeResultTab, setActiveResultTab] = useState(0);

  const executeWorkflow = async () => {
    if (!contractCode.trim()) {
      setError('Please enter contract code');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);
    setCurrentStep(0);

    // Simulate step progression
    const stepInterval = setInterval(() => {
      setCurrentStep(prev => {
        if (prev < selectedWorkflow.steps.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 3000);

    try {
      const response = await fetch(`${API_BASE}/api/workflows/${selectedWorkflow.id}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contract_code: contractCode,
          language: language,
          chains: ['aptos', 'ethereum', 'solana', 'sui', 'arbitrum']
        })
      });

      clearInterval(stepInterval);

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Workflow execution failed');
      }

      const data = await response.json();
      setResult(data);
      setCurrentStep(selectedWorkflow.steps.length);
    } catch (err: any) {
      setError(err.message || 'Failed to execute workflow');
    } finally {
      clearInterval(stepInterval);
      setLoading(false);
    }
  };

  const parseJsonSafely = (text: string) => {
    try {
      // Try to extract JSON from markdown code blocks
      const jsonMatch = text.match(/```(?:json)?\s*([\s\S]*?)```/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[1]);
      }
      return JSON.parse(text);
    } catch {
      return null;
    }
  };

  const renderResultContent = (content: string) => {
    const parsed = parseJsonSafely(content);
    if (parsed) {
      return (
        <pre className="result-json">
          {JSON.stringify(parsed, null, 2)}
        </pre>
      );
    }
    return <div className="result-text">{content}</div>;
  };

  const getResultKeys = () => {
    if (!result?.results) return [];
    return Object.keys(result.results);
  };

  return (
    <div className="workflows-page">
      <Navbar />
      
      {/* Background Effects */}
      <div className="workflows-bg">
        <div className="gradient-orb orb-1" style={{ background: selectedWorkflow.gradient }}></div>
        <div className="gradient-orb orb-2" style={{ background: selectedWorkflow.gradient }}></div>
        <div className="gradient-orb orb-3"></div>
        <div className="grid-pattern"></div>
      </div>

      <main className="workflows-main">
        {/* Header */}
        <header className="workflows-header">
          <div className="header-badge">
            <span className="badge-icon">⚡</span>
            <span>On-Demand.io Workflows</span>
          </div>
          <h1>AI-Powered Security Workflows</h1>
          <p className="header-subtitle">
            Multi-agent orchestrated analysis pipelines for comprehensive smart contract security
          </p>
        </header>

        {/* Workflow Selector */}
        <section className="workflow-selector">
          {WORKFLOWS.map((workflow) => (
            <button
              key={workflow.id}
              className={`workflow-card ${selectedWorkflow.id === workflow.id ? 'active' : ''}`}
              onClick={() => {
                setSelectedWorkflow(workflow);
                setResult(null);
                setError(null);
                setCurrentStep(-1);
                setActiveResultTab(0);
              }}
              style={{ '--accent-color': workflow.accentColor } as React.CSSProperties}
            >
              <div className="workflow-card-gradient" style={{ background: workflow.gradient }}></div>
              <div className="workflow-card-content">
                <span className="workflow-icon">{workflow.icon}</span>
                <h3>{workflow.name.replace(workflow.icon, '').trim()}</h3>
                <p className="workflow-tagline">{workflow.tagline}</p>
              </div>
              {selectedWorkflow.id === workflow.id && (
                <div className="workflow-selected-indicator"></div>
              )}
            </button>
          ))}
        </section>

        {/* Selected Workflow Details */}
        <section className="workflow-details">
          <div className="workflow-info-panel">
            <div className="workflow-info-header">
              <span className="workflow-large-icon">{selectedWorkflow.icon}</span>
              <div>
                <h2>{selectedWorkflow.name}</h2>
                <p className="workflow-description">{selectedWorkflow.description}</p>
              </div>
            </div>

            {/* Workflow Steps */}
            <div className="workflow-steps">
              <h3>Workflow Pipeline</h3>
              <div className="steps-container">
                {selectedWorkflow.steps.map((step, index) => (
                  <div 
                    key={index} 
                    className={`workflow-step ${currentStep === index ? 'active' : ''} ${currentStep > index ? 'completed' : ''}`}
                  >
                    <div className="step-indicator">
                      {currentStep > index ? (
                        <span className="step-check">✓</span>
                      ) : currentStep === index ? (
                        <span className="step-spinner"></span>
                      ) : (
                        <span className="step-number">{index + 1}</span>
                      )}
                    </div>
                    <div className="step-content">
                      <span className="step-icon">{step.icon}</span>
                      <div className="step-text">
                        <span className="step-agent">{step.agent}</span>
                        <span className="step-task">{step.task}</span>
                      </div>
                    </div>
                    {index < selectedWorkflow.steps.length - 1 && (
                      <div className={`step-connector ${currentStep > index ? 'active' : ''}`}></div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Input Section */}
        <section className="workflow-input-section">
          <div className="input-header">
            <h3>📝 Contract Code</h3>
            <div className="input-controls">
              <select 
                value={language} 
                onChange={(e) => setLanguage(e.target.value)}
                className="language-select"
              >
                <option value="move">Move (Aptos)</option>
                <option value="solidity">Solidity (EVM)</option>
                <option value="rust">Rust (Solana)</option>
              </select>
              <button 
                className="sample-btn"
                onClick={() => setContractCode(SAMPLE_CONTRACT)}
              >
                Load Sample
              </button>
            </div>
          </div>
          <div className="code-input-container">
            <textarea
              value={contractCode}
              onChange={(e) => setContractCode(e.target.value)}
              placeholder="Paste your smart contract code here..."
              className="code-textarea"
              spellCheck={false}
            />
            <div className="code-line-numbers">
              {contractCode.split('\n').map((_, i) => (
                <span key={i}>{i + 1}</span>
              ))}
            </div>
          </div>
          
          <button 
            className="execute-btn"
            onClick={executeWorkflow}
            disabled={loading}
            style={{ background: loading ? undefined : selectedWorkflow.gradient }}
          >
            {loading ? (
              <>
                <span className="execute-spinner"></span>
                <span>Executing {selectedWorkflow.name}...</span>
              </>
            ) : (
              <>
                <span className="execute-icon">▶</span>
                <span>Execute Workflow</span>
              </>
            )}
          </button>
        </section>

        {/* Error Display */}
        {error && (
          <div className="workflow-error">
            <span className="error-icon">⚠️</span>
            <span>{error}</span>
          </div>
        )}

        {/* Results Section */}
        {result && (
          <section className="workflow-results">
            <div className="results-header">
              <div className="results-title">
                <span className="results-icon">{selectedWorkflow.icon}</span>
                <div>
                  <h2>Analysis Complete</h2>
                  <p>
                    <span className="result-meta">
                      Executed at {new Date(result.execution_time).toLocaleString()}
                    </span>
                    <span className="result-meta">
                      • {result.steps_completed} steps completed
                    </span>
                  </p>
                </div>
              </div>
              <div className="results-badge" style={{ background: selectedWorkflow.gradient }}>
                ✓ Success
              </div>
            </div>

            {/* Result Tabs */}
            <div className="result-tabs">
              {getResultKeys().map((key, index) => (
                <button
                  key={key}
                  className={`result-tab ${activeResultTab === index ? 'active' : ''}`}
                  onClick={() => setActiveResultTab(index)}
                  style={{ '--tab-accent': selectedWorkflow.accentColor } as React.CSSProperties}
                >
                  <span className="tab-step">{index + 1}</span>
                  <span className="tab-name">
                    {key.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}
                  </span>
                </button>
              ))}
            </div>

            {/* Active Result Content */}
            <div className="result-content">
              <div className="result-panel">
                {getResultKeys()[activeResultTab] && (
                  renderResultContent(result.results[getResultKeys()[activeResultTab]])
                )}
              </div>
            </div>
          </section>
        )}
      </main>
    </div>
  );
}
