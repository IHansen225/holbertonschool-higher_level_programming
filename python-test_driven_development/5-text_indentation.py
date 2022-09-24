#!/usr/bin/python3
""" text indentation function """

def text_indentation(text):
    """ print two new lines after .?: """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in {'.', '?', ':'}:
            print(f"{text[i]}\n")
        elif text[i] == " " and text[i - 1] == " ":
            pass
        else:
            print(text[i], end="")
