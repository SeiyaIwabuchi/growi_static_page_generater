from param_source import ParamSource


class Config:
    param_source: ParamSource = ParamSource(ParamSource.config_file)
    host_name: str = "hostname"
    port: int = 80
    rest_server_url: str = "http://rest_server:8080/endpoint"
    endpoint_pages = "/pages.list"
    endpoint_page = "/page"
    api_key = "hogehoge"