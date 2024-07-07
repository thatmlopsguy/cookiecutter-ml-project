import logging
from pathlib import Path
import yaml

_logger: logging.Logger = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = "config.yaml"

class ConfigReader:
    @classmethod
    def read(cls):
        config = {}
        # Look for a config file - if we don't find one, that's fine. :)
        p = Path(DEFAULT_CONFIG_PATH)
        if not p.is_file():
            return config

        with p.open() as infile:
            try:
                config = yaml.safe_load(infile)
                return config
            except yaml.YAMLError as exc:
                _logger.info(f"There was an error parsing the config file: {exc}")
                return config
