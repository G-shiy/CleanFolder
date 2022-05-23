import os
from watchdog.events import FileSystemEventHandler
from src.get_files import is_code_file, is_doc_file, is_executable_file, is_image_file, is_mp3_file, is_pdf_file, is_presentation_file, is_spreadsheet_file, extension_type, is_video_file, is_text_file, move_to_new_corresponding_folder, make_folder, is_compressed_file


class Handler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    @staticmethod
    def on_created(event):
        print(f"O arquivo foi criado em {event.src_path}")

    @staticmethod
    def on_deleted(event):
        print(f"O arquivo foi deletado de {event.src_path}")

    @staticmethod
    def on_modified(event):
        if os.path.isdir(event.src_path):
            return 0
        if is_code_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_doc_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_executable_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_image_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_pdf_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_mp3_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_video_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_spreadsheet_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_text_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_presentation_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
        elif is_compressed_file(event) == True:
            path_to_folder = make_folder('Audio')
            try:
                move_to_new_corresponding_folder(event, path_to_folder)
                return 1
            except Exception as e:
                print(e)
                return 0
