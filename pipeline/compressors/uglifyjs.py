from __future__ import unicode_literals

import os

from pipeline.conf import settings
from pipeline.compressors import SubProcessCompressor

class UglifyJSCompressor(SubProcessCompressor):
    def compress_js(self, js):
        command = '%s %s' % (settings.PIPELINE_UGLIFYJS_BINARY, settings.PIPELINE_UGLIFYJS_ARGUMENTS)
        if self.verbose:
            command += ' --verbose'
        return self.execute_command(command, js)

    def compress_js_with_source_map(self, paths, source_map_filename, root_url, path_prefix):
        # Compute number of directory levels to drop from relative paths in source map
        path_prefix = os.path.normpath(path_prefix)
        dir_levels = path_prefix.count('/', 1) + 1

        map_url = root_url + source_map_filename

        if root_url.endswith('/'):
            root_url = root_url[0:-1] # Chrome (maybe other browsers) tacks on a trailing /

        tmp_source_map = 'test.map'
        command = '%s %s --source-map %s --source-map-url %s -p %d --source-map-root %s' % (
            settings.PIPELINE_UGLIFYJS_BINARY,
            ' '.join(paths),
            tmp_source_map,
            map_url,
            dir_levels,
            root_url
        )
        if self.verbose:
            command += ' --verbose'

        js = self.execute_command(command, paths)

        # Read off source map
        f = open(tmp_source_map, 'r')
        source_map = f.read()
        f.close()
        os.remove(tmp_source_map)

        return [js, source_map]
