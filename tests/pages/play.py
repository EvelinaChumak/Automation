from framework.pages.base_page import BasePage
from framework.elements.label import Label
from framework.utils.random import Random
from tests.config.sequence_of_moves import ROW, COLUMN
from tests.config.sequence_of_moves import SEQUENCE_OF_MOVES


class Play(BasePage):

    _for_hit = 4
    hit_cell = None
    _row = 0
    _col = 0

    move_list = list(SEQUENCE_OF_MOVES)

    lbl_chat_loc = "//*[@class='chat-gap']"

    lbl_cell_loc = "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]"
    lbl_cell = Label(locator=lbl_cell_loc, name="Cell")

    style_miss_auto = "battlefield-cell__miss__auto"
    style_miss = "battlefield-cell__miss"
    style_hit = "battlefield-cell__hit"
    style_done = "battlefield-cell__done"

    def __init__(self):
        super().__init__(locator=Play.lbl_chat_loc, page_name=self.__class__.__name__)
        self.lbl_chat = Label(locator=self.lbl_chat_loc, name="Chat")

    def _create_cell(self, row, collummn):
        lbl_cell_loc = (
            "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]".format(
                row, collummn
            )
        )
        for key, value in ROW.items():
            if value == row:
                row = key
        for key, value in COLUMN.items():
            if value == collummn:
                collummn = key
        lbl_cell = Label(locator=lbl_cell_loc, name="Cell: {} {}".format(row, collummn))
        return lbl_cell

    def find_neighboring_cell(self):

        hit_attribute = self.hit_cell.get_attribute_class()
        cell_attribute = hit_attribute

        while self.style_hit in hit_attribute:
            lbl_cell = self.hit_cell
            i = self._row
            j = self._col
            rand = Random.get_number_1_to_4()
            if rand == 1 and i != 1:  # top row = 1
                i = i - 1
                self._for_hit = self._for_hit - 1
                lbl_cell = self._create_cell(i, j)
                cell_attribute = lbl_cell.get_attribute_class()
                if (
                    self.style_miss in cell_attribute
                    or self.style_hit in cell_attribute
                ):
                    i = i + 1
                else:
                    lbl_cell.click()

            elif rand == 2 and i != 10:  # bottom row = 10
                i = i + 1
                lbl_cell = self._create_cell(i, j)
                cell_attribute = lbl_cell.get_attribute_class()
                self._for_hit = self._for_hit - 1
                if (
                    self.style_miss in cell_attribute
                    or self.style_hit in cell_attribute
                ):
                    i = i - 1
                else:
                    lbl_cell.click()

            elif rand == 3 and j != 1:  # left collumn = 1
                j = j - 1
                lbl_cell = self._create_cell(i, j)
                cell_attribute = lbl_cell.get_attribute_class()
                self._for_hit = self._for_hit - 1
                if (
                    self.style_miss in cell_attribute
                    or self.style_hit in cell_attribute
                ):
                    j = j + 1
                else:
                    lbl_cell.click()

            elif rand == 4 and j != 10:  # right collumn = 1
                j = j + 1
                lbl_cell = self._create_cell(i, j)
                cell_attribute = lbl_cell.get_attribute_class()
                self._for_hit = self._for_hit - 1
                if (
                    self.style_miss in cell_attribute
                    or self.style_hit in cell_attribute
                ):
                    j = j - 1
                else:
                    lbl_cell.click()

            cell_attribute = lbl_cell.get_attribute_class()

            if (
                self.style_hit in cell_attribute
                and self.style_done not in cell_attribute
                and self._for_hit != 0
            ):
                self.hit_cell = lbl_cell
                self._for_hit = 4
                self._col = j
                self._row = i
            elif self._for_hit == 0 or self.style_done in cell_attribute:
                self.hit_cell = None
                break

    def my_move(self):

        if self.hit_cell is None:

            i = ROW[self.move_list[0][0]]
            j = COLUMN[self.move_list[0][1]]

            lbl_cell = self._create_cell(i, j)
            cell_attribute = lbl_cell.get_attribute_class()

            if not (
                self.style_miss in cell_attribute or self.style_hit in cell_attribute
            ):

                lbl_cell.click()
                cell_attribute = lbl_cell.get_attribute_class()

                if self.style_hit in cell_attribute:
                    self.hit_cell = lbl_cell
                    self._for_hit = 4
                    self._row = i
                    self._col = j

            self.move_list.pop(0)

        else:
            self.find_neighboring_cell()
