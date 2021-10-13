import yaml

with open(".\\ConfigOfflineSnippet\\config.yaml") as _f:
    _config = yaml.load(_f, Loader=yaml.FullLoader)
    print(_config)

_config["operation_mode"] = "online"  # [0] =  mode

with open(".\\ConfigOfflineSnippet\\config.yaml", "w") as _f:
    _config = yaml.dump(_config, _f)
    print(_config)
