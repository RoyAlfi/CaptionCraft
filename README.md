# Caption Craft: Automated Subtitle Generation

## Description
Caption Craft is a two-part software tool developed at #### VeriSoft LTD.
Caption Craft designed to automate the creation of subtitles for video files. It utilizes advanced AI models to transcribe audio to text and then format this text into SRT files. The project consists of a Python script for processing the video and audio, and a user-friendly GUI application for easy operation without needing to write any code.

## Features
- **Automatic subtitle generation**: Convert spoken language in videos to accurate subtitles.
- **Support for multiple AI models**: Choose between models like tiny, base, small, medium, and large based on the desired balance between accuracy and performance.
- **Easy-to-use GUI**: Non-technical users can generate subtitles with just a few clicks.
- **Cross-platform**: Works on both Windows and macOS.

## Installation

### Prerequisites
- [Python] 3.11 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CaptionCraft.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd CaptionCraft
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### For Non-Technical Users
1. Install [python] from this link.
2. [Donload this project](https://github.com/RoyAlfi/CaptionCraft/archive/refs/heads/main.zip) and unzip it.
3. Do steps 2,3 from 'Setup', easy setup will upload in the future.
4. Open the `CaptionCraft.py` application.
5. Use the "Browse File" button to select your video file.
6. Choose the model size from the dropdown menu based on your preference for speed or accuracy.
you can see the models description [here](https://github.com/openai/whisper/blob/main/model-card.md)
7. Click "Create subtitles!" to start generating subtitles. The application will inform you when the subtitles are ready and open the folder containing the SRT file.

### For Technical Users
If you prefer to use the command line (faster):
1. Navigate to the project directory.
2. Run the script using the following command:
   ```bash
   python SrtAi.py <path_to_video> <model_name>
   ```
   Replace `<path_to_video>` with the path to your video file and `<model_name>` with either `tiny`, `base`, `small`, `medium`, or `large`.
3. The script will process the video, extract audio, and generate an SRT file in the same directory as the video.

## Contributing
Contributions are welcome! Please fork the project and submit a pull request with your improvements.


## Credits
This project uses several open-source packages:
- [PyQt5] for the GUI interface.
- [moviepy] for video processing.
- [termcolor] for terminal output coloring.
- [stable-ts] for the transcription using Whisper models.

[//]: #
[Python]: <https://www.python.org/downloads/>
[PyQt5]:<https://pypi.org/project/PyQt5/>
[moviepy]:<https://pypi.org/project/moviepy/>
[termcolor]:<https://pypi.org/project/termcolor/>
[stable-ts]: <https://pypi.org/project/stable-ts/1.4.0/>
