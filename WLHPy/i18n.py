import locale


class ckI18N:
    _current_language = None
    _modules = {}

    def __init__(self, language=None):
        if language is None:
            self._current_language = locale.getdefaultlocale()[0]

    def set_language(self, language):
        self._current_language = language

    def load_module(self, module_name):
        pass


class TranslationData:
    def __init__(self):
        pass
