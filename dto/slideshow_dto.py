from dataclasses import dataclass

@dataclass
class Slide:
    title: str
    type: str

@dataclass
class Item:
    item_text: str

@dataclass
class SlideshowDTO:
    author: str
    date: str
    slides: list[Slide]
    title: str

    def from_json(json_data):
        return SlideshowDTO(author=json_data['author'],
                        date=json_data['date'],
                        slides=[Slide(s['title'], s['type']) for s in json_data['slides'] if isinstance(s, dict) and 'items' not in s],
                        title=json_data['title'])