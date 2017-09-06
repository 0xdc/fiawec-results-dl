try:
    import requests_cache
    requests_cache.install_cache()
except ImportError:
    pass

def main():
    from .seasons import sub
    [ [ c.all() for c in b ] for b in [a.sub() for a in sub()] ]

if __name__ == "__main__":
    main()
