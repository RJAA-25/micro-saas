from django.contrib import messages
from django.core.files.base import ContentFile
from django.shortcuts import redirect, render
from django.urls import reverse
from openai import APIConnectionError, APIError, OpenAI, RateLimitError

from .models import Image, Speech


def index(request):
    images = Image.objects.all()
    context = {
        "images": images,
    }
    return render(request, "image_speech/index.html", context)


def create(request):
    return render(request, "image_speech/create.html")


def generate(request):
    if request.method == "POST":
        image_url = request.POST.get("image_url", None)
        voice = request.POST.get("voice", "alloy")
        fail_url = reverse("image_speech:create")
        print(image_url)
        if image_url is None:
            return redirect(fail_url)

        client = OpenAI()
        try:
            # Image to Text
            vision = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "If there are any readable text found inside the image, extract the information and return only a short transcript containing the important details. If not, provide a short description for the image. No need to notify about missing text. Present it in a way that is to be delivered in speech for people with visual difficulties.",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=1000,
            )
            transcript = vision.choices[0].message.content
            image = Image.objects.create(image_url=image_url)

            # Text to Speech
            speech = Speech(image=image, transcript=transcript)
            audio = client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=transcript,
                response_format="mp3",
            )
            speech.audio_file.save(f"{speech.uuid}.mp3", ContentFile(audio.content))
            speech.save()

            messages.success(request, "Sample successfully generated")
            success_url = reverse("image_speech:detail", kwargs={"uuid": image.uuid})
            return redirect(success_url)

        except APIConnectionError as e:
            messages.error(request, "Failed to connect to OpenAI API")
        except RateLimitError as e:
            messages.error(request, "OpenAI API request exceeded rate limit")
        except APIError as e:
            messages.error(request, "OpenAI API returned an API Error")
    return redirect(fail_url)


def detail(request, uuid=None):
    image = Image.objects.get(uuid=uuid)
    speeches = image.speech_set.order_by("-created_at").all()
    context = {
        "image": image,
        "speeches": speeches,
    }

    return render(request, "image_speech/detail.html", context)


def regenerate(request, uuid=None):
    if request.method == "POST":
        image = Image.objects.get(uuid=uuid)
        voice = request.POST.get("voice", "alloy")
        client = OpenAI()
        try:
            # Image to Text
            vision = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "If there are any readable text found inside the image, extract the information and return only a short transcript containing the important details. If not, provide a short description for the image. No need to notify about missing text. Present it in a way that is to be delivered in speech for people with visual difficulties.",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image.image_url,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=1000,
            )
            transcript = vision.choices[0].message.content

            # Text to Speech
            speech = Speech(image=image, transcript=transcript)
            audio = client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=transcript,
                response_format="mp3",
            )
            speech.audio_file.save(f"{speech.uuid}.mp3", ContentFile(audio.content))
            speech.save()
            messages.success(request, "Sample successfully generated")
            success_url = reverse("image_speech:detail", kwargs={"uuid": image.uuid})
            return redirect(success_url)

        except APIConnectionError as e:
            messages.error(request, "Failed to connect to OpenAI API")
        except RateLimitError as e:
            messages.error(request, "OpenAI API request exceeded rate limit")
        except APIError as e:
            messages.error(request, "OpenAI API returned an API Error")

        success_url = reverse("image_speech:detail", kwargs={"uuid": image.uuid})
        return redirect(success_url)
    fail_url = reverse("image_speech:detail", kwargs={"uuid": image.uuid})
    return redirect(fail_url)
