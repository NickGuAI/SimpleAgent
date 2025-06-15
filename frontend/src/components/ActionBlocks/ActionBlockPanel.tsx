import React from 'react';
import { ActionBlock } from '../../types/agent';
import {
  Navigation,
  MousePointer,
  Keyboard,
  Clock,
  Database,
  GitBranch,
  Repeat,
} from 'lucide-react';
import './ActionBlockPanel.css';

const actionBlocks: ActionBlock[] = [
  {
    id: 'navigate',
    type: 'navigate',
    label: 'Navigate',
    icon: 'Navigation',
    defaultConfig: { type: 'navigate' },
  },
  {
    id: 'click',
    type: 'click',
    label: 'Click',
    icon: 'MousePointer',
    defaultConfig: { type: 'click' },
  },
  {
    id: 'type',
    type: 'type',
    label: 'Type Text',
    icon: 'Keyboard',
    defaultConfig: { type: 'type' },
  },
  {
    id: 'wait',
    type: 'wait',
    label: 'Wait',
    icon: 'Clock',
    defaultConfig: { type: 'wait', value: 1000 },
  },
  {
    id: 'extract',
    type: 'extract',
    label: 'Extract Data',
    icon: 'Database',
    defaultConfig: { type: 'extract' },
  },
  {
    id: 'conditional',
    type: 'conditional',
    label: 'Conditional',
    icon: 'GitBranch',
    defaultConfig: { type: 'conditional' },
  },
  {
    id: 'loop',
    type: 'loop',
    label: 'Loop',
    icon: 'Repeat',
    defaultConfig: { type: 'loop' },
  },
];

const getIcon = (iconName: string) => {
  switch (iconName) {
    case 'Navigation':
      return <Navigation size={20} />;
    case 'MousePointer':
      return <MousePointer size={20} />;
    case 'Keyboard':
      return <Keyboard size={20} />;
    case 'Clock':
      return <Clock size={20} />;
    case 'Database':
      return <Database size={20} />;
    case 'GitBranch':
      return <GitBranch size={20} />;
    case 'Repeat':
      return <Repeat size={20} />;
    default:
      return null;
  }
};

const ActionBlockPanel: React.FC = () => {
  const onDragStart = (event: React.DragEvent, blockType: string) => {
    event.dataTransfer.setData('instructionType', blockType);
    event.dataTransfer.effectAllowed = 'copy';
  };

  return (
    <div className="action-block-panel">
      <h3 className="action-block-panel__title">Actions</h3>
      <div className="action-block-panel__blocks">
        {actionBlocks.map((block) => (
          <div
            key={block.id}
            className={`action-block action-block--${block.type}`}
            draggable
            onDragStart={(e) => onDragStart(e, block.type)}
          >
            <span className="action-block__icon">{getIcon(block.icon)}</span>
            <span className="action-block__label">{block.label}</span>
          </div>
        ))}
      </div>
      
      <div className="action-block-panel__help">
        <p>Drag blocks to the canvas to build your automation flow</p>
      </div>
    </div>
  );
};

export default ActionBlockPanel;