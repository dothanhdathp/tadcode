def define_env(env):
    @env.macro
    def linkslide(title, html_path):
        return f'''<a href="javascript:void(0);" onclick="openSlide('http://localhost:65000/{html_path}')">⧉ {title}</a>'''

    @env.macro
    def book(title, book, page=""):
        return f'''[{title}](http://localhost:65000/book/{book}/{page})'''