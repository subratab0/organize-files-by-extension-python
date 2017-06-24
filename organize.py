import os;

"""
	function organize all files in
	a directory by its extension type
"""
def get_files():
	w_dir = os.path.dirname(os.path.realpath(__file__))
	all_dir_files = os.listdir(w_dir)

	if all_dir_files:
		extensions = []
		all_files = []
		for i in all_dir_files:
			if os.path.isfile(i) and i != 'organize.py':
				ext = i.split('.')[-1]
				extensions.append(ext)
				all_files.append(i)

		#search each file type and organize
		if extensions:
			for ext in extensions:
				if not os.path.exists(ext):
					os.makedirs(ext)

			for temp_file in all_files:
				ext = temp_file.split('.')[-1];
				existing 	= os.path.join(w_dir,temp_file)
				targeting 	= os.path.join(w_dir , ext)
				try:
					print( "Moving %s to %s" % (temp_file, targeting) )
					os.rename(existing, os.path.join(targeting,temp_file))
				except PermissionError as e:
					print("permission issue on '%s': %s" % (temp_file, str(e)))
				except Exception as e:
					print("Issue: %s" % str(e))

		else:
			print("No files found to organize.")
			return


get_files()
