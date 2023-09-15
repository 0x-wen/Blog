from wsgiref.simple_server import make_server


def index(env):
    return "index"


def about(env):
    return "about"


urls = [
    ("/index", index),
    ("/about", about),
]


def app(env, start_response):
    """
    :param env: 请求有关的数据
    :param start_response: 响应有的数据
    :return: 响应给浏览器的数据
    """
    current_path = env["PATH_INFO"]
    func = None
    for url in urls:
        if current_path == url[0]:
            func = url[1]
            break
    if func:
        res = func(env)
    else:
        res = "hello world"

    start_response("200 OK", [("AAA", "aaa")])
    return [res.encode("utf-8")]


server = make_server("127.0.0.1", 8080, app)
server.serve_forever()  # 启动服务

