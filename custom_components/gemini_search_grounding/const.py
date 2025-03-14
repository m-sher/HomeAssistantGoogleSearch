"""Constants for the Google Generative AI Conversation integration."""

import logging

DOMAIN = "gemini_search_grounding"
LOGGER = logging.getLogger(__package__)
CONF_PROMPT = "prompt"

CONF_RECOMMENDED = "recommended"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODEL = "models/gemini-2.0-flash"
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 1.0
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 0.95
CONF_TOP_K = "top_k"
RECOMMENDED_TOP_K = 64
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 150
CONF_DYNAMIC_THRESHOLD = "dynamic_threshold"
RECOMMENDED_DYNAMIC_THRESHOLD = 0.3
CONF_HARASSMENT_BLOCK_THRESHOLD = "harassment_block_threshold"
CONF_HATE_BLOCK_THRESHOLD = "hate_block_threshold"
CONF_SEXUAL_BLOCK_THRESHOLD = "sexual_block_threshold"
CONF_DANGEROUS_BLOCK_THRESHOLD = "dangerous_block_threshold"
RECOMMENDED_HARM_BLOCK_THRESHOLD = "BLOCK_MEDIUM_AND_ABOVE"

TIMEOUT_MILLIS = 10000
