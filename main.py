def define_env(env):
    @env.macro
    def linkslide(html_path, title):
        return f'''<a href="javascript:void(0);" onclick="openSlide('http://localhost:65000/{html_path}')">⧉ {title}</a>'''