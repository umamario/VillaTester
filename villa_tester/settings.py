import os

TIMEZONE = 'Asia/Bangkok'

SCRAPY_SETTINGS = {
    "HTTPERROR_ALLOWED_CODES": [200, 301, 302, 400, 401, 403, 404, 500, 502, 503, 504],
    "FEED_FORMAT": 'csv',
    "ITEM_PIPELINE": {
        'scrapy.pipelines.files.S3FilesStore': 1
    },
    "FEED_URI": 's3://villa-tester/villatest-{}.csv',
    "AWS_ACCESS_KEY_ID": os.environ['AWS_ACCESS_KEY_ID'],
    "AWS_SECRET_ACCESS_KEY": os.environ['AWS_SECRET_ACCESS_KEY'],
    "AWS_REGION_NAME": os.environ['AWS_REGION_NAME'],
    "CONCURRENT_REQUESTS": 100
}

ERROR_MESSAGES = {
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found	Requested",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Time-Out",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request-URL Too Large",
    415: "Unsupported Media Type",
    500: "Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Out of Resources",
    504: "Gateway Time-Out",
    505: "HTTP Version Not Supported",
}
