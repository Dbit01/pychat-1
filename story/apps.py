from django.apps import AppConfig
from Chat.settings import BASE_DIR
import xml.etree.ElementTree as etree


class DefaultSettingsConfig(AppConfig):
	name = 'story'
	verbose_name = 'djangochat'

	colors = {}

	def ready(self):
		tree = etree.parse(BASE_DIR + '/Chat/DefaultScheme.xml')
		root = tree.getroot().find('colors')
		for child in root:
			self.colors[child.tag] = child.text