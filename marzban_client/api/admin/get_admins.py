from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Admin, Forbidden, HTTPValidationError, Unauthorized
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/admins",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Admin.model_validate(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.model_validate(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Forbidden.model_validate(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    """Get Admins

     Fetch a list of admins with optional filters for pagination and username.

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPValidationError, List['Admin'], Unauthorized]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    """Get Admins

     Fetch a list of admins with optional filters for pagination and username.

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPValidationError, List['Admin'], Unauthorized]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    """Get Admins

     Fetch a list of admins with optional filters for pagination and username.

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPValidationError, List['Admin'], Unauthorized]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[Forbidden, HTTPValidationError, List["Admin"], Unauthorized]]:
    """Get Admins

     Fetch a list of admins with optional filters for pagination and username.

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPValidationError, List['Admin'], Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            username=username,
        )
    ).parsed
