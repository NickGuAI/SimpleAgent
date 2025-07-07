# MUI Component Challenge Creation Guidelines

## Overview

This directory contains browser-based challenges for testing Material UI components. Each challenge is designed to test AI agents' ability to interact with specific MUI components through browser automation tools.

## Directory Structure

```
src/
├── inputs/          # Input components (Button, TextField, Select, etc.)
├── data-display/    # Data display components (Table, List, Typography, etc.)
├── feedback/        # Feedback components (Alert, Dialog, Snackbar, etc.)
├── surfaces/        # Surface components (Card, Paper, Accordion, etc.)
├── navigation/      # Navigation components (Tabs, Menu, Drawer, etc.)
├── layout/          # Layout components (Grid, Box, Container, etc.)
├── utils/           # Utility components (Modal, Popover, etc.)
├── lab/             # Experimental components
└── base-template.html  # Base template for creating new challenges
```

## Creating a New Component Challenge

### 1. File Naming Convention
- Use kebab-case matching the component name
- Examples: `button.html`, `text-field.html`, `data-grid.html`

### 2. Challenge Structure

Each challenge should follow this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Standard imports and styles from base-template.html -->
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>MUI Component Challenge: [Component Name]</h1>
            <p>Test the functionality and behavior of the Material UI [Component]</p>
        </div>
        
        <div id="app"></div>
    </div>
    
    <script type="text/babel">
        // Component implementation and tests
    </script>
</body>
</html>
```

### 3. Test Implementation Guidelines

#### Test Harness Usage
Each test should use the `TestHarness` component:

```javascript
<TestHarness
    testId="unique-test-id"
    testName="Descriptive Test Name"
    description="What this test validates"
    onComplete={handleTestComplete}
>
    <YourTestComponent />
</TestHarness>
```

#### Test Component Structure
```javascript
const YourTestComponent = ({ completeTest }) => {
    // State and logic for the test
    
    const handleSuccess = () => {
        completeTest(true, 'Success message');
    };
    
    const handleFailure = () => {
        completeTest(false, 'Failure message');
    };
    
    return (
        // Your MUI component implementation
    );
};
```

### 4. Testing Requirements

Each component challenge should test:

1. **Basic Functionality**
   - Core component behavior
   - Primary props and their effects

2. **User Interactions**
   - Click events
   - Keyboard navigation
   - Focus management

3. **State Management**
   - Controlled vs uncontrolled behavior
   - Value changes and updates

4. **Accessibility**
   - ARIA attributes
   - Keyboard accessibility
   - Screen reader compatibility

5. **Edge Cases**
   - Disabled states
   - Error states
   - Loading states

### 5. Component Categories

#### Input Components
Test user input handling, validation, and state management:
- Text input and changes
- Selection from options
- Toggle states
- Range/slider values

#### Data Display Components
Test data presentation and interaction:
- List item interactions
- Table sorting/filtering
- Tooltip displays
- Badge updates

#### Feedback Components
Test user feedback mechanisms:
- Alert dismissal
- Dialog interactions
- Snackbar timing
- Progress updates

#### Surface Components
Test container behaviors:
- Accordion expansion
- Card interactions
- Paper elevation changes

#### Navigation Components
Test navigation flows:
- Tab switching
- Menu selection
- Drawer toggling
- Breadcrumb navigation

#### Layout Components
Test responsive behavior:
- Grid breakpoints
- Stack spacing
- Container sizing

### 6. Best Practices

1. **Keep Tests Focused**
   - One component per file
   - Clear test objectives
   - Minimal external dependencies

2. **Provide Clear Instructions**
   - Explicit user actions required
   - Expected outcomes documented
   - Visual feedback for test status

3. **Handle Edge Cases**
   - Test error conditions
   - Validate boundary values
   - Check disabled states

4. **Accessibility First**
   - Include keyboard navigation
   - Test with screen readers
   - Proper ARIA labels

5. **Browser Compatibility**
   - Test in multiple browsers
   - Handle vendor prefixes
   - Graceful degradation

### 7. Integration with challenge.html

Each component challenge will be:
1. Listed in the appropriate category
2. Loaded dynamically when selected
3. Report results back to the main challenge page
4. Track completion status

### 8. Example Component Test

See `inputs/button.html` for a complete example implementation that demonstrates:
- Multiple test scenarios
- Proper event handling
- State management
- Result reporting
- Accessibility testing