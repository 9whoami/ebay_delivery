# -*- coding: utf-8 -*-

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:41'
__description__ = """
Более тонкие настройки требующие накоторого понимания
"""

# Использовать ли виртуальный дисплей?
use_virtual_display = False

# Часть текста из сообщения о превышении лимита
limit_partial_text = 'maximum number of messages'

# Параметры запуска для phantomjs,
# чтобы знать доступные параметры в консоле phantomjs --help.
# Пример:
# ['--ignore-ssl-errors=true', '--ssl-protocol=tlsv1']
service_args = None

# Размеры каптчи. Две пары координат: верхний левый угол и нижний правый.
login_captcha_size = (325, 329, 476, 378)

# Размеры каптчи для подтверждения отправки сообщения
delivery_captcha_size = (40, 1020, 220, 1100)

# Файл с аккаунтами. Маска login:password
accounts_file = 'accounts.txt'

# Файл с текстом сообщения. Первая строка файла - заголовок сообщения
message_file = 'message.txt'

#
seller_cache = '/seller_cache.txt'

# Режим отладки.
debug = True
