HEADERS = {"User-Agent":"Mozilla/5.0"}
TIMEOUT = 10
RATE_LIMIT_SECONDS = 1
ERROR_CODES = {
    "timeout":"Request timed out",
    "connection_error":"Connection failed",
    "http_403":"Access denied",
    "http_404":"Page not found",
    "invalid_content":"Response is not HTML",
    "empty_content":"No meaningful content extracted",
    "url_resolution_failed":"Could not resolve website"
}