"""Common module."""

from bs4 import BeautifulSoup


class Common:
    """
    Common class.

    This class consists of common methods used by Other
    modules.
    """

    def __init__(self):
        """Initialisations."""
        pass

    def get_html(self, session, url):
        """To get the HTML page for `url` and return soup."""
        raw = session.get(url)
        raw = raw.content
        soup = BeautifulSoup(raw, "lxml")
        return soup
