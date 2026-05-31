from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from typing import Protocol


class Command(Protocol):
    def run(self) -> Iterator[None]:
        ...


def _as_command(command: Command | Callable[[], object]) -> Command:
    if hasattr(command, "run"):
        return command
    return Call(command)


@dataclass(frozen=True)
class Call:
    callback: Callable[[], object]

    def run(self) -> Iterator[None]:
        self.callback()
        if False:
            yield None


@dataclass(frozen=True)
class Wait:
    seconds: float

    def run(self) -> Iterator[None]:
        from .runtime import current_stage

        target_time = current_stage().time + self.seconds
        while current_stage().time < target_time:
            yield None


@dataclass(frozen=True)
class Sequence:
    commands: tuple[Command | Callable[[], object], ...]

    def run(self) -> Iterator[None]:
        for command in self.commands:
            yield from _as_command(command).run()


@dataclass(frozen=True)
class Repeat:
    times: int
    body: Sequence

    def run(self) -> Iterator[None]:
        for _ in range(self.times):
            yield from self.body.run()


@dataclass(frozen=True)
class Forever:
    body: Sequence

    def run(self) -> Iterator[None]:
        while True:
            yield from self.body.run()
            yield None


def wait(seconds: float) -> Wait:
    return Wait(seconds)


def sequence(*commands: Command | Callable[[], object]) -> Sequence:
    return Sequence(commands)


def repeat(times: int, *commands: Command | Callable[[], object]) -> Repeat:
    return Repeat(times, sequence(*commands))


def forever(*commands: Command | Callable[[], object]) -> Forever:
    return Forever(sequence(*commands))
