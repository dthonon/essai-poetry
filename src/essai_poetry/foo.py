"""Command-line interface."""

import click


def foo(bar: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """

    return bar


@click.command()
@click.version_option()
def main() -> None:
    """Essai Poetry."""


if __name__ == "__main__":
    main(prog_name="essai-poetry")  # pragma: no cover
