# Happy Little Robot

A chess companion that takes screenshots and gives encouraging commentary.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```env
GOOGLE_API_KEY=your_google_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

3. Add a robot image as `pip.png`

## Usage

```bash
python main.py
```

Takes a screenshot every 30 seconds, analyzes it with AI, and plays encouraging audio through a robot character overlay. Press Escape to dismiss the robot early.
