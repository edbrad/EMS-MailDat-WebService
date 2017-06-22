# extract each
def unzip_artifact( local_directory, file_path ):
    fileName, ext = os.path.splitext( file_path )
    if ext == ".zip":
        print 'unzipping file ' + basename(fileName) + ext
        try:
            with zipfile.ZipFile(file_path) as zf:
                for member in zf.infolist():
                        # Path traversal defense copied from
                        # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
                        zf.extract(member, local_directory)
        except zipfile.error, e:
            print "Bad zipfile: %s" % (e)
        return

# extract all
def unzip_artifact( local_directory, file_path ):
    fileName, ext = os.path.splitext( file_path )
    if ext == ".zip":
        print 'unzipping file ' + basename(fileName) + ext
        try:
            zipfile.ZipFile(file_path).extractall(local_directory)
        except zipfile.error, e:
            print "Bad zipfile: %s" % (e)
        return