from infomaniak.resource import AsyncResource, Resouce
from infomaniak.models.domain import (
    UpdateNameserversRequest,
    UpdateNameserversResponse,
)
from dacite import from_dict


class Nameservers(Resouce):
    """Domain nameserver endpoints."""

    def update(
        self,
        domain: str,
        *,
        nameservers: list[str] | None = None,
        use_infomaniak_ns: bool | None = None,
        verify_ns_availability: bool = False,
    ) -> UpdateNameserversResponse:
        """Update a domain's nameservers with `PUT /2/domains/domains/{domain}/nameservers`.

        Args:
            domain: Domain name to update.
            nameservers: Custom nameservers to assign to the domain. Must include at least
                2 entries when provided.
            use_infomaniak_ns: Whether to use Infomaniak nameservers instead of custom
                nameservers.
            verify_ns_availability: When `True`, verify that the new nameservers are
                functional before applying changes.

        Returns:
            Parsed API response with the operation result and a boolean status in `data`.

        Raises:
            ValueError: If neither `nameservers` nor `use_infomaniak_ns` is provided, or if
                `nameservers` contains fewer than 2 values.
        """
        if nameservers is None and use_infomaniak_ns is None:
            raise ValueError(
                "Either nameservers or use_infomaniak_ns must be provided."
            )
        if nameservers is not None and len(nameservers) < 2:
            raise ValueError("nameservers must contain at least 2 values.")

        payload = UpdateNameserversRequest(
            nameservers=nameservers,
            use_infomaniak_ns=use_infomaniak_ns,
            verify_ns_availability=verify_ns_availability,
        )
        json_payload = {
            key: value for key, value in payload.__dict__.items() if value is not None
        }

        response = self._client.put(
            f"/2/domains/domains/{domain}/nameservers",
            json=json_payload,
        )
        return from_dict(UpdateNameserversResponse, response.json())


class AsyncNameservers(AsyncResource):
    """Async domain nameserver endpoints."""

    async def update(
        self,
        domain: str,
        *,
        nameservers: list[str] | None = None,
        use_infomaniak_ns: bool | None = None,
        verify_ns_availability: bool = False,
    ) -> UpdateNameserversResponse:
        """Update a domain's nameservers with `PUT /2/domains/domains/{domain}/nameservers`.

        Args:
            domain: Domain name to update.
            nameservers: Custom nameservers to assign to the domain. Must include at least
                2 entries when provided.
            use_infomaniak_ns: Whether to use Infomaniak nameservers instead of custom
                nameservers.
            verify_ns_availability: When `True`, verify that the new nameservers are
                functional before applying changes.

        Returns:
            Parsed API response with the operation result and a boolean status in `data`.

        Raises:
            ValueError: If neither `nameservers` nor `use_infomaniak_ns` is provided, or if
                `nameservers` contains fewer than 2 values.
        """
        if nameservers is None and use_infomaniak_ns is None:
            raise ValueError(
                "Either nameservers or use_infomaniak_ns must be provided."
            )
        if nameservers is not None and len(nameservers) < 2:
            raise ValueError("nameservers must contain at least 2 values.")

        payload = UpdateNameserversRequest(
            nameservers=nameservers,
            use_infomaniak_ns=use_infomaniak_ns,
            verify_ns_availability=verify_ns_availability,
        )
        json_payload = {
            key: value for key, value in payload.__dict__.items() if value is not None
        }
        response = await self._client.put(
            f"/2/domains/domains/{domain}/nameservers",
            json=json_payload,
        )
        return from_dict(UpdateNameserversResponse, response.json())
