"""Main Tkinter user interface and event bindings for the writing app."""

import tkinter as tk

import config
from timer import InactivityTimer


class App(tk.Tk):
    """Main application window for the Disappearing Text Writing App.

        Manages the editor layout, filters valid user input events, and
        coordinates UI updates with the inactivity timer.
        """

    def __init__(self):
        super().__init__()
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.config(bg=config.BG_COLOR, padx=20, pady=20)
        self.status_label: tk.Label
        self.text_area: tk.Text

        self._setup_ui()
        self._bind_events()
        self.timer = InactivityTimer(
            root=self,
            duration_sec=config.INACTIVITY_LIMIT_SEC,
            on_tick=self._handle_tick,
            on_timeout=self._handle_timeout,
        )

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

    def _bind_events(self) -> None:
        self.text_area.bind("<Key>", self._on_key_press)
        self.text_area.bind("<<Paste>>", self._on_paste)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_key_press(self, event: tk.Event) -> None:
        if not event.char:
            return

        # print(f"Valid keystroke: {event.keysym}")
        self.timer.reset()

    def _handle_tick(self, seconds_left: int) -> None:
        self.status_label.config(text=f"Time left: {seconds_left}s")

    def _handle_timeout(self) -> None:
        self.text_area.delete("1.0", tk.END)
        self.status_label.config(text="Time's up! Start typing to begin...")

    def _on_paste(self, event: tk.Event) -> None:
        self.timer.reset()

    def _on_close(self) -> None:
        self.timer.stop()
        self.destroy()
