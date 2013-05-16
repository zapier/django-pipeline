import os

from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compressors import SubProcessCompressor


class UglifyJSCompressor(SubProcessCompressor):
    def compress_js(self, js):
        command = '%s %s' % (settings.PIPELINE_UGLIFYJS_BINARY, settings.PIPELINE_UGLIFYJS_ARGUMENTS)
        if self.verbose:
            command += ' --verbose'
        return self.execute_command(command, js)

    def compress_js_with_source_map(self, paths):
        source_map_path = 'temp.map.out'
        command = '%s --source-map %s %s' % (settings.PIPELINE_UGLIFYJS_BINARY, source_map_path, settings.PIPELINE_UGLIFYJS_ARGUMENTS)
        if self.verbose:
            command += ' --verbose'
        js = self.execute_command(command, paths)

        # Read off source map
        f = open(source_map_path, 'r')
        source_map = f.read()
        f.close()
        os.remove(source_map_path)

        return [js, source_map]
