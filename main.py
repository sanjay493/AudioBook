import pyttsx3
import PyPDF2

book = open('pdfbook.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)
speaker = pyttsx3.init()
""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)  # printing current voice rate
speaker.setProperty('rate', 125)     # setting up new voice rate

"""VOLUME"""
volume = speaker.getProperty(
    'volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
# setting up volume level  between 0 and 1
speaker.setProperty('volume', 1.0)

# """VOICE"""
voices = speaker.getProperty('voices')  # getting details of current voice
# speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# changing index, changes voices. 1 for female
speaker.setProperty('voice', voices[1].id)

for num in range(10, 10):
    page = pdfReader.getPage(10)
    text = page.extractText()
    # print(text)
    # speaker.say(text)
    # """Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
    speaker.save_to_file(text, 'test.mp3')
    speaker.runAndWait()
