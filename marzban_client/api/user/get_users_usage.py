from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, Unauthorized, UsersUsagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
    admin: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    json_admin: Union[Unset, List[str]] = UNSET
    if not isinstance(admin, Unset):
        json_admin = admin

    params["admin"] = json_admin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/users/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersUsagesResponse.model_validate(response.json())

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
) -> Response[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
    admin: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    """Get Users Usage

     Get all users usage

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.
        admin (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        admin=admin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
    admin: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    """Get Users Usage

     Get all users usage

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.
        admin (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        admin=admin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
    admin: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    """Get Users Usage

     Get all users usage

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.
        admin (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        admin=admin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
    admin: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]]:
    """Get Users Usage

     Get all users usage

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.
        admin (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Unauthorized, UsersUsagesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            admin=admin,
        )
    ).parsed
