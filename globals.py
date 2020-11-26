from configparser import ConfigParser as CP


class ConfigParser(CP):
    def get(self, *args, **kwargs):
        value = super(ConfigParser, self).get(*args, **kwargs)

        try:
            return int(value)

        except ValueError:
            try:
                return float(value)

            except ValueError:
                if value == "True":
                    return True
                if value == "False":
                    return True
                else:
                    return str(value)


baseSysConfig = ConfigParser()
baseSysConfig.read("HexOSBase/data/config_files/base_sys_config.ini")

path = ""
