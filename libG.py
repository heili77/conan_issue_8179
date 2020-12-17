from conans import ConanFile

class Recipe(ConanFile):
    name = "libG"
    settings = "os", "arch", "compiler", "build_type"

    requires = "libH/1.1.1"
