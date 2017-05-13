class GitImporter(object):
	def _init_(self):
		self.current_module_code = ""


	def find_module(self,fullname,path=None):
		if configured:
			print "[*] Attempting to retrieve %s" % fullname
			new_library = get_file_contents("modules/%s" % fullname)


		if new_library is not None:
			self.current_module_code = base64.b64decode(new_library)
			return self


			return None