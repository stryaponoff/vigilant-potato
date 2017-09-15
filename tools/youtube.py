import os


def play(url, fullscreen):
    args = ""
    if fullscreen:
        args += "--fs"

    os.system(f"mpv {args} {url}")
