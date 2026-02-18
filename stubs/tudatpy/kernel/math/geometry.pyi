from __future__ import annotations
import typing
__all__: list[str] = ['Capsule', 'CompositeSurfaceGeometry', 'SurfaceGeometry']
class Capsule(CompositeSurfaceGeometry):
    def __init__(self, nose_radius: typing.SupportsFloat, middle_radius: typing.SupportsFloat, rear_length: typing.SupportsFloat, rear_angle: typing.SupportsFloat, side_radius: typing.SupportsFloat) -> None:
        ...
    @property
    def length(self) -> float:
        ...
    @property
    def middle_radius(self) -> float:
        ...
    @property
    def volume(self) -> float:
        ...
class CompositeSurfaceGeometry(SurfaceGeometry):
    pass
class SurfaceGeometry:
    pass
