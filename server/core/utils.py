from .extensions import cache

def invalidate_cache(path: str):
    cache.delete(f"view/{path}")