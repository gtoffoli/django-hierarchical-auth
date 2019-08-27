from django.conf import settings

ASCENDING_STRATEGY = getattr(settings, 'HIERARCHICAL_AUTH_STRATEGY_ASCENDING', True)
