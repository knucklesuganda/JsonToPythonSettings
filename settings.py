import sys
import json


class Settings:
    __slots__ = (
        "instance_name",
        "instance_version",
        "instance_is_master",
        "connected_instances",
        "logging"
    )

    def handle_error(self, exc):
        print(exc)
        exit(-1)

    def __init__(self):
        try:
            settings_file = sys.argv[1]
            user_settings = json.load(open(settings_file))

            for user_setting_key in user_settings:
                setattr(self, user_setting_key, user_settings[user_setting_key])

        except IndexError as exc:
            self.handle_error(f"Provide config name. Exception: {exc}")
        except FileNotFoundError as exc:
            self.handle_error(f"File not found. Exception: {exc}")
        except json.JSONDecodeError as exc:
            self.handle_error(f"Json error. Exception: {exc}")
        except AttributeError as exc:
            self.handle_error(f"No setting available. Exception: {exc}")


settings = Settings()
print(settings.instance_name)
