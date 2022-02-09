class MetaSingleton(type):
    def __init__(cls, name, bases, attr, **kwargs):
        super().__init__(name, bases, attr)
        cls._instances = {}

    def __call__(cls, *args, **kwargs):
        name = ''
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls._instances:
            return cls._instances
        else:
            cls._instances[name] = super().__call__(*args, **kwargs)
            return cls._instances[name]