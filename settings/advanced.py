# -*- coding: utf-8 -*-

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:41'
__description__ = """
Более тонкие настройки требующие накоторого понимания
"""

# Параметры запуска для phantomjs,
# чтобы знать доступные параметры в консоле phantomjs --help.
# Пример:
# ['--ignore-ssl-errors=true', '--ssl-protocol=tlsv1']
service_args = None

# Размеры каптчи. Две пары координат: верхний левый угол и нижний правый.
captcha_size = (325, 329, 476, 378)

# Режим отладки.
debug = True
