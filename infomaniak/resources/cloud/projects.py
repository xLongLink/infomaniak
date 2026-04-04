from __future__ import annotations

from dacite import from_dict

from infomaniak.models.cloud import (
    CreatePublicCloudProjectResponse,
    PublicCloudProject,
    PublicCloudProjectAsyncActionResponse,
    PublicCloudProjectInvitationResponse,
    PublicCloudProjectListResponse,
)
from infomaniak.resource import AsyncResource, Resouce


class Projects(Resouce):
    """Public cloud projects endpoints."""

    def create(
        self,
        public_cloud_id: int,
        project_name: str,
        user_password: str,
        *,
        user_description: str | None = None,
        user_email: str | None = None,
    ) -> CreatePublicCloudProjectResponse:
        """
        Create a new public cloud project with user.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            project_name (str): The project name.
            user_password (str): The user password for the initial project user.
            user_description (str | None): Optional user description.
            user_email (str | None): Optional email for the initial project user.

        Returns:
            CreatePublicCloudProjectResponse: The asynchronous task payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects"
        payload: dict[str, str] = {
            "project_name": project_name,
            "user_password": user_password,
        }
        if user_description is not None:
            payload["user_description"] = user_description
        if user_email is not None:
            payload["user_email"] = user_email

        response = self._client.post(url, json=payload)
        return from_dict(CreatePublicCloudProjectResponse, response.json())

    def create_with_invitation(
        self,
        public_cloud_id: int,
        project_name: str,
        user_email: str,
        *,
        user_description: str | None = None,
    ) -> PublicCloudProjectInvitationResponse:
        """
        Create a new public cloud project with a user invitation.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            project_name (str): The project name.
            user_email (str): The email address to invite to the project.
            user_description (str | None): Optional description for the invited user.

        Returns:
            PublicCloudProjectInvitationResponse: The asynchronous invitation payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/invite"
        payload: dict[str, str] = {
            "project_name": project_name,
            "user_email": user_email,
        }
        if user_description is not None:
            payload["user_description"] = user_description

        response = self._client.post(url, json=payload)
        return from_dict(PublicCloudProjectInvitationResponse, response.json())

    def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        name: str,
    ) -> PublicCloudProjectAsyncActionResponse:
        """
        Update a public cloud project.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.
            name (str): The new project name.

        Returns:
            PublicCloudProjectAsyncActionResponse: The asynchronous update payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        response = self._client.patch(url, json={"name": name})
        return from_dict(PublicCloudProjectAsyncActionResponse, response.json())

    def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
    ) -> PublicCloudProjectAsyncActionResponse:
        """
        Delete a public cloud project and its users.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.

        Returns:
            PublicCloudProjectAsyncActionResponse: The asynchronous deletion payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        response = self._client.delete(url)
        return from_dict(PublicCloudProjectAsyncActionResponse, response.json())

    def list(
        self,
        public_cloud_id: int,
        *,
        with_: str | None = None,
    ) -> PublicCloudProjectListResponse:
        """
        List all projects of a public cloud product.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            with_ (str | None): Optional expansion parameter, such as ``services``.

        Returns:
            PublicCloudProjectListResponse: The list of public cloud projects and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects"
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        payload = response.json()
        return PublicCloudProjectListResponse(
            data=[from_dict(PublicCloudProject, item) for item in payload["data"]],
            total=payload.get("total"),
            page=payload.get("page"),
            pages=payload.get("pages"),
            items_per_page=payload.get("items_per_page"),
        )

    def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
    ) -> PublicCloudProject:
        """
        Retrieve a public cloud project.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.
            with_ (str | None): Optional expansion parameter, such as ``services``.

        Returns:
            PublicCloudProject: The requested public cloud project details.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        return from_dict(PublicCloudProject, response.json()["data"])


class AsyncProjects(AsyncResource):
    """Async public cloud projects endpoints."""

    async def create(
        self,
        public_cloud_id: int,
        project_name: str,
        user_password: str,
        *,
        user_description: str | None = None,
        user_email: str | None = None,
    ) -> CreatePublicCloudProjectResponse:
        """
        Create a new public cloud project with user.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            project_name (str): The project name.
            user_password (str): The user password for the initial project user.
            user_description (str | None): Optional user description.
            user_email (str | None): Optional email for the initial project user.

        Returns:
            CreatePublicCloudProjectResponse: The asynchronous task payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects"
        payload: dict[str, str] = {
            "project_name": project_name,
            "user_password": user_password,
        }
        if user_description is not None:
            payload["user_description"] = user_description
        if user_email is not None:
            payload["user_email"] = user_email

        response = await self._client.post(url, json=payload)
        return from_dict(CreatePublicCloudProjectResponse, response.json())

    async def create_with_invitation(
        self,
        public_cloud_id: int,
        project_name: str,
        user_email: str,
        *,
        user_description: str | None = None,
    ) -> PublicCloudProjectInvitationResponse:
        """
        Create a new public cloud project with a user invitation.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            project_name (str): The project name.
            user_email (str): The email address to invite to the project.
            user_description (str | None): Optional description for the invited user.

        Returns:
            PublicCloudProjectInvitationResponse: The asynchronous invitation payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/invite"
        payload: dict[str, str] = {
            "project_name": project_name,
            "user_email": user_email,
        }
        if user_description is not None:
            payload["user_description"] = user_description

        response = await self._client.post(url, json=payload)
        return from_dict(PublicCloudProjectInvitationResponse, response.json())

    async def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        name: str,
    ) -> PublicCloudProjectAsyncActionResponse:
        """
        Update a public cloud project.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.
            name (str): The new project name.

        Returns:
            PublicCloudProjectAsyncActionResponse: The asynchronous update payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        response = await self._client.patch(url, json={"name": name})
        return from_dict(PublicCloudProjectAsyncActionResponse, response.json())

    async def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
    ) -> PublicCloudProjectAsyncActionResponse:
        """
        Delete a public cloud project and its users.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.

        Returns:
            PublicCloudProjectAsyncActionResponse: The asynchronous deletion payload returned by the API.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        response = await self._client.delete(url)
        return from_dict(PublicCloudProjectAsyncActionResponse, response.json())

    async def list(
        self,
        public_cloud_id: int,
        *,
        with_: str | None = None,
    ) -> PublicCloudProjectListResponse:
        """
        List all projects of a public cloud product.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            with_ (str | None): Optional expansion parameter, such as ``services``.

        Returns:
            PublicCloudProjectListResponse: The list of public cloud projects and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects"
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        payload = response.json()
        return PublicCloudProjectListResponse(
            data=[from_dict(PublicCloudProject, item) for item in payload["data"]],
            total=payload.get("total"),
            page=payload.get("page"),
            pages=payload.get("pages"),
            items_per_page=payload.get("items_per_page"),
        )

    async def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
    ) -> PublicCloudProject:
        """
        Retrieve a public cloud project.

        Args:
            public_cloud_id (int): The unique identifier of the public cloud product.
            public_cloud_project_id (int): The unique identifier of the public cloud project.
            with_ (str | None): Optional expansion parameter, such as ``services``.

        Returns:
            PublicCloudProject: The requested public cloud project details.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}"
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        return from_dict(PublicCloudProject, response.json()["data"])


__all__ = ["Projects", "AsyncProjects"]
