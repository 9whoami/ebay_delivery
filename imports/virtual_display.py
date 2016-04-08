# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
import settings as conf


def start() -> Display:
    display = None
    if conf.use_virtual_display:
        display = Display(visible=0, size=(1280, 720))
        display.start()
    return display


def stop(display: Display):
    if conf.use_virtual_display:
        display.stop()