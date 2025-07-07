# MUI Component Examples

## 1. Button Component

### Basic Usage
```jsx
import Button from '@mui/material/Button';

// Basic buttons
<Button variant="text">Text</Button>
<Button variant="contained">Contained</Button>
<Button variant="outlined">Outlined</Button>
```

### Different Variants and States
```jsx
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import SendIcon from '@mui/icons-material/Send';
import Stack from '@mui/material/Stack';

// Variants
<Button variant="text">Text Button</Button>
<Button variant="contained">Contained Button</Button>
<Button variant="outlined">Outlined Button</Button>

// Disabled state
<Button variant="outlined" disabled>
  Disabled
</Button>

// Different colors
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
```

### Event Handling
```jsx
import Button from '@mui/material/Button';

function HandleClick() {
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <Button variant="contained" onClick={handleClick}>
      Click me
    </Button>
  );
}
```

## 2. TextField Component

### Basic Usage
```jsx
import TextField from '@mui/material/TextField';

// Basic text field
<TextField id="outlined-basic" label="Outlined" variant="outlined" />
<TextField id="filled-basic" label="Filled" variant="filled" />
<TextField id="standard-basic" label="Standard" variant="standard" />
```

### Different Variants and Props
```jsx
import TextField from '@mui/material/TextField';

// Required field
<TextField
  required
  id="outlined-required"
  label="Required"
  defaultValue="Hello World"
/>

// Disabled field
<TextField
  disabled
  id="outlined-disabled"
  label="Disabled"
  defaultValue="Hello World"
/>

// Password field
<TextField
  id="outlined-password-input"
  label="Password"
  type="password"
  autoComplete="current-password"
/>

// Read only
<TextField
  id="outlined-read-only-input"
  label="Read Only"
  defaultValue="Hello World"
  InputProps={{
    readOnly: true,
  }}
/>

// Number input
<TextField
  id="outlined-number"
  label="Number"
  type="number"
  InputLabelProps={{
    shrink: true,
  }}
/>

// Multiline
<TextField
  id="outlined-multiline-static"
  label="Multiline"
  multiline
  rows={4}
  defaultValue="Default Value"
/>

// With helper text
<TextField
  id="outlined-helperText"
  label="Helper text"
  defaultValue="Default Value"
  helperText="Some important text"
/>

// Error state
<TextField
  error
  id="outlined-error"
  label="Error"
  defaultValue="Hello World"
  helperText="Incorrect entry."
/>
```

### Event Handling
```jsx
import React, { useState } from 'react';
import TextField from '@mui/material/TextField';

function ControlledTextField() {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <TextField
      id="outlined-controlled"
      label="Controlled"
      value={value}
      onChange={handleChange}
    />
  );
}
```

## 3. Select Component

### Basic Usage
```jsx
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

<FormControl fullWidth>
  <InputLabel id="demo-simple-select-label">Age</InputLabel>
  <Select
    labelId="demo-simple-select-label"
    id="demo-simple-select"
    value={age}
    label="Age"
    onChange={handleChange}
  >
    <MenuItem value={10}>Ten</MenuItem>
    <MenuItem value={20}>Twenty</MenuItem>
    <MenuItem value={30}>Thirty</MenuItem>
  </Select>
</FormControl>
```

### Different Variants
```jsx
import React, { useState } from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

function BasicSelect() {
  const [age, setAge] = useState('');

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Age</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          label="Age"
          onChange={handleChange}
        >
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>

      {/* Filled variant */}
      <FormControl variant="filled" sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-filled-label">Age</InputLabel>
        <Select
          labelId="demo-simple-select-filled-label"
          id="demo-simple-select-filled"
          value={age}
          onChange={handleChange}
        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>

      {/* Standard variant */}
      <FormControl variant="standard" sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-standard-label">Age</InputLabel>
        <Select
          labelId="demo-simple-select-standard-label"
          id="demo-simple-select-standard"
          value={age}
          onChange={handleChange}
          label="Age"
        >
          <MenuItem value="">
            <em>None</em>
          </MenuItem>
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}
```

### Multiple Selection
```jsx
import React, { useState } from 'react';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const names = [
  'Oliver Hansen',
  'Van Henry',
  'April Tucker',
  'Ralph Hubbard',
];

function MultipleSelect() {
  const [personName, setPersonName] = useState([]);

  const handleChange = (event) => {
    const {
      target: { value },
    } = event;
    setPersonName(
      typeof value === 'string' ? value.split(',') : value,
    );
  };

  return (
    <FormControl sx={{ m: 1, width: 300 }}>
      <InputLabel id="demo-multiple-name-label">Name</InputLabel>
      <Select
        labelId="demo-multiple-name-label"
        id="demo-multiple-name"
        multiple
        value={personName}
        onChange={handleChange}
        input={<OutlinedInput label="Name" />}
      >
        {names.map((name) => (
          <MenuItem key={name} value={name}>
            {name}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
```

## 4. Checkbox Component

### Basic Usage
```jsx
import Checkbox from '@mui/material/Checkbox';

<Checkbox defaultChecked />
<Checkbox />
<Checkbox disabled />
<Checkbox disabled checked />
```

### With Label
```jsx
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

<FormGroup>
  <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
  <FormControlLabel disabled control={<Checkbox />} label="Disabled" />
</FormGroup>
```

### Different States and Colors
```jsx
import Checkbox from '@mui/material/Checkbox';
import { pink } from '@mui/material/colors';

// Different colors
<Checkbox defaultChecked />
<Checkbox defaultChecked color="secondary" />
<Checkbox defaultChecked color="success" />
<Checkbox defaultChecked color="default" />

// Custom color
<Checkbox
  defaultChecked
  sx={{
    color: pink[800],
    '&.Mui-checked': {
      color: pink[600],
    },
  }}
/>

// Different sizes
<Checkbox defaultChecked size="small" />
<Checkbox defaultChecked />
<Checkbox
  defaultChecked
  sx={{ '& .MuiSvgIcon-root': { fontSize: 28 } }}
/>
```

### Event Handling
```jsx
import React, { useState } from 'react';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

function ControlledCheckbox() {
  const [checked, setChecked] = useState(true);

  const handleChange = (event) => {
    setChecked(event.target.checked);
  };

  return (
    <FormControlLabel
      control={
        <Checkbox
          checked={checked}
          onChange={handleChange}
          name="checkedB"
          color="primary"
        />
      }
      label="Controlled Checkbox"
    />
  );
}
```

## 5. Switch Component

### Basic Usage
```jsx
import Switch from '@mui/material/Switch';

<Switch defaultChecked />
<Switch />
<Switch disabled defaultChecked />
<Switch disabled />
```

### With Label
```jsx
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';

<FormGroup>
  <FormControlLabel control={<Switch defaultChecked />} label="Label" />
  <FormControlLabel disabled control={<Switch />} label="Disabled" />
</FormGroup>
```

### Different Sizes and Colors
```jsx
import Switch from '@mui/material/Switch';
import FormControlLabel from '@mui/material/FormControlLabel';

// Sizes
<FormControlLabel control={<Switch defaultChecked size="small" />} label="Small" />
<FormControlLabel control={<Switch defaultChecked />} label="Medium" />

// Colors
<Switch defaultChecked color="primary" />
<Switch defaultChecked color="secondary" />
<Switch defaultChecked color="warning" />
<Switch defaultChecked color="default" />
```

### Event Handling
```jsx
import React, { useState } from 'react';
import Switch from '@mui/material/Switch';

function ControlledSwitch() {
  const [checked, setChecked] = useState(true);

  const handleChange = (event) => {
    setChecked(event.target.checked);
  };

  return (
    <Switch
      checked={checked}
      onChange={handleChange}
      inputProps={{ 'aria-label': 'controlled' }}
    />
  );
}
```

## 6. Radio Component

### Basic Usage
```jsx
import Radio from '@mui/material/Radio';

<Radio />
<Radio checked />
<Radio disabled />
```

### Radio Group
```jsx
import React, { useState } from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

function RadioButtonsGroup() {
  const [value, setValue] = useState('female');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <FormControl>
      <FormLabel id="demo-radio-buttons-group-label">Gender</FormLabel>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="female"
        name="radio-buttons-group"
        value={value}
        onChange={handleChange}
      >
        <FormControlLabel value="female" control={<Radio />} label="Female" />
        <FormControlLabel value="male" control={<Radio />} label="Male" />
        <FormControlLabel value="other" control={<Radio />} label="Other" />
      </RadioGroup>
    </FormControl>
  );
}
```

### Different Arrangements
```jsx
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

// Row direction
<FormControl>
  <FormLabel id="demo-row-radio-buttons-group-label">Gender</FormLabel>
  <RadioGroup
    row
    aria-labelledby="demo-row-radio-buttons-group-label"
    name="row-radio-buttons-group"
  >
    <FormControlLabel value="female" control={<Radio />} label="Female" />
    <FormControlLabel value="male" control={<Radio />} label="Male" />
    <FormControlLabel value="other" control={<Radio />} label="Other" />
    <FormControlLabel
      value="disabled"
      disabled
      control={<Radio />}
      label="Disabled"
    />
  </RadioGroup>
</FormControl>
```

### Custom Colors
```jsx
import Radio from '@mui/material/Radio';
import { pink } from '@mui/material/colors';

<Radio color="secondary" />
<Radio color="success" />
<Radio color="default" />
<Radio
  sx={{
    color: pink[800],
    '&.Mui-checked': {
      color: pink[600],
    },
  }}
/>
```

## 7. Autocomplete Component

### Basic Usage
```jsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

const top100Films = [
  { label: 'The Shawshank Redemption', year: 1994 },
  { label: 'The Godfather', year: 1972 },
  { label: 'The Godfather: Part II', year: 1974 },
  // ... more options
];

<Autocomplete
  disablePortal
  id="combo-box-demo"
  options={top100Films}
  sx={{ width: 300 }}
  renderInput={(params) => <TextField {...params} label="Movie" />}
/>
```

### Controlled Component
```jsx
import React, { useState } from 'react';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

function ControlledAutocomplete() {
  const [value, setValue] = useState(null);
  const [inputValue, setInputValue] = useState('');

  return (
    <Autocomplete
      value={value}
      onChange={(event, newValue) => {
        setValue(newValue);
      }}
      inputValue={inputValue}
      onInputChange={(event, newInputValue) => {
        setInputValue(newInputValue);
      }}
      id="controllable-states-demo"
      options={options}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="Controllable" />}
    />
  );
}
```

### Free Solo (Allow Custom Values)
```jsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

<Autocomplete
  freeSolo
  id="free-solo-demo"
  disableClearable
  options={top100Films.map((option) => option.label)}
  renderInput={(params) => (
    <TextField
      {...params}
      label="Search input"
      InputProps={{
        ...params.InputProps,
        type: 'search',
      }}
    />
  )}
/>
```

### Multiple Selection
```jsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Chip from '@mui/material/Chip';

<Autocomplete
  multiple
  id="tags-filled"
  options={top100Films.map((option) => option.label)}
  defaultValue={[top100Films[13].label]}
  freeSolo
  renderTags={(value, getTagProps) =>
    value.map((option, index) => (
      <Chip variant="outlined" label={option} {...getTagProps({ index })} />
    ))
  }
  renderInput={(params) => (
    <TextField
      {...params}
      variant="filled"
      label="Favorites"
      placeholder="Favorites"
    />
  )}
/>
```

### Custom Rendering
```jsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';

<Autocomplete
  id="country-select-demo"
  sx={{ width: 300 }}
  options={countries}
  autoHighlight
  getOptionLabel={(option) => option.label}
  renderOption={(props, option) => (
    <Box component="li" sx={{ '& > img': { mr: 2, flexShrink: 0 } }} {...props}>
      <img
        loading="lazy"
        width="20"
        src={`https://flagcdn.com/w20/${option.code.toLowerCase()}.png`}
        srcSet={`https://flagcdn.com/w40/${option.code.toLowerCase()}.png 2x`}
        alt=""
      />
      {option.label} ({option.code}) +{option.phone}
    </Box>
  )}
  renderInput={(params) => (
    <TextField
      {...params}
      label="Choose a country"
      inputProps={{
        ...params.inputProps,
        autoComplete: 'new-password', // disable autocomplete and autofill
      }}
    />
  )}
/>
```

## 8. Slider Component

### Basic Usage
```jsx
import Slider from '@mui/material/Slider';

<Slider defaultValue={30} />
<Slider defaultValue={30} disabled />
```

### Different Configurations
```jsx
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';

// Discrete slider
<Slider
  aria-label="Temperature"
  defaultValue={30}
  valueLabelDisplay="auto"
  step={10}
  marks
  min={10}
  max={110}
/>

// Small steps
<Slider
  defaultValue={0.00000005}
  aria-label="Small steps"
  step={0.00000001}
  marks
  min={-0.00000005}
  max={0.0000001}
  valueLabelDisplay="auto"
/>

// Custom marks
const marks = [
  {
    value: 0,
    label: '0°C',
  },
  {
    value: 20,
    label: '20°C',
  },
  {
    value: 37,
    label: '37°C',
  },
  {
    value: 100,
    label: '100°C',
  },
];

<Slider
  aria-label="Always visible"
  defaultValue={80}
  step={10}
  marks={marks}
  valueLabelDisplay="on"
/>

// Range slider
<Slider
  getAriaLabel={() => 'Temperature range'}
  value={value}
  onChange={handleChange}
  valueLabelDisplay="auto"
  getAriaValueText={valuetext}
/>
```

### Vertical Slider
```jsx
import Slider from '@mui/material/Slider';

<Slider
  sx={{
    '& input[type="range"]': {
      WebkitAppearance: 'slider-vertical',
    },
  }}
  orientation="vertical"
  defaultValue={30}
  aria-label="Temperature"
  valueLabelDisplay="auto"
/>
```

### Event Handling
```jsx
import React, { useState } from 'react';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';

function ControlledSlider() {
  const [value, setValue] = useState(30);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <>
      <Typography id="input-slider" gutterBottom>
        Value: {value}
      </Typography>
      <Slider
        value={value}
        onChange={handleChange}
        aria-labelledby="input-slider"
      />
    </>
  );
}
```

### Custom Styling
```jsx
import Slider from '@mui/material/Slider';
import { styled } from '@mui/material/styles';

const PrettoSlider = styled(Slider)({
  color: '#52af77',
  height: 8,
  '& .MuiSlider-track': {
    border: 'none',
  },
  '& .MuiSlider-thumb': {
    height: 24,
    width: 24,
    backgroundColor: '#fff',
    border: '2px solid currentColor',
    '&:focus, &:hover, &.Mui-active, &.Mui-focusVisible': {
      boxShadow: 'inherit',
    },
    '&:before': {
      display: 'none',
    },
  },
  '& .MuiSlider-valueLabel': {
    lineHeight: 1.2,
    fontSize: 12,
    background: 'unset',
    padding: 0,
    width: 32,
    height: 32,
    borderRadius: '50% 50% 50% 0',
    backgroundColor: '#52af77',
    transformOrigin: 'bottom left',
    transform: 'translate(50%, -100%) rotate(-45deg) scale(0)',
    '&:before': { display: 'none' },
    '&.MuiSlider-valueLabelOpen': {
      transform: 'translate(50%, -100%) rotate(-45deg) scale(1)',
    },
    '& > *': {
      transform: 'rotate(45deg)',
    },
  },
});

<PrettoSlider
  valueLabelDisplay="auto"
  aria-label="pretto slider"
  defaultValue={20}
/>
```