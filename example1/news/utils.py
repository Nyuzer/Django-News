class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, string):
        if isinstance(string, str):
            return string.upper()
        else:
            return string.title.upper()
