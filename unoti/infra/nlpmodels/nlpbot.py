from abc import ABC, abstractmethod
from IPython.display import display, Markdown


def MarkdownFormatter(bot_instance, text: str):
    """Formats output as Markdown suitable for use in a Jupyter notebook."""
    return display(Markdown(text))


class NlpBot(ABC):
    formatter = MarkdownFormatter

    @abstractmethod
    def complete(self, prompt: str) -> str:
        """Complete some text given some input text."""

    def __call__(self, prompt: str):
        text_output = self.complete(prompt)
        if not self.formatter:
            return text_output
        else:
            return self.formatter(text_output)

class TestBot(NlpBot):
    def complete(self, prompt):
        return 'test'