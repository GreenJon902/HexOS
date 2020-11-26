from globals import baseSysConfig


def return_real_type(value):
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


class BaseSysConfigurator:
    def __init__(self):
        for each_section in baseSysConfig.sections():
            for (each_key, each_val) in baseSysConfig.items(each_section):
                pass # print(each_section, each_key, each_val, type(return_real_type(each_val)))