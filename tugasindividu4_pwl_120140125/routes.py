def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("user", "/user")
    config.add_route("register", "/register")
    config.add_route("login", "/login")
    config.add_route("logout", "/logout")
    config.add_route("anime", "/anime")
    config.add_route("anime_id", "/anime/{id}")
