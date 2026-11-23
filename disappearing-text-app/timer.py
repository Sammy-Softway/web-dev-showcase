"""Non-blocking inactivity countdown timer for Tkinter applications."""

import tkinter as tk
from typing import Callable


class InactivityTimer:
    """Manage a resettable countdown timer decoupled from UI widgets.

    Schedules non-blocking ticks via Tkinter's event loop and notifies
    the caller through `on_tick` and `on_timeout` callbacks.
    """

    def __init__(
            self,
            root: tk.Misc,
            duration_sec: int,
            on_tick: Callable[[int], None],
            on_timeout: Callable[[], None],
    ) -> None:
        self.root = root
        self.duration_sec = duration_sec
        self.on_tick = on_tick
        self.on_timeout = on_timeout
        self.seconds_left: int = duration_sec
        self.timer_id: str | None = None

    def reset(self) -> None:
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)

        self.seconds_left = self.duration_sec
        self.on_tick(self.seconds_left)
        self.timer_id = self.root.after(1000, self._tick)

    def _tick(self) -> None:
        self.seconds_left -= 1
        if self.seconds_left > 0:
            self.on_tick(self.seconds_left)
            self.timer_id = self.root.after(1000, self._tick)
        else:
            self.timer_id = None
            self.on_timeout()

    def stop(self) -> None:
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None