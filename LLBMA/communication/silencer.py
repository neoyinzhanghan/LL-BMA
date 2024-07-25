import logging


class RayLoggingSilencer:
    def __init__(self):
        self.previous_levels = {}
        self.ray_loggers = ["ray", "ray.rllib", "ray.tune"]

    def __enter__(self):
        # Backup current logging levels and set to ERROR for Ray loggers
        for logger_name in self.ray_loggers:
            logger = logging.getLogger(logger_name)
            self.previous_levels[logger_name] = logger.level
            logger.setLevel(logging.ERROR)

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore previous logging levels
        for logger_name, level in self.previous_levels.items():
            logger = logging.getLogger(logger_name)
            logger.setLevel(level)
