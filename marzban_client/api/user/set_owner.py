from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, Unauthorized, UserResponse
from ...types import UNSET, Response


def _get_kwargs(
    username: str,
    *,
    admin_username: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["admin_username"] = admin_username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/user/{username}/set-owner",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserResponse.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.model_validate(response.json())

        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    admin_username: str,
) -> Response[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    """Set Owner

     Set a new owner (admin) for a user.

    Args:
        username (str):
        admin_username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Unauthorized, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        admin_username=admin_username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    admin_username: str,
) -> Optional[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    """Set Owner

     Set a new owner (admin) for a user.

    Args:
        username (str):
        admin_username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Unauthorized, UserResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
        admin_username=admin_username,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    admin_username: str,
) -> Response[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    """Set Owner

     Set a new owner (admin) for a user.

    Args:
        username (str):
        admin_username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Unauthorized, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        admin_username=admin_username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    admin_username: str,
) -> Optional[Union[HTTPValidationError, Unauthorized, UserResponse]]:
    """Set Owner

     Set a new owner (admin) for a user.

    Args:
        username (str):
        admin_username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Unauthorized, UserResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            admin_username=admin_username,
        )
    ).parsed
