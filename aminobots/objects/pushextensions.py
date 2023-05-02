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
from dataclasses import dataclass
from functools import cached_property

__all__ = ('PushExtensions',)


@dataclass(repr=False)
class PushExtensions:
    """Represents the Global/Community notification settings.

    Attributes
    ----------
    json : :class:`dict`
        The raw API data.
    activitiesEnabled : :class:`bool`
        Notifications from others members activities.
    broadcastsEnabled : :class:`bool`
        Broadcasts from Leaders.
    enabled : :class:`bool`
        All notifications from the community.

    """
    json: dict

    @cached_property
    def activitiesEnabled(self) -> bool:
        """Notifications from others members activities.

        Push notifications for others posts and comments.

        """
        return self.json.get('communityActivitiesEnabled')

    @cached_property
    def broadcastsEnabled(self) -> bool:
        """Broadcasts from Leaders.

        Push notifications sent by Leaders of the community.

        """
        return self.json.get('communityBroadcastsEnabled')

    @cached_property
    def enabled(self) -> bool:
        """All notifications from the community.
        
        Chat Messages, Comments, etc...

        """
        return self.json.get('systemEnabled')
