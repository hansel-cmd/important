class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = host
        return self._cache[host]

    def has_host(self, host):
        return host in self._cache

    def clear(self):
        self._cache.clear()

resolver = Resolver()
print(resolver.has_host('123'))
resolver('123')
print(resolver.has_host('123'))
