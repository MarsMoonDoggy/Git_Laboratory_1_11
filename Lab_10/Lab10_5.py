from get_datetime import get_datetime
get_datetime()

class ConfigurationError(Exception):
    def __init__(self, message, config_name):
        super().__init__(f"Ошибка в конфигурации '{config_name}': {message}")
        self.config_name = config_name

def load_config(filepath):
    config = {"path": "/usr/local/bin", "timeout": None}
    if 'path' not in config:
        raise ConfigurationError("Отсутствует обязательный параметр 'path'", filepath)
    if config['timeout'] is None:
        raise ConfigurationError("Параметр 'timeout' должен быть задан", filepath)
    return config

def validate_config(config, filepath):
    if config['timeout'] is not None and type(config['timeout']) is not int:
        raise ConfigurationError("Параметр 'timeout' должен быть целым числом", filepath)
    print("Конфигурация валидна.")

try:
    config = load_config("myapp.config")
except ConfigurationError as e:
    print(e)

try:
    config = {"path": "/usr/local/bin", "timeout": "immediate"}
    validate_config(config, "myapp.config")
except ConfigurationError as e:
    print(e)
