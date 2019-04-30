class Room:
	status = 0
	shortDescr = ""
	longDescr = ""
	playerFlag = 0
	itemList = []
	featureList = []

	def __init__(self, stat, pf):
		self.status = stat
		self.playerFlag = pf

	def set_status(self, stat):
		self.status = stat

	def get_status(self):
		return self.status

	def set_shortDescr(self, sd):
		self.shortDescr = sd

	def get_shortDescr(self):
		return self.shortDescr

	def set_longDescr(self, ld):
                self.longDescr = ld

        def get_longDescr(self):
                return self.longDescr

	def set_playerFlag(self, pf):
		self.playerFlag = pf

	def get_playerFlag(self):
		return self.playerFlag

	def add_item(self, item):
		self.itemList.append(item)

	def rem_item(self, item):
		self.itemList.remove(item)

	def get_itemList(self):
		return self.itemList

	def print_itemList(self):
		return #code needed to convert list to string

	def add_feature(self, feat):
		self.featureList.append(feat)

	def get_featureList(self):
		return self.featureList

	def print_featureList(self):
		return #code needed to convert list to string
