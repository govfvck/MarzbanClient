from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token: str,
    *,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sub/{token}/usage",
        "params": params,
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
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """User Get Usage

     Fetches the usage statistics for the user within a specified date range.

    Args:
        token (str):
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token=token,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """User Get Usage

     Fetches the usage statistics for the user within a specified date range.

    Args:
        token (str):
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        token=token,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """User Get Usage

     Fetches the usage statistics for the user within a specified date range.

    Args:
        token (str):
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token=token,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """User Get Usage

     Fetches the usage statistics for the user within a specified date range.

    Args:
        token (str):
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            token=token,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
