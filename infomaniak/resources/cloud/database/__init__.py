from __future__ import annotations

from .ip import Ip, AsyncIp
from .data import Data, AsyncData
from .config import Config, AsyncConfig
from .backups import Backups, AsyncBackups
from .restore import Restore, AsyncRestore
from infomaniak.utils import parse, plist
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.cloud import (
    DatabaseService, DatabaseServiceBoolResponse,
    DatabaseServiceCreationResponse, DatabaseServiceConnectionResponse,
    CreateDatabaseServiceBackupScheduleRequest)


class Database(Resouce):
    """Cloud database resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.backups = Backups(client)
        self.config = Config(client)
        self.data = Data(client)
        self.ip = Ip(client)
        self.restore = Restore(client)

    def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DatabaseService]:
        """
        List database services for a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[DatabaseService]: The list of database services and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas"
        params: dict[str, str | int] = {}
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = self._client.get(url, params=params or None)
        payload = response.json()

        return plist(
            [parse(DatabaseService, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def list_all(
        self,
        account_id: int,
        *,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DatabaseService]:
        """
        List database services for all public clouds in an account.

        Args:
            account_id: The unique identifier of the account.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[DatabaseService]: The list of database services and pagination metadata.
        """
        url = "/1/public_clouds/dbaas"
        params: dict[str, str | int] = {"account_id": account_id}
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = self._client.get(url, params=params)
        payload = response.json()

        return plist(
            [parse(DatabaseService, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        name: str,
        pack_id: str,
        region: str,
        type_: str,
        version: str,
        *,
        backup_schedule: CreateDatabaseServiceBackupScheduleRequest | None = None,
    ) -> DatabaseServiceCreationResponse:
        """
        Create a database service in a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            name: The database service name.
            pack_id: The database service pack identifier.
            region: The public cloud region.
            type_: The database engine type.
            version: The database engine version.
            backup_schedule: Optional backup schedule settings.

        Returns:
            DatabaseServiceCreationResponse: The created service bootstrap payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas"
        payload: dict[str, str | dict[str, int | bool | str | None]] = {
            "name": name,
            "pack_id": pack_id,
            "region": region,
            "type": type_,
            "version": version,
        }
        if backup_schedule is not None:
            payload["backup_schedule"] = {
                "add_default_schedule": backup_schedule.add_default_schedule,
                "is_pitr_enabled": backup_schedule.is_pitr_enabled,
                "retention": backup_schedule.retention,
                "scheduled_at": backup_schedule.scheduled_at,
            }

        response = self._client.post(url, json=payload)
        return parse(DatabaseServiceCreationResponse, response.json())

    def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        with_: str | None = None,
    ) -> DatabaseService:
        """
        Retrieve a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.

        Returns:
            DatabaseService: The requested database service details.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        return parse(DatabaseService, response.json()["data"])

    def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        keep_backup_files: bool | None = None,
    ) -> DatabaseServiceBoolResponse:
        """
        Delete a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            keep_backup_files: Whether backups should be preserved after deletion.

        Returns:
            DatabaseServiceBoolResponse: The API operation result with a boolean data payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        params = {"keep_backup_files": keep_backup_files} if keep_backup_files is not None else None

        response = self._client.delete(url, params=params)
        return parse(DatabaseServiceBoolResponse, response.json())

    def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        name: str | None = None,
        pack_id: str | None = None,
    ) -> DatabaseServiceBoolResponse:
        """
        Update a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            name: Optional new database service name.
            pack_id: Optional new database service pack identifier.

        Returns:
            DatabaseServiceBoolResponse: The API operation result with a boolean data payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        payload = {"name": name, "pack_id": pack_id}
        response = self._client.patch(
            url,
            json={key: value for key, value in payload.items() if value is not None},
        )
        return parse(DatabaseServiceBoolResponse, response.json())

    def password(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
    ) -> DatabaseServiceConnectionResponse:
        """
        Reset the root password of a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.

        Returns:
            DatabaseServiceConnectionResponse: The connection payload with the new credentials.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/dbaas/{dbaas_id}/reset_password"
        )
        response = self._client.post(url)
        return parse(DatabaseServiceConnectionResponse, response.json())


class AsyncDatabase(AsyncResource):
    """Async cloud database resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.backups = AsyncBackups(client)
        self.config = AsyncConfig(client)
        self.data = AsyncData(client)
        self.ip = AsyncIp(client)
        self.restore = AsyncRestore(client)

    async def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DatabaseService]:
        """
        List database services for a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[DatabaseService]: The list of database services and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas"
        params: dict[str, str | int] = {}
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = await self._client.get(url, params=params or None)
        payload = response.json()

        return plist(
            [parse(DatabaseService, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def list_all(
        self,
        account_id: int,
        *,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DatabaseService]:
        """
        List database services for all public clouds in an account.

        Args:
            account_id: The unique identifier of the account.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[DatabaseService]: The list of database services and pagination metadata.
        """
        url = "/1/public_clouds/dbaas"
        params: dict[str, str | int] = {"account_id": account_id}
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = await self._client.get(url, params=params)
        payload = response.json()

        return plist(
            [parse(DatabaseService, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        name: str,
        pack_id: str,
        region: str,
        type_: str,
        version: str,
        *,
        backup_schedule: CreateDatabaseServiceBackupScheduleRequest | None = None,
    ) -> DatabaseServiceCreationResponse:
        """
        Create a database service in a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            name: The database service name.
            pack_id: The database service pack identifier.
            region: The public cloud region.
            type_: The database engine type.
            version: The database engine version.
            backup_schedule: Optional backup schedule settings.

        Returns:
            DatabaseServiceCreationResponse: The created service bootstrap payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas"
        payload: dict[str, str | dict[str, int | bool | str | None]] = {
            "name": name,
            "pack_id": pack_id,
            "region": region,
            "type": type_,
            "version": version,
        }
        if backup_schedule is not None:
            payload["backup_schedule"] = {
                "add_default_schedule": backup_schedule.add_default_schedule,
                "is_pitr_enabled": backup_schedule.is_pitr_enabled,
                "retention": backup_schedule.retention,
                "scheduled_at": backup_schedule.scheduled_at,
            }

        response = await self._client.post(url, json=payload)
        return parse(DatabaseServiceCreationResponse, response.json())

    async def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        with_: str | None = None,
    ) -> DatabaseService:
        """
        Retrieve a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            with_: Optional expansion parameter such as ``projects`` or ``backups``.

        Returns:
            DatabaseService: The requested database service details.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        return parse(DatabaseService, response.json()["data"])

    async def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        keep_backup_files: bool | None = None,
    ) -> DatabaseServiceBoolResponse:
        """
        Delete a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            keep_backup_files: Whether backups should be preserved after deletion.

        Returns:
            DatabaseServiceBoolResponse: The API operation result with a boolean data payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        params = {"keep_backup_files": keep_backup_files} if keep_backup_files is not None else None

        response = await self._client.delete(url, params=params)
        return parse(DatabaseServiceBoolResponse, response.json())

    async def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
        *,
        name: str | None = None,
        pack_id: str | None = None,
    ) -> DatabaseServiceBoolResponse:
        """
        Update a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.
            name: Optional new database service name.
            pack_id: Optional new database service pack identifier.

        Returns:
            DatabaseServiceBoolResponse: The API operation result with a boolean data payload.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/dbaas/{dbaas_id}"
        payload = {"name": name, "pack_id": pack_id}
        response = await self._client.patch(
            url,
            json={key: value for key, value in payload.items() if value is not None},
        )
        return parse(DatabaseServiceBoolResponse, response.json())

    async def password(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        dbaas_id: int,
    ) -> DatabaseServiceConnectionResponse:
        """
        Reset the root password of a database service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            dbaas_id: The unique identifier of the database service.

        Returns:
            DatabaseServiceConnectionResponse: The connection payload with the new credentials.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/dbaas/{dbaas_id}/reset_password"
        )
        response = await self._client.post(url)
        return parse(DatabaseServiceConnectionResponse, response.json())
