{
	'targets':
	[
		{
			'target_name': 'addon',
			'include_dirs': ['../..'],
			'cflags_cc': ['-std=c++11', '-fexceptions', '-frtti'],
			'msvs_settings': { 'VCLinkerTool': { 'AdditionalOptions': ['/FORCE:MULTIPLE'] } },
			'sources': ['addon.cc', 'myobject.cc'],
		}
	]
}