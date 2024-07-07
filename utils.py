def get_extension_from_mime(mime_type):
    mime_extensions = {
        'application/pdf': '.pdf',
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'video/mp4': '.mp4',
        'audio/mpeg': '.mp3',
    }
    return mime_extensions.get(mime_type, '')