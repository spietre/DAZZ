# coincidencia alebo aj podobnost dvoch objektov
class Coincidence:
	@staticmethod
	def russel(positiveCoincidences: int, noObjects: int):
		return positiveCoincidences / noObjects

	@staticmethod
	def sokal(positiveCoincidences: int, negativeCoincidences: int, noObjects: int):
		return (positiveCoincidences + negativeCoincidences) / noObjects

	@staticmethod
	def jaccard(positiveCoincidences: int, negativeCoincidences: int, noObjects: int):
		return positiveCoincidences / (noObjects - negativeCoincidences)