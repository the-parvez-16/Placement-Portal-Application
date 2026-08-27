from .extensions import cache

def invalidate_cache(path: str):
    cache.delete(f"view/{path}")
    
    try:
        redis_client = cache.cache._client
        for key in redis_client.scan_iter(f"flask_cache_view/{path}*"):
            redis_client.delete(key)
    except Exception as e:
        print(f"Failed to clear pattern cache: {e}")
