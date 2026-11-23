import tkinter as tk

import config


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.config(bg=config.BG_COLOR, padx=20, pady=20)

        self._setup_ui()

    def _setup_ui(self) -> None:
        self.status_label = tk.Label(self,
                                     text="Start typing to begin...",
                                     font=config.FONT_STATUS,
                                     bg=config.BG_COLOR,
                                     fg=config.STATUS_COLOR)
        self.status_label.pack(pady=(0, 15))
        self.text_area = tk.Text(self,
                                 font=config.FONT_TEXT,
                                 bg=config.BG_COLOR,
                                 fg=config.TEXT_COLOR,
                                 insertbackground=config.CURSOR_COLOR,
                                 wrap="word",
                                 bd=0,
                                 highlightthickness=0)
        self.text_area.pack(fill="both", expand=True)
        self.text_area.focus_set()
