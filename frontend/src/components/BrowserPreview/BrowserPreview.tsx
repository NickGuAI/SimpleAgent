import React, { useState, useEffect } from 'react';
import { BrowserAgent } from '../../types/agent';
import { Play, Pause, RotateCcw, Monitor } from 'lucide-react';
import './BrowserPreview.css';

interface BrowserPreviewProps {
  agent: BrowserAgent;
  isActive: boolean;
}

const BrowserPreview: React.FC<BrowserPreviewProps> = ({ agent, isActive }) => {
  const [isRunning, setIsRunning] = useState(false);
  const [previewUrl, setPreviewUrl] = useState('');
  const [logs, setLogs] = useState<string[]>([]);

  useEffect(() => {
    if (agent.targetWebsite) {
      setPreviewUrl(agent.targetWebsite);
    }
  }, [agent.targetWebsite]);

  const handleRun = async () => {
    if (!agent.targetWebsite || agent.instructions.length === 0) {
      setLogs(['No target website or instructions defined']);
      return;
    }

    setIsRunning(true);
    setLogs(['Starting browser automation...']);

    // Send request to backend to execute agent
    try {
      const response = await fetch('http://localhost:8000/api/agents/preview', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          agent: agent,
          mode: 'preview',
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to start preview');
      }

      // In a real implementation, this would be a WebSocket connection
      // to receive real-time updates from the browser automation
      setLogs(prev => [...prev, 'Browser session started']);
      
    } catch (error) {
      setLogs(prev => [...prev, `Error: ${error}`]);
    } finally {
      setIsRunning(false);
    }
  };

  const handleStop = () => {
    setIsRunning(false);
    setLogs(prev => [...prev, 'Automation stopped']);
  };

  const handleReset = () => {
    setLogs([]);
    setIsRunning(false);
  };

  return (
    <div className="browser-preview">
      <div className="browser-preview__header">
        <h3 className="browser-preview__title">
          <Monitor size={16} />
          Browser Preview
        </h3>
        <div className="browser-preview__controls">
          {!isRunning ? (
            <button
              className="preview-btn preview-btn--play"
              onClick={handleRun}
              disabled={!isActive || !agent.targetWebsite}
            >
              <Play size={16} />
              Run
            </button>
          ) : (
            <button
              className="preview-btn preview-btn--pause"
              onClick={handleStop}
            >
              <Pause size={16} />
              Stop
            </button>
          )}
          <button
            className="preview-btn preview-btn--reset"
            onClick={handleReset}
            disabled={isRunning}
          >
            <RotateCcw size={16} />
            Reset
          </button>
        </div>
      </div>

      <div className="browser-preview__content">
        {isActive ? (
          <>
            <div className="browser-preview__frame">
              {previewUrl ? (
                <div className="browser-preview__placeholder">
                  <div className="browser-preview__url-bar">
                    <span>{previewUrl}</span>
                  </div>
                  <div className="browser-preview__viewport">
                    <p>Live browser preview will appear here</p>
                    <p className="browser-preview__hint">
                      Connect to backend service to see real-time automation
                    </p>
                  </div>
                </div>
              ) : (
                <div className="browser-preview__empty">
                  <p>Enter a target website URL to begin</p>
                </div>
              )}
            </div>

            <div className="browser-preview__logs">
              <h4>Execution Logs</h4>
              <div className="browser-preview__log-content">
                {logs.map((log, index) => (
                  <div key={index} className="log-entry">
                    <span className="log-time">
                      {new Date().toLocaleTimeString()}
                    </span>
                    <span className="log-message">{log}</span>
                  </div>
                ))}
              </div>
            </div>
          </>
        ) : (
          <div className="browser-preview__inactive">
            <p>Switch to Preview Mode to test your automation</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default BrowserPreview;