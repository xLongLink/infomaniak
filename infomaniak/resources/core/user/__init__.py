from infomaniak.resource import Resouce, AsyncResource


class User(Resouce):
    """Core resources for Infomaniak services."""

    def invite(self):
        """https://developer.infomaniak.com/docs/api/post/1/accounts/%7Baccount%7D/invitations"""
        pass

    def revoke(self, account: int, invitation: int):
        """
        Cancel an invitation to join an account.

        This operation deletes a previously created user invitation associated
        with a specific account. The request requires authentication and appropriate
        permissions.

        Args:
            account_id (int): Unique identifier of the account.
            invitation_id (int): Unique identifier of the user invitation.

        Returns:
            bool: True if the invitation was successfully cancelled.

        Raises:
            UnauthorizedError: If authentication is missing or invalid (HTTP 401).
            ForbiddenError: If the user does not have permission to cancel the invitation (HTTP 403).
            NotFoundError: If the account or invitation does not exist or is not accessible (HTTP 404).
            CannotDeleteError: If the invitation cannot be deleted due to a server-side issue (HTTP 500).

        Notes:
            API endpoint:
            https://developer.infomaniak.com/docs/api/delete/1/accounts/{account}/invitations/{invitation}
        """
        URL = f"/accounts/{account}/invitations/{invitation}"
        self._client.delete(URL)

    
class AsyncUser(AsyncResource):
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    async def user(self):
        """Get the current authenticated user."""
        return await self._client._request("GET", "/user")
    