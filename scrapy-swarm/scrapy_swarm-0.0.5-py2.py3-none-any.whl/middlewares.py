

# 原文件有此类，只需在process_response方法中加入判断
class DupeFilterDownloaderMiddleware:
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        print("==============")
        if response.status != 200:
            fp = DupefiltersMiddleware.request_fingerprint(request)
            DupefiltersMiddleware.remove_fp(fp)  #删除已经记录的指纹

        return response
