import tkinter as tk
import wikipedia
import pyperclip
from features.speak_and_play import speak_and_play
import threading

def get_info():
    topic = entry.get()
    if topic:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    return "No topic provided."

def show_info(event=None):
    info = get_info()
    processed_info = process_text(info)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, processed_info)
    text_box.see(tk.END)  # Scroll to the end to show the latest text
    threading.Thread(target=speak_and_play, args=(f"Boss, here is the summary for {entry.get()}. {info},",)).start()

def show_full_info(event=None):
    topic = entry.get()
    if topic:
        full_info = wikipedia.page(topic).content
        processed_info = process_text(full_info)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, processed_info)
        text_box.see(tk.END)  # Scroll to the end to show the latest text
        threading.Thread(target=speak_and_play, args=(f"Boss, here is the full information for {topic}. {full_info[:500]}.",)).start()

def process_text(text):
    return text.strip().replace('\n', ' ').replace('==', '').replace('===', '')

def copy_to_clipboard(event=None):
    text = text_box.get(1.0, tk.END).strip()
    pyperclip.copy(text)

def create_gui():
    global entry, text_box
    
    root = tk.Tk()
    root.title("Wikipedia Info")
    root.geometry("800x600")

    label = tk.Label(root, text="Enter a topic:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    btn_summary = tk.Button(button_frame, text="Get Summary", command=show_info)
    btn_summary.pack(side=tk.LEFT, padx=5, pady=5)

    btn_full = tk.Button(button_frame, text="Get Full Info", command=show_full_info)
    btn_full.pack(side=tk.LEFT, padx=5, pady=5)

    btn_copy = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
    btn_copy.pack(side=tk.LEFT, padx=5, pady=5)

    entry.bind('<Return>', show_info)  # Bind Enter key for summary
    entry.bind('<Control-Return>', show_full_info)  # Bind Ctrl+Enter for full info
    text_box = tk.Text(root, wrap='word', height=25, width=100)
    text_box.pack()

    root.bind('<Control-c>', copy_to_clipboard)  # Ctrl+C to copy

    root.mainloop()

