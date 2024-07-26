import sys
import os
from moviepy.editor import VideoFileClip
import stable_whisper
from termcolor import colored
import subprocess


def print_full_width_line(color='white', default_width=80):
    try:
        # Try to get the dynamic width of the terminal window
        width = os.get_terminal_size().columns
    except OSError:
        # Fallback to a default width if terminal size can't be determined
        width = default_width
    # Print a line of asterisks in the specified color
    print(colored('*' * width, color))







def extract_audio_from_video(video_path, output_audio_path):
    stage_color = 'yellow'
    # Log the initiation of the audio extraction process.
    print_full_width_line(stage_color)
    print(colored(f"Extracting audio from video: {video_path}", stage_color))
    
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(output_audio_path, codec='mp3')
        audio.close()
    
    # Confirm the completion of the audio extraction.
    print(colored(f"Audio extracted and saved to: {output_audio_path}", 'green'))
    print_full_width_line(stage_color)
    print("\n\n")

def transcribe_audio_to_srt(audio_path, video_file_path, model_name="small"):
    stage_color = 'light_cyan'
    print_full_width_line(stage_color)
    # Log the initiation of the transcription process.
    print(colored("Transcribing Audio...", stage_color))
    
    model = stable_whisper.load_model(model_name)

    
    result = model.transcribe(audio_path, fp16=False, regroup=False, only_voice_freq=True, word_timestamps = False)


    srt_content = result.to_srt_vtt()
    srt_file_path = f"{video_file_path[:-4]}.srt"  # replace .mp3 with .srt
    
    with open(srt_file_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    

    print_full_width_line(stage_color)
    print("\n\n")
    # Use green color to highlight the completion message.
    print_full_width_line('green')
    print(colored(f"Transcription Complete! Subtitles saved to -> [{srt_file_path}]", 'green'))
    print_full_width_line('green')
    print("\n\n\n")   
    

def open_folder(path):
    if sys.platform == "win32":
        path = path.replace('/', '\\')
        subprocess.run(['explorer', path], check=False)
    elif sys.platform == "darwin":
        subprocess.run(['open', path], check=True)
    else:  # Assuming Linux
        subprocess.run(['xdg-open', path], check=True) 



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <video_file_path> <model_name>")
        sys.exit(1)

    video_file_path = sys.argv[1]
    model_name = sys.argv[2]
    output_directory = os.path.dirname(video_file_path)

    audio_file_path = os.path.join(output_directory, 'extracted_audio.mp3')

    # Execute the audio extraction function.
    extract_audio_from_video(video_file_path, audio_file_path)
    
    # Execute the transcription function.
    transcribe_audio_to_srt(audio_file_path, video_file_path, model_name)

    # Open the folder containing the output files
    open_folder(output_directory)

    # Instructions for how to use the script, placed here for clarity.
    # python subtitlesScript.py path_to_video.mp4 model_name
    # model_name options: tiny, base, small, medium, large
