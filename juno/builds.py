import functools
from shutil import copyfile
from typing import NamedTuple

from juno.renderables import Renderable, render
from pytils.paths import UrlPath

__all__ = [
    'Buildable',
    'RecipePlan',
    'ResourcePlan'
]

open_file_out = functools.partial(open, mode='w', newline='\n')


class Buildable:

    def build(self, root_path: UrlPath):
        raise NotImplementedError


class RecipePlan(Buildable, NamedTuple):
    build_path: UrlPath
    output: Renderable
    file_name: str = 'index.htm'

    def build(self, root_path: UrlPath):
        target_path = root_path.concatenate(self.build_path)[self.file_name].path
        with open_file_out(target_path) as f:
            render(f, self.output)


class ResourcePlan(Buildable, NamedTuple):
    build_path: UrlPath
    source_path: UrlPath

    def build(self, root_path: UrlPath):
        target_path = root_path.concatenate(self.build_path).path
        copyfile(self.source_path.path, target_path)
