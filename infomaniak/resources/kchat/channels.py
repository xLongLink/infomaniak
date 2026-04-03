from infomaniak.resource import AsyncResource, Resouce


class ChannelPrivacy(Resouce):
    def update(self) -> None:
        """Update channel privacy."""
        raise NotImplementedError("kChat channels.privacy.update endpoint is not implemented yet.")


class AsyncChannelPrivacy(AsyncResource):
    async def update(self) -> None:
        """Update channel privacy."""
        raise NotImplementedError("kChat channels.privacy.update endpoint is not implemented yet.")


class ChannelMembersRoles(Resouce):
    def update(self) -> None:
        """Update channel roles."""
        raise NotImplementedError("kChat channels.members.roles.update endpoint is not implemented yet.")


class AsyncChannelMembersRoles(AsyncResource):
    async def update(self) -> None:
        """Update channel roles."""
        raise NotImplementedError("kChat channels.members.roles.update endpoint is not implemented yet.")


class ChannelMembersSchemeRoles(Resouce):
    def update(self) -> None:
        """Update scheme-derived roles."""
        raise NotImplementedError("kChat channels.members.scheme_roles.update endpoint is not implemented yet.")


class AsyncChannelMembersSchemeRoles(AsyncResource):
    async def update(self) -> None:
        """Update scheme-derived roles."""
        raise NotImplementedError("kChat channels.members.scheme_roles.update endpoint is not implemented yet.")


class ChannelMembers(Resouce):
    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = ChannelMembersRoles(client)
        self.scheme_roles = ChannelMembersSchemeRoles(client)

    def list(self) -> None:
        raise NotImplementedError("kChat channels.members.list endpoint is not implemented yet.")

    def add(self) -> None:
        raise NotImplementedError("kChat channels.members.add endpoint is not implemented yet.")

    def by_ids(self) -> None:
        raise NotImplementedError("kChat channels.members.by_ids endpoint is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("kChat channels.members.display endpoint is not implemented yet.")

    def remove(self) -> None:
        raise NotImplementedError("kChat channels.members.remove endpoint is not implemented yet.")


class AsyncChannelMembers(AsyncResource):
    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = AsyncChannelMembersRoles(client)
        self.scheme_roles = AsyncChannelMembersSchemeRoles(client)

    async def list(self) -> None:
        raise NotImplementedError("kChat channels.members.list endpoint is not implemented yet.")

    async def add(self) -> None:
        raise NotImplementedError("kChat channels.members.add endpoint is not implemented yet.")

    async def by_ids(self) -> None:
        raise NotImplementedError("kChat channels.members.by_ids endpoint is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("kChat channels.members.display endpoint is not implemented yet.")

    async def remove(self) -> None:
        raise NotImplementedError("kChat channels.members.remove endpoint is not implemented yet.")


class ChannelNotifications(Resouce):
    def update(self) -> None:
        raise NotImplementedError("kChat channels.notifications.update endpoint is not implemented yet.")


class AsyncChannelNotifications(AsyncResource):
    async def update(self) -> None:
        raise NotImplementedError("kChat channels.notifications.update endpoint is not implemented yet.")


class ChannelScheme(Resouce):
    def set(self) -> None:
        raise NotImplementedError("kChat channels.scheme.set endpoint is not implemented yet.")


class AsyncChannelScheme(AsyncResource):
    async def set(self) -> None:
        raise NotImplementedError("kChat channels.scheme.set endpoint is not implemented yet.")


class ChannelModeration(Resouce):
    def get(self) -> None:
        raise NotImplementedError("kChat channels.moderation.get endpoint is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("kChat channels.moderation.update endpoint is not implemented yet.")


class AsyncChannelModeration(AsyncResource):
    async def get(self) -> None:
        raise NotImplementedError("kChat channels.moderation.get endpoint is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("kChat channels.moderation.update endpoint is not implemented yet.")


class ChannelSidebarCategories(Resouce):
    def list(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.list endpoint is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.create endpoint is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.update endpoint is not implemented yet.")


class AsyncChannelSidebarCategories(AsyncResource):
    async def list(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.list endpoint is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.create endpoint is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.categories.update endpoint is not implemented yet.")


class ChannelSidebarOrder(Resouce):
    def get(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.order.get endpoint is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.order.update endpoint is not implemented yet.")


class AsyncChannelSidebarOrder(AsyncResource):
    async def get(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.order.get endpoint is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.order.update endpoint is not implemented yet.")


class ChannelSidebarCategory(Resouce):
    def display(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.display endpoint is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.update endpoint is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.delete endpoint is not implemented yet.")


class AsyncChannelSidebarCategory(AsyncResource):
    async def display(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.display endpoint is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.update endpoint is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("kChat channels.sidebar.category.delete endpoint is not implemented yet.")


class ChannelSidebar(Resouce):
    def __init__(self, client) -> None:
        super().__init__(client)
        self.categories = ChannelSidebarCategories(client)
        self.order = ChannelSidebarOrder(client)
        self.category = ChannelSidebarCategory(client)


class AsyncChannelSidebar(AsyncResource):
    def __init__(self, client) -> None:
        super().__init__(client)
        self.categories = AsyncChannelSidebarCategories(client)
        self.order = AsyncChannelSidebarOrder(client)
        self.category = AsyncChannelSidebarCategory(client)


class Channels(Resouce):
    """kChat resource for channels endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.privacy = ChannelPrivacy(client)
        self.members = ChannelMembers(client)
        self.notifications = ChannelNotifications(client)
        self.scheme = ChannelScheme(client)
        self.moderation = ChannelModeration(client)
        self.sidebar = ChannelSidebar(client)

    def list(self) -> None:
        raise NotImplementedError("kChat channels.list endpoint is not implemented yet.")

    def create(self) -> None:
        raise NotImplementedError("kChat channels.create endpoint is not implemented yet.")

    def create_direct_message(self) -> None:
        raise NotImplementedError("kChat channels.create_direct_message endpoint is not implemented yet.")

    def create_group_message(self) -> None:
        raise NotImplementedError("kChat channels.create_group_message endpoint is not implemented yet.")

    def search_all(self) -> None:
        raise NotImplementedError("kChat channels.search_all endpoint is not implemented yet.")

    def search_group(self) -> None:
        raise NotImplementedError("kChat channels.search_group endpoint is not implemented yet.")

    def by_ids(self) -> None:
        raise NotImplementedError("kChat channels.by_ids endpoint is not implemented yet.")

    def display(self) -> None:
        raise NotImplementedError("kChat channels.display endpoint is not implemented yet.")

    def update(self) -> None:
        raise NotImplementedError("kChat channels.update endpoint is not implemented yet.")

    def delete(self) -> None:
        raise NotImplementedError("kChat channels.delete endpoint is not implemented yet.")

    def patch(self) -> None:
        raise NotImplementedError("kChat channels.patch endpoint is not implemented yet.")

    def restore(self) -> None:
        raise NotImplementedError("kChat channels.restore endpoint is not implemented yet.")

    def move(self) -> None:
        raise NotImplementedError("kChat channels.move endpoint is not implemented yet.")

    def stats(self) -> None:
        raise NotImplementedError("kChat channels.stats endpoint is not implemented yet.")

    def pinned_posts(self) -> None:
        raise NotImplementedError("kChat channels.pinned_posts endpoint is not implemented yet.")

    def public(self) -> None:
        raise NotImplementedError("kChat channels.public endpoint is not implemented yet.")

    def private(self) -> None:
        raise NotImplementedError("kChat channels.private endpoint is not implemented yet.")

    def deleted(self) -> None:
        raise NotImplementedError("kChat channels.deleted endpoint is not implemented yet.")

    def autocomplete(self) -> None:
        raise NotImplementedError("kChat channels.autocomplete endpoint is not implemented yet.")

    def autocomplete_search(self) -> None:
        raise NotImplementedError("kChat channels.autocomplete_search endpoint is not implemented yet.")

    def search(self) -> None:
        raise NotImplementedError("kChat channels.search endpoint is not implemented yet.")

    def search_archived(self) -> None:
        raise NotImplementedError("kChat channels.search_archived endpoint is not implemented yet.")

    def by_name(self) -> None:
        raise NotImplementedError("kChat channels.by_name endpoint is not implemented yet.")

    def by_name_and_team_name(self) -> None:
        raise NotImplementedError("kChat channels.by_name_and_team_name endpoint is not implemented yet.")

    def view(self) -> None:
        raise NotImplementedError("kChat channels.view endpoint is not implemented yet.")

    def memberships_and_roles(self) -> None:
        raise NotImplementedError("kChat channels.memberships_and_roles endpoint is not implemented yet.")

    def for_user(self) -> None:
        raise NotImplementedError("kChat channels.for_user endpoint is not implemented yet.")

    def all(self) -> None:
        raise NotImplementedError("kChat channels.all endpoint is not implemented yet.")

    def unread_messages(self) -> None:
        raise NotImplementedError("kChat channels.unread_messages endpoint is not implemented yet.")


class AsyncChannels(AsyncResource):
    """Async kChat resource for channels endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.privacy = AsyncChannelPrivacy(client)
        self.members = AsyncChannelMembers(client)
        self.notifications = AsyncChannelNotifications(client)
        self.scheme = AsyncChannelScheme(client)
        self.moderation = AsyncChannelModeration(client)
        self.sidebar = AsyncChannelSidebar(client)

    async def list(self) -> None:
        raise NotImplementedError("kChat channels.list endpoint is not implemented yet.")

    async def create(self) -> None:
        raise NotImplementedError("kChat channels.create endpoint is not implemented yet.")

    async def create_direct_message(self) -> None:
        raise NotImplementedError("kChat channels.create_direct_message endpoint is not implemented yet.")

    async def create_group_message(self) -> None:
        raise NotImplementedError("kChat channels.create_group_message endpoint is not implemented yet.")

    async def search_all(self) -> None:
        raise NotImplementedError("kChat channels.search_all endpoint is not implemented yet.")

    async def search_group(self) -> None:
        raise NotImplementedError("kChat channels.search_group endpoint is not implemented yet.")

    async def by_ids(self) -> None:
        raise NotImplementedError("kChat channels.by_ids endpoint is not implemented yet.")

    async def display(self) -> None:
        raise NotImplementedError("kChat channels.display endpoint is not implemented yet.")

    async def update(self) -> None:
        raise NotImplementedError("kChat channels.update endpoint is not implemented yet.")

    async def delete(self) -> None:
        raise NotImplementedError("kChat channels.delete endpoint is not implemented yet.")

    async def patch(self) -> None:
        raise NotImplementedError("kChat channels.patch endpoint is not implemented yet.")

    async def restore(self) -> None:
        raise NotImplementedError("kChat channels.restore endpoint is not implemented yet.")

    async def move(self) -> None:
        raise NotImplementedError("kChat channels.move endpoint is not implemented yet.")

    async def stats(self) -> None:
        raise NotImplementedError("kChat channels.stats endpoint is not implemented yet.")

    async def pinned_posts(self) -> None:
        raise NotImplementedError("kChat channels.pinned_posts endpoint is not implemented yet.")

    async def public(self) -> None:
        raise NotImplementedError("kChat channels.public endpoint is not implemented yet.")

    async def private(self) -> None:
        raise NotImplementedError("kChat channels.private endpoint is not implemented yet.")

    async def deleted(self) -> None:
        raise NotImplementedError("kChat channels.deleted endpoint is not implemented yet.")

    async def autocomplete(self) -> None:
        raise NotImplementedError("kChat channels.autocomplete endpoint is not implemented yet.")

    async def autocomplete_search(self) -> None:
        raise NotImplementedError("kChat channels.autocomplete_search endpoint is not implemented yet.")

    async def search(self) -> None:
        raise NotImplementedError("kChat channels.search endpoint is not implemented yet.")

    async def search_archived(self) -> None:
        raise NotImplementedError("kChat channels.search_archived endpoint is not implemented yet.")

    async def by_name(self) -> None:
        raise NotImplementedError("kChat channels.by_name endpoint is not implemented yet.")

    async def by_name_and_team_name(self) -> None:
        raise NotImplementedError("kChat channels.by_name_and_team_name endpoint is not implemented yet.")

    async def view(self) -> None:
        raise NotImplementedError("kChat channels.view endpoint is not implemented yet.")

    async def memberships_and_roles(self) -> None:
        raise NotImplementedError("kChat channels.memberships_and_roles endpoint is not implemented yet.")

    async def for_user(self) -> None:
        raise NotImplementedError("kChat channels.for_user endpoint is not implemented yet.")

    async def all(self) -> None:
        raise NotImplementedError("kChat channels.all endpoint is not implemented yet.")

    async def unread_messages(self) -> None:
        raise NotImplementedError("kChat channels.unread_messages endpoint is not implemented yet.")
