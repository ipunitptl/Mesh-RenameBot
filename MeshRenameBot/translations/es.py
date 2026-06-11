from dataclasses import dataclass


@dataclass
class SpanishTranslations:
    LANGUAGE_NAME = "Español"
    LANGUAGE_CODE = "es"

    WRONG_VALUE_ERROR = (
        "❌ Valor inválido ingresado para la variable {{ variable_name }}."
    )

    START_MSG = (
        "👋 ¡Hola! Soy **Molly File Rename**.\n\n"
    )

    CANCEL_MESSAGE = (
        "⚠️ El cambio de nombre ha sido **cancelado**. Se actualizará pronto."
    )

    RENAME_NO_FILTER_MATCH = (
        "🚫 **NO SE HA ENCONTRADO UN FILTRO - ABORTANDO EL CAMBIO DE NOMBRE**\n\n"
        "🔍 Usando filtros para renombrar ya que no se especificó un nombre.\n"
        "📌 Administra tus filtros usando /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Usando filtros para renombrar ya que no se especificó un nombre.\n"
        "📌 Administra tus filtros usando /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Ingresa el nuevo nombre de archivo en el formato:\n"
        "```/rename my_new_filename.extension```\n"
        "o usa `/filters` para configurar filtros de renombre."
    )

    RENAME_CANCEL = "❌ Cancelar este cambio de nombre."

    RENAMING_FILE = "🔄 Renombrando el archivo... Por favor espera."

    DL_RENAMING_FILE = "📥 Descargando el archivo... Por favor espera."

    RENAME_ERRORED_REPORT = "❗ La descarga encontró un error. Reporta este problema."

    RENAME_CANCEL_BY_USER = "🚫 **Cancelado por el usuario.**"

    FLTR_ADD_LEFT_STR = (
        "➕ Filtro añadido: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    )
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtro añadido: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )
    FLTR_RM_STR = "❌ Eliminar filtro: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = "🔄 Reemplazar filtro: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."

    CURRENT_FLTRS = "⚙️ **Tus Filtros Actuales:**"
    ADD_FLTR = "➕ Añadir Filtro"
    RM_FLTR = "❌ Eliminar Filtro"

    FILTERS_INTRO = (
        "🛠 **Guía de Filtros:**\n"
        "Hay 3 tipos de filtros:\n\n"
        "🔄 **Filtro de Reemplazo:** Reemplaza una palabra dada con otra.\n"
        "➕ **Filtro de Adición:** Añade una palabra al principio o al final.\n"
        "❌ **Filtro de Eliminación:** Elimina una palabra del nombre del archivo."
    )

    ADD_REPLACE_FLTR = "➕ Añadir Filtro de Reemplazo"
    ADD_ADDITION_FLTR = "➕ Añadir Filtro de Adición"
    ADD_REMOVE_FLTR = "➕ Añadir Filtro de Eliminación"
    BACK = "🔙 Atrás"

    REPALCE_FILTER_INIT_MSG = "✍️ Envía el formato: `<code>qué_reemplazar | reemplazo</code>` o `/ignore` para regresar."

    NO_INPUT_FROM_USER = "⚠️ No se recibió ninguna entrada de tu parte."
    INPUT_IGNORE = "✅ **Ignorado.**"
    WRONG_INPUT_FORMAT = "❌ Formato inválido. Verifica el formato proporcionado."
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtro de reemplazo añadido:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto a añadir usando `<code>|</code>`\n"
        "Ejemplo: `<code>| texto para añadir |</code>`\n"
        "o `/ignore` para regresar."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtro añadido: `<code>{{ text_1 }}</code>` **a la IZQUIERDA**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtro añadido: `<code>{{ text_1 }}</code>` **a la DERECHA**."
    )

    ADDITION_LEFT = "🔄 Adición a la IZQUIERDA"
    ADDITION_RIGHT = "🔄 Adición a la DERECHA"

    ADDITION_POSITION_PROMPT = "📍 **¿Dónde quieres añadir el texto?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Ingresa el texto que deseas eliminar o `/ignore` para regresar."
    )

    REMOVE_FILTER_SUCCESS = "✅ **Filtro de eliminación añadido:** `<code>{{ text_1 }}</code>` será eliminado."

    REPLY_TO_MEDIA = "📂 Responde `/rename` a un archivo de medios."

    RENAME_DOWNLOADING_DONE = "✅ Descarga completa. Ahora renombrando el archivo..."
    RENAME_ERRORED = "❗ El proceso de renombrado encontró un error."
    RENAME_CANCEL_BY_USER = "🚫 **Descarga cancelada.**"

    UPLOADING_THE_FILE = "📤 Subiendo el archivo: **{{ new_file_name }}**"

    RENAME_UPLOAD_CANCELLED_BY_USER = "🚫 **Subida cancelada por el usuario.**"
    RENAME_UPLOADING_DONE = "✅ **Proceso de renombrado completado.**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Inicio de ejecución de la tarea de renombrado**\n"
        "🆔 ID de Tarea: `{{ uid }}`\n\n"
        "👤 **Nombre de Usuario:** @{{ username }}\n"
        "📛 **Nombre:** {{ name }}\n"
        "🆔 **ID de Usuario:** `<code>{{ user_id }}</code>`\n"
        "📂 **Nombre de Archivo:** `<code>{{ file_name }}</code>`"
    )

    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Tarea de renombrado añadida**\n\n"
        "👤 **Nombre de Usuario:** @{{ username }}\n"
        "📛 **Nombre:** {{ name }}\n"
        "🆔 **ID de Usuario:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "📌 **NOTA:** Puedes establecer el título usando `/setcaption` seguido del texto que desees.\n"
        "📂 Usa `<code>{file_name}</code>` para insertar dinámicamente el nombre del archivo renombrado en el título."
    )

    DELETE_CAPTION = "🗑 Eliminar Título"
    CLOSE = "❌ Cerrar"

    CAPTION_CURRENT = "📝 **Tu Título Actual:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **No se ha establecido un título.**"
    CAPTION_SET = "✅ **Título actualizado a:** {{ caption }}"
    CAPTION_DELETED = "🗑 **Título eliminado exitosamente.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Tarea de renombrado añadida a la cola**\n"
        "🆔 **ID de DC:** {{ dc_id }}\n"
        "📌 **ID de Medio:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **Estado de la Cola de Renombrado:**\n"
        "📌 **Total de Tareas en la Cola:** {{ total_tasks }}\n"
        "📌 **Capacidad de la Cola:** {{ queue_capacity }}\n"
        "⏳ **Actualmente Procesando:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Tu tarea está actualmente en ejecución**\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Posición de tu tarea en la cola:** {{ task_number }}\n"
        "🆔 **ID de Tarea:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🚷 **Has sido eliminado del chat. No puedes usar este bot.**"
    USER_NOT_PARTICIPANT = "⚠️ **Únete al chat requerido para usar este bot.**"
    JOIN_CHANNEL = "🔗 Únete al Canal de Actualizaciones"

    MODE_INITIAL_MSG = (
        "📂 **Modo de Salida de Archivos:**\n\n"
        "1️⃣ **Mismo formato que se envía.**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forzar a Documento.**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Subir como Medios Generales.**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "📌 **Selecciona el modo de renombrado:**\n"
        "🅰️ **Renombrar con comando.**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renombrar sin comando.**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Responde a una imagen para establecerla como miniatura."
    THUMB_SET_SUCCESS = "✅ **Miniatura establecida exitosamente.**"
    THUMB_NOT_FOUND = "⚠️ **No se encontró la miniatura.**"
    THUMB_CLEARED = "🗑 **Miniatura eliminada exitosamente.**"

    HELP_STR = (
        "📖 **Comandos del Bot:**\n"
        "`{{ startcmd }}` - ✅ Verificar si el bot está en funcionamiento.\n"
        "`{{ renamecmd }}` - ✍️ Responde a un archivo de medios con `/rename filename.extension` para renombrarlo.\n"
        "`{{ filterscmd }}` - ⚙️ Gestionar tus filtros de renombrado.\n"
        "`{{ setthumbcmd }}` - 📷 Establecer una miniatura permanente (responde a una imagen).\n"
        "`{{ getthumbcmd }}` - 📸 Obtener la miniatura actualmente establecida.\n"
        "`{{ clrthumbcmd }}` - ❌ Eliminar la miniatura establecida.\n"
        "`{{ modecmd }}` - 🔄 Cambiar entre 3 modos de salida:\n"
        "    - 📝 Mismo formato que se envía.\n"
        "    - 📂 Forzado a Documento.\n"
        "    - 🎥 Medios Generales (video/audio en streaming).\n\n"
        "    🔄 Cambiar entre modos de renombrado:\n"
        "    - 🏷 Renombrar **con comando**.\n"
        "    - ✨ Renombrar **sin comando**.\n\n"
        "`{{ queuecmd }}` - 📊 Ver el estado de la cola de renombrado del bot.\n"
        "`{{ setcaptioncmd }}` - 📝 Establecer un título para los archivos renombrados.\n"
        "`{{ helpcmd }}` - 📖 Mostrar este mensaje de ayuda.\n"
        "`{{ setlanguagecmd }}` - 🌐 Cambiar el idioma del bot.\n"
    )

    CURRENT_LOCALE = "🌐 **Tu idioma actual:** {{ user_locale }}"
