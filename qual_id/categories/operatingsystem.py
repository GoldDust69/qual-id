from ..category import Category


class OperatingSystem(Category):
    def get_values(self):
        return [
            "android",
            "archlinux",
            "centos",
            "chromeos",
            "fedora",
            "freebsd",
            "haiku",
            "macos",
            "mandriva",
            "redhatlinux",
            "solaris",
            "steamos",
            "ubuntu",
            "windows",
        ]
