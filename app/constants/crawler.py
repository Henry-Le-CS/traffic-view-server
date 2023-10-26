# Used for getting the necessary cookies
CRAWLER_AUTH_ENDPOINT_GT = "http://giaothong.hochiminhcity.gov.vn"
CRAWLER_AUTH_HEADER_GT = {
    "Host": "giaothong.hochiminhcity.gov.vn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Used for getting the image
# Important note: append camera_id at the end of the url
CRAWLER_IMAGE_ENDPOINT_GT = "http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id=" 
CRAWLER_IMAGE_HEADER_GT = {
    "Host": "giaothong.hochiminhcity.gov.vn:8007",
}


