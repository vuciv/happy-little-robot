# 🤖✨ Happy Little Robot

*A Bob Ross-inspired coding companion that cheers you on while you play chess*

## Description

Welcome back, friends. Today on The Joy of Coding, we're going to paint ourselves a happy little program. Nothing too fancy — just a friendly little robot who cheers me on while I play chess.

We'll start with a blank canvas, a simple `main.py`, and gently brush in some happy little functions. Along the way, we'll make a few "happy little accidents" — missed imports, typos, even a panicked checkmate or two. But that's okay. In coding, just like in life, there are no mistakes… only opportunities to learn.

By the end, we'll have ourselves a supportive cowboy robot, whispering sweet encouragements as I blunder my way through the chessboard. It's silly, it's soothing, and it just might make you smile.

So grab your keyboard, your imagination, and maybe a cup of tea. Let's make something joyful together.

## What It Does

This delightful little program:
- 📸 Takes periodic screenshots of your screen
- 👁️ Uses Google's Gemini AI to analyze what's happening in your chess game
- 🎙️ Generates encouraging commentary using ElevenLabs text-to-speech
- 🤖 Shows a cute robot character overlay while speaking
- 💝 Spreads positivity and joy during your chess sessions

## Features

- **AI-Powered Encouragement**: Uses Google Gemini 2.0 Flash to understand your chess position and generate contextual support
- **Natural Voice**: ElevenLabs TTS brings your robot friend to life with a warm, encouraging voice
- **Visual Companion**: A charming robot character appears on screen during encouragement sessions
- **Non-Intrusive**: Runs quietly in the background, only appearing when you need a boost
- **Cross-Platform**: Works on macOS, Windows, and Linux

## Setup

### Prerequisites

- Python 3.8+
- Google API key (for Gemini)
- ElevenLabs API key

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/happy-little-robot.git
cd happy-little-robot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
GOOGLE_API_KEY=your_google_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

5. Add your robot character image as `pip.png` in the project directory

### Getting API Keys

**Google API Key:**
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Enable the Gemini API

**ElevenLabs API Key:**
1. Sign up at [ElevenLabs](https://elevenlabs.io/)
2. Go to your profile settings
3. Generate an API key

## Usage

Simply run the program and let it work its magic:

```bash
python main.py
```

The robot will:
1. Wait 3 seconds before starting
2. Take a screenshot every 30 seconds
3. Analyze your chess position
4. Provide encouraging commentary if it detects a chess game
5. Display the robot character while speaking

Press `Escape` while the robot is visible to dismiss it early.

## Customization

### Changing the Voice
Edit the `voice_id` in the `tts()` function to use different ElevenLabs voices.

### Adjusting Timing
Modify the `time.sleep()` values in the main loop to change how often the robot checks in.

### Personalizing Messages
Update the `PROMPT` variable to change the robot's personality and speaking style.

## File Structure

```
happy-little-robot/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── pip.png             # Robot character image
├── .env                # API keys (create this)
├── README.md           # This file
├── screenshot.png      # Temporary screenshot file
└── response.mp3        # Temporary audio file
```

## Technical Details

- **Screenshot Capture**: Uses PIL's ImageGrab for cross-platform screen capture
- **AI Vision**: Google Gemini 2.0 Flash analyzes screenshots for chess content
- **Text-to-Speech**: ElevenLabs API generates natural-sounding encouragement
- **Audio Playback**: pygame handles audio playback
- **UI Overlay**: tkinter creates the floating robot character window

## Contributing

This project was born from the joy of coding and the spirit of Bob Ross. Contributions are welcome! Whether you want to:

- Add new encouraging phrases
- Improve the robot's chess understanding
- Create new character designs
- Fix bugs or improve performance

Remember: there are no mistakes in open source, only happy little pull requests! 🎨

## Inspiration

This project channels the peaceful, encouraging spirit of Bob Ross's "The Joy of Painting." Just as Bob taught us that painting should be joyful and stress-free, this little robot reminds us that coding (and chess) should be fun too.

## License

This project is open source and available under the MIT License. Share the joy! ✨

---

*Remember: you are doing great, and you've got this.* 🤖💙

## Support

If you enjoy this project, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs or suggesting features
- 🎨 Contributing your own happy little improvements
- ☕ Buying the creator a coffee (because robots run on caffeine too)

Happy coding, friends! 🎨🤖✨
