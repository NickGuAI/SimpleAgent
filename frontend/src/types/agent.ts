export interface BrowserAgent {
  id: string;
  name: string;
  description: string;
  targetWebsite: string;
  instructions: Instruction[];
  tools: Tool[];
  triggers: Trigger[];
  outputConfig: OutputConfig;
}

export interface Instruction {
  id: string;
  type: 'navigate' | 'click' | 'type' | 'wait' | 'extract' | 'conditional' | 'loop';
  selector?: string;
  value?: any;
  conditions?: Condition[];
  nextInstructionId?: string;
  position?: { x: number; y: number };
}

export interface Tool {
  id: string;
  name: string;
  type: 'screenshot' | 'download' | 'save_data' | 'api_call';
  config: Record<string, any>;
}

export interface Trigger {
  id: string;
  type: 'manual' | 'schedule' | 'webhook';
  config: Record<string, any>;
}

export interface Condition {
  field: string;
  operator: 'equals' | 'contains' | 'exists' | 'not_exists';
  value?: any;
}

export interface OutputConfig {
  type: 'json' | 'csv' | 'webhook';
  destination?: string;
  format?: Record<string, any>;
}

export interface ActionBlock {
  id: string;
  type: Instruction['type'];
  label: string;
  icon: string;
  defaultConfig: Partial<Instruction>;
}