from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user


def admin_required(func):
    """
    Декоратор для вызова пользователем функций администратора.
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash('Эта страница доступна только админам')
            return redirect(url_for('main.home'))
        return func(*args, **kwargs)
    return decorated_view


def manager_required(func):
    """
    Декоратор для вызова пользователем функций manager.
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.is_admin:
            return func(*args, **kwargs)
        elif not current_user.is_manager:
            flash('Эта страница доступна только manager')
            return redirect(url_for('main.home'))
        return func(*args, **kwargs)
    return decorated_view
