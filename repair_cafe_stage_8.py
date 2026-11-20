# === Stage 8: Теги ===
# Project: RepairCafe
class RepairRequestTags:
    def __init__(self):
        self._tags = set()

    def add_tag(self, tag):
        if not tag:
            return False
        self._tags.add(tag)
        return True

    def remove_tag(self, tag):
        return self._tags.discard(tag) or True

    def has_tag(self, tag):
        return tag in self._tags

    def tags(self):
        return set(self._tags)

    def search_by_tag(self, tag):
        return [t for t in self._tags if t == tag]
