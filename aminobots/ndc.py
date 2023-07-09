import typing_extensions

__all__ = ('NDC',)


class NDC(str):

    @classmethod
    def user(cls, userId: str, /) -> typing_extensions.Self:
        return cls(f'ndc://user-profile/{userId}')

    @classmethod
    def community(cls, comId: int, /) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/default')

    @classmethod
    def leaderboards(cls, comId: int, /) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/leaderboards')

    @classmethod
    def featured(cls, comId: int, /) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/featured')

    @classmethod
    def shared_folder(cls, comId: int, /) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/shared-folder')

    @classmethod
    def blog(cls, blogId: str, comId: int = 0) -> typing_extensions.Self:
        return cls(f'ndc://' + ('x{comId}' if comId else '') + f'blog/{blogId}')

    @classmethod
    def wiki(cls, wikiId) -> typing_extensions.Self:
        return cls(f'ndc://item/{wikiId}')

    @classmethod
    def chat(cls, comId: int, chatId: str) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/chat-thread/{chatId}')

    @classmethod
    def public_chatrooms(cls, comId: int, /) -> typing_extensions.Self:
        return cls(f'ndc://x{comId}/public-chats')

    @classmethod
    def chat_bubble(cls, bubbleId: str, /) -> typing_extensions.Self:
        return cls(f'ndc://chat-bubble/{bubbleId}')
