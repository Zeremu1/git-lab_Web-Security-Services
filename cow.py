#!/usr/bin/env python3
# cow.py — prints an ASCII art cow

def get_cow():
    return r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """

def main():
    print(get_cow())

if __name__ == "__main__":
    main()
