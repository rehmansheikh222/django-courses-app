"""
Badges app toggles.
"""
from edx_toggles.toggles import SettingDictToggle
# .. toggle_name: SHOW_TOPICS_ENABLED
# .. toggle_implementation: DjangoSetting
# .. toggle_default: False
# .. toggle_description: Determines if the topics should be shown with the courses
# .. toggle_life_expectancy: permanent
# .. toggle_permanent_justification: Topics are optional for usage.
# .. toggle_creation_date: 2024-09-12
# .. toggle_use_cases: open_edx
ENABLE_SHOW_TOPICS = SettingDictToggle(
    "FEATURES", "SHOW_TOPICS_ENABLED", default=False, module_name=__name__
)


def is_show_topics_enabled():
    """
    Check main feature flag.
    """
    return ENABLE_SHOW_TOPICS.is_enabled()


def check_ahow_topics_enabled(func):
    """
    Decorator for checking the applicability of a topics app.
    """
    def wrapper(*args, **kwargs):
        if is_show_topics_enabled():
            return func(*args, **kwargs)
        return None
    return wrapper
