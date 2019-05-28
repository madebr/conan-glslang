# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    exports_sources = ['shader.frag', ]

    def test(self):
        try:
            os.unlink("shader.spv")
        except FileNotFoundError:
            pass
        self.run('glslangValidator -V "{}/shader.frag" -o shader.spv'.format(self.source_folder))
        assert os.path.exists("shader.spv")
