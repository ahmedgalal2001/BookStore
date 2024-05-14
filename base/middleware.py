class RequestInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # This code is executed before the view is called
        print("Path:", request.path)
        print("Method:", request.method)
        print("GET parameters:", request.GET)
        print("POST parameters:", request.POST)
        
        # Call the next middleware or the view
        response = self.get_response(request)
        
        # This code is executed after the view is called
        return response
