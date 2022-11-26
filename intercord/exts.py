import attrs

__all__: tuple[str, ...] = ("ExtsContainer",)


@attrs.define(kw_only=True)
class ExtsContainer:
    folders: set = attrs.field(default=set())
    files: set = attrs.field(default=set())

    @folders.validator
    def check(self, attr, value):
        if not isinstance(value, set):
            raise ValueError(f"Expected type set, got {value.__class__!r}")

    @files.validator
    def check(self, attr, value):
        if not isinstance(value, set):
            raise ValueError(f"Expected type set, got {value.__class__!r}")

    def __repr__(self) -> str:
        return f"<ExtsContainer folders={self.folders} files={self.files}>"
