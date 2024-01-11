import logging
from .version import __version__
from .oai import *
from .agentchat import *
from .code_utils import DEFAULT_MODEL, FAST_MODEL


# Set the root logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
__all__ = [
    "OpenAIWrapper",
    "Completion",
    "ChatCompletion",
    "get_config_list",
    "config_list_gpt4_gpt35",
    "config_list_openai_aoai",
    "config_list_from_models",
    "config_list_from_json",
    "config_list_from_dotenv",
]
