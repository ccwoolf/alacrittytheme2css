#!/usr/bin/env python

import sys
import yaml


def hex2css(hex: str):
    return hex.replace("0x", "#").lower()


def css_var_name(scheme, colour):
    if scheme in ["normal", "primary"]:
        scheme = ""
    else:
        scheme = f"{scheme}-"

    return f"--{scheme}{colour}"


def create_css(theme):
    css_string = ":root {\n"

    for scheme, colours in theme["colors"].items():
        if scheme in ["search", "indexed_colors"]:
            continue

        for colour, value in colours.items():
            css_string += f"  {css_var_name(scheme, colour)}: {hex2css(value)};\n"

    css_string += "}\n"

    return css_string


def yaml2dict(file):
    with open(file) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    for file in sys.argv[1:]:
        theme_name = file.split("/")[-1].split(".")[0]
        theme = yaml2dict(file)

        with open(f"{theme_name}.css", "w") as file:
            file.write(create_css(theme))
