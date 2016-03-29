# -*- coding: utf-8 -*-
from configparser import ConfigParser, Error

__author__ = 'whoami'


def write_cfg(file, section, option, value):
    """
    Записывает настройки в файл
    :param file:
    :param section:
    :param option:
    :param value:
    :return:
    """
    parser = ConfigParser()

    try:
        parser.read(file)
        parser.set(section, option, str(value))
        with open(file, "w") as f:
            parser.write(f)

    except (Error, TypeError) as e:
        del parser
        raise SystemExit(e)
    else:
        del parser


def read_cfg(*args, **kwargs):
    """
    Читает настройки
    :param args: первыйм параметром идет имя файла, затем имя секции
    :param kwargs: file, section
    :return: dict в случае успеха иначе None
    """

    try:
        if args:
            conf_file, section = args
        elif kwargs:
            conf_file = kwargs['file']
            section = kwargs['section']
        else:
            return None
    except (KeyError, ValueError) as e:
        print("Error in read_cfg with message {!r}".format(e))
        return None

    parser = ConfigParser()

    try:
        parser.read(conf_file)
        result = dict()
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                result[item[0]] = item[1]
        else:
            raise Error(
                '{0!r} not found in the {1!r} file'.format(section, conf_file))
    except Error as e:
        print(e)
        return None
    else:
        return result
    finally:
        del parser
