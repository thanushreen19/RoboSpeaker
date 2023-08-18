import tkinter as tk
import wikipedia
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

window = tk.Tk()
window.title("Speak")
window.config(background="#e6d7ff")

# Increase font size
# font_style = ("Arial", 10, "bold")
button_style = {
    "font": ("Arial", 12),
    "relief": tk.GROOVE,
}

def speak_text(input_text):
    speak(input_text)
    text_widget.insert(tk.END, input_text + '\n')

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            speak(content)
            text_widget.insert(tk.END, content + '\n')
    except FileNotFoundError:
        speak("File not found.")
        text_widget.insert(tk.END, "File not found.\n")
    except IOError:
        speak("Error reading the file.")
        text_widget.insert(tk.END, "Error reading the file.\n")

def search_wikipedia(query):
    wikipedia.set_lang("en")
    print(query)
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
        text_widget.insert(tk.END, summary + '\n')
    except Exception as e:
        speak("No Wikipedia page found for the given query.")
        text_widget.insert(tk.END, "No Wikipedia page found for the given query.\n")

label1 = tk.Label(window, text="Enter the Text", font=button_style["font"],background="#e6d7ff")
label1.pack()

enter = tk.Entry(window)
enter.pack(pady=10)

label2 = tk.Label(window, text="Select an option", font=button_style["font"],background="#e6d7ff")
label2.pack()

button1 = tk.Button(window, text="Text To Speech", **button_style, background="#d8b9ff",command=lambda: speak_text(enter.get()))
button1.pack(pady=10)

button2 = tk.Button(window, text="Read File", **button_style,background="#d8b9ff",command=lambda: read_file(enter.get()))
button2.pack(pady=10)

button3 = tk.Button(window, text="Search in Wikipedia", **button_style,background="#d8b9ff", command=lambda: search_wikipedia(enter.get()))
button3.pack(pady=10)

text_widget = tk.Text(window, height=10, width=60)
text_widget.pack(pady=10)

window.mainloop()
