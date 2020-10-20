class Archive:
    def __init__(
        self,
        url, archive_ext, archive_dir, extract_dir,
        **kwargs
    ):
        self.url = url
        self.archive_ext = archive_ext
        self.archive_dir = archive_dir
        self.extract_dir = extract_dir
        super().__init__(**kwargs)

    def get(self):
        archive = path.join(self.extract_dir, f"temp.{self.archive_ext}")
        action.download(url, archive)
        action.extract(archive, self.extract_dir)
        action.move(path.join(self.extract_dir, self.archive_dir), self.location)
