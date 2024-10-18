from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, UserModify, UserResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    body: UserModify,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/user/{username}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UserResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserResponse.model_validate(response.json())

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
) -> Response[Union[HTTPValidationError, UserResponse]]:
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
    body: UserModify,
) -> Response[Union[HTTPValidationError, UserResponse]]:
    """Modify User

     Modify an existing user

    - **username**: Cannot be changed. Used to identify the user.
    - **status**: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'.
    - **expire**: UTC timestamp for new account expiration. Set to `0` for unlimited, `null` for no
    change.
    - **data_limit**: New max data usage in bytes (e.g., `1073741824` for 1GB). Set to `0` for
    unlimited, `null` for no change.
    - **data_limit_reset_strategy**: New strategy for data limit reset. Options include 'daily',
    'weekly', 'monthly', or 'no_reset'.
    - **proxies**: Dictionary of new protocol settings (e.g., `vmess`, `vless`). Empty dictionary means
    no change.
    - **inbounds**: Dictionary of new protocol tags to specify inbound connections. Empty dictionary
    means no change.
    - **note**: New optional text for additional user information or notes. `null` means no change.
    - **on_hold_timeout**: New UTC timestamp for when `on_hold` status should start or end. Only
    applicable if status is changed to 'on_hold'.
    - **on_hold_expire_duration**: New duration (in seconds) for how long the user should stay in
    `on_hold` status. Only applicable if status is changed to 'on_hold'.

    Note: Fields set to `null` or omitted will not be modified.

    Args:
        username (str):
        body (UserModify):  Example: {'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    body: UserModify,
) -> Optional[Union[HTTPValidationError, UserResponse]]:
    """Modify User

     Modify an existing user

    - **username**: Cannot be changed. Used to identify the user.
    - **status**: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'.
    - **expire**: UTC timestamp for new account expiration. Set to `0` for unlimited, `null` for no
    change.
    - **data_limit**: New max data usage in bytes (e.g., `1073741824` for 1GB). Set to `0` for
    unlimited, `null` for no change.
    - **data_limit_reset_strategy**: New strategy for data limit reset. Options include 'daily',
    'weekly', 'monthly', or 'no_reset'.
    - **proxies**: Dictionary of new protocol settings (e.g., `vmess`, `vless`). Empty dictionary means
    no change.
    - **inbounds**: Dictionary of new protocol tags to specify inbound connections. Empty dictionary
    means no change.
    - **note**: New optional text for additional user information or notes. `null` means no change.
    - **on_hold_timeout**: New UTC timestamp for when `on_hold` status should start or end. Only
    applicable if status is changed to 'on_hold'.
    - **on_hold_expire_duration**: New duration (in seconds) for how long the user should stay in
    `on_hold` status. Only applicable if status is changed to 'on_hold'.

    Note: Fields set to `null` or omitted will not be modified.

    Args:
        username (str):
        body (UserModify):  Example: {'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: UserModify,
) -> Response[Union[HTTPValidationError, UserResponse]]:
    """Modify User

     Modify an existing user

    - **username**: Cannot be changed. Used to identify the user.
    - **status**: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'.
    - **expire**: UTC timestamp for new account expiration. Set to `0` for unlimited, `null` for no
    change.
    - **data_limit**: New max data usage in bytes (e.g., `1073741824` for 1GB). Set to `0` for
    unlimited, `null` for no change.
    - **data_limit_reset_strategy**: New strategy for data limit reset. Options include 'daily',
    'weekly', 'monthly', or 'no_reset'.
    - **proxies**: Dictionary of new protocol settings (e.g., `vmess`, `vless`). Empty dictionary means
    no change.
    - **inbounds**: Dictionary of new protocol tags to specify inbound connections. Empty dictionary
    means no change.
    - **note**: New optional text for additional user information or notes. `null` means no change.
    - **on_hold_timeout**: New UTC timestamp for when `on_hold` status should start or end. Only
    applicable if status is changed to 'on_hold'.
    - **on_hold_expire_duration**: New duration (in seconds) for how long the user should stay in
    `on_hold` status. Only applicable if status is changed to 'on_hold'.

    Note: Fields set to `null` or omitted will not be modified.

    Args:
        username (str):
        body (UserModify):  Example: {'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    body: UserModify,
) -> Optional[Union[HTTPValidationError, UserResponse]]:
    """Modify User

     Modify an existing user

    - **username**: Cannot be changed. Used to identify the user.
    - **status**: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'.
    - **expire**: UTC timestamp for new account expiration. Set to `0` for unlimited, `null` for no
    change.
    - **data_limit**: New max data usage in bytes (e.g., `1073741824` for 1GB). Set to `0` for
    unlimited, `null` for no change.
    - **data_limit_reset_strategy**: New strategy for data limit reset. Options include 'daily',
    'weekly', 'monthly', or 'no_reset'.
    - **proxies**: Dictionary of new protocol settings (e.g., `vmess`, `vless`). Empty dictionary means
    no change.
    - **inbounds**: Dictionary of new protocol tags to specify inbound connections. Empty dictionary
    means no change.
    - **note**: New optional text for additional user information or notes. `null` means no change.
    - **on_hold_timeout**: New UTC timestamp for when `on_hold` status should start or end. Only
    applicable if status is changed to 'on_hold'.
    - **on_hold_expire_duration**: New duration (in seconds) for how long the user should stay in
    `on_hold` status. Only applicable if status is changed to 'on_hold'.

    Note: Fields set to `null` or omitted will not be modified.

    Args:
        username (str):
        body (UserModify):  Example: {'proxies': {'vmess': {'id':
            '35e4e39c-7d5c-4f4b-8b71-558e4f37ff53'}, 'vless': {}}, 'inbounds': {'vmess': ['VMess TCP',
            'VMess Websocket'], 'vless': ['VLESS TCP REALITY', 'VLESS GRPC REALITY']}, 'expire': 0,
            'data_limit': 0, 'data_limit_reset_strategy': 'no_reset', 'status': 'active', 'note': '',
            'on_hold_timeout': '2023-11-03T20:30:00', 'on_hold_expire_duration': 0}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
