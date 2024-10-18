from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import GetCoreConfigResponseGetCoreConfigApiCoreConfigGet
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/core/config",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCoreConfigResponseGetCoreConfigApiCoreConfigGet.model_validate(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    """Get Core Config

     Get the current core configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    """Get Core Config

     Get the current core configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoreConfigResponseGetCoreConfigApiCoreConfigGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    """Get Core Config

     Get the current core configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[GetCoreConfigResponseGetCoreConfigApiCoreConfigGet]:
    """Get Core Config

     Get the current core configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCoreConfigResponseGetCoreConfigApiCoreConfigGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
