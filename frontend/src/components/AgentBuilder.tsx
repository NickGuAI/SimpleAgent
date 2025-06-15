import React, { useState } from 'react';
import FlowBuilder from './FlowBuilder/FlowBuilder';
import ActionBlockPanel from './ActionBlocks/ActionBlockPanel';
import BrowserPreview from './BrowserPreview/BrowserPreview';
import { BrowserAgent } from '../types/agent';
import './AgentBuilder.css';

const AgentBuilder: React.FC = () => {
  const [agent, setAgent] = useState<BrowserAgent>({
    id: 'new-agent',
    name: 'New Browser Agent',
    description: '',
    targetWebsite: '',
    instructions: [],
    tools: [],
    triggers: [],
    outputConfig: { type: 'json' }
  });

  const [selectedInstructionId, setSelectedInstructionId] = useState<string | null>(null);
  const [isPreviewMode, setIsPreviewMode] = useState(false);

  return (
    <div className="agent-builder">
      <header className="agent-builder__header">
        <div className="agent-builder__title">
          <h1>Visual Browser Agent Builder</h1>
          <input
            type="text"
            value={agent.name}
            onChange={(e) => setAgent({ ...agent, name: e.target.value })}
            className="agent-name-input"
            placeholder="Agent Name"
          />
        </div>
        <div className="agent-builder__actions">
          <button className="btn btn-secondary" onClick={() => setIsPreviewMode(!isPreviewMode)}>
            {isPreviewMode ? 'Edit Mode' : 'Preview Mode'}
          </button>
          <button className="btn btn-primary">Save Agent</button>
        </div>
      </header>
      
      <div className="agent-builder__main">
        <aside className="agent-builder__sidebar">
          <ActionBlockPanel />
        </aside>
        
        <section className="agent-builder__canvas">
          <FlowBuilder
            agent={agent}
            onAgentUpdate={setAgent}
            selectedInstructionId={selectedInstructionId}
            onInstructionSelect={setSelectedInstructionId}
          />
        </section>
        
        <aside className="agent-builder__preview">
          <BrowserPreview
            agent={agent}
            isActive={isPreviewMode}
          />
        </aside>
      </div>
    </div>
  );
};

export default AgentBuilder;