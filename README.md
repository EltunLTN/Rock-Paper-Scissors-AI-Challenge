# Rock-Paper-Scissors AI Challenge 🎮

A web-based interactive Rock-Paper-Scissors game where you play against an AI opponent using hand gesture recognition via your webcam.

## Features

- 🖐️ **Real-time Hand Gesture Recognition** - Uses MediaPipe for accurate hand landmark detection
- 🎮 **Interactive Gameplay** - Play Rock, Paper, or Scissors with hand gestures
- 🤖 **AI Opponent** - Computer makes random moves
- 💻 **Web Interface** - Beautiful, responsive web UI built with Flask
- 📊 **Score Tracking** - Keep track of wins, losses, and ties
- ⚡ **Real-time Video Feed** - Live webcam stream with gesture detection

## Project Structure

```
rock-paper-scissors/
├── app.py                 # Flask application and game logic
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Web interface
└── static/
    ├── script.js         # Frontend JavaScript logic
    └── style.css         # Styling
```

## Requirements

- Python 3.8+
- Webcam/Camera device
- Modern web browser

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/rock-paper-scissors.git
cd rock-paper-scissors
```

2. **Install dependencies:**
```bash
pip install flask opencv-python mediapipe
```

## Usage

1. **Start the Flask server:**
```bash
python app.py
```

2. **Open your browser:**
Navigate to `http://localhost:5000`

3. **Play the game:**
   - Position your hand in front of the webcam
   - Show one of these gestures:
     - ✊ **Rock** - All fingers closed (fist)
     - ✋ **Paper** - All fingers open (palm)
     - ✌️ **Scissors** - Index and middle fingers up, others closed
   - The game will recognize your gesture and compare it with the AI's move
   - Score is updated in real-time

## Gesture Recognition Guide

| Gesture | Description | Code |
|---------|-------------|------|
| Rock ✊ | All fingers closed | `[0, 0, 0, 0, 0]` |
| Paper ✋ | All fingers open | `[1, 1, 1, 1, 1]` |
| Scissors ✌️ | Index + Middle up, others closed | `[0, 1, 1, 0, 0]` |
| Unknown | Unrecognized gesture | `unknown` |

## How It Works

1. **Hand Detection** - MediaPipe detects hand landmarks in real-time
2. **Gesture Recognition** - Analyzes finger positions to determine Rock/Paper/Scissors
3. **Game Logic** - Compares your move with computer's random selection
4. **Score Update** - Tracks wins and displays results on the web interface
5. **Real-time Display** - Video feed with detected gestures shown to user

## Game Rules

- **Rock beats Scissors** ✊ > ✌️
- **Scissors beats Paper** ✌️ > ✋
- **Paper beats Rock** ✋ > ✊
- **Same moves result in a tie**

## Troubleshooting

### Camera not working
- Check camera permissions in system settings
- Ensure no other application is using the camera
- Try reconnecting the camera device

### Gesture not recognized
- Ensure good lighting for accurate detection
- Keep your hand clearly visible to the camera
- Make clean, distinct hand gestures
- Try gestures at different distances from camera

### Flask server won't start
- Check if port 5000 is already in use
- Try running with a different port: `flask run --port 5001`
- Ensure Flask is properly installed

### MediaPipe errors
- Reinstall MediaPipe: `pip install --upgrade mediapipe`
- Check Python version compatibility (3.8+)

## Technologies Used

- **Flask** - Web framework
- **MediaPipe** - Hand gesture recognition
- **OpenCV** - Video capture and processing
- **HTML/CSS/JavaScript** - Frontend
- **Python** - Backend logic

## Future Enhancements

- [ ] Multiplayer mode
- [ ] Game statistics and history
- [ ] Difficulty levels
- [ ] Sound effects
- [ ] Mobile support
- [ ] Best-of-N matches
- [ ] Leaderboard system
- [ ] Gesture training mode

## License

This project is open source and available under the MIT License.

## Author

Created as an AI challenge project combining computer vision and interactive gaming.

## Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.

---

**Last Updated:** February 1, 2026