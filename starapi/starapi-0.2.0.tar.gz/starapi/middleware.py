from starlette.middleware.base import BaseHTTPMiddleware


class TraceRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if hasattr(request.state, "_trace_request") and hasattr(request.app.state, "logger"):
            request.app.state.logger.info(request.state._trace_request)

        return response
