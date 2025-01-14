"""Get Transcript Given a YouTube Video ID."""

from youtube_transcript_api import YouTubeTranscriptApi # type: ignore[import-untyped]


def get_video_transcript(input_video_id: str) -> str:
    """
    Retrieve and process transcript from a YouTube Video.

    Input:
    -----
    video_id : String containing id of YouTube Video get the transcript from

    Returns
    -------
    video_transcript: Multi-Line String containing full transcript of the requested video

    """
    # Call YoutubeTranscriptAPI to retrieve transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id=input_video_id)

    return transcript
