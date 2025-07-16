from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_youtube_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Print transcript with timestamps
        print("\n--- Transcript with Timestamps ---\n")
        for entry in transcript:
            start = entry['start']
            end = entry['start'] + entry['duration']
            text = entry['text']
            print(f"[{start:.2f}s - {end:.2f}s] {text}")

        # Optionally return raw data
        return transcript

    except Exception as e:
        print(f"Error: {e}")

# Example usage (replace with your own YouTube video ID)
video_url = "https://www.youtube.com/watch?v=hSw0rFS0V5A"  # Example
video_id = video_url.split("v=")[-1]
get_youtube_transcript(video_id)
