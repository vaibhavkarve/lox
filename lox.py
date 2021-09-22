#!/usr/bin/env python3.9
"""Python translation of Lox.java.

Lox's lexical scanner as seen in the Crafting Interpreters book.
"""

from pathlib import Path
import readline
import sys

from lox.scanner import Scanner
from lox.token import Token

class Lox:
    had_error: bool = False

    @classmethod
    def main(cls, *args: str) -> None:
        if len(args) > 1:
            print("Usage: jlox [script]")
            sys.exit(64)
        elif len(args) == 1:
            cls.run_file(Path(args[0]))
        else:
            cls.run_prompt()

    @classmethod
    def run_file(cls, path: Path) -> None:
        """Thin wrapper around run()."""
        with open(path, "r") as readfile:
            bytes: str = readfile.read()
            cls.run(bytes)
        # Indicate an error in the exit code.
        if cls.had_error:
            sys.exit(65)

    @classmethod
    def run_prompt(cls) -> None:
        """Thin wrapper around none, making it a REPL."""
        while True:
            line: str = input('> ')
            if line is None:
                # Reached EOF because user input "C-d".
                break
            cls.run(line)
            cls.had_error = False  # Reset in order to continue session.

    @classmethod
    def run(cls, source: str) -> None:
        """Core run command."""
        scanner: Scanner = Scanner(source)
        tokens: list[Token] = scanner.scan_tokens()

        # For now, just print the tokens.
        token: Token
        for token in tokens:
            print(token)

    @classmethod
    def error(self, line: int, message: str) -> None:
        self.report(line, "", message)

    @classmethod
    def report(cls, line: int, where: str, message: str) -> None:
        print(f'[line {line}] Error{where}: {message}')
        cls.had_error = True
