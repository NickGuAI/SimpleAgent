#!/bin/bash

# SimpleAgent Launch Script
# This script starts both the backend service and frontend application

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[SimpleAgent]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SimpleAgent]${NC} $1"
}

print_error() {
    echo -e "${RED}[SimpleAgent]${NC} $1"
}

# Function to check if a port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null ; then
        return 0
    else
        return 1
    fi
}

# Function to kill process on port
kill_port() {
    if check_port $1; then
        print_status "Killing process on port $1..."
        lsof -ti:$1 | xargs kill -9 2>/dev/null || true
        sleep 1
    fi
}

# Cleanup function
cleanup() {
    print_status "Shutting down SimpleAgent..."
    
    # Kill backend
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
    fi
    
    # Kill frontend
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    
    # Clean up any remaining processes on the ports
    kill_port 8000
    kill_port 3000
    
    print_success "SimpleAgent stopped."
    exit 0
}

# Set up trap to handle Ctrl+C
trap cleanup INT TERM

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "service" ] || [ ! -d "frontend" ]; then
    print_error "Please run this script from the SimpleAgent root directory"
    exit 1
fi

print_status "Starting SimpleAgent..."

# Check and clean ports if needed
if check_port 8000; then
    print_status "Port 8000 is in use. Cleaning up..."
    kill_port 8000
fi

if check_port 3000; then
    print_status "Port 3000 is in use. Cleaning up..."
    kill_port 3000
fi

# Start Backend Service
print_status "Starting backend service..."
cd service

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    # Check if uv exists in local bin
    if [ -f "$HOME/.local/bin/uv" ]; then
        export PATH="$HOME/.local/bin:$PATH"
    else
        print_status "Installing uv..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
    fi
fi

# Install dependencies with uv
print_status "Installing backend dependencies..."
uv sync

# Start backend with uv
uv run python -m app.main &
BACKEND_PID=$!
cd ..

# Wait for backend to start
print_status "Waiting for backend to start..."
for i in {1..30}; do
    if curl -s http://localhost:8000/health >/dev/null 2>&1; then
        print_success "Backend started successfully!"
        break
    fi
    if [ $i -eq 30 ]; then
        print_error "Backend failed to start"
        cleanup
    fi
    sleep 1
done

# Start Frontend
print_status "Starting frontend application..."
cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    print_status "Installing frontend dependencies..."
    npm install
fi

# Start frontend in background
npm start &
FRONTEND_PID=$!
cd ..

# Wait for frontend to start
print_status "Waiting for frontend to start..."
for i in {1..60}; do
    if curl -s http://localhost:3000 >/dev/null 2>&1; then
        print_success "Frontend started successfully!"
        break
    fi
    if [ $i -eq 60 ]; then
        print_error "Frontend failed to start"
        cleanup
    fi
    sleep 1
done

# Print success message
echo ""
print_success "SimpleAgent is running!"
echo ""
echo -e "${GREEN}➜${NC} Frontend: ${BLUE}http://localhost:3000${NC}"
echo -e "${GREEN}➜${NC} Backend API: ${BLUE}http://localhost:8000${NC}"
echo -e "${GREEN}➜${NC} API Docs: ${BLUE}http://localhost:8000/api/docs${NC}"
echo ""
echo -e "Press ${RED}Ctrl+C${NC} to stop all services"
echo ""

# Keep script running
wait