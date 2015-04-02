import sys, inspect

class CommandLineParser(object):
    def __init__(self, line):
        self.line = line
        self.args = []
        self.kwargs = {}

    # TODO: quotes around vars
    def parse(self):
        for entry in self.line:
            if ':' in entry:
                k, v = entry.split(":", 1)
                self.kwargs[k] = v
            else:
                self.args.append(entry)

        return self.args, self.kwargs


COMMANDS = {}

class Command(object):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def call(self, args, kwargs):
        return self.func(args, **kwargs)

    def options(self):
        spec = inspect.getargspec(self.func)
        return zip(spec.args[-len(spec.defaults):], spec.defaults)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def command(*args, **kwargs):
    def deco(f):
        COMMANDS[f.__name__] = Command(f.__name__, f, *args, **kwargs)
        return f
    return deco

def print_help():
    print("Waffle Usage:")

    for obj in COMMANDS.values():
        print("    {} {}\n        {}".format(
            obj.name,
            ' '.join(["%s=%s" % (k, v or '?') for k, v in obj.options()]),
            obj.func.__doc__.strip() + '\n' if obj.func.__doc__ else ''
        ))

def main():
    parser = CommandLineParser(sys.argv[1:])
    args, kwargs = parser.parse()

    if not len(args) or args[0] == "help":
        print_help()
        sys.exit(1)

    if args[0].lower() in COMMANDS:
        COMMANDS[args[0].lower()].call(args, kwargs)
    sys.exit(0)

