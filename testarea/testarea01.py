
class NoneOnTile:
    """Base Class for OnTile Classes"""
    name_id = 'NONE'
    name = 'Empty Tile'
    quote = 'A plain square of land.'
    description = 'Vacant Plot of Land. You can plant your vegetables on it.'

    status_prerequisite = []

    def __init__(self, parent_tile):
        self.parent_tile = [parent_tile]

    def update_cycle(self):
        return 0

    def get_txt_top(self) -> str:
        return '===='

    def get_txt_bot(self) -> str:
        return '===='

    def get_txt_mid(self) -> str:
        return self.name_id

class Tile:
    def __init__(self, parent_plot):
        self.parent_plot = parent_plot
        self.status_effects = []
        self.txt_top = '===='
        self.txt_mid = '===='
        self.txt_bot = '===='
        self.set_OnTile('NONE')



    def set_OnTile(self, child_ontile_id:str):
        self.child_ontile = OnTileREF[child_ontile_id](self)
        self.txt_top = self.child_ontile.get_txt_top()
        self.txt_mid = self.child_ontile.get_txt_mid()
        self.txt_bot = self.child_ontile.get_txt_bot()

    def cycle_update(self):
        self.child_ontile.cycle_update()

    def set_update_all(self, child_ontile_id:str=False, txt_top=False, txt_mid=False, txt_bot=False):
        if child_ontile_id:
            self.set_OnTile(child_ontile_id)
        if txt_top:
            self.txt_top = txt_top
        if txt_mid:
            self.txt_mid = txt_mid
        if txt_bot:
            self.txt_bot = txt_bot

    def set_update_txt(self, txt_top=False, txt_mid=False, txt_bot=False):
        if txt_top:
            self.txt_top = txt_top
        else:
            self.txt_top = '===='
        if txt_mid:
            self.txt_mid = txt_mid
        else:
            self.txt_mid = '===='
        if txt_bot:
            self.txt_bot = txt_bot
        else:
            self.txt_bot = '===='

    def debug_print(self):
        print(self.child_ontile.name, self.txt_top, self.txt_mid, self.txt_bot, sep='||')

class GrowableOnTile(NoneOnTile):
    """Intermediate Class for Growable Ontile Classes"""
    name_id = 'D_PL'
    name = 'debug_PlantOnTile'
    quote = 'You are not supposed to see this.'
    description = 'Intermediate Class for Growable Ontile Classes'

    status_prerequisite = ['debug_test']

    cycles_to_harvest = 2

    def __init__(self, parent_tile: Tile):
        super().__init__(parent_tile)
        self.cycles_left_harvest = self.cycles_to_harvest
        self.parent_tile[0].txt_bot = self.cycles_to_harvest

    def get_txt_bot(self) -> str:
        if self.cycles_left_harvest > -1:
            return f"={self.cycles_left_harvest:02}="
        else:
            return f"={self.cycles_left_harvest}="

    def cycle_update(self):
        self.cycles_left_harvest -= 1
        print(self.cycles_left_harvest)

        self.parent_tile[0].set_update_txt(False, self.get_txt_mid(), self.get_txt_bot())
        [p.set_update_txt(False, self.get_txt_mid()) for p in self.parent_tile[1:]]

        return self.cycles_left_harvest







OnTileREF = {'NONE': NoneOnTile, 'D_GR':GrowableOnTile}

testTile = Tile(None)
testTile.set_OnTile('D_GR')
testTile.cycle_update()
testTile.debug_print()

