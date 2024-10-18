from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.modify_core_config_payload import ModifyCoreConfigPayload
from ...models.modify_core_config_response_modify_core_config_api_core_config_put import (
    ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ModifyCoreConfigPayload,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/core/config",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModifyCoreConfigPayload,
) -> Response[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    """Modify Core Config

     Modify the core configuration and restart the core.

    Args:
        body (ModifyCoreConfigPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModifyCoreConfigPayload,
) -> Optional[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    """Modify Core Config

     Modify the core configuration and restart the core.

    Args:
        body (ModifyCoreConfigPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModifyCoreConfigPayload,
) -> Response[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    """Modify Core Config

     Modify the core configuration and restart the core.

    Args:
        body (ModifyCoreConfigPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModifyCoreConfigPayload,
) -> Optional[Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]]:
    """Modify Core Config

     Modify the core configuration and restart the core.

    Args:
        body (ModifyCoreConfigPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ModifyCoreConfigResponseModifyCoreConfigApiCoreConfigPut]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed