from distutils.core import setup

setup(
    name='testing_editable_dots',
    install_requires=["ruamel-yaml"],
    entry_points={
            "console_scripts": [
                "test-with-editable-dots=testing_editable_dots.main:main",
            ],
        },
)