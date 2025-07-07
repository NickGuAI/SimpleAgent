# MUI Testable Components Documentation

## Overview

This document provides a comprehensive list of all Material UI components available for testing, organized by category. Each component includes its description, key testable properties, and important behaviors for creating test challenges.

## Component Categories

### 1. Input Components (15 components)

#### Autocomplete
- **Description**: Combo box with suggestions and filtering capabilities
- **Key Testable Properties**:
  - `onChange`: Value selection event
  - `onInputChange`: Text input change event
  - `options`: Array of selectable options
  - `value`: Currently selected value
  - `disabled`: Disable interaction
  - `multiple`: Allow multiple selections
  - `freeSolo`: Allow arbitrary text input
  - `loading`: Show loading state

**Code Example**:
```jsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

const options = ['Option 1', 'Option 2', 'Option 3'];

// Basic autocomplete
<Autocomplete
  options={options}
  renderInput={(params) => <TextField {...params} label="Select option" />}
/>

// Controlled autocomplete
const [value, setValue] = React.useState(null);

<Autocomplete
  value={value}
  onChange={(event, newValue) => setValue(newValue)}
  options={options}
  renderInput={(params) => <TextField {...params} label="Controlled" />}
/>

// Multiple selection
<Autocomplete
  multiple
  options={options}
  defaultValue={[options[0]]}
  renderInput={(params) => <TextField {...params} label="Multiple" />}
/>

// Free solo (custom values)
<Autocomplete
  freeSolo
  options={options}
  renderInput={(params) => <TextField {...params} label="Free solo" />}
/>
```

#### Button
- **Description**: Basic clickable element for triggering actions
- **Key Testable Properties**:
  - `onClick`: Click event handler
  - `disabled`: Disable interaction
  - `variant`: text/contained/outlined
  - `color`: primary/secondary/error/warning/info/success
  - `size`: small/medium/large
  - `startIcon`/`endIcon`: Icon placement

**Code Example**:
```jsx
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import SendIcon from '@mui/icons-material/Send';

// Basic button variants
<Button variant="text">Text</Button>
<Button variant="contained">Contained</Button>
<Button variant="outlined">Outlined</Button>

// Disabled button
<Button variant="contained" disabled>
  Disabled
</Button>

// Color variants
<Button variant="contained" color="primary">Primary</Button>
<Button variant="contained" color="secondary">Secondary</Button>
<Button variant="contained" color="success">Success</Button>
<Button variant="contained" color="error">Error</Button>

// Sizes
<Button size="small">Small</Button>
<Button size="medium">Medium</Button>
<Button size="large">Large</Button>

// With icons
<Button variant="outlined" startIcon={<DeleteIcon />}>
  Delete
</Button>
<Button variant="contained" endIcon={<SendIcon />}>
  Send
</Button>

// Click handler
<Button
  variant="contained"
  onClick={() => console.log('Button clicked')}
>
  Click me
</Button>
```

#### Button Group
- **Description**: Groups multiple related buttons together
- **Key Testable Properties**:
  - `variant`: text/contained/outlined
  - `orientation`: horizontal/vertical
  - `disabled`: Disable all buttons
  - `color`: Theme color
  - `size`: Button sizes

#### Checkbox
- **Description**: Binary selection control for on/off states
- **Key Testable Properties**:
  - `checked`: Current state
  - `onChange`: State change event
  - `disabled`: Disable interaction
  - `indeterminate`: Partial selection state
  - `required`: Form validation
  - `color`: Theme color

**Code Example**:
```jsx
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

// Basic checkbox
<Checkbox defaultChecked />
<Checkbox />
<Checkbox disabled />
<Checkbox disabled checked />

// Controlled checkbox
const [checked, setChecked] = React.useState(true);

<Checkbox
  checked={checked}
  onChange={(event) => setChecked(event.target.checked)}
  inputProps={{ 'aria-label': 'controlled' }}
/>

// With label
<FormControlLabel 
  control={<Checkbox defaultChecked />} 
  label="Label" 
/>

// Color variants
<Checkbox defaultChecked color="primary" />
<Checkbox defaultChecked color="secondary" />
<Checkbox defaultChecked color="success" />
<Checkbox defaultChecked color="default" />

// Indeterminate state
<Checkbox indeterminate />

// Size
<Checkbox defaultChecked size="small" />
<Checkbox defaultChecked />
<Checkbox defaultChecked size="large" />
```

#### Floating Action Button (FAB)
- **Description**: Circular button for primary page actions
- **Key Testable Properties**:
  - `onClick`: Click event
  - `disabled`: Disable state
  - `size`: small/medium/large
  - `color`: Theme color
  - `variant`: circular/extended

#### Radio Group
- **Description**: Single selection from multiple options
- **Key Testable Properties**:
  - `value`: Selected option
  - `onChange`: Selection change event
  - `disabled`: Disable all options
  - `row`: Horizontal layout
  - `required`: Form validation

#### Rating
- **Description**: Star-based rating input component
- **Key Testable Properties**:
  - `value`: Current rating
  - `onChange`: Rating change event
  - `disabled`: Disable interaction
  - `readOnly`: View-only mode
  - `precision`: Rating increments (0.5, 1)
  - `max`: Maximum rating value

#### Select
- **Description**: Dropdown selection menu
- **Key Testable Properties**:
  - `value`: Selected value(s)
  - `onChange`: Selection change event
  - `multiple`: Multi-select mode
  - `disabled`: Disable selection
  - `required`: Form validation
  - `open`/`onOpen`/`onClose`: Menu state control

**Code Example**:
```jsx
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';

// Basic select
const [age, setAge] = React.useState('');

<FormControl fullWidth>
  <InputLabel id="demo-simple-select-label">Age</InputLabel>
  <Select
    labelId="demo-simple-select-label"
    id="demo-simple-select"
    value={age}
    label="Age"
    onChange={(event) => setAge(event.target.value)}
  >
    <MenuItem value={10}>Ten</MenuItem>
    <MenuItem value={20}>Twenty</MenuItem>
    <MenuItem value={30}>Thirty</MenuItem>
  </Select>
</FormControl>

// Multiple select
const [names, setNames] = React.useState([]);

<FormControl fullWidth>
  <InputLabel>Names</InputLabel>
  <Select
    multiple
    value={names}
    onChange={(event) => setNames(event.target.value)}
    label="Names"
  >
    <MenuItem value="Oliver">Oliver</MenuItem>
    <MenuItem value="Van">Van</MenuItem>
    <MenuItem value="April">April</MenuItem>
  </Select>
</FormControl>

// Disabled select
<Select disabled value="">
  <MenuItem value="">None</MenuItem>
</Select>
```

#### Slider
- **Description**: Range selection on a continuous or discrete track
- **Key Testable Properties**:
  - `value`: Current value(s)
  - `onChange`: Value change event
  - `disabled`: Disable interaction
  - `min`/`max`: Value range
  - `step`: Value increments
  - `marks`: Track markers
  - `orientation`: horizontal/vertical

**Code Example**:
```jsx
import Slider from '@mui/material/Slider';

// Basic slider
<Slider defaultValue={30} />
<Slider defaultValue={50} disabled />

// Controlled slider
const [value, setValue] = React.useState(30);

<Slider 
  value={value} 
  onChange={(event, newValue) => setValue(newValue)}
/>

// Discrete slider
<Slider
  defaultValue={30}
  step={10}
  marks
  min={10}
  max={110}
/>

// Custom marks
const marks = [
  { value: 0, label: '0°C' },
  { value: 20, label: '20°C' },
  { value: 37, label: '37°C' },
  { value: 100, label: '100°C' },
];

<Slider
  defaultValue={20}
  marks={marks}
  step={10}
  valueLabelDisplay="auto"
/>

// Range slider
const [rangeValue, setRangeValue] = React.useState([20, 37]);

<Slider
  value={rangeValue}
  onChange={(event, newValue) => setRangeValue(newValue)}
  valueLabelDisplay="auto"
/>

// Vertical slider
<Slider
  orientation="vertical"
  defaultValue={30}
  sx={{ height: 300 }}
/>

// Color
<Slider defaultValue={30} color="secondary" />
```

#### Switch
- **Description**: Toggle between on/off states
- **Key Testable Properties**:
  - `checked`: Current state
  - `onChange`: Toggle event
  - `disabled`: Disable interaction
  - `required`: Form validation
  - `color`: Theme color

**Code Example**:
```jsx
import Switch from '@mui/material/Switch';
import FormControlLabel from '@mui/material/FormControlLabel';

// Basic switches
<Switch defaultChecked />
<Switch />
<Switch disabled defaultChecked />
<Switch disabled />

// Controlled switch
const [checked, setChecked] = React.useState(true);

<Switch
  checked={checked}
  onChange={(event) => setChecked(event.target.checked)}
  inputProps={{ 'aria-label': 'controlled' }}
/>

// With label
<FormControlLabel 
  control={<Switch defaultChecked />} 
  label="Label" 
/>

// Color variants
<Switch defaultChecked color="primary" />
<Switch defaultChecked color="secondary" />
<Switch defaultChecked color="warning" />
<Switch defaultChecked color="default" />

// Size
<Switch defaultChecked size="small" />
<Switch defaultChecked />
```

#### Text Field
- **Description**: Text input with various configurations
- **Key Testable Properties**:
  - `value`: Input value
  - `onChange`: Value change event
  - `disabled`: Disable input
  - `required`: Form validation
  - `error`: Error state
  - `helperText`: Helper/error message
  - `variant`: standard/filled/outlined
  - `multiline`: Multi-line input
  - `type`: text/password/email/number/etc

**Code Example**:
```jsx
import TextField from '@mui/material/TextField';

// Basic text fields
<TextField id="outlined-basic" label="Outlined" variant="outlined" />
<TextField id="filled-basic" label="Filled" variant="filled" />
<TextField id="standard-basic" label="Standard" variant="standard" />

// Controlled text field
const [value, setValue] = React.useState('Controlled');

<TextField
  id="controlled"
  label="Controlled"
  value={value}
  onChange={(event) => setValue(event.target.value)}
/>

// Validation states
<TextField error label="Error" defaultValue="Hello World" />
<TextField
  error
  label="Error"
  defaultValue="Hello World"
  helperText="Incorrect entry."
/>

// Form props
<TextField required label="Required" defaultValue="Hello World" />
<TextField disabled label="Disabled" defaultValue="Hello World" />
<TextField
  type="password"
  label="Password"
  autoComplete="current-password"
/>

// Read only
<TextField
  label="Read Only"
  defaultValue="Hello World"
  InputProps={{
    readOnly: true,
  }}
/>

// Number input
<TextField
  label="Number"
  type="number"
  InputLabelProps={{
    shrink: true,
  }}
/>

// Multiline
<TextField
  label="Multiline"
  multiline
  rows={4}
  defaultValue="Default Value"
/>

// Select
<TextField
  select
  label="Select"
  value={currency}
  onChange={handleChange}
  SelectProps={{
    native: true,
  }}
>
  {currencies.map((option) => (
    <option key={option.value} value={option.value}>
      {option.label}
    </option>
  ))}
</TextField>
```

#### Transfer List
- **Description**: Move items between two lists
- **Key Testable Properties**:
  - `onChange`: Item transfer event
  - `disabled`: Disable transfers
  - Item selection management
  - List filtering capabilities

#### Toggle Button
- **Description**: Button with selectable on/off states
- **Key Testable Properties**:
  - `value`: Button value
  - `onChange`: Selection change
  - `selected`: Current state
  - `disabled`: Disable interaction
  - `exclusive`: Single selection mode

### 2. Data Display Components (9 components)

#### Avatar
- **Description**: User profile picture or initials display
- **Key Testable Properties**:
  - `alt`: Alternative text
  - `src`: Image source
  - `variant`: circular/rounded/square
  - `sizes`: Responsive sizing
  - Fallback to initials

**Code Example**:
```jsx
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import { deepOrange, deepPurple } from '@mui/material/colors';

// Image avatars
<Stack direction="row" spacing={2}>
  <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
  <Avatar alt="Travis Howard" src="/static/images/avatar/2.jpg" />
</Stack>

// Letter avatars
<Stack direction="row" spacing={2}>
  <Avatar>H</Avatar>
  <Avatar sx={{ bgcolor: deepOrange[500] }}>N</Avatar>
  <Avatar sx={{ bgcolor: deepPurple[500] }}>OP</Avatar>
</Stack>

// Sizes
<Stack direction="row" spacing={2}>
  <Avatar sx={{ width: 24, height: 24 }}>S</Avatar>
  <Avatar>M</Avatar>
  <Avatar sx={{ width: 56, height: 56 }}>L</Avatar>
</Stack>

// Variants
<Stack direction="row" spacing={2}>
  <Avatar variant="circular">C</Avatar>
  <Avatar variant="rounded">R</Avatar>
  <Avatar variant="square">S</Avatar>
</Stack>

// Fallback
<Avatar alt="Broken Image" src="/broken-image.jpg">B</Avatar>
```

#### Badge
- **Description**: Small count or status indicator overlay
- **Key Testable Properties**:
  - `badgeContent`: Display content
  - `color`: Theme color
  - `variant`: dot/standard
  - `max`: Maximum display value
  - `invisible`: Hide badge
  - `showZero`: Show zero values

**Code Example**:
```jsx
import Badge from '@mui/material/Badge';
import MailIcon from '@mui/icons-material/Mail';

// Basic badge
<Badge badgeContent={4} color="primary">
  <MailIcon />
</Badge>

// Colors
<Stack spacing={2} direction="row">
  <Badge badgeContent={4} color="secondary">
    <MailIcon />
  </Badge>
  <Badge badgeContent={4} color="success">
    <MailIcon />
  </Badge>
  <Badge badgeContent={4} color="error">
    <MailIcon />
  </Badge>
</Stack>

// Max value
<Stack spacing={2} direction="row">
  <Badge badgeContent={99} color="primary">
    <MailIcon />
  </Badge>
  <Badge badgeContent={100} color="primary">
    <MailIcon />
  </Badge>
  <Badge badgeContent={1000} max={999} color="primary">
    <MailIcon />
  </Badge>
</Stack>

// Dot variant
<Badge color="secondary" variant="dot">
  <MailIcon />
</Badge>

// Show zero
<Badge badgeContent={0} showZero color="primary">
  <MailIcon />
</Badge>

// Invisible
const [invisible, setInvisible] = React.useState(false);

<Badge 
  color="secondary" 
  badgeContent={4} 
  invisible={invisible}
>
  <MailIcon />
</Badge>
```

#### Chip
- **Description**: Compact element representing information or actions
- **Key Testable Properties**:
  - `label`: Display text
  - `onDelete`: Delete action
  - `onClick`: Click action
  - `disabled`: Disable interaction
  - `variant`: filled/outlined
  - `color`: Theme color
  - `icon`: Leading icon

**Code Example**:
```jsx
import Chip from '@mui/material/Chip';
import Avatar from '@mui/material/Avatar';
import FaceIcon from '@mui/icons-material/Face';
import DoneIcon from '@mui/icons-material/Done';

// Basic chip
<Chip label="Chip Filled" />
<Chip label="Chip Outlined" variant="outlined" />

// Clickable
<Chip label="Clickable" onClick={() => console.log('clicked')} />
<Chip 
  label="Clickable" 
  variant="outlined" 
  onClick={() => console.log('clicked')} 
/>

// Deletable
<Chip label="Deletable" onDelete={() => console.log('deleted')} />
<Chip 
  label="Deletable" 
  variant="outlined" 
  onDelete={() => console.log('deleted')} 
/>

// Custom delete icon
<Chip
  label="Custom delete icon"
  onDelete={() => console.log('deleted')}
  deleteIcon={<DoneIcon />}
/>

// With avatar
<Chip avatar={<Avatar>M</Avatar>} label="Avatar" />
<Chip
  avatar={<Avatar alt="Natacha" src="/static/images/avatar/1.jpg" />}
  label="Avatar"
  variant="outlined"
/>

// With icon
<Chip icon={<FaceIcon />} label="With Icon" />
<Chip icon={<FaceIcon />} label="With Icon" variant="outlined" />

// Colors
<Stack direction="row" spacing={1}>
  <Chip label="primary" color="primary" />
  <Chip label="success" color="success" />
  <Chip label="primary" color="primary" variant="outlined" />
  <Chip label="success" color="success" variant="outlined" />
</Stack>

// Sizes
<Chip label="Small" size="small" />
<Chip label="Medium" />
```

#### Divider
- **Description**: Visual separator between content sections
- **Key Testable Properties**:
  - `orientation`: horizontal/vertical
  - `variant`: fullWidth/inset/middle
  - `textAlign`: left/center/right
  - `flexItem`: Flex container behavior

#### Icons
- **Description**: Visual symbols and indicators
- **Key Testable Properties**:
  - `fontSize`: inherit/small/medium/large
  - `color`: Theme color
  - `onClick`: Click event (when wrapped in IconButton)

#### List
- **Description**: Vertical arrangement of related items
- **Key Testable Properties**:
  - `dense`: Compact spacing
  - `disablePadding`: Remove padding
  - `subheader`: Section header
  - Item selection states

**Code Example**:
```jsx
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListSubheader from '@mui/material/ListSubheader';
import Divider from '@mui/material/Divider';
import InboxIcon from '@mui/icons-material/Inbox';
import DraftsIcon from '@mui/icons-material/Drafts';

// Basic list
<List>
  <ListItem>
    <ListItemText primary="Inbox" />
  </ListItem>
  <ListItem>
    <ListItemText primary="Drafts" />
  </ListItem>
</List>

// With icons
<List>
  <ListItem>
    <ListItemIcon>
      <InboxIcon />
    </ListItemIcon>
    <ListItemText primary="Inbox" />
  </ListItem>
  <ListItem>
    <ListItemIcon>
      <DraftsIcon />
    </ListItemIcon>
    <ListItemText primary="Drafts" />
  </ListItem>
</List>

// Interactive list
<List component="nav">
  <ListItemButton>
    <ListItemIcon>
      <InboxIcon />
    </ListItemIcon>
    <ListItemText primary="Inbox" />
  </ListItemButton>
  <ListItemButton>
    <ListItemIcon>
      <DraftsIcon />
    </ListItemIcon>
    <ListItemText primary="Drafts" />
  </ListItemButton>
</List>

// Selected item
const [selectedIndex, setSelectedIndex] = React.useState(1);

<List component="nav">
  <ListItemButton
    selected={selectedIndex === 0}
    onClick={() => setSelectedIndex(0)}
  >
    <ListItemText primary="Inbox" />
  </ListItemButton>
  <ListItemButton
    selected={selectedIndex === 1}
    onClick={() => setSelectedIndex(1)}
  >
    <ListItemText primary="Drafts" />
  </ListItemButton>
</List>

// With subheader
<List
  subheader={
    <ListSubheader component="div">
      Nested List Items
    </ListSubheader>
  }
>
  <ListItem>
    <ListItemText primary="Item 1" />
  </ListItem>
</List>

// Dense list
<List dense>
  <ListItem>
    <ListItemText primary="Dense item 1" />
  </ListItem>
  <ListItem>
    <ListItemText primary="Dense item 2" />
  </ListItem>
</List>
```

#### Table
- **Description**: Data display in rows and columns
- **Key Testable Properties**:
  - `size`: small/medium
  - `stickyHeader`: Fixed header
  - `onSort`: Column sorting
  - Row selection
  - Pagination integration

**Code Example**:
```jsx
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

// Basic table
function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
  createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
  createData('Eclair', 262, 16.0, 24, 6.0),
];

<TableContainer component={Paper}>
  <Table sx={{ minWidth: 650 }} aria-label="simple table">
    <TableHead>
      <TableRow>
        <TableCell>Dessert (100g serving)</TableCell>
        <TableCell align="right">Calories</TableCell>
        <TableCell align="right">Fat&nbsp;(g)</TableCell>
        <TableCell align="right">Carbs&nbsp;(g)</TableCell>
        <TableCell align="right">Protein&nbsp;(g)</TableCell>
      </TableRow>
    </TableHead>
    <TableBody>
      {rows.map((row) => (
        <TableRow
          key={row.name}
          sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
        >
          <TableCell component="th" scope="row">
            {row.name}
          </TableCell>
          <TableCell align="right">{row.calories}</TableCell>
          <TableCell align="right">{row.fat}</TableCell>
          <TableCell align="right">{row.carbs}</TableCell>
          <TableCell align="right">{row.protein}</TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
</TableContainer>

// Dense table
<Table size="small">
  {/* table content */}
</Table>

// Sticky header
<TableContainer component={Paper} sx={{ maxHeight: 440 }}>
  <Table stickyHeader aria-label="sticky table">
    {/* table content */}
  </Table>
</TableContainer>
```

#### Tooltip
- **Description**: Informative text shown on hover/focus
- **Key Testable Properties**:
  - `title`: Tooltip content
  - `open`: Controlled state
  - `onOpen`/`onClose`: State events
  - `placement`: Position relative to target
  - `arrow`: Show arrow pointer

#### Typography
- **Description**: Text with consistent Material Design styling
- **Key Testable Properties**:
  - `variant`: h1-h6/subtitle/body/caption/etc
  - `component`: HTML element override
  - `color`: Text color
  - `align`: Text alignment
  - `gutterBottom`: Bottom margin

**Code Example**:
```jsx
import Typography from '@mui/material/Typography';

// Variants
<Typography variant="h1">h1. Heading</Typography>
<Typography variant="h2">h2. Heading</Typography>
<Typography variant="h3">h3. Heading</Typography>
<Typography variant="h4">h4. Heading</Typography>
<Typography variant="h5">h5. Heading</Typography>
<Typography variant="h6">h6. Heading</Typography>
<Typography variant="subtitle1">
  subtitle1. Lorem ipsum dolor sit amet
</Typography>
<Typography variant="subtitle2">
  subtitle2. Lorem ipsum dolor sit amet
</Typography>
<Typography variant="body1">
  body1. Lorem ipsum dolor sit amet
</Typography>
<Typography variant="body2">
  body2. Lorem ipsum dolor sit amet
</Typography>
<Typography variant="button" display="block">
  button text
</Typography>
<Typography variant="caption" display="block">
  caption text
</Typography>
<Typography variant="overline" display="block">
  overline text
</Typography>

// Component prop
<Typography variant="h1" component="h2">
  h1 styled as h2
</Typography>

// Colors
<Typography color="text.primary">text.primary</Typography>
<Typography color="text.secondary">text.secondary</Typography>
<Typography color="primary">primary</Typography>
<Typography color="secondary">secondary</Typography>
<Typography color="error">error</Typography>

// Alignment
<Typography align="left">Left aligned</Typography>
<Typography align="center">Center aligned</Typography>
<Typography align="right">Right aligned</Typography>
<Typography align="justify">Justified text</Typography>

// Gutter bottom
<Typography variant="body1" gutterBottom>
  Text with bottom margin
</Typography>
```

### 3. Feedback Components (6 components)

#### Alert
- **Description**: Prominent messages and notifications
- **Key Testable Properties**:
  - `severity`: error/warning/info/success
  - `onClose`: Dismissal event
  - `variant`: filled/outlined/standard
  - `icon`: Custom icon
  - `action`: Action buttons

**Code Example**:
```jsx
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

// Basic alerts
<Stack sx={{ width: '100%' }} spacing={2}>
  <Alert severity="error">This is an error alert!</Alert>
  <Alert severity="warning">This is a warning alert!</Alert>
  <Alert severity="info">This is an info alert!</Alert>
  <Alert severity="success">This is a success alert!</Alert>
</Stack>

// With titles
<Alert severity="error">
  <AlertTitle>Error</AlertTitle>
  This is an error alert — <strong>check it out!</strong>
</Alert>

// Outlined variant
<Stack sx={{ width: '100%' }} spacing={2}>
  <Alert variant="outlined" severity="error">
    This is an error alert!
  </Alert>
  <Alert variant="outlined" severity="warning">
    This is a warning alert!
  </Alert>
</Stack>

// Filled variant
<Stack sx={{ width: '100%' }} spacing={2}>
  <Alert variant="filled" severity="error">
    This is an error alert!
  </Alert>
  <Alert variant="filled" severity="success">
    This is a success alert!
  </Alert>
</Stack>

// With action
<Alert
  onClose={() => {}}
  action={
    <Button color="inherit" size="small">
      UNDO
    </Button>
  }
>
  This Alert displays a custom action.
</Alert>
```

#### Backdrop
- **Description**: Background overlay for focus management
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClick`: Click event
  - `invisible`: Transparent mode

#### Dialog
- **Description**: Modal popup window for user interactions
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `fullScreen`: Full screen mode
  - `maxWidth`: Size constraint
  - `scroll`: paper/body

**Code Example**:
```jsx
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

// Basic dialog
const [open, setOpen] = React.useState(false);

<Button variant="outlined" onClick={() => setOpen(true)}>
  Open dialog
</Button>
<Dialog open={open} onClose={() => setOpen(false)}>
  <DialogTitle>Subscribe</DialogTitle>
  <DialogContent>
    <DialogContentText>
      To subscribe to this website, please enter your email address here.
    </DialogContentText>
    <TextField
      autoFocus
      margin="dense"
      id="email"
      label="Email Address"
      type="email"
      fullWidth
      variant="standard"
    />
  </DialogContent>
  <DialogActions>
    <Button onClick={() => setOpen(false)}>Cancel</Button>
    <Button onClick={() => setOpen(false)}>Subscribe</Button>
  </DialogActions>
</Dialog>

// Alert dialog
<Dialog
  open={open}
  onClose={handleClose}
  aria-labelledby="alert-dialog-title"
  aria-describedby="alert-dialog-description"
>
  <DialogTitle id="alert-dialog-title">
    {"Use Google's location service?"}
  </DialogTitle>
  <DialogContent>
    <DialogContentText id="alert-dialog-description">
      Let Google help apps determine location.
    </DialogContentText>
  </DialogContent>
  <DialogActions>
    <Button onClick={handleClose}>Disagree</Button>
    <Button onClick={handleClose} autoFocus>
      Agree
    </Button>
  </DialogActions>
</Dialog>

// Full-screen dialog
<Dialog
  fullScreen={fullScreen}
  open={open}
  onClose={handleClose}
>
  <DialogTitle>Full Screen Dialog</DialogTitle>
  {/* content */}
</Dialog>

// Max width
<Dialog
  open={open}
  onClose={handleClose}
  maxWidth="sm"
  fullWidth
>
  <DialogTitle>Optional sizes</DialogTitle>
  {/* content */}
</Dialog>
```

#### Progress (Circular/Linear)
- **Description**: Loading or progress indicators
- **Key Testable Properties**:
  - `variant`: determinate/indeterminate
  - `value`: Progress percentage
  - `color`: Theme color
  - `size`: Component size

#### Skeleton
- **Description**: Loading placeholder animations
- **Key Testable Properties**:
  - `variant`: text/circular/rectangular
  - `animation`: wave/pulse/false
  - `width`/`height`: Dimensions

#### Snackbar
- **Description**: Brief notification messages
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `autoHideDuration`: Auto-dismiss time
  - `message`: Notification text
  - `action`: Action buttons

**Code Example**:
```jsx
import Snackbar from '@mui/material/Snackbar';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import Alert from '@mui/material/Alert';

// Basic snackbar
const [open, setOpen] = React.useState(false);

<Button onClick={() => setOpen(true)}>Open snackbar</Button>
<Snackbar
  open={open}
  autoHideDuration={6000}
  onClose={() => setOpen(false)}
  message="Note archived"
/>

// With action
<Snackbar
  open={open}
  autoHideDuration={6000}
  onClose={() => setOpen(false)}
  message="Note archived"
  action={
    <Button color="secondary" size="small" onClick={() => setOpen(false)}>
      UNDO
    </Button>
  }
/>

// Positioned snackbar
<Snackbar
  anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
  open={open}
  onClose={handleClose}
  message="I love snacks"
/>

// With Alert
<Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
  <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
    This is a success message!
  </Alert>
</Snackbar>

// Custom close icon
const action = (
  <React.Fragment>
    <Button color="secondary" size="small" onClick={handleClose}>
      UNDO
    </Button>
    <IconButton
      size="small"
      aria-label="close"
      color="inherit"
      onClick={handleClose}
    >
      <CloseIcon fontSize="small" />
    </IconButton>
  </React.Fragment>
);

<Snackbar
  open={open}
  autoHideDuration={6000}
  onClose={handleClose}
  message="Note archived"
  action={action}
/>
```

### 4. Surface Components (4 components)

#### Accordion
- **Description**: Expandable/collapsible content panels
- **Key Testable Properties**:
  - `expanded`: Expansion state
  - `onChange`: State change event
  - `disabled`: Disable interaction
  - `defaultExpanded`: Initial state

#### App Bar
- **Description**: Top navigation and branding header
- **Key Testable Properties**:
  - `position`: fixed/absolute/sticky/static/relative
  - `color`: Theme color
  - `elevation`: Shadow depth
  - `variant`: regular/dense

#### Card
- **Description**: Container for related content and actions
- **Key Testable Properties**:
  - `raised`: Elevation on hover
  - `variant`: outlined/elevation
  - `onClick`: Click event (if actionable)

#### Paper
- **Description**: Physical sheet surface with elevation
- **Key Testable Properties**:
  - `elevation`: 0-24 shadow depth
  - `variant`: outlined/elevation
  - `square`: Remove border radius

### 5. Navigation Components (9 components)

#### Bottom Navigation
- **Description**: Mobile navigation bar at screen bottom
- **Key Testable Properties**:
  - `value`: Selected item
  - `onChange`: Selection change
  - `showLabels`: Always show labels

#### Breadcrumbs
- **Description**: Navigation path indicator
- **Key Testable Properties**:
  - `separator`: Custom separator
  - `maxItems`: Collapse threshold
  - `itemsBeforeCollapse`/`itemsAfterCollapse`: Collapse behavior

#### Drawer
- **Description**: Side navigation panel
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `anchor`: left/right/top/bottom
  - `variant`: permanent/persistent/temporary

#### Link
- **Description**: Navigation hyperlink component
- **Key Testable Properties**:
  - `href`: Target URL
  - `onClick`: Click event
  - `underline`: hover/always/none
  - `variant`: Typography variant
  - `color`: Link color

#### Menu
- **Description**: Popup list of options or actions
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `anchorEl`: Anchor element
  - `anchorOrigin`/`transformOrigin`: Positioning

#### Pagination
- **Description**: Page navigation controls
- **Key Testable Properties**:
  - `count`: Total pages
  - `page`: Current page
  - `onChange`: Page change event
  - `disabled`: Disable navigation
  - `variant`: text/outlined
  - `shape`: circular/rounded

#### Speed Dial
- **Description**: Floating action button with sub-actions
- **Key Testable Properties**:
  - `open`: Expansion state
  - `onOpen`/`onClose`: State events
  - `direction`: up/down/left/right
  - `hidden`: Visibility state

#### Stepper
- **Description**: Multi-step process progress indicator
- **Key Testable Properties**:
  - `activeStep`: Current step
  - `orientation`: horizontal/vertical
  - `variant`: linear/nonLinear
  - Step completion states

#### Tabs
- **Description**: Tabbed content navigation
- **Key Testable Properties**:
  - `value`: Selected tab
  - `onChange`: Tab change event
  - `variant`: standard/scrollable/fullWidth
  - `orientation`: horizontal/vertical
  - `scrollButtons`: auto/desktop/on/off

### 6. Layout Components (5 components)

#### Box
- **Description**: Generic flexible container component
- **Key Testable Properties**:
  - `sx`: Styling system
  - `component`: HTML element
  - Display and flex properties
  - Spacing and positioning

#### Container
- **Description**: Centers content horizontally with max-width
- **Key Testable Properties**:
  - `maxWidth`: xs/sm/md/lg/xl/false
  - `fixed`: Fixed max-width
  - `disableGutters`: Remove padding

#### Grid
- **Description**: Responsive 12-column layout system
- **Key Testable Properties**:
  - `container`/`item`: Component role
  - `spacing`: Gap between items
  - `xs/sm/md/lg/xl`: Breakpoint columns
  - `direction`: row/column
  - `justify`/`alignItems`: Alignment

#### Stack
- **Description**: One-dimensional layout helper
- **Key Testable Properties**:
  - `direction`: row/column
  - `spacing`: Gap between children
  - `divider`: Separator element
  - `alignItems`/`justifyContent`: Alignment

#### Image List
- **Description**: Responsive grid of images
- **Key Testable Properties**:
  - `cols`: Number of columns
  - `rowHeight`: Row height
  - `gap`: Spacing between images
  - `variant`: standard/quilted/woven/masonry

### 7. Utility Components (8 components)

#### Click Away Listener
- **Description**: Detects clicks outside wrapped element
- **Key Testable Properties**:
  - `onClickAway`: Outside click event
  - `mouseEvent`: Click event type
  - `touchEvent`: Touch event type

#### Modal
- **Description**: Base component for modal dialogs
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `disableEscapeKeyDown`: Disable ESC key
  - `keepMounted`: Keep in DOM when closed

#### No SSR
- **Description**: Prevents server-side rendering
- **Key Testable Properties**:
  - `fallback`: Loading content
  - `defer`: Defer rendering

#### Popover
- **Description**: Positioned floating content container
- **Key Testable Properties**:
  - `open`: Visibility state
  - `onClose`: Close event
  - `anchorEl`: Anchor element
  - `anchorOrigin`/`transformOrigin`: Positioning

#### Popper
- **Description**: Low-level positioning primitive
- **Key Testable Properties**:
  - `open`: Visibility state
  - `anchorEl`: Anchor element
  - `placement`: Position relative to anchor
  - `modifiers`: Positioning modifiers

#### Portal
- **Description**: Renders children outside DOM hierarchy
- **Key Testable Properties**:
  - `container`: Target container
  - `disablePortal`: Disable portal behavior

#### Textarea Autosize
- **Description**: Auto-resizing textarea component
- **Key Testable Properties**:
  - `minRows`: Minimum rows
  - `maxRows`: Maximum rows
  - `onChange`: Value change event

#### Transitions
- **Description**: Animation wrapper components
- **Types**: Fade, Grow, Slide, Zoom, Collapse
- **Key Testable Properties**:
  - `in`: Show/hide state
  - `timeout`: Animation duration
  - `direction`: Animation direction (for Slide)
  - `mountOnEnter`: Mount on first show
  - `unmountOnExit`: Unmount when hidden

### 8. Lab Components (Experimental) (3 components)

#### Timeline
- **Description**: Vertical timeline for chronological content
- **Key Testable Properties**:
  - `position`: left/right/alternate
  - Timeline item arrangement
  - Content alignment

#### Tree View
- **Description**: Hierarchical list with expandable nodes
- **Key Testable Properties**:
  - `expanded`: Expanded nodes
  - `selected`: Selected nodes
  - `onNodeToggle`: Expansion event
  - `onNodeSelect`: Selection event

#### Date/Time Pickers
- **Description**: Date and time selection components
- **Key Testable Properties**:
  - `value`: Selected date/time
  - `onChange`: Value change event
  - `disabled`: Disable selection
  - `minDate`/`maxDate`: Date constraints
  - `views`: Available views

## Common Properties

All MUI components support these common properties:
- **className**: Custom CSS class names
- **style**: Inline style object
- **sx**: MUI's powerful styling system
- **ref**: React ref forwarding
- **data-testid**: Testing library identifier

## Testing Considerations

### Interaction Testing
1. **Click Events**: Test onClick handlers and ripple effects
2. **Keyboard Navigation**: Tab order, Enter/Space activation
3. **Focus Management**: Focus states and accessibility
4. **Form Integration**: Value changes, validation, submission

### State Testing
1. **Controlled vs Uncontrolled**: Test both component modes
2. **Disabled States**: Ensure proper behavior when disabled
3. **Loading States**: Test async operations and placeholders
4. **Error States**: Validation and error display

### Accessibility Testing
1. **ARIA Attributes**: Proper roles and labels
2. **Keyboard Support**: Full keyboard operability
3. **Screen Reader**: Meaningful announcements
4. **Color Contrast**: WCAG compliance

### Responsive Testing
1. **Breakpoints**: xs, sm, md, lg, xl behavior
2. **Touch Support**: Mobile interactions
3. **Viewport Changes**: Dynamic layout adjustments

## Component Complexity Levels

### Basic (OK)
- Simple props and single interaction
- Examples: Button, Chip, Divider, Avatar

### Intermediate (GOOD)
- Multiple states and interactions
- Examples: TextField, Select, Checkbox, Switch

### Advanced (GREAT)
- Complex state management
- Examples: Autocomplete, DataGrid, DatePicker

### Expert (EXCELLENT)
- Multiple components integration
- Examples: Transfer List, Stepper with Forms, Complex Tables

This categorization helps prioritize test implementation and allocate appropriate testing resources for each component type.

## Code Examples Added

This document has been enhanced with practical code examples for key MUI components including:
- **Input Components**: Autocomplete, Button, Checkbox, Select, Switch, TextField, Slider
- **Data Display Components**: Avatar, Badge, Chip, Typography, List, Table  
- **Feedback Components**: Alert, Dialog, Snackbar

Each code example demonstrates:
- Basic usage patterns
- Different variants and states
- Event handling
- Common configurations
- Accessibility considerations

These examples provide a foundation for creating comprehensive test challenges for each component.