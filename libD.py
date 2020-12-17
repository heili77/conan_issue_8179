from conans import ConanFile

class Recipe(ConanFile):
    name = "libD"
    settings = "os", "arch", "compiler", "build_type"

    build_requires = "libE/1.1.2", "libF/1.1.2", "libG/1.1.2"