"""MIT License

Copyright (c) 2022 ViktorSky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from . import community

__all__ = ('EndpointMatchedCommunity',)


class EndpointMatchedCommunity(community.Community):
    """Represent the AminoId matched community. (endpoint matched)

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    activeInfo: :class:`ActiveInfo`
        Community active info.
    addedTopic: :class:`AddedTopic`
        Community added topics.
    advancedSettings: :class:`AdvancedSettings`
        Community advanced settings.
    agent: :class:`Agent`
        Community user agent profile.
    aminoId: :class:`str`
        Community amino id.
    configuration: :class:`Configuration`
        Community configuration.
    createdTime: :class:`str`
        Community created date.
    description: :class:`str`
        Community description.
    extensions: :class:`Extensions`
        Community extensions.
    heat: :class:`int`
        ...
    icon: :class:`str`
        Community icon url.
    id: :class:`int`
        Community id.
    isStandaloneAppDeprecated: :class:`bool`
        Is tandalone app deprecated.
    isStandaloneAppMonetizationEnabled: :bool:`bool`
        Is standalone app monetization enabled.
    joinType: :class:`int`
        Community join type.
    keywords: Optional[:class:`str`]
        Community search keywords.
    link: :class:`str`
        Community link.
    listedStatus: :class:`int`
        Community listed status.
    media: :class:`MediaList`
        Community media list.
    membersCount: :class:`int`
        Community members count.
    modifiedTime: :class:`str`
        Community last modified date.
    name: :class:`str`
        Community name.
    primaryLanguage: :class:`str`
        Community language.
    probationStatus: :class:`int`
        Community probation status.
    promotionalMedia: :class:`PromotionalMedia`
        Community promotional media.
    searchable: :class:`bool`
        Searchable community.
    status: :class:`int`
        Community status.
    tagline: :class:`str`
        Community tagline.
    themePack: :class:`ThemePack`
        Community theme pack.
    templateId: :class:`int`
        Community template id.
    updatedTime: :class:`str`
        Community updated date.
    vips: :class:`UserProfileList`
        Community vip users.

    """
