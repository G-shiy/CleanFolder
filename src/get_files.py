import os
import shutil
from pathlib import Path


videos = ["mkv", "mp4", "m4v", "mov", "mpeg", "wmv", "avi", "flv", "webm"]
audio = ["aiff", "au", "mid", "midi", "mp3", "m4a", "wav", "ogg"]
imagens = ["jpeg", "jpg", "png", "gif", "svg", "tiff", "exif", "raw", "webp"]
code_language = ['py', 'cs', 'js', 'ts', 'html', 'sql', 'css']
folders = ["Apresentacoes", "Programacao", "Documentos", "Executáveis",
           "Imagens", "Imagens", "Ebooks", "Audio", "Videos", "Planilhas", "Textos"]


def extension_type(event: dict):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) in audio:
        return True
    return False


def is_image_file(event):
    if extension_type(event) in imagens:
        return True
    return False


def is_video_file(event):
    if extension_type(event) in videos:
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_compressed_file(event):
    if extension_type(event) in ('zip', 'rar', '7z'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in code_language:
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def make_folder(foldername):
    os.chdir(str(Path.home() / "Downloads"))
    if os.path.exists(foldername) == True:
        print('Folder already exists and another one cannot be created')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print('moving file')
    except:
        print('File already existed in target folder')
        pass


def FixDownload():
    for folder in folders:
        make_folder(folder)
    return True
