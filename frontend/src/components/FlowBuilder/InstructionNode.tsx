import React from 'react';
import { Handle, Position } from '@xyflow/react';
import { Instruction } from '../../types/agent';
import {
  Navigation,
  MousePointer,
  Keyboard,
  Clock,
  Database,
  GitBranch,
  Repeat,
} from 'lucide-react';
import './InstructionNode.css';

interface InstructionNodeProps {
  data: {
    instruction: Instruction;
    isSelected: boolean;
  };
}

const getIcon = (type: Instruction['type']) => {
  switch (type) {
    case 'navigate':
      return <Navigation size={16} />;
    case 'click':
      return <MousePointer size={16} />;
    case 'type':
      return <Keyboard size={16} />;
    case 'wait':
      return <Clock size={16} />;
    case 'extract':
      return <Database size={16} />;
    case 'conditional':
      return <GitBranch size={16} />;
    case 'loop':
      return <Repeat size={16} />;
    default:
      return null;
  }
};

const InstructionNode: React.FC<InstructionNodeProps> = ({ data }) => {
  const { instruction, isSelected } = data;

  return (
    <div className={`instruction-node ${isSelected ? 'selected' : ''} ${instruction.type}`}>
      <Handle type="target" position={Position.Top} />
      
      <div className="instruction-node__header">
        <span className="instruction-node__icon">{getIcon(instruction.type)}</span>
        <span className="instruction-node__type">{instruction.type}</span>
      </div>
      
      <div className="instruction-node__content">
        {instruction.selector && (
          <div className="instruction-node__field">
            <label>Selector:</label>
            <span>{instruction.selector}</span>
          </div>
        )}
        {instruction.value && (
          <div className="instruction-node__field">
            <label>Value:</label>
            <span>{instruction.value}</span>
          </div>
        )}
      </div>
      
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
};

export default InstructionNode;