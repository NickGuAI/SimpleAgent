import axios from 'axios';
import { BrowserAgent } from '../types/agent';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const agentService = {
  // Create a new agent
  create: async (agent: BrowserAgent) => {
    const response = await api.post('/agents', agent);
    return response.data;
  },

  // Get all agents
  list: async () => {
    const response = await api.get('/agents');
    return response.data;
  },

  // Get a specific agent
  get: async (id: string) => {
    const response = await api.get(`/agents/${id}`);
    return response.data;
  },

  // Update an agent
  update: async (id: string, agent: Partial<BrowserAgent>) => {
    const response = await api.put(`/agents/${id}`, agent);
    return response.data;
  },

  // Delete an agent
  delete: async (id: string) => {
    const response = await api.delete(`/agents/${id}`);
    return response.data;
  },

  // Run agent in preview mode
  preview: async (agent: BrowserAgent) => {
    const response = await api.post('/agents/preview', { agent, mode: 'preview' });
    return response.data;
  },

  // Execute agent
  execute: async (id: string) => {
    const response = await api.post(`/agents/${id}/execute`);
    return response.data;
  },
};

export default api;