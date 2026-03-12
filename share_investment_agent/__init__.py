# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""share-investment-agent - A Bindu Agent for Share Investment Analysis."""

from share_investment_agent.__version__ import __version__
from share_investment_agent.main import (
    handler,
    initialize_agent,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "main",
]
