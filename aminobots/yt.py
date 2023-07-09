import dataclasses
import functools
import typing


@dataclasses.dataclass(repr=False, frozen=True)
class ThumbnailList:
    json: typing.List[dict]

    @functools.cached_property
    def width(self) -> typing.List[int]:
        return [t.get('width', 0) for t in self.json]

    @functools.cached_property
    def height(self) -> typing.List[int]:
        return [t.get('height', 0) for t in self.json]

    @functools.cached_property
    def url(self) -> typing.List[str]:
        return [t.get('url') for t in self.json]

    @functools.cached_property
    def size(self) -> typing.Tuple[int, int]:
        return zip(self.width, self.height)


@dataclasses.dataclass(repr=False, frozen=True)
class VideoRender:
    json: dict

    @functools.cached_property
    def id(self) -> str:
        """Video ID."""
        return self.json.get('videoId')

    @functools.cached_property
    def title(self) -> str:
        return self.json.get('title', {}).get('runs', [{}])[0].get('text')

    @functools.cached_property
    def thumbnail(self) -> ThumbnailList:
        return ThumbnailList(self.json.get('thumbnzail', {}).get('thumbnails', []))

    @functools.cached_property
    def publishedTime(self) -> str:
        return self.json.get('publishedTimeText', {}).get('simpleText')

    @functools.cached_property
    def duration(self) -> int:
        vals = self.json.get('lengthText', {}).get('simpleText', '0:0').split(':')[::-1]
        return sum(60**c * int(n) for c, n in enumerate(vals))

    @functools.cached_property
    def viewCount(self) -> str:
        return self.json.get('viewCountText', {}).get('simpleText')


@dataclasses.dataclass(repr=False, frozen=True)
class VideoRenderList:
    json: typing.List[dict]

    @functools.lru_cache()
    def __getitem__(self, index, /) -> VideoRender:
        return VideoRender(self.json[index])

    @functools.cached_property
    def ids(self) -> typing.List[str]:
        return [vr.get('videoId') for vr in self.json]


@dataclasses.dataclass(repr=False, frozen=True)
class Results:
    json: dict
