class PaginationHelper:

    def __init__(self, collection, items_per_page):
        """
        Saves collection of items and the number of items per page to instance.
        Also creates a page index for each item

        """
        self.items = collection
        self.items_per_page = items_per_page
        self.page_indexes = [
            i // items_per_page for i in range(len(collection))]

    def item_count(self):
        """Returns the number of items within the entire collection"""
        return len(self.items)

    def page_count(self):
        """Returns the number of pages"""
        return self.page_indexes[-1] + 1

    def page_item_count(self, page_index):
        """
        Returns the number of items on the current page. page_index is zero based
        Returns -1 if page_index is out of range
        """
        if page_index < 0 or page_index >= self.page_count():
            return -1

        return self.page_indexes.count(page_index)

    def page_index(self, item_index):
        """
        Determines what page an item is on. Zero based indexes.
        Returns -1 if item_index is out of range
        """
        if item_index < 0 or item_index >= self.item_count():
            return -1

        return self.page_indexes[item_index]
