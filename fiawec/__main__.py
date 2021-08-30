try:
    import requests_cache
    requests_cache.install_cache()
except ImportError:
    pass

def main():
    from .seasons import Seasons, NoticeBoard, Committee
    [ [ c.all() for c in b ] for b in [a.sub() for a in Seasons.sub()] ]
    [ [ c.all() for c in b ] for b in [a.sub() for a in NoticeBoard.sub()] ]
    [ a.all() for a in Committee.sub() ]

if __name__ == "__main__":
    main()
