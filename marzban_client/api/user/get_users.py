from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse, UserStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    search: Union[Unset, str] = UNSET,
    admin: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_username: Union[Unset, List[str]] = UNSET
    if not isinstance(username, Unset):
        json_username = username

    params["username"] = json_username

    params["search"] = search

    json_admin: Union[Unset, List[str]] = UNSET
    if not isinstance(admin, Unset):
        json_admin = admin

    params["admin"] = json_admin

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersResponse.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.model_validate(response.json())

        return response_401
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = HTTPException.model_validate(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Forbidden.model_validate(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.model_validate(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
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
    username: Union[Unset, List[str]] = UNSET,
    search: Union[Unset, str] = UNSET,
    admin: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        search (Union[Unset, str]):
        admin (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
        search=search,
        admin=admin,
        status=status,
        sort=sort,
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
    username: Union[Unset, List[str]] = UNSET,
    search: Union[Unset, str] = UNSET,
    admin: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        search (Union[Unset, str]):
        admin (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        username=username,
        search=search,
        admin=admin,
        status=status,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    search: Union[Unset, str] = UNSET,
    admin: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        search (Union[Unset, str]):
        admin (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        username=username,
        search=search,
        admin=admin,
        status=status,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    username: Union[Unset, List[str]] = UNSET,
    search: Union[Unset, str] = UNSET,
    admin: Union[Unset, List[str]] = UNSET,
    status: Union[Unset, UserStatus] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]]:
    """Get Users

     Get all users

    Args:
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        username (Union[Unset, List[str]]):
        search (Union[Unset, str]):
        admin (Union[Unset, List[str]]):
        status (Union[Unset, UserStatus]): An enumeration.
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPException, HTTPValidationError, NotFound, Unauthorized, UsersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            username=username,
            search=search,
            admin=admin,
            status=status,
            sort=sort,
        )
    ).parsed
