import fitz
import os
# import concurrent.futures

from utils.archive_utils import decompress_archive


def convert_pdf_to_txt(f, filename):
    doc = None
    txt = None
    filename, _ = os.path.splitext(os.path.basename(filename))
    try:
        print('Cnv', filename)
        doc = fitz.open(stream=f, filetype='pdf')
        print(f"Elaborating file {filename}\nPages: {doc.page_count}")

        txt = "\n".join(page.get_text('text') for page in doc)
        print('Txt', filename)

    finally:
        print('Fin', filename)
        if doc is not None:
            doc.close()
    print('Ret',filename)
    return txt, filename
    # try:
    #     doc = fitz.open(stream=f, filetype='pdf')
    #     print(f"Elaborating file {filename}\nPages: {doc.pageCount}")
    #
    #     txt = "\n".join(page.getText('text') for page in doc)
    # except Exception as e:
    #     print(f"Something went wrong with file {f}, it will not be converted: {e}")
    # finally:
    #     if doc is not None:
    #         doc.close()
    #     return txt, filename


def __dummy_txt(f, fname):
    return f.decode('utf-8'), os.path.splitext(os.path.basename(fname))[0]


def convert_archive_to_txt(archive_path: str):#, executor: concurrent.futures.ProcessPoolExecutor):
    decompressed = decompress_archive(archive_path)
    # futures = list()
    for f, fname in decompressed:
        if os.path.splitext(fname)[1] == '.pdf':
            try:
                yield convert_pdf_to_txt(f, fname)
            except Exception as e:
                print(f"Something went wrong with file {fname}, it will not be converted: {type(e)}: {e}")
        # futures.append(executor.submit(convert_pdf_to_txt, f, fname))
        else:
            try:
                yield __dummy_txt(f, fname)
            except Exception as e:
                print(f"Something went wrong with file {fname}, it will not be converted: {type(e)}: {e}")
            # futures.append(executor.submit(__dummy_txt, f, fname))
    # for future in concurrent.futures.as_completed(futures):
    #     yield future.result()
