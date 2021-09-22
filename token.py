#!/usr/bin/env python3.9

from typing import Any, Final

from lox.token_type import TokenType


class Token:
    def __init__(self, type_: TokenType, lexeme: str, literal: Any, line: int):
        self.type_: Final[TokenType] = type_
        self.lexeme: Final[str] = lexeme
        self.literal: Final[Any] = literal
        self.line: Final[int] = line

    def __repr__(self) -> str:
        return f'{self.type_} {self.lexeme} {self.literal}'
