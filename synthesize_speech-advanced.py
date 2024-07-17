import customtkinter as ctk
from tkinter import filedialog, messagebox
import boto3
import os
import pygame
import io

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        pygame.init()  # Initialize Pygame

        self.title("Text-to-Speech with Amazon Polly")
        self.geometry(f"{1100}x{580}")

        # Initialize a Polly client globally
        self.polly_client = boto3.client('polly')

        # Create frames for layout
        self.sidebar_frame = ctk.CTkFrame(self, width=200)
        self.sidebar_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Dropdown for selecting output mode
        output_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Output Mode:")
        output_mode_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.output_option = ctk.StringVar(value="Play Audio")
        output_mode_dropdown = ctk.CTkOptionMenu(self.sidebar_frame, variable=self.output_option,
                                                 values=["Play Audio", "Save Audio as MP3"], corner_radius=10)
        output_mode_dropdown.pack(padx=10, pady=(0, 10), fill="x")

        # Theme selection in sidebar
        theme_label = ctk.CTkLabel(self.sidebar_frame, text="Select Theme:")
        theme_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.theme_var = ctk.StringVar(value="System")
        theme_dropdown = ctk.CTkOptionMenu(self.sidebar_frame, variable=self.theme_var,
                                           values=["Light", "Dark", "System"], command=self.change_theme)
        theme_dropdown.pack(padx=10, pady=(0, 10), fill="x")

        # UI Scale factor in sidebar
        scale_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scale:")
        scale_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.scale_var = ctk.StringVar(value="100%")
        scale_dropdown = ctk.CTkOptionMenu(self.sidebar_frame, variable=self.scale_var,
                                           values=["50%", "75%", "100%", "125%", "150%"], command=self.change_scale)
        scale_dropdown.pack(padx=10, pady=(0, 10), fill="x")

        # Voice selection in sidebar
        voice_label = ctk.CTkLabel(self.sidebar_frame, text="Choose Voice:")
        voice_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.voice_var = ctk.StringVar(value="Joanna")
        voices = ["Joanna", "Matthew", "Salli", "Ivy", "Joey", "Justin"]
        voice_dropdown = ctk.CTkOptionMenu(self.sidebar_frame, variable=self.voice_var, values=voices, corner_radius=10)
        voice_dropdown.pack(padx=10, pady=(0, 10), fill="x")

        # Text field in main frame
        self.text_widget = ctk.CTkTextbox(self.main_frame, height=120, corner_radius=10)
        self.text_widget.pack(padx=10, pady=10, fill="both", expand=True)

        # Speak button in main frame at the bottom
        speak_button = ctk.CTkButton(self.main_frame, text="Speak", command=self.on_speak_button_clicked)
        speak_button.pack(side="bottom", padx=10, pady=20, fill="x")

    def on_speak_button_clicked(self):
        text_to_speak = self.text_widget.get("1.0", "end-1c").strip()
        voice_id = self.voice_var.get()
        if text_to_speak:
            self.synthesize_speech(text_to_speak, voice_id)

    def synthesize_speech(self, text_to_speak, voice_id):
        try:
            response = self.polly_client.synthesize_speech(VoiceId=voice_id, OutputFormat='mp3', Text=text_to_speak)
            audio_stream = io.BytesIO(response['AudioStream'].read())

            if self.output_option.get() == "Play Audio":
                # Play the audio directly using Pygame
                pygame.mixer.music.load(audio_stream)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():  # Check if the music is playing.
                    pygame.time.Clock().tick(10)
            elif self.output_option.get() == "Save Audio as MP3":
                # Save the audio to a file
                file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
                if file_path:
                    with open(file_path, 'wb') as f:
                        f.write(audio_stream.getbuffer())
                    messagebox.showinfo("Success", f"Audio file saved as {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def change_theme(self, theme):
        if theme == "Light":
            ctk.set_appearance_mode("light")
        elif theme == "Dark":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("system")

    def change_scale(self, scale):
        new_scaling_float = int(scale.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()
