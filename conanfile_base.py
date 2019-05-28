# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class ConanfileBase(ConanFile):
    _base_name = "glslang"
    name = "glslang"
    version = "7.11.3214"
    description = "Khronos reference front-end for GLSL and ESSL, and sample SPIR-V generator"
    topics = ("conan", "khronos", "glsl", "shader", "fragment", "vertex", "spirv", )
    url = "https://github.com/bincrafters/conan-glslang_installer"
    homepage = "https://github.com/KhronosGroup/glslang"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = ("MIT", "NVIDEA", )
    exports = ["LICENSE.md", ]
    exports_sources = ["CMakeLists.txt", ]
    generators = "cmake",

    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/KhronosGroup/{}/archive/{}.tar.gz".format(self._base_name, self.version)
        sha256 = "b30b4668734328d256e30c94037e60d3775b1055743c04d8fd709f2960f302a9"
        tools.get(source_url, sha256=sha256)
        os.rename("glslang-{}".format(self.version), self._source_subfolder)

        tools.replace_in_file(os.path.join(self._source_subfolder, "OGLCompilersDLL", "CMakeLists.txt"),
                              "add_library(OGLCompiler STATIC",
                              "add_library(OGLCompiler")
        for subdir in ("Unix", "Windows", ):
            tools.replace_in_file(os.path.join(self._source_subfolder, "glslang", "OSDependent", subdir, "CMakeLists.txt"),
                                  "add_library(OSDependent STATIC",
                                  "add_library(OSDependent")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
