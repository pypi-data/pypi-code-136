from typing import Any, Dict

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from wefaas.core import Wefaas
from wefaas.api.fastapi_utils import patch_fastapi


def launch_api(wefaas_path: str, port: int = 8501, host: str = "0.0.0.0") -> None:
    import uvicorn

    from wefaas.core import Wefaas
    from wefaas.api import create_api

    app = create_api(Wefaas(wefaas_path))
    uvicorn.run(app, host=host, port=port, log_level="info")


def create_api(wefaas: Wefaas) -> FastAPI:

    title = wefaas.name
    if "wefaas" not in wefaas.name.lower():
        title += " - Wefaas"

    # TODO: what about version?
    app = FastAPI(title=title, description=wefaas.description)

    patch_fastapi(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post(
        "/call",
        operation_id="call",
        response_model=wefaas.output_type,
        # response_model_exclude_unset=True,
        summary="Execute the wefaas.",
        status_code=status.HTTP_200_OK,
    )
    def call(input: wefaas.input_type) -> Any:  # type: ignore
        """Executes this wefaas."""
        return wefaas(input)

    @app.get(
        "/info",
        operation_id="info",
        response_model=Dict,
        # response_model_exclude_unset=True,
        summary="Get info metadata.",
        status_code=status.HTTP_200_OK,
    )
    def info() -> Any:  # type: ignore
        """Returns informational metadata about this Wefaas."""
        return {}

    # Redirect to docs
    @app.get("/", include_in_schema=False)
    def root() -> Any:
        return RedirectResponse("./docs")

    return app
