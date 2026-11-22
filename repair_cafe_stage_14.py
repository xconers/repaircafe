# === Stage 14: Избранное ===
# Project: RepairCafe
from dataclasses import dataclass, field
from typing import List, Set, Dict


@dataclass
class Favorite:
    request_id: str
    added_at: str = ""


class FavoriteManager:
    def __init__(self) -> None:
        self._favorites: Set[str] = set()
        self._details: Dict[str, Favorite] = {}

    def is_favorited(self, request_id: str) -> bool:
        return request_id in self._favorites

    def toggle_favorite(self, request_id: str, now: str = "") -> bool:
        if request_id in self._favorites:
            self._favorites.discard(request_id)
            self._details.pop(request_id, None)
            return False
        favorite = Favorite(request_id=request_id, added_at=now)
        self._favorites.add(request_id)
        self._details[request_id] = favorite
        return True

    def remove_favorite(self, request_id: str) -> bool:
        if request_id not in self._favorites:
            return False
        self._favorites.discard(request_id)
        self._details.pop(request_id, None)
        return True

    def get_favorite(self, request_id: str) -> Favorite | None:
        return self._details.get(request_id)

    def add_favorite(self, request_id: str, now: str = "") -> None:
        if request_id not in self._favorites:
            favorite = Favorite(request_id=request_id, added_at=now)
            self._favorites.add(request_id)
            self._details[request_id] = favorite

    def remove_favorite_now(self, request_id: str, now: str = "") -> None:
        if request_id in self._favorites:
            favorite = Favorite(request_id=request_id, added_at=now)
            self._favorites.add(request_id)
            self._details[request_id] = favorite

    def list_favorites(self) -> List[str]:
        return sorted(self._favorites)

    def clear(self) -> None:
        self._favorites.clear()
        self._details.clear()
