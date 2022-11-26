__all__: tuple[str, ...] = (
    "ExtsContainer",
)


class ExtsContainer:

    def __init__(
        self,
        *,
        folders: set[str] = set(),
        files: set[str] = set(),
    ) -> None:
        
        if not isinstance(folders, set) or not isinstance(files, set):
            raise ValueError(f"Expected set, got {folders.__class__!r}")
        self.folders = folders
        self.files = files
    
    def __repr__(self) -> str:
        return f"<ExtsContainer folders={self.folders} files={self.files}>"