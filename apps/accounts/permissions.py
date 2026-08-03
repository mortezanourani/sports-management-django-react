from ninja.errors import HttpError

def require_role(*allowed_roles):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.auth.role not in allowed_roles:
                raise HttpError(403, 'شما دسترسی لازم برای این عملیات را ندارید')
            return func(request, *args, **kwargs)

        return wrapper

    return decorator