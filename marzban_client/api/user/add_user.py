from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, UserCreate, UserResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UserCreate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/user",
    }

    _body = body.model_dump()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserResponse.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreate,
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
    """Add User

     Add a new user

    - **username**: 3 to 32 characters, can include a-z, 0-9, and underscores.
    - **status**: User's status, defaults to `active`. Special rules if `on_hold`.
    - **expire**: UTC timestamp for account expiration. Use `0` for unlimited.
    - **data_limit**: Max data usage in bytes (e.g., `1073741824` for 1GB). `0` means unlimited.
    - **data_limit_reset_strategy**: Defines how/if data limit resets. `no_reset` means it never resets.
    - **proxies**: Dictionary of protocol settings (e.g., `vmess`, `vless`).
    - **inbounds**: Dictionary of protocol tags to specify inbound connections.
    - **note**: Optional text field for additional user information or notes.
    - **on_hold_timeout**: UTC timestamp when `on_hold` status should start or end.
    - **on_hold_expire_duration**: Duration (in seconds) for how long the user should stay in `on_hold`
    status.

    Args:
        body (UserCreate):  Example: {'username': 'user1234', 'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserResponse]]
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
    body: UserCreate,
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    """Add User

     Add a new user

    - **username**: 3 to 32 characters, can include a-z, 0-9, and underscores.
    - **status**: User's status, defaults to `active`. Special rules if `on_hold`.
    - **expire**: UTC timestamp for account expiration. Use `0` for unlimited.
    - **data_limit**: Max data usage in bytes (e.g., `1073741824` for 1GB). `0` means unlimited.
    - **data_limit_reset_strategy**: Defines how/if data limit resets. `no_reset` means it never resets.
    - **proxies**: Dictionary of protocol settings (e.g., `vmess`, `vless`).
    - **inbounds**: Dictionary of protocol tags to specify inbound connections.
    - **note**: Optional text field for additional user information or notes.
    - **on_hold_timeout**: UTC timestamp when `on_hold` status should start or end.
    - **on_hold_expire_duration**: Duration (in seconds) for how long the user should stay in `on_hold`
    status.

    Args:
        body (UserCreate):  Example: {'username': 'user1234', 'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreate,
) -> Response[Union[Any, HTTPValidationError, UserResponse]]:
    """Add User

     Add a new user

    - **username**: 3 to 32 characters, can include a-z, 0-9, and underscores.
    - **status**: User's status, defaults to `active`. Special rules if `on_hold`.
    - **expire**: UTC timestamp for account expiration. Use `0` for unlimited.
    - **data_limit**: Max data usage in bytes (e.g., `1073741824` for 1GB). `0` means unlimited.
    - **data_limit_reset_strategy**: Defines how/if data limit resets. `no_reset` means it never resets.
    - **proxies**: Dictionary of protocol settings (e.g., `vmess`, `vless`).
    - **inbounds**: Dictionary of protocol tags to specify inbound connections.
    - **note**: Optional text field for additional user information or notes.
    - **on_hold_timeout**: UTC timestamp when `on_hold` status should start or end.
    - **on_hold_expire_duration**: Duration (in seconds) for how long the user should stay in `on_hold`
    status.

    Args:
        body (UserCreate):  Example: {'username': 'user1234', 'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserCreate,
) -> Optional[Union[Any, HTTPValidationError, UserResponse]]:
    """Add User

     Add a new user

    - **username**: 3 to 32 characters, can include a-z, 0-9, and underscores.
    - **status**: User's status, defaults to `active`. Special rules if `on_hold`.
    - **expire**: UTC timestamp for account expiration. Use `0` for unlimited.
    - **data_limit**: Max data usage in bytes (e.g., `1073741824` for 1GB). `0` means unlimited.
    - **data_limit_reset_strategy**: Defines how/if data limit resets. `no_reset` means it never resets.
    - **proxies**: Dictionary of protocol settings (e.g., `vmess`, `vless`).
    - **inbounds**: Dictionary of protocol tags to specify inbound connections.
    - **note**: Optional text field for additional user information or notes.
    - **on_hold_timeout**: UTC timestamp when `on_hold` status should start or end.
    - **on_hold_expire_duration**: Duration (in seconds) for how long the user should stay in `on_hold`
    status.

    Args:
        body (UserCreate):  Example: {'username': 'user1234', 'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
