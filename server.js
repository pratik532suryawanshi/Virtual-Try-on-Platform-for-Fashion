const express = require('express');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;

app.use(express.json());

// Mock user data (you'll replace this with a database)
const users = [];

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const { username, password } = req.body;

    // Check if the username is already taken
    if (users.find(user => user.username === username)) {
      return res.status(400).send('Username already exists');
    }

    // Hash the user's password before saving it
    const hashedPassword = await bcrypt.hash(password, 10);
    
    // Save the user data (you'll use a database in a real application)
    users.push({ username, password: hashedPassword });
    
    res.status(201).send('User registered successfully');
  } catch {
    res.status(500).send('An error occurred');
  }
});

// Mock glasses frames data
const glassesFrames = [
  { id: 1, name: 'Classic Aviator', imageUrl: 'aviator.png' },
  { id: 2, name: 'Round Frames', imageUrl: 'round.png' },
  // Add more frames data as needed
];

// Get the list of glasses frames
app.get('/glasses', (req, res) => {
  res.json(glassesFrames);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
