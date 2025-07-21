import json
import os
import re
from pathlib import Path
from kokoro.__main__ import generate_and_save_audio
# from kokoro.pipeline import KPipeline
# from kokoro.model import KModel

def clean_filename(text, max_length=50):
    """Create a safe filename from text"""
    # Remove special characters and replace with underscores
    filename = re.sub(r'[^\w\s-]', '', text)
    filename = re.sub(r'[-\s]+', '_', filename)
    # Limit length
    return filename[:max_length].strip('_')

def clean_content_for_tts(content):
    """Clean content for better TTS output"""
    # Remove markdown formatting
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)  # Bold
    content = re.sub(r'\*(.*?)\*', r'\1', content)      # Italic
    content = re.sub(r'`(.*?)`', r'\1', content)        # Code
    
    # Remove URLs
    content = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', content)
    
    # Remove excessive newlines and whitespace
    content = re.sub(r'\n+', ' ', content)
    content = re.sub(r'\s+', ' ', content)
    
    return content.strip()

def generate_audio_from_json(json_file_path, output_dir="audio_output", voice="af_bella"):
    """
    Generate audio files from JSON content using Kokoro TTS
    
    Args:
        json_file_path: Path to the JSON file
        output_dir: Directory to save audio files
        voice: Kokoro voice to use (options: af_bella, af_sarah, af_nicole, am_adam, am_michael, bf_emma, bf_isabella, bm_lewis, bm_george)
    """
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Initialize Kokoro TTS
    print("Initializing Kokoro TTS...")
    # tts = KPipeline('a')
    # tts.load_single_voice('af_bella')
    
    # Load JSON data
    print(f"Loading JSON data from {json_file_path}...")
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Found {len(data)} posts to process")
    
    # Process each post
    for i, post in enumerate(data, 1):
        try:
            print(f"Processing post {i}/{len(data)}: {post.get('title', 'Untitled')[:50]}...")
            
            # Get content
            content = post.get('content', '')
            if not content or len(content.strip()) < 10:
                print(f"Skipping post {i}: No substantial content")
                continue
            
            # Clean content for TTS
            clean_content = clean_content_for_tts(content)
            
            # Create filename
            title = post.get('title', f'Post_{i}')
            filename = clean_filename(title)
            post_id = post.get('id', str(i))
            audio_filename = f"{i:03d}_{filename}_{post_id}.wav"
            audio_path = Path(output_dir) / audio_filename
            
            # Skip if file already exists
            if os.path.exists(audio_path):
                print(f"Audio file already exists: {audio_filename}")
                continue
            
            # Generate audio
            print(f"Generating audio for: {title[:50]}...")
            # audio = tts.generate(clean_content, voice=voice)
            generate_and_save_audio(
                output_file=audio_path,
                text=clean_content,
                kokoro_language='a',  # Assuming English for simplicity
                voice= 'af_bella',  # Change this to the desired voice
                speed=1
            )
        
            # Save audio file
            # tts.save(audio, audio_path)
            print(f"Saved: {filename}+'.wav'")
            
        except Exception as e:
            print(f"Error processing post {i}: {str(e)}")
            continue
    
    print(f"Audio generation complete! Files saved in '{output_dir}' directory")

def list_available_voices():
    """List all available Kokoro voices"""
    voices = [
        "af_bella",    # American Female - Bella
        "af_sarah",    # American Female - Sarah  
        "af_nicole",   # American Female - Nicole
        "am_adam",     # American Male - Adam
        "am_michael",  # American Male - Michael
        "bf_emma",     # British Female - Emma
        "bf_isabella", # British Female - Isabella
        "bm_lewis",    # British Male - Lewis
        "bm_george"    # British Male - George
    ]
    
    print("Available Kokoro voices:")
    for voice in voices:
        print(f"  - {voice}")
    
    return voices

def main():
    """Main function to run the audio generator"""
    print("Kokoro TTS Audio Generator")
    print("=" * 30)
    
    # List available voices
    list_available_voices()
    
    # Configuration
    json_file = "reddit_content.json"  # Update this to your JSON file path
    output_directory = "audio_output"
    selected_voice = "af_bella"  # Change this to your preferred voice
    
    print(f"\nConfiguration:")
    print(f"JSON file: {json_file}")
    print(f"Output directory: {output_directory}")
    print(f"Selected voice: {selected_voice}")
    
    # Check if JSON file exists
    if not os.path.exists(json_file):
        print(f"\nError: JSON file '{json_file}' not found!")
        print("Please update the 'json_file' variable with the correct path to your JSON file.")
        return
    
    # Generate audio files
    print(f"\nStarting audio generation...")
    generate_audio_from_json(json_file, output_directory, selected_voice)

if __name__ == "__main__":
    main()

# Alternative usage examples:
"""
# Example 1: Basic usage
generate_audio_from_json("your_data.json")

# Example 2: Custom output directory and voice
generate_audio_from_json(
    json_file_path="reddit_posts.json",
    output_dir="my_audio_files", 
    voice="am_adam"
)

# Example 3: Process specific posts only
with open("reddit_posts.json", 'r') as f:
    data = json.load(f)

# Filter posts (e.g., only high-scoring posts)
high_score_posts = [post for post in data if post.get('score', 0) > 1000]

# Save filtered posts and generate audio
with open("high_score_posts.json", 'w') as f:
    json.dump(high_score_posts, f)

generate_audio_from_json("high_score_posts.json", "high_score_audio")
"""