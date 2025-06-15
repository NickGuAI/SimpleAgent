import React, { useCallback, useMemo } from 'react';
import {
  ReactFlow,
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  ConnectionMode,
  Panel,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import { BrowserAgent, Instruction } from '../../types/agent';
import InstructionNode from './InstructionNode';
import './FlowBuilder.css';

interface FlowBuilderProps {
  agent: BrowserAgent;
  onAgentUpdate: (agent: BrowserAgent) => void;
  selectedInstructionId: string | null;
  onInstructionSelect: (id: string | null) => void;
}

const nodeTypes = {
  instruction: InstructionNode,
};

const FlowBuilder: React.FC<FlowBuilderProps> = ({
  agent,
  onAgentUpdate,
  selectedInstructionId,
  onInstructionSelect,
}) => {
  const initialNodes = useMemo(() => {
    return agent.instructions.map((instruction, index) => ({
      id: instruction.id,
      type: 'instruction',
      position: instruction.position || { x: 250, y: 100 + index * 150 },
      data: { instruction, isSelected: instruction.id === selectedInstructionId },
    }));
  }, [agent.instructions, selectedInstructionId]);

  const initialEdges = useMemo(() => {
    const edges: Edge[] = [];
    agent.instructions.forEach((instruction) => {
      if (instruction.nextInstructionId) {
        edges.push({
          id: `${instruction.id}-${instruction.nextInstructionId}`,
          source: instruction.id,
          target: instruction.nextInstructionId,
          type: 'smoothstep',
        });
      }
    });
    return edges;
  }, [agent.instructions]);

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params: Connection) => {
      const newEdges = addEdge(params, edges);
      setEdges(newEdges);
      
      // Update instruction connections
      const updatedInstructions = agent.instructions.map((inst) => {
        if (inst.id === params.source) {
          return { ...inst, nextInstructionId: params.target };
        }
        return inst;
      });
      
      onAgentUpdate({ ...agent, instructions: updatedInstructions });
    },
    [edges, agent, onAgentUpdate, setEdges]
  );

  const onNodeClick = useCallback(
    (event: React.MouseEvent, node: Node) => {
      onInstructionSelect(node.id);
    },
    [onInstructionSelect]
  );

  const onPaneClick = useCallback(() => {
    onInstructionSelect(null);
  }, [onInstructionSelect]);

  const onNodeDragStop = useCallback(
    (event: React.MouseEvent, node: Node) => {
      const updatedInstructions = agent.instructions.map((inst) => {
        if (inst.id === node.id) {
          return { ...inst, position: node.position };
        }
        return inst;
      });
      onAgentUpdate({ ...agent, instructions: updatedInstructions });
    },
    [agent, onAgentUpdate]
  );

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();
      
      const type = event.dataTransfer.getData('instructionType');
      if (!type) return;
      
      const position = {
        x: event.clientX - event.currentTarget.getBoundingClientRect().left,
        y: event.clientY - event.currentTarget.getBoundingClientRect().top,
      };
      
      const newInstruction: Instruction = {
        id: `instruction-${Date.now()}`,
        type: type as Instruction['type'],
        position,
      };
      
      onAgentUpdate({
        ...agent,
        instructions: [...agent.instructions, newInstruction],
      });
    },
    [agent, onAgentUpdate]
  );

  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  return (
    <div className="flow-builder" onDrop={onDrop} onDragOver={onDragOver}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodeClick={onNodeClick}
        onPaneClick={onPaneClick}
        onNodeDragStop={onNodeDragStop}
        nodeTypes={nodeTypes}
        connectionMode={ConnectionMode.Loose}
        fitView
      >
        <Background />
        <Controls />
        <Panel position="top-left">
          <div className="flow-info">
            <input
              type="url"
              placeholder="Target Website URL"
              value={agent.targetWebsite}
              onChange={(e) => onAgentUpdate({ ...agent, targetWebsite: e.target.value })}
              className="target-url-input"
            />
          </div>
        </Panel>
      </ReactFlow>
    </div>
  );
};

export default FlowBuilder;