import tarfile
import zipfile


def decompress_archive(file: str):
    if zipfile.is_zipfile(file):
        with zipfile.ZipFile(file) as zf:
            for fname in zf.namelist():
                with zf.open(fname) as f:
                    yield f.read(), fname
    else:
        with tarfile.open(file) as tf:
            for fname in tf.getnames():
                with tf.extractfile(fname) as f:
                    yield f.read(), fname


def new_zip_archive(files: [(str, str)]):
    with zipfile.ZipFile("output.zip", mode='w') as archive:
        for file, filename in files:
            archive.writestr(filename, file)
