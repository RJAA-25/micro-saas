from pathlib import Path

from openai import OpenAI

client = OpenAI()

vision_response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Can you extract the information presented inside this image? Return only a short transcript containing the important details. Present it in a way that is to be delivered in speech for people with visual problems.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.unsplash.com/photo-1698795635777-09ddc4efbecd?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    },
                },
            ],
        }
    ],
    max_tokens=1000,
)

vision_summary = vision_response.choices[0].message.content
print(vision_summary)


speech_file_path = Path(__file__).parent / "speech.mp3"

speech_response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=vision_summary,
)

speech_response.stream_to_file(speech_file_path)
