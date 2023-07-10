from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, Field

__all__ = ('Link',)


class Link(BaseModel):
    """Represent a link for the content of posts, chat messages, etc.

    Examples
    --------
    >>> content = "Hello!, see your {}.".format(Link('ndc://user-me', 'profile'))
    >>> content
    'Hello!, see your [ndc://user-me|profile].'
    >>> blog = await amino.post_blog(communityId, input('Blog Title:'), content)

    Parameters
    ----------
    url : :class:`str`
        The link. (amino, ndc, external)
    title : :class:`str` | `None`
        The link title.

    """

    url: Union[AnyUrl, str]
    title: Optional[str] = Field(default=None)

    def __str__(self) -> str:
        return f'[{self.url}|{self.title}]' if self.title else self.url
