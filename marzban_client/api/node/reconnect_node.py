from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError
from ...types import Response


def _get_kwargs(
    node_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/node/{node_id}/reconnect",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Reconnect Node

     Trigger a reconnection for the specified node. Only accessible to sudo admins.

    Args:
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Reconnect Node

     Trigger a reconnection for the specified node. Only accessible to sudo admins.

    Args:
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Reconnect Node

     Trigger a reconnection for the specified node. Only accessible to sudo admins.

    Args:
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Reconnect Node

     Trigger a reconnection for the specified node. Only accessible to sudo admins.

    Args:
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
        )
    ).parsed
