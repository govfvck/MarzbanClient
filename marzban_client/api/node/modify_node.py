from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, NodeModify, NodeResponse
from ...types import Response


def _get_kwargs(
    node_id: int,
    *,
    body: NodeModify,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/node/{node_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, NodeResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NodeResponse.model_validate(response.json())

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
) -> Response[Union[HTTPValidationError, NodeResponse]]:
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
    body: NodeModify,
) -> Response[Union[HTTPValidationError, NodeResponse]]:
    """Modify Node

     Update a node's details. Only accessible to sudo admins.

    Args:
        node_id (int):
        body (NodeModify):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'status': 'disabled', 'usage_coefficient': 1.0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NodeResponse]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: int,
    *,
    client: AuthenticatedClient,
    body: NodeModify,
) -> Optional[Union[HTTPValidationError, NodeResponse]]:
    """Modify Node

     Update a node's details. Only accessible to sudo admins.

    Args:
        node_id (int):
        body (NodeModify):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'status': 'disabled', 'usage_coefficient': 1.0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NodeResponse]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node_id: int,
    *,
    client: AuthenticatedClient,
    body: NodeModify,
) -> Response[Union[HTTPValidationError, NodeResponse]]:
    """Modify Node

     Update a node's details. Only accessible to sudo admins.

    Args:
        node_id (int):
        body (NodeModify):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'status': 'disabled', 'usage_coefficient': 1.0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NodeResponse]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: int,
    *,
    client: AuthenticatedClient,
    body: NodeModify,
) -> Optional[Union[HTTPValidationError, NodeResponse]]:
    """Modify Node

     Update a node's details. Only accessible to sudo admins.

    Args:
        node_id (int):
        body (NodeModify):  Example: {'name': 'DE node', 'address': '192.168.1.1', 'port': 62050,
            'api_port': 62051, 'status': 'disabled', 'usage_coefficient': 1.0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NodeResponse]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
