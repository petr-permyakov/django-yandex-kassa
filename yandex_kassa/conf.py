# -*- coding: utf-8 -*-

from django.conf import settings

DEBUG = getattr(settings, 'YANDEX_KASSA_DEBUG', False)

SCID = getattr(settings, 'YANDEX_KASSA_SCID')
SHOP_ID = getattr(settings, 'YANDEX_KASSA_SHOP_ID')
SHOP_PASSWORD = getattr(settings, 'YANDEX_KASSA_SHOP_PASSWORD')

DISPLAY_FIELDS = getattr(settings, 'YANDEX_KASSA_DISPLAY_FIELDS',
                         ['paymentType', 'cps_email', 'cps_phone'])

CALLBACK_URL = getattr(settings, 'YANDEX_KASSA_CALLBACK_URL', '/kassa/callback/')
FAIL_URL = getattr(settings, 'YANDEX_KASSA_FAIL_URL', '/kassa/fail/')
SUCCESS_URL = getattr(settings, 'YANDEX_KASSA_SUCCESS_URL', '/kassa/success/')