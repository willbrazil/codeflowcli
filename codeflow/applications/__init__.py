from ..application import Application
from .node.node_application import NodeApplication
from .npm.npm_application import NpmApplication
from .sublimetext.sublime_application import SublimeTextApplication
from .virtualenv.virtualenv_application import VirtualEnvApplication

Application = Application
NodeApplication = NodeApplication
NpmApplication = NpmApplication
SublimeTextApplication = SublimeTextApplication
VirtualEnvApplication = VirtualEnvApplication


from .npm.npm_config import config as npm_config
from .sublimetext.sublime_text_config import config as sublime_text_config
from .virtualenv.virtualenv_config import config as virtualenv_config
from .node.node_config import config as node_config

config = {
	NpmApplication.name: npm_config,
	SublimeTextApplication.name: sublime_text_config,
	VirtualEnvApplication.name: virtualenv_config,
	NodeApplication.name: node_config
}