from django.contrib.auth.decorators import user_passes_test

def admin_only(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)
    return decorated_view_func(view_func)