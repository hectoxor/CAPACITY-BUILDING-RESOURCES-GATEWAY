import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
def videotrcsp(vidfile, vidname, lang):
    vidaud = vidname+'.wav'
    audioclip = AudioFileClip(vidfile)
    audioclip.write_audiofile(vidaud)
    with contextlib.closing(wave.open(vidaud,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    total_duration = math.ceil(duration / 60)
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(vidaud) as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open(vidname+'.txt', "a")
        f.write(r.recognize_google(audio, language=lang))
        f.write(" ")
    f.close()
def audiotrcsp(audfile, audname, lang):
    audioclip.write_audiofile(audfile)
    with contextlib.closing(wave.open(audfile,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    total_duration = math.ceil(duration / 60)
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(audfile) as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open(audname+'.txt', "a")
        f.write(r.recognize_google(audio, language=lang))
        f.write(" ")
    f.close()
